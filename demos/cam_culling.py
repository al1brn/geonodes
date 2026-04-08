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

module : camera culling
-----------------------

Camera culling and multi res mesh

updates
-------
- created : 2025/01/12
- updated : 2026/04/07

This module provides several independant features:

- Random normal: normal law implementation for values and vectors
- Camera culling: culls points, edges and faces which are not visible in the field of view of the camera
- Multi resolution: surfaces with a resolution depending on the distance to the camera

All the modifiers can be generated using demo function.
Specific modifiers can be generated using specic functions:
- random_normal : random modifiers
- camera_culling : camera culling modifiers
- multires_surface : multi resolution modifiers


## Modifiers:
> - Camera Projection
> - Camera Point Culling
> - Camrea Edge Culling
> - Camera Face Culling
> - Multires Surface
> - Multires Faces
> - DEMO Multires Faces
"""

from geonodes import *

FOCAL_FACTOR = .04939

def demo():

    DEBUG_GEO = False

    # ====================================================================================================
    # Camera Data
    # ====================================================================================================

    with GeoNodes("Camera Data", is_group=True):

        with Panel("Camera Culling"):
            ok_cc        = Boolean(True, "Culling", shape="Single")
            use_active   = Boolean(True, "Use Active Camera", shape="Single")
            cam_obj      = Object(None,  "Camera")
            aspect_ratio = Float(16/9,   "Aspect ratio", tip="Render Width/Height : 16/9, 4/3,...", shape="Single")

        cam_obj.switch(use_active, nd.active_camera)

        cam_info = cam_obj.camera_info()

        focal_length = cam_info.focal_length
        focal_length *= FOCAL_FACTOR

        obj_info = cam_obj.info(transform_space='RELATIVE')

        ok_cc.out("Culling")
        cam_obj.out("Camera")
        aspect_ratio.out("Aspect Ratio")
        focal_length.out("Focal Length")
        cam_info.projection_matrix.out("Projection Matrix")

        obj_info.location.out("Location")
        obj_info.rotation.invert().out("Rotation")


    # ====================================================================================================
    # Camera Projection
    # ====================================================================================================

    with GeoNodes("Camera Projection", is_group=True):
        """ Project points with radius and normal

        Arguments
        ---------
        - Position : Position to project
        - Radius : Point radius
        - Normal : Normal vector (with any length)

        Returns
        -------
        - Projection (Vector) : projected positions
        - Behind (Boolean) : point is behind the camera
        - Outside (Boolean) : point is outside the camera
        - Radius (Float) : shrinked radius as seen from the camera
        - Normal (Float) : normal projected along the observation direction
        - Distance (Float) : distance from the camera to the point
        - Ratio (Float) : sizer ratio : 1/distance
        - Outside Left (Boolean) : point is outside to the left
        - Outside Right (Boolean) : point is outside to the right
        - Outside Bot (Boolean) : point is outside to the top
        - Outside Top (Boolean) : point is outside to the bot
        - Position (Vector) : input positions
        
        """

        position = Vector(0,   "Position",      tip = "Point position", default_input='POSITION')
        radius   = Float(0,    "Radius", min=0, tip = "Position radius")
        normal   = Vector(0,   "Normal",        tip = "Point direction", default_input='NORMAL')

        cam_data = G().camera_data().node.link_inputs()

        aspect_ratio = cam_data.aspect_ratio
        focal_length = cam_data.focal_length
        rot          = cam_data.rotation

        vect     = position - cam_data.location
        pos      = rot @ vect
        distance = pos.length()

        # ===== Position above sensor are behind the camera
        # Taking into account the radius

        with Layout("Behind the Sensor"):
            z_pos = pos.z._lc("Z Position")
            behind = (z_pos - radius > 0) # & ok_cc

        # ===== Projection of the normal along the observation direction
        # Negative values are for escaping normals

        with Layout("Normal direction relatively to position"):
            outwards = normal.dot(vect.normalize())

        # ===== Projection ratio

        with Layout("Radius ratio"):
            ratio = focal_length/gnmath.max(.0001, distance - radius)
            app_radius = ratio*radius

        with Layout("Projection"):
            rz   = -focal_length/pos.z
            proj = Vector((pos.x*rz, pos.y*rz, 0))

        # ===== Outside the sensor
        # sensor dims : (aspect_ratio, 1)

        with Layout("Projected outside the sensor borders"):
            half_width  = aspect_ratio/2 + app_radius
            half_height = .5 + app_radius

            outside_left  = (proj.x < -half_width)# & ok_cc
            outside_right = (proj.x >  half_width)# & ok_cc
            outside_bot   = (proj.y < -half_height)# & ok_cc
            outside_top   = (proj.y >  half_height)# & ok_cc

            outside = outside_left | outside_right | outside_bot | outside_top

        # ===== Returns

        proj.out(         "Projection")
        behind.out(       "Behind")
        outside.out(      "Outside")
        outwards.out(     "Normal")
        app_radius.out(   "Radius")
        distance.out(     "Distance")
        ratio.out(        "Ratio")
        outside_left.out( "Outside Left")
        outside_right.out("Outside Right")
        outside_bot.out(  "Outside Bot")
        outside_top.out(  "Outside Top")

        pos.out(          "Position")

        cam_data.culling.out("Culling", panel="Camera")
        cam_data.camera.out("Camera", panel="Camera")
        cam_data.aspect_ratio.out("Aspect Ratio", panel="Camera")
        cam_data.focal_length.out("Focal Length", panel="Camera")

    # ====================================================================================================
    # Domains culling
    # ====================================================================================================

    # ----------------------------------------------------------------------------------------------------
    # Position Culling
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Camera Point Culling"):

        cloud = Cloud(Geometry())
        min_radius = Float(0, "Min Radius", 0)

        # ===== Projection into the camera space

        node = G().camera_projection(radius=nd.radius).link_inputs(from_panel="Camera Culling", panel="Camera Culling").node
        use_culling = node.culling

        cloud.points.Visible = (node.behind | node.outside | (node.radius < min_radius)).bnot()

        with Layout("Done"):
            keep = Cloud(cloud)
            keep.points[Boolean("Visible")].separate()

            cloud.switch(use_culling, keep).out("Mesh")
            keep.inverted.switch_false(use_culling).out("Deleted")

            # Propagates camera info
            node.link_outputs(to_panel="Camera", panel="Camera")

    # ----------------------------------------------------------------------------------------------------
    # Edge Culling
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Camera Edge Culling") as tree:

        mesh       = Mesh()
        radius     = Float(1, "Vertex radius", 0)
        min_radius = Float(0, "Min Radius", 0)

        # ===== Projection

        node = G().camera_projection(radius=radius).link_inputs(from_panel="Camera Culling", panel="Camera Culling").node
        aspect_ratio = node.aspect_ratio
        use_culling = node.culling

        # Get the created input sockets
        #radius = Float.Input("Radius")

        # ===== Both indices are behind

        with Layout("Sensor halt sizes and diagonal"):
            half_height = Float(.5)._lc("Height/2")
            diag = (half_height*gnmath.sqrt(1 + aspect_ratio**2))._lc("Diagonal/2")

        with Layout("Edge's vertex indices"):
            i1 = nd.edge_vertices().vertex_index_1
            i2 = nd.edge_vertices().vertex_index_2

        with Layout("A, B: Edge's vertex projected positions"):
            A  = mesh.points.sample_index(node.projection, i1)._lc("A")
            rA = mesh.points.sample_index(node.radius,     i1)._lc("A Radius")
            B  = mesh.points.sample_index(node.projection, i2)._lc("B")
            rB = mesh.points.sample_index(node.radius,     i2)._lc("B Radius")
            small = gnmath.max(rA, rB) < min_radius

        with Layout("Projection of the origin on the edge line"):
            # Line equation is: OM = OA + tAB
            # Projection H is such as: OH.AB = 0 ==> (A + tAB).AB = 0 <=> t = -A.AB/AB**2
            AB = B - A
            l2 = AB.x**2 + AB.y**2
            t = -(A.dot(AB))/l2

            C  =  A.switch(t > 0,  B.switch(t < 1,  A + AB*t))._lc("C")
            rC = rA.switch(t > 0, rB.switch(t < 1, rA + (rB - rA)*t))._lc("C Radius")

        with Layout("Both vertices are behind"):
            ignore = mesh.points.sample_index(node.behind, i1) & mesh.points.sample_index(node.behind, i2)
            ignore |= small

        with Layout("Both vertices are outside but on the same side"):
            ignore |= mesh.points.sample_index(node.outside_left,  i1) & mesh.points.sample_index(node.outside_left,  i2)
            ignore |= mesh.points.sample_index(node.outside_right, i1) & mesh.points.sample_index(node.outside_right, i2)
            ignore |= mesh.points.sample_index(node.outside_bot,   i1) & mesh.points.sample_index(node.outside_bot,   i2)
            ignore |= mesh.points.sample_index(node.outside_top,   i1) & mesh.points.sample_index(node.outside_top,   i2)

        with Layout("Nearest point farer than diagonal"):
            ignore |= C.length() > diag + rC

        mesh.edges.Visible = ignore.bnot()

        with Layout("Done"):
            keep = Mesh(mesh)
            keep.edges[Boolean("Visible")].separate()

            mesh.switch(use_culling, keep).out("Mesh")
            keep.inverted.switch_false(use_culling).out("Deleted")

            # Propagates camera info
            node.link_outputs(to_panel="Camera", panel="Camera")

    # ----------------------------------------------------------------------------------------------------
    # Face Culling
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Camera Face Culling"):

        mesh = Mesh()

        back_faces = Float.Factor(1, "Back Faces", min=0, max=1, tip="Ignore faces oriented backward (1: keep all).")
        min_radius = Float(0.0, "Min Radius", 0.0, tip="Min approximated size")

        # ---------------------------------------------------------------------------
        # Faces facing outwards
        # ---------------------------------------------------------------------------

        dual = Mesh(mesh).dual()

        dual.points.store("Normal", mesh.faces.sample_index(nd.normal, nd.index))

        face_radius = nd.face_area.sqrt()/2
        dual.points.Face_radius = mesh.faces.sample_index(face_radius, nd.index)

        cam_node = G().camera_projection(normal=Vector.Named("Normal"), radius=Float("Face radius")).node
        cam_node.link_inputs(from_panel="Camera Culling", panel="Camera Culling")
        use_culling = cam_node.culling

        outwards = dual.points.sample_index(cam_node.normal, index=nd.index)
        f_rad = dual.points.sample_index(cam_node.radius, index=nd.index)

        mesh.faces.Visible = (outwards <= back_faces) & (f_rad >= min_radius)

        # ---------------------------------------------------------------------------
        # Faces with all their corners behind the camera
        # ---------------------------------------------------------------------------

        node = G().camera_projection().node.link_inputs(from_panel="Camera Culling", panel="Camera Culling")
        aspect_ratio = node.aspect_ratio

        with Layout("Faces with all vertices behind the sensor"):
            mesh.points.store("TEMP Vertex Behind", Float(node.behind))
            mesh.faces.store("TEMP Face Behind", Float.Named("TEMP Vertex Behind"))

            visible = Float.Named("TEMP Face Behind") <= 1 - 1/Face.corners_total(nd.index)
            mesh.faces.Visible = Boolean("Visible") & visible

        # ---------------------------------------------------------------------------
        # Faces outside the sensor
        # ---------------------------------------------------------------------------

        projected = Mesh(mesh)
        projected.points.position = node.projection

        half_width  = aspect_ratio/2
        half_height = .5

        for feel in projected.faces.for_each():

            face = Mesh(feel.element)
            bbox = face.bounding_box()

            outside =  bbox.max_.x < -half_width
            outside |= bbox.min_.x >  half_width
            outside |= bbox.max_.y < -half_height
            outside |= bbox.min_.y >  half_height

            face.faces.Visible = Boolean("Visible") & outside.bnot()
            face.out()

        # ---------------------------------------------------------------------------
        # Separate
        # ---------------------------------------------------------------------------

        mesh.faces.Visible = Mesh(feel.generated).faces.sample_index(Boolean("Visible"), index=nd.index)
        mesh.remove_named_attribute("Wildcard", "TEMP*")

        with Layout("Done"):
            keep = Mesh(mesh)
            keep.faces[Boolean("Visible")].separate()

            mesh.switch(use_culling, keep).out("Mesh")
            keep.inverted.switch_false(use_culling).out("Deleted")

            # Propagates camera info
            cam_node.link_outputs(to_panel="Camera", panel="Camera")

    # =============================================================================================================================
    # Camera Debug
    # =============================================================================================================================

    with ShaderNodes("DBG Face", replace_material=True):

        col = snd.attribute(attribute_name="Color").color
        fac = snd.attribute(attribute_name="Transparent").factor
        ped = Shader.Principled(base_color=col)
        transp = Shader.Transparent()

        ped.mix(transp, factor=fac).out()

        #ped.out()

    with ShaderNodes("DBG Point"):

        col = snd.attribute(attribute_name="Point Color").color
        ped = Shader.Principled(base_color=col)
        ped.out()

    # ====================================================================================================
    # Culling demo
    # ====================================================================================================
    
    with GeoNodes("Camera Demo"):

        mesh = Mesh()

        with Mesh.MenuSwitch(menu=Input("Domain")) as res:

            with Panel("Points"):
                radius = Float(0.05, "Radius", 0)
                min_radius = Float(0, "Min Radius", 0)
                del_faces = Boolean(False, "Del Faces")

            c = mesh.to_points()
            c.points.radius = radius
            c.points.Color = (1, 0, 0)

            node = G().camera_point_culling(c, min_radius=min_radius).node
            node.link_inputs(from_panel="Camera Culling", panel="Camera Culling")

            c = node.mesh
            c.points[Boolean("Visible")].Color = (0, 1, 0)
            spheres = Mesh(c.points.instance_on(instance=Mesh.UVSphere(radius=gnmath.max(0.001, radius))).realize())
            spheres.faces.material = "DBG Face"

            (Mesh(mesh).faces[del_faces].delete_only_face() + spheres).out("Points")

        with res:
            with Panel("Edges"):
                radius = Float(0.05, "Vertex Radius", 0)
                min_radius = Float(0, "Min Radius", 0)
                del_faces = Boolean(False, "Del Faces")

            m = Mesh(mesh)
            m.edges.Color = (1, 0, 0)

            node = G().camera_edge_culling(m, vertex_radius=radius, min_radius=min_radius).node
            node.link_inputs(from_panel="Camera Culling", panel="Camera Culling")

            m = Mesh(node.mesh)
            m.edges[Boolean("Visible")].Color = (0, 1, 0)
            m.faces.delete_only_face()

            curves = m.to_curve().to_mesh(profile_curve=Curve.Circle(radius=gnmath.max(0.001, radius), resolution=6))
            curves.faces.material = "DBG Face"

            (Mesh(mesh).faces[del_faces].delete_only_face() + curves).mesh.out("Edges")

        with res:
            with Panel("Faces"):
                back_faces = Float.Factor(0, "Back Faces", min=0, max=1, tip="Ignore faces oriented backward (1: keep all).")
                min_radius = Float(0.0, "Min Radius", 0.0, tip="Min approximated size")

            m = Mesh(mesh)
            m.faces.Color = (1, 0, 0)
            m.faces.material = "DBG Face"

            node = G().camera_face_culling(m, back_faces=back_faces, min_radius=min_radius).node
            node.link_inputs(from_panel="Camera Culling", panel="Camera Culling")

            m = node.mesh
            m.faces[Boolean("Visible")].Color = (0, 1, 0)
            m.out("Faces")

        res.out("Mesh")

    # ====================================================================================================
    # Debug
    # ====================================================================================================

    with GeoNodes("Camera Debug"):

        mesh          = Mesh(Geometry())
        prec          = Float(10,     "Precision", min=0, tip="Precision in 1000th (use with care)")/1000 * Integer(1).switch(nd.is_viewport, 10)
        show_grid     = Boolean(False, "Grid")

        show_points   = Boolean(True, "Show Points")
        show_faces    = Boolean(True, "Show Faces")
        transp        = Float.Factor(.5, "Transparent", 0, 1)
        show_edges    = Boolean(True, "Show Edges")
        show_proj     = Boolean(True, "Show Projected")

        mesh.faces.material = "DBG Face"

        node = G().camera_projection(position=nd.position, radius=None, normal=None).node
        node.link_inputs(from_panel="Camera Culling", panel="Camera Culling")
        cam_obj = node.camera
        aspect_ratio = node.aspect_ratio
        focal_length = node.focal_length

        # ---------------------------------------------------------------------------
        # Sensor
        # ---------------------------------------------------------------------------

        with Layout("Sensor"):
            sensor = Mesh.Grid(size_x=aspect_ratio, size_y=1, vertices_x=2, vertices_y=2)
            sensor.faces.delete_only_face()

            grid = Mesh.Grid(size_x=10*prec, size_y=10*prec, vertices_x=11, vertices_y=11)
            grid.faces.delete_only_face()

            sensor += grid.switch(-show_grid)

        # ---------------------------------------------------------------------------
        # Projected Mesh
        # ---------------------------------------------------------------------------

        with Layout("Projected Mesh"):

            proj = Mesh(mesh)
            proj.points.position = node.projection
            proj.faces.delete_only_face()
            proj.switch_false(show_proj)

        # ---------------------------------------------------------------------------
        # Points
        # ---------------------------------------------------------------------------

        with Layout("Points"):

            with Boolean.MenuSwitch(menu=Input("Hidden Points")) as hidden:
                node.behind.out("Behind")
                node.outside.out("Outside")
                (node.behind | node.outside).out("All")

            mesh.points.store("Point Color", Color((0, 1, 0)).switch(hidden, (1, 0, 0)))
            pts = Mesh(mesh.points.instance_on(instance=Mesh.UVSphere(radius=.05)).realize())
            pts.faces.material = "DBG Point"

            geo = sensor + proj
            cam_info = cam_obj.info()

            geo.transform(translation=(0, 0, -focal_length))
            geo.transform(translation=cam_info.location, rotation=cam_info.rotation)

        # ---------------------------------------------------------------------------
        # Edges
        # ---------------------------------------------------------------------------

        with Layout("Edges"):

            edges = G().camera_edge_culling(mesh).link_inputs(from_panel="Camera Culling", panel="Camera Culling")
            edges.faces.delete_only_face()
            curves = edges.to_curve().to_mesh(profile_curve=Curve.Circle(radius=0.01, resolution=6))

            geo += curves.switch_false(show_edges)

        # ---------------------------------------------------------------------------
        # Faces
        # ---------------------------------------------------------------------------

        with Layout("Faces"):

            node = G().camera_projection(position=nd.position, radius=gnmath.sqrt(nd.face_area), normal=nd.normal).node
            node.link_inputs(from_panel="Camera Culling", panel="Camera Culling")

            face_behind = node.behind
            face_outside = node.outside
            face_back = node.normal > 0
            face_size = node.radius < prec
            face_all = face_behind | face_outside | face_size | face_back

            with Boolean.MenuSwitch(menu=Input("Hidden Surfaces")) as hidden:
                face_all.out("All")
                face_behind.out("Behind")
                face_outside.out("Outside")
                face_back.out("Backwards")
                face_size.out("Radius")

            mesh.faces.store("Color", Color((0, 1, 0)).switch(hidden,  (1, 0, 0)))
            mesh.faces.store("Transparent", transp)

            mesh.switch_false(show_faces).join(geo, pts.switch_false(show_points)).out()


    # ====================================================================================================
    # Multi resolution faces
    # ====================================================================================================

    def iterations_panel(def_iter=3, def_prec=10):
        with Panel("Iterations"):
            iterations = Integer(def_iter, "Iterations", 1)
            precision  = Float(def_prec, "Precision", 0)

        return iterations, precision

    with GeoNodes("Multires Faces") as tree:

        mesh = Mesh()

        iterations, prec = iterations_panel(3, 10)

        with Panel("Camera Culling"):
            back_faces = Float.Factor(.1, "Back Faces Culling", min=0, max=1, tip="Don't iterate initial backward faces (-1: iterate all).")

        # ===== Prepare the mesh

        mesh.faces.store("Iterate", True)

        max_points = 1000000 * Integer(10).switch(nd.is_viewport, 1)

        # ===== Subdivision loop
        
        for rep in repeat(iterations, mesh=mesh):

            iterate = Boolean.Named("Iterate")

            # ----- Max number of points is reached

            npoints = rep.mesh.points.count
            iterate = iterate & npoints < max_points

            # ----- Face projection

            radius = 4*gnmath.sqrt(nd.face_area)

            node = G().camera_projection(radius=radius, normal=nd.normal).node
            node.link_inputs(from_node=tree.input_node, from_panel="Camera Culling", panel="Camera Culling")
            use_culling = node.culling

            hidden = use_culling & (node.behind | node.outside | (node.radius < prec) | (node.normal > back_faces))
            iterate = iterate & -hidden

            rep.mesh.faces[Boolean.Named("Iterate")].store("Iterate", iterate)

            subdiv = Mesh(rep.mesh.faces[Boolean.Named("Iterate")].separate().selection)
            keep   = subdiv.inverted

            subdiv.subdivide(1)

            rep.mesh = keep + subdiv

        mesh = rep.mesh

        mesh.remove_named_attribute(name="Iterate")

        mesh.out()


    # ====================================================================================================
    # Multi resolution surface
    # ====================================================================================================

    # An UV Map is divided according the dimension of the faces
    #
    # An initial division is performed to compute the face sizes and normals
    # During the fractal iteration, the size if the faces is estimated by tdividing the initial surface by 2
    #
    # The surface is computed by a group taking (position.x, position.y) as uv map coordinates in space (0, 1), (0, 1)
    # (See DEMO Multires Surface)


    with GeoNodes("Multires Surface", is_group=True) as tree:

        position   = Vector(None,  "Position")

        iterations, prec = iterations_panel(3, 10)
        with Panel("Iterations"):
            init_split = Integer(3, "Initial UV Subdivisions", min=0, max=5)

        with Panel("Camera Culling"):
            back_faces = Float.Factor(.1, "Back Faces Culling", min=0, max=1, tip="Don't iterate initial backward faces (-1: iterate all).")

        # ===== Surface clouds

        # uv coordinates

        with Layout("UV Coordinates"):
            segments = 2**init_split
            vertices = segments + 1
            surface = Mesh.Grid(size_x=1, size_y=1, vertices_x=vertices, vertices_y=vertices)
            surface.points.offset = (.5, .5, 0)
            uv = Mesh(surface).dual().points.to_points()

        # Surface

        with Layout("Surface"):

            surface.points.position = position

            uv.points.store("Size",  surface.faces.sample_index(gnmath.sqrt(nd.face_area), nd.index))
            uv.points.store("Scale", surface.faces.sample_index(1/segments, nd.index))
            uv.points.store("Normal", surface.faces.sample_index(nd.normal, nd.index))

        with Layout("Don't iterate faces pointing outwards"):
            node = G().camera_projection(position=position, normal=Vector.Named("Normal"), radius=None).node.link_inputs()
            use_culling = node.culling
            outwards = node.normal
            uv.points.store("Iterate", outwards < back_faces)

        # ===== Division loop

        max_points = 10000000 * Integer(10).switch(nd.is_viewport, 1)

        for rep in repeat(iterations, uv=uv, iter_scale=0.5/segments, max_iteration=0):

            iterate = Boolean.Named("Iterate")

            # ===== Number max of points is reached

            with Layout("Max number of points is reached"):
                count = Mesh(rep.uv).points.count
                stop = count > max_points
                iterate = iterate & (-stop)
                rep.max_iteration = rep.iteration.switch(stop, rep.max_iteration)

            # ===== Camera projection

            node = G().camera_projection(position=position, radius=Float.Named("Size")).node
            node.link_inputs(from_node=tree.input_node, from_panel="Camera Culling", panel="Camera Culling")

            # ===== Stop iteration for hidden points or small apparent size

            with Layout("Stop Iteration conditions"):
                hidden = use_culling & (node.behind | node.outside | (node.radius < prec))
                iterate = iterate & -hidden

            # ===== We can divide remaining points

            with Layout("Divide remaining points"):
                square = Mesh.Grid(size_x=1, size_y=1, vertices_x=2, vertices_y=2).points.to_points()
                new_squares = Cloud(Mesh(rep.uv).points[iterate].instance_on(instance=square, scale=rep.iter_scale).realize())
                new_squares.points.store("Size",  Float.Named("Size")/2)
                new_squares.points.store("Scale", Float.Named("Scale")/2)

            with Layout("Replace iterated points"):

                rep.uv = Mesh(rep.uv).points[iterate].delete()
                rep.uv += new_squares

            rep.iter_scale /= 2

        uv = Cloud(rep.uv)

        # ----- Finalize the uv grid

        with Layout("Build the final surface"):
            square  = Mesh.Grid(vertices_x=2, vertices_y=2)
            surface  = Mesh(uv.points.instance_on(instance=square, scale=Float.Named("Scale")).realize()).merge_by_distance(distance=rep.iter_scale)

            surface.corners.store("UV Map", nd.position)
            surface.points.position = position

        surface.out()

        Boolean(True).info("Faces: " + surface.faces.count.to_string() + ", Iterations: " + rep.max_iteration.to_string())


    # ----------------------------------------------------------------------------------------------------
    # Demo on how to use the Multires Surface group
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("DEMO Multires Surface"):

        size = Float(100, "Size", min=1)

        with Layout("UV coordinates"):
            u, v, _ = nd.position.xyz

        with Layout("Some Fractal Noise"):
            scale, fac = 1000, .2
            noise = Float(0)
            for _ in range(6):
                with Layout(f"Noise scale {scale}"):
                    noise += (Texture.Noise(scale=scale) - .5)*fac
                    scale /= 10
                    fac += .2

        # ----- A flat plane

        with Layout("Plane"):
            plane = (nd.position - (.5, .5, 0))*size + (0, 0, noise)

        with Layout("Sphere"):
            theta = (2*pi)*u
            phi   = -pi/2 + pi*v

            cphi = gnmath.cos(phi)
            v = Vector((cphi*gnmath.cos(theta), cphi*gnmath.sin(theta), gnmath.sin(phi)))
            sphere = v.scale(size + noise)

        position = Vector.MenuSwitch({'Plane': plane, 'Sphere': sphere}, menu=Input("Surface"))

        surface = Mesh(G().multires_surface(position=position).link_inputs())

        with Layout("Finalize"):
            surface.faces.smooth = True
            surface.faces.material = Material(None, "Material")

        surface.out()




































