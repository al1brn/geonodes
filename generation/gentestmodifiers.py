from geonodes import *

def demo():

    with GeoNodes("Break Demo"):
        Geometry().out()
        raise Break()

        # Not executed
        Float(10).out()

    with GeoNodes("Layout Demo"):

        with Layout("Some maths"):
            z = gnmath.atan2(nd.position.z, Vector((nd.position.x, nd.position.y, 0)).length)

        geo = Mesh()
        geo.points.offset = (0, 0, z)

        geo.out()

    with GeoNodes("Connect several sockets"):

        Geometry().out()

        # Node with 'Value' output socket
        a = Node("Grid")

        # Create Group inputs to feed the node
        # 'Size X' and 'Size Y' are created in the group input not
        # 'Vertices X' and 'Vertices Y' are connected to the same 'Vertices' which is created
        a.link_from(rename={'Vertices X': 'Vertices', 'Vertices Y': 'Vertices'})

        a = Node("Math")

        # Connect the 'Value' output socket to the 'Value' input socket
        # The third socket is exclude by its index
        # Input values are renamed 'First' and 'Second'
        a.link_from(exclude=2, rename={'Value': 'First', 'Value_001': 'Second'})

        b = Node("Math", operation='SQRT')

        # Plug the previous math node on a single socket
        b.link_from(node=a, include='Value')

    # =============================================================================================================================
    # Float Math

    with GeoNodes("Test Float Math"):

        Geometry().out()

        with Layout("Base operators"):
            a, b, c = Float(10), Float(20), Float(pi)

            a += b*c/123 - 789
            A = (gnmath.multiply_add(a, b, c))._lc("gnmath")
            #B = (A * (b, c))._lc("v * (m, a)")
            #B *= b, c
            #B._lc("v *= m, a")

        with Layout("Power"):
            a, b = Float(10), Float(20)

            B = a**b + gnmath.log(a, b) + gnmath.ln(a) + gnmath.exp(a) + gnmath.sqrt(a) + gnmath.inverse_sqrt(a) + gnmath.abs(a)

        with Layout("Comparison"):
            a, b, c = Float(10), Float(20), Float(pi)

            C = gnmath.min(a, b) + gnmath.max(a, b) + gnmath.smooth_min(a, b) + gnmath.smooth_max(a, b) + gnmath.sign(a)
            C = gnmath.less_than(a, b) + gnmath.greater_than(a, b) + gnmath.compare(a, b, c)


        with Layout("Rounding Integer"):
            a, b, c = Float(10), Float(20), Float(pi)

            D = round(a) + gnmath.floor(a) + gnmath.ceil(a) + gnmath.trunc(a)

        with Layout("Rounding Float"):
            a, b = Float(10), Float(20)

            E = gnmath.fract(a) + a % b + gnmath.floored_modulo(a, b) + gnmath.wrap(a) + gnmath.snap(a) + gnmath.ping_pong(a)


        with Layout("Trigo"):
            a, b = Float(10), Float(20)

            F = gnmath.cos(a) + gnmath.sin(a) + gnmath.tan(a) + gnmath.acos(a) + gnmath.asin(a) + gnmath.atan(a) + gnmath.atan2(a, b)

        with Layout("Hyperbolic Trigo"):
            a = Float(10)

            F = gnmath.cosh(a) + gnmath.sinh(a) + gnmath.tanh(a)

        with Layout("Conversions"):
            a = Float(10)

            G = gnmath.radians(a) + gnmath.degrees(a)

    # =============================================================================================================================
    # Vector Math

    with GeoNodes("Test Vector Math"):

        Geometry().out()

        with Layout("Base operators"):
            a, b, c = Vector((1, 2, 3)), Vector((2, 2, 2)), Vector(0)

            A = b*c/123 - 789
            A = (gnmath.multiply_add(a, b, c))._lc("gnmath")
            #B = (A * (b, c))._lc("v * (m, a)")
            #B *= b, c
            #B._lc("v *= m, a")
            C = a*pi

        with Layout("Vectors operations"):
            a, b, c = Vector((1, 2, 3)), Vector((2, 2, 2)), Vector(0)

            B = (a.cross(b) + a.project(b) + a.reflect(b) + a.refract(b, ior=1.5) + a.faceforward(b, c)).scale(a.dot(b))

        with Layout("Length"):
            a, b = Vector((1, 2, 3)), Vector((2, 2, 2))

            C = a.normalize().scale(a.distance(b) + a.length)

        with Layout("Misc"):
            a, b, c = Vector((1, 2, 3)), Vector((2, 2, 2)), Vector(0)

            D = abs(a) + gnmath.vmin(a, b) + gnmath.vmax(a, b) + gnmath.vfloor(a) + gnmath.vceil(a) + gnmath.vfract(a)
            D += a % b + gnmath.vwrap(a, b, c) + gnmath.vsnap(a, b)

        with Layout("Trigo"):
            a = Vector((1, 2, 3))

            E = gnmath.vcos(a) + gnmath.vsin(a) + gnmath.vtan(a)

    # =============================================================================================================================
    # Boolean Math

    with GeoNodes("Test Boolean Math"):

        Geometry().out()

        with Layout("Basic Operations"):
            a, b = Boolean(True), Boolean(False)

            with Layout("Bitwise operators"):
                A = (a | b) & -a

            with Layout("Arithmetic operators"):
                A = (a + b) * -a

        with Layout("Advanced Operations"):
            a, b = Boolean(True), Boolean(False)

            with Layout("Operators"):
                B = a^b | (a + b) | (a - b)

            with Layout("Functions"):
                B = gnmath.nand(a, b) | gnmath.nor(a, b) | gnmath.equal(a, b) | gnmath.not_equal(a, b) | gnmath.imply(a, b) | gnmath.nimply(a, b)

    # =============================================================================================================================
    # String

    with GeoNodes("Test String"):

        Geometry().out()

        s = String("A String")
        s = s + " Other"
        s += " yet another"
        s += " a", " b", " c"

        sepa = String("/")
        sepa *= "a", "b", "c"


    # =============================================================================================================================
    # Color

    with GeoNodes("Test Color"):

        Geometry().out()

        with Layout("Mix"):

            a, b, = Color((.1, .2, .3)), Color((.6, .7, .8, .1))

            c = a.mix(.1, b, False, False)
            c = a.darken(.1, b, True, True)
            c = a.multiply(.1, b)
            c = a.burn(.1, b)
            c = a.lighten(.1, b)
            c = a.screen(.1, b)
            c = a.dodge(.1, b)
            c = a.add(.1, b)
            c = a.overlay(.1, b)
            c = a.soft_light(.1, b)
            c = a.linear_light(.1, b)
            c = a.difference(.1, b)
            c = a.exclusion(.1, b)
            c = a.subtract(.1, b)
            c = a.divide(.1, b)
            c = a.mix_hue(.1, b)
            c = a.mix_saturation(.1, b)
            c = a.mix_color(.1, b)
            c = a.mix_value(.1, b)

        with Layout("Comprison"):

            #a, b, = Color((.1, .2, .3)), Color((.6, .7, .8, .1))

            c = a.equal(b) | a.not_equal(b) | a.brighter(b) | a.darker(b)

    # =============================================================================================================================
    # Input

    with GeoNodes("Test Group Inputs", is_group=True):

        # ----- Geometries

        geo   = Geometry()
        curve = Curve(None, "Curve")
        mesh  = Mesh(name="Mesh")
        cloud = Cloud("Cloud")
        insts = Instances("Instances")
        vol   = Volume("Volume")

        # ----- Menu

        menu = Geometry.MenuSwitch({"Geometry": geo, "Mesh": mesh, "Curve": curve, "Cloud": cloud, "Instances": insts, "Volume": vol}, menu="Cloud").out()

        # ----- String

        a = String("The string", "String", tip="String input")

        # ----- Boolean

        a = Boolean(False, "Boolean", tip="Boolean input")

        # ----- Float

        a = Float(1, "Float", tip="A simple value")
        a = Float.Factor(.5, "Factor", 0, 1)
        a = Float.Percentage(.5, "Percentage", 0, 1)
        a = Float.Angle(0, "Angle")
        a = Float.TimeAbsolute(0, "Time Absolute")
        a = Float.Distance(0, "Distance")
        a = Float.WaveLength(0, "Wave Length")

        # ----- Integer

        a = Integer(123, "Integer", tip="A simple integer")
        a = Integer.Percentage(50, "Integer Percentage", 0, 100)
        a = Integer.Factor(15, "Integer Factor", 10, 20)

        # ----- Vector

        a = Vector(0, "Vector", tip="A simple vecteur")
        a = Vector.Translation(0, "Translation")
        a = Vector.Direction(0, "Translation")
        a = Vector.Velocity(0, "Translation")
        a = Vector.Acceleration(0, "Translation")
        a = Vector.Euler(0, "Translation")
        a = Vector.XYZ(0, "Translation")

        # ----- Transformations

        a = Matrix(name="Matrix")
        a = Rotation(name="Rotation")

        # ----- Color

        a = Color((.1, .2, .3), "Color")
        a = Color((.1, .2, .3, .5), "Transparent Color")

        # ----- Blender resources

        mat = Material("Material", "Material")
        obj = Object("Cube", "Object")
        coll = Collection("Collection", "Collection")
        img = Image(None, "Image")
        text = Texture(name="Texture")


    # =============================================================================================================================
    # Domain

    with GeoNodes("Test Domain"):

        i = Integer(123)
        f = Float(pi)
        v = Vector((1, 2, 3))

        with Layout("Viewer"):
            mesh = Mesh()

            mesh.points.viewer(nd.position)
            mesh.faces.viewer(nd.material_index)

        with Layout("Getters"):
            mesh = Mesh()

            a = mesh.points.attribute_statistic(nd.position)
            a = mesh.points.proximity(i, v, nd.id)
            a = mesh.points.sample_index(nd.position, index=i, clamp=True)
            a = mesh.faces.accumulate_field(value=v, group_id=i)
            a = mesh.points.evaluate_at_index(index=i, value=f)
            a = mesh.corners.evaluate_on_domain(value=v)

        with Layout("Capture Attribute"):
            mesh = Mesh()

            mesh.points.capture_attribute(pos = nd.position, index=nd.index)
            assert(isinstance(mesh.pos_, Vector))
            assert(isinstance(mesh.index_, Integer))


        with Layout("Operations"):
            mesh = Mesh()

            mesh.points.duplicate_elements(10)

            mesh.faces.delete_faces()
            mesh.edges.delete_edges_and_faces()
            mesh.points.delete_all()
            mesh.edges.sort_elements(group_id=i, sort_weight=f)
            selected = mesh.points.separate()
            inverted = selected.inverted_
            mesh.faces.split_to_instances(group_id=i)
            mesh.faces.to_points(position=v, radius=f)

        with Layout("Extrusion"):

            cube = Mesh.Cube()

            cube.faces.extrude(nd.normal, .5)
            cube.faces[cube.top_].extrude(offset_scale=0)

            # Next cube extrusion will change top_
            top = cube.top_

            cube.faces[top].scale(scale=.8, uniform=False)
            cube.faces[top].scale(scale=.6, uniform=True)
            cube.faces[top].extrude(offset_scale=.5)
            cube.faces[cube.top_].flip()


        with Layout("Vertex"):
            mesh = Mesh()

            a = mesh.points.count + 1
            a = mesh.points.instance_on(instance=Mesh.Cube(), pick_instance=False, instance_index=i, rotation=(1, 2, 3), scale=3)
            a = mesh.points.neighbors
            a = mesh.points.neighbors_vertex_count
            a = mesh.points.neighbors_face_count
            a = mesh.points.paths_to_selection(i)
            a = mesh.points.edge_paths_to_curves(i)
            a = mesh.points.edge_index(i, f, True)
            a = mesh.points.corner_index(i, f, True)

        with Layout("Face"):
            mesh = Mesh()

            a = mesh.faces.count
            mesh.faces.smooth = -mesh.faces.smooth
            a = mesh.faces.area
            a = mesh.faces.is_planar
            a = mesh.faces.neighbors_face_count
            a = mesh.faces.neighbors_vertex_count
            mesh.faces.flip()
            mesh.faces.scale(2, 0, False)
            a = mesh.faces.corner_index(i, f, False)
            points = mesh.faces.distribute_points(density=1.)
            points = mesh.faces.distribute_points(density=None)

        with Layout("Edge"):
            mesh = Mesh()

            a = mesh.edges.count
            a = mesh.edges.paths_to_curves(False, i)
            a = mesh.edges.signed_angle
            a = mesh.edges.unsigned_angle
            a = mesh.edges.neighbors
            a = mesh.edges.vertex_index_1
            a = mesh.edges.vertex_index_2
            a = mesh.edges.position_1
            a = mesh.edges.position_2
            mesh.edges.smooth = -mesh.edges.smooth
            a = mesh.edges.shortest_paths(f)
            a = mesh.edges.to_face_groups
            mesh = mesh.edges.split()
            mesh.edges.scale(scale=f, center=v, uniform=True)
            a = mesh.edges.corner_index(i, f, True)
            a = mesh.edges.paths_to_curves(start_vertices=True, next_vertex_index=i)

        with Layout("Corner"):
            mesh = Mesh()

            a = mesh.corners.count
            a = mesh.corners.next_edge_index(i)
            a = mesh.corners.face_index(i)
            a = mesh.corners.offset_in_face(i, 10)
            a = mesh.corners.vertex_index(i)

        with Layout("Spline Point"):
            curve = Curve()

            a = curve.points.count + 1

        with Layout("Spline"):
            curve = Curve()

            a = curve.splines.count
            curve.splines.is_cyclic = -curve.splines.is_cyclic
            curve.splines.resolution = curve.splines.resolution + 5
            curve.splines.type = 'BEZIER'
            a = curve.splines.parameter
            a = curve.splines.length * curve.splines.point_count

        with Layout("Instance"):
            instances = Instances()

            a = instances.insts.count
            instances.insts.transform = instances.insts.transform
            instances.insts.translate(v, False)
            instances.insts.scale = instances.insts.scale + (1, 2, 3)
            instances.insts.scale = {'Scale': (1, 2, 3), 'Center': (10, 11, 12), 'Local Space': False}
            instances.insts.rotation = instances.insts.rotation + (1, 2, 3)
            instances.insts.rotation = {'Rotation': (1, 2, 3), 'Pivot Point': (10, 11, 12), 'Local Space': False}

        with Layout("Cloud Point"):
            cloud = Cloud()

            a = cloud.points.count + 1


    # =============================================================================================================================
    # Curve Handles

    with GeoNodes("Test Curve handles"):
        curve = Curve.Line(0, (20, 0, 0)).resample(20)

        curve.splines.type = 'BEZIER'

        with Layout("Set by str"):
            curve.points.left_handle_type = 'AUTO'
            curve.points.right_handle_type = 'AUTO'
            curve.points[(nd.index % 2).equal(0)].handle_type = 'ALIGN'

            curve.points[curve.points.handle_align].offset = (0, 0, 2)

        with Layout("Both set boolean"):
            curve.points[1].handle_auto = True
            curve.points[3].handle_free = True
            curve.points[5].handle_vector = True
            curve.points[7].handle_align = True

        with Layout("Left / right set boolean"):
            curve.points[9].left_handle_auto = True
            curve.points[9].right_handle_free = True
            curve.points[11].left_handle_free = True
            curve.points[11].right_handle_vector = True
            curve.points[13].left_handle_vector = True
            curve.points[13].right_handle_align = True
            curve.points[15].left_handle_align = True
            curve.points[15].right_handle_auto = True

        with Layout("Left selection"):
            curve.points[curve.points.left_handle_auto].offset = (0, 0.5, 0)
            curve.points[curve.points.left_handle_free].offset = (0, 1.0, 0)
            curve.points[curve.points.left_handle_vector].offset = (0, 1.5, 0)
            curve.points[curve.points.left_handle_align].offset = (0, 2.0, 0)

        with Layout("Right selection"):
            curve.points[curve.points.right_handle_auto].offset = (0, 0, 0.5)
            curve.points[curve.points.right_handle_free].offset = (0, 0, 1.0)
            curve.points[curve.points.right_handle_vector].offset = (0, 0, 1.5)
            curve.points[curve.points.right_handle_align].offset = (0, 0, 2.0)

        with Layout("Moving handles"):
            curve.points[curve.points.left_handle_free].left_handle_position = (5, 0, 0)
            curve.points[curve.points.right_handle_free].right_handle_position = (-5, 0, 0)

            curve.points[curve.points.left_handle_vector].left_handle_offset = (0, 5, 0)
            curve.points[curve.points.right_handle_vector].right_handle_offset = (0, -5, 0)

        curve.out()

    # =============================================================================================================================
    # Geometry

    with GeoNodes("Test Geometry"):

        geo = Geometry()

        with Layout("Basic"):

            geo.set_position(nd.position, 2)


        with Layout("Join"):

            geo = Geometry.Join(Mesh.Cube(), Mesh.IcoSphere(), Curve.Circle())
            geo = Mesh.Join(Mesh.Cube(), Mesh.IcoSphere(), Curve.Circle())
            geo.join(Mesh.Cube())

            geo = geo + Mesh.Cube().set_position(offset=(3, 0, 0))
            geo += Mesh.Cone().set_position(offset=(6, 0, 0)), Mesh.IcoSphere().set_position(offset=(9, 0, 0)),

        with Layout("Operations"):

            geo.replace_material()

        geo.out()

    # =============================================================================================================================
    # Mesh

    with GeoNodes("Test Mesh"):

        mesh = Mesh()
        mesh.out()

        with Layout("Primitives"):

            cone   = Mesh.Cone(vertices=32, side_segments=3, fill_segments=3, radius_top=.5, radius_bottom=2, depth=2, fill_type='TRIANGLE_FAN')
            cube   = Mesh.Cube(size=(1, 2, 3), vertices_x=2, vertices_y=3, vertices_z=3)
            cyl    = Mesh.Cylinder(vertices=32, side_segments=3, fill_segments=3, radius=.5, depth=5, fill_type='NGON')
            grid   = Mesh.Plane(size_x=2, size_y=1)
            ico    = Mesh.IcoSphere(radius=2, subdivisions=2)
            sphere = Mesh.UVSphere(segments=6, rings=7, radius=1.5)
            line0  = Mesh.LineTo(0, 2, count=100)._lc("End points Count")
            line1  = Mesh.LineTo(0, 2, resolution=.1)._lc("End points Resolution")
            line2  = Mesh.LineOffset(0, .1, 10)._lc("Offset")
            circle = Mesh.Disk(vertices=8, radius=.5)

            meshes = [cone, cube, cyl, grid, ico, sphere, line0, line1, line2, circle]

            meshes.append(Mesh.FromCurve(Curve.Spiral(), profile_curve=Curve.Circle(radius=.1), fill_caps=True))
            meshes.append(Mesh.FromPoints(Cloud.Points(10)))
            meshes.append(Mesh.FromVolume(None, 1, 2, 3, 4))

            a = mesh.island_index + mesh.island_count

        with Layout("Sample"):

            cube = Mesh.Cube()
            a = cube.sample_nearest_surface(value=pi, group_id=i, sample_position=v, sample_group_id=i+1)
            a = cube.sample_nearest_surface(value=123, group_id=i, sample_position=v, sample_group_id=i+1)
            a = cube.sample_nearest_surface(value=Vector(0), group_id=i, sample_position=v, sample_group_id=i+1)
            a = cube.sample_nearest_surface(value=Color(0), group_id=i, sample_position=v, sample_group_id=i+1)
            a = cube.sample_nearest_surface(value=Boolean(True), group_id=i, sample_position=v, sample_group_id=i+1)
            a = cube.sample_nearest_surface(value=Matrix(), group_id=i, sample_position=v, sample_group_id=i+1)
            a = cube.sample_uv_surface(value=v, uv_map=cube.uv_map_, sample_uv=v)

        with Layout("Conversions"):

            cube = Mesh.Cube()
            a = cube.to_curve()
            a = cube.to_volume(density=1., voxel_amount=2., interior_band_width=3., voxel_size=3., amount=True)._lc("Amount")
            a = cube.to_volume(density=1., voxel_amount=2., interior_band_width=3., voxel_size=3., amount=False)._lc("Size")

        with Layout("Operations"):

            cube = Mesh.Cube()
            cube.dual()
            cube.subdivide(2)
            cube.triangulate()
            cube.subdivision_surface()
            cube.distribute_points_on_faces()

        with Layout("Boolean"):
            meshes.append(Mesh.Intersect(cyl, cone))
            meshes.append(Mesh.Union(cyl, cone))
            meshes.append(Mesh.Difference(cyl, cone))

            meshes.append(cyl - cone) # Difference
            meshes.append(cyl / cone) # Intersection
            meshes.append(cyl * cone) # Union

            meshes.append(cone.intersect(cyl))
            meshes.append(cone.union(cyl))
            meshes.append(cone.difference(cyl))

        with Layout("Transformation Join"):
            node = nd.join_geometry().node
            locs = Mesh.Grid(size_x=20, size_y=20, vertices_x=5, vertices_y=5)
            for i, mesh in enumerate(meshes):
                node.geometry = mesh.transform(translation=locs.points.sample_index(nd.position, index=i))

            node.geometry.out()

        with Layout("UV"):
            cube = Mesh.Cube()
            a = cube.pack_uv_islands()
            a = cube.uv_unwrap()

    with GeoNodes("Test Curve"):

        curve = Curve()
        curve.out()

        with Layout("Constructors"):

            curve = Curve.Circle(radius=.8)._lc("Circle Radius")
            curve += Curve.Circle(point_2=1)._lc("Circle Points")
            curve += Curve.Arc()._lc("Arc Radius")
            curve += Curve.Arc(offset_angle=halfpi)._lc("Arc Points")
            curve += Curve.Line()._lc("Line Points")
            curve += Curve.Line(direction=v)._lc("Line Direction")
            curve += Curve.BezierSegment(10, 0, 1, 2, 3, 'POSITION')
            curve += Curve.BezierSegment(10, 0, 1, 2, 3, 'OFFSET')
            curve += Curve.QuadraticBezier(10, 1, 2, 3)
            curve += Curve.Spiral(10, 0, 1, 2, 3, True)
            curve += Curve.Star(10, 1, 2, True)

            curve += Curve.Rectangle(1, 2)
            curve += Curve.Parallelogram(1, 2)
            curve += Curve.Trapezoid(1, 2)
            curve += Curve.Kite(1, 2)
            curve += Curve.Points(1, 2, 3, 4)

            curve += Curve.FromMesh(Mesh.Cube()[0])
            curve += Curve.FromEdgePaths(Mesh.Cube()[1])
            curve += Curve.FromPoints(Cloud.Points(10)[2])

        with Layout("Properties"):
            curve = Curve()

            a = curve.tangent
            a += curve.length
            a += curve.endpoint_selection(i, i)
            curve.radius = curve.radius + 1
            curve.tilt = curve.tilt + 1
            curve.normal = 'Z_UP'

        with Layout("Topology"):
            curve = Curve()

            a = curve.curve_of_point(1)
            a += a.index_in_curve_
            b = curve.offset_point_in_curve(1, 1)
            a += b
            c = b.is_valid_offset_
            b = curve.points_of_curve(1, 2, False)
            a += b
            a += b.total_

            curve.set_normal().set_normal_z_up().set_normal_free()

        with Layout("Operations"):
            curve = Curve()

            a = curve.sample((1, 2, 3), 1, 2, 3, True)
            geo = curve.to_mesh()
            geo += curve.to_points()
            geo += curve.deform_on_surface()
            geo += curve.fill(a)
            geo += curve.fillet(1., False, 10)
            geo += curve.interpolate(v, i, Cloud.Points(), v, i, i)
            curve.resample(10)._lc("Resample COUNT")
            curve.resample(length=.1)._lc("Resample LENGTH")
            curve.resample()._lc("Resample EVALUATED")
            curve.trim_length(1, 2)
            curve.trim_factor(.1, .2)
            curve.reverse()
            curve.subdivide(2)

    with GeoNodes("Test Cloud"):
        cloud = Cloud()
        cloud.out()

        with Layout("Constructors"):

            cloud = Cloud.Points(10, (1, 2, 3), .1)
            cloud += Cloud.FromCurve(Curve.Spiral(), 10, 5., 'COUNT')
            cloud += Cloud.FromInstances(Cloud.Points(10).points.instance_on(Mesh.Cube())[0], v, f)
            cloud += Cloud.FromMesh(Mesh.Cube()[1:3], (1, 2, 3), 1., 'CORNERS')
            cloud += Cloud.FromVertices(Mesh.Cube()[2:], (1, 2, 3), 1.)
            cloud += Cloud.FromEdges(Mesh.Cube(), (1, 2, 3), 1.)
            cloud += Cloud.FromFaces(Mesh.Cube(), (1, 2, 3), 1.)
            cloud += Cloud.FromCorners(Mesh.Cube(), (1, 2, 3), 1.)

        with Layout("Methods"):
            cloud = Cloud()

            geo = cloud.to_curves(i, f)
            geo += cloud.to_vertices()
            geo += cloud.to_volume(f, f, f, f, 'VOXEL_SIZE')

    with GeoNodes("Test Instances"):
        instances = Instances()
        instances.out()

        with Layout("Constructors"):

            insts = Instances.FromGeometry(Mesh.Cube(), Curve.Spiral())
            insts += Instances.FromString("Default", size=1, character_spacing=2, word_spacing=3, line_spacing=4, text_box_width=5, text_box_height=6,
                        overflow='OVERFLOW', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT')
            insts += Instances.FromString("Truncate", size=1, character_spacing=2, word_spacing=3, line_spacing=4, text_box_width=5, text_box_height=6,
                        overflow='TRUNCATE', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT')

        with Layout("Operations"):
            insts = Instances()

            geo = insts.realize(True, i)
            geo += insts.to_points(1., 2.)
            geo += insts.on_points(Mesh.Cube().points[1:3], True, i, (1, 2, 3), (1, 2, 3))
            geo += insts.on_points(Curve.Spiral()[2], True, i, (1, 2, 3), (1, 2, 3))
            geo += insts.on_points(instances, True, i, (1, 2, 3), (1, 2, 3))
            geo += insts.translate((1, 2, 3), False)
            geo += insts.scale((1, 2, 3), 1, True)
            geo += insts.scale((1, 2, 3), 2, False)


    with GeoNodes("Test Volume"):
        volume = Volume()
        volume.out()

        with Layout("Constructors"):

            vol = Volume.Cube(1., 2., (1, 2, 3), (3, 4, 5), 10, 11, 12)
            vol += Volume.FromMesh(Mesh.Cube(), 1, 2, 3)
            vol += Volume.FromPoints(Cloud.Points(), 1., 2., 3., 4.)

        with Layout("Operations"):
            vol = Volume()

            geo = vol.distribute_points()
            geo += vol.distribute_random(1., 123)
            geo += vol.distribute_grid(1., .5)
            geo += vol.to_mesh(1, 2, 3, 4)
            geo += vol.to_mesh_grid(10, 20)
            geo += vol.to_mesh_amount(11, 21, 31)
            geo += vol.to_mesh_size(12, 22, 23)

    with GeoNodes("Test Float / Integer"):

        Geometry().out()

        f = Float(pi)

        with Layout("Float Int"):
            a = f.mix(.5, 12, False)
            a += f.clamp(0, 2)
            a += f.map_range_linear(0, 1, 2, 3)
            a += f.map_range_smooth(0, 1, 2, 3)
            a += f.map_range_smoother(0, 1, 2, 3)
            a += f.map_range_stepped(0, 1, 2, 3)
            a += Float(f.color_ramp())
            s = f.to_string(3)
            a += f.curve(.5)


    with GeoNodes("Test Textures"):

        Geometry().out()

        color = Texture.Brick().color
        color = color.mix(.5, Texture.Checker().color)
        color = color.mix(.5, Texture.Gradient().color)
        color = color.mix(.5, Texture.Image().color)
        color = color.mix(.5, Texture.Magic().color)
        color = color.mix(.5, Texture.Noise().color)
        color = color.mix(.5, Texture.Voronoi().color)
        color = color.mix(.5, Texture.Wave().color)
        color = color.mix(.5, Texture.WhiteNoise().color)

    with ShaderNodes("Surface Shader"):

        # ----- Principled BSDF

        ped = Shader.Principled(
            base_color = (.1, .2, .3),
            roughness = .2,
        )

        # ----- To surface output

        ped.out()

        # ----- Noise displacement

        noise = Texture.Noise()

        bump = snd.bump(height=noise)
        bump.out()

        # ----- Thickness

        a_float = Float(.1)

        a_float.out()

        # ----- AOV Output

        snd.aov_output(color=Color((.6, .7, .9)), value=pi, aov_name='Test')

    with ShaderNodes("Volume Shader"):

        # ----- Principled BSDF

        ped = VolumeShader.Principled(
            color = (.1, .2, .3),
            density = .01,
        )

        # ----- To surface output

        ped.out()

    # ====================================================================================================
    # Blender 4.3

    with GeoNodes("Blender 4.3"):

        # ----------------------------------------------------------------------------------------------------
        # Grease Pencil

        with Layout("Grease Pencil"):
            curve = Curve.Spiral()
            gp = curve.to_grease_pencil()
            gp = GreasePencil.FromCurve(curve.to_instance())

            gp = Geometry().grease_pencil.layers.separate()

            n = gp.layers.count

            gp.merge_layers()
            gp.merge_layers_by_name()
            gp.merge_layers_by_group_id()

            curve = gp.to_curves()

        # ----------------------------------------------------------------------------------------------------
        # Messages

        with Layout("Warning"):
            b = Boolean(True)
            b.info("This is info")
            b.warning("This is warning")
            b.error("This is error")

        # ----------------------------------------------------------------------------------------------------
        # Hash

        with Layout("Hash"):
            s = String("Test")
            a = s.hash_value(0)
            b = Integer(100).hash_value(1)
            int_value = a + b

        # Raises an error
        #curve.hash_value(100)

        # ----------------------------------------------------------------------------------------------------
        # Gabor Texture

        with Layout("Gabor Texture"):
            tex = Texture.Gabor()
            float_value = tex.value

        # ----------------------------------------------------------------------------------------------------
        # Matrix determinant

        with Layout("Matrix determinant"):
            float_value += Matrix().determinant

        # ----------------------------------------------------------------------------------------------------
        # Imports

        with Layout("Import"):
            imp_geo = Mesh.ImportOBJ("Path")
            imp_geo += Mesh.ImportSTL("Path")
            imp_geo += Instances.ImportPLY("Ply")
            imp_geo.name = "Imported Geometries"

        # ----------------------------------------------------------------------------------------------------
        # Integer Math

        with Layout("Integer Math"):
            a = Integer(123)
            a = a + a
            a = a + 10
            a = 10 + a
            a += 10

            b = Integer(345)
            b = b - a
            b = 10 - b
            b = b - 10
            b += 34

            c = Integer(456)
            c = c * b
            c = c * 10
            c = 10 * c
            c *= 10

            d = Integer(567)
            d = d // c
            d = d // 10
            d = 10 // d
            d //= 10

            a = a.multiply_add(2, 3)

            a = abs(a)
            a = -a
            a = a.sign()
            s
            c = a**b

            a = d.min(a).max(c)

            a = d.divide_round(a)
            b = d.divide_floor(b)
            c = d.divide_ceiling(c)

            a = a.floored_modulo(b)
            b = b.modulo(c)

            c = a.GCD(b)
            a = a.LCM(c)

            int_value += a

        # ----------------------------------------------------------------------------------------------------
        # Gizmo

        with Layout("Gizmo"):

            val = Float(3.14)
            #gizmo = val.linear_gizmo()

            lg = nd.linear_gizmo(val)
            lg.value = 1
            lg.value = 2
            lg.value = 3

            dg = val.dial_gizmo()
            val.pin_gizmo = True

            tg = Matrix().transform_gizmo()
            tg.node.pin_gizmo = True

        # ----------------------------------------------------------------------------------------------------
        # Geometry name

        with Layout("Geometry name"):
            spiral = Curve.Spiral()
            spiral.name = "Spiral (Curve)"
            circle = Mesh.Circle()
            circle.name = "Circle (Mesh)"

            named_geo = spiral.to_instance() + circle.to_instance()

        # ----------------------------------------------------------------------------------------------------
        # For each element

        with Layout("For Each Element"):

            cube = Mesh.Cube()
            with cube.faces.for_each(position=nd.position) as feel:
                elem = feel.element
                elem.offset = (feel.index, 0, 0)
                feel.generated.geometry = elem


        # Done

        geo = imp_geo.to_instance()
        geo += named_geo
        geo += feel.generated.geometry
        geo.out()

        val = int_value + float_value
        val.out("Value")
