import numpy as np

#from random import Random

from .. import nd, snd, gnmath, GeoNodes, ShaderNodes, Group, G
from .. import Geometry, Mesh, Curve, Cloud, Material
from .. import Repeat, Simulation, Layout
from .. import Boolean, Integer, Float, Vector, Rotation, Matrix, Color
from .. import pi, tau

# =============================================================================================================================
# Utilities and macros

# -----------------------------------------------------------------------------------------------------------------------------
# Random normal

def random_normal():

    # Macro
    def expand_seed(ID, seed, n):

        MAX_INT = 1 << 31 - 1

        with Layout(f"Expand Seed {n} Times"):

            cloud = Cloud.Points(n)
            values = cloud.points.capture(Integer.Random(0, MAX_INT, id=ID, seed=seed))

            seeds = ()
            for i in range(n):
                seeds = seeds + (cloud.points.sample_index(values, i),)

        return seeds

    with GeoNodes("Normal Value", prefix="Random", is_group=True):

        value = Float(0,   "Value")
        scale = Float(1,   "Scale")
        ID    = Integer(0, "ID")
        seed  = Integer(0, "Seed")

        seed0, seed1 = expand_seed(ID, seed, 2)

        x1 = Float.Random(0, 1, id=ID, seed=seed0)
        x2 = Float.Random(0, 1, id=ID, seed=seed1)

        y1 = gnmath.sqrt(-2*gnmath.log(x1))*gnmath.cos(2*np.pi*x2)

        y = value + scale*y1

        y.out("Value")

    with GeoNodes("Normal Vector", prefix="Random", is_group=True):

        length = Float(1,       "Length",   tip="Vector average length")
        scale  = Float(0,       "Scale",    tip="Length scale")
        two_d  = Boolean(False, "2D", tip="2D Vectors (Z = 0)")

        ID     = Integer(0, "ID")
        seed   = Integer(0, "Seed")

        # ===== 2D normalized vectors

        seed0, seed1, seed2 = expand_seed(ID, seed, 3)

        theta    = Float.Random(0, 2*pi, seed=seed0)
        normal2D = Vector((gnmath.cos(theta), gnmath.sin(theta), 0))

        # ===== 3D normalized vectors

        phi = Float.Random(-pi/2, pi/2, seed=seed1)
        cphi = gnmath.cos(phi)
        normal3D = Vector((cphi*gnmath.cos(theta), cphi*gnmath.sin(theta), gnmath.sin(phi)))

        # ===== Length

        l = G.random.normal_value(length, scale, id=ID, seed=seed2)

        normal = normal3D.switch(two_d, normal2D)
        (normal * l).out("Vector")
        normal.out("Direction")

    with GeoNodes("Shaked Z", prefix="Random", is_group=True):

        c_scale  = Float(0, "Cap Scale",       tip="Cap scale")
        length   = Float(1, "Length",          tip="Vector average length")
        l_scale  = Float(0, "Length Scale",    tip="Length scale")
        ID       = Integer(0, "ID")
        seed     = Integer(0, "Seed")

        seed0, seed1, seed2 = expand_seed(ID, seed, 3)

        theta  = Float.Random(0, 2*pi, seed=seed0)
        phi    = G.random.normal_value(pi/2, c_scale, id=ID, seed=seed1)

        cphi   = gnmath.cos(phi)
        normal = Vector((cphi*gnmath.cos(theta), cphi*gnmath.sin(theta), gnmath.sin(phi)))

        l = G.random.normal_value(length, l_scale, id=ID, seed=seed2)

        (normal * l).out("Vector")
        normal.out("Direction")

# =============================================================================================================================
# Camera Culling

def camera_culling():
    """ Camera culling

    Removes geometry which is not visible from the camera.

    The camera is defined by the following arguments
    - Aspect Ratio (Float) : width / height
    - Focal Length (Float) : expressed in mm
    - Margin (Float) : margin extended the visibility area

    Relative
    ========

    > Group

    Transform position in space relative to camera and project the points on the sensor

    Arguments
    ---------
    - Focal Length (Float = 50) : camera focal

    Returns
    -------
    - Position (Vector) : points position in the camera space
    - Projection (Vector) : projection on the sensr
    - Ratio (Float) : distance divided by focal length
    - Behind (Vector) : the points are behind the sensor

    Point Culling
    =============

    > Mesh, Cloud or Curve Modifier

    Delete the points which are not visible.

    Delete all the points which are not visible (calling "Position Culling").

    Arguments
    ---------
    - Geometry (Geometry with point domain) : Input geometry
    - Focal Length (Float = 50) : camera focal
    - Aspect Ratio (Float = 16/9) : camera aspect ratio
    - Margin (Float = .1) : culling margin

    Returns
    -------
    - Geometry

    Face Culling
    =============

    > Mesh Modifier

    Delete the faces which are not visible.

    To determine if a face is visible, it is subdivided and if all the points are not visible, the face is not visible

    Arguments
    ---------
    - Mesh (Mesh) : Input geometry
    - Use Normal (Boolean = True) : delete backward faces
    - Aspect Ratio (Float = 16/9) : camera aspect ratio
    - Focal Length (Float = 50) : camera focal
    - Margin (Float = .1) : culling margin

    Returns
    -------
    - Geometry

    Edge Culling
    =============

    > Mesh Modifier

    Delete the edges which are not visible.

    > [!NODE]
    > This particular modifier is relevant only for meshes made only of edges

    Arguments
    ---------
    - Mesh (Mesh) : Input geometry
    - Aspect Ratio (Float = 16/9) : camera aspect ratio
    - Focal Length (Float = 50) : camera focal
    - Margin (Float = .1) : culling margin

    Returns
    -------
    - Geometry
    """

    DEBUG_GEO = False

    # -----------------------------------------------------------------------------------------------------------------------------
    # Camera relative

    with GeoNodes("Relative", prefix="Camera", is_group=True):

        focal_length  = Float(50, "Focal Length", min=1, tip="Focal length in mm")
        aspect_ratio = Float(16/9, "Aspect Ratio", tip="Camera aspect ratio, 16/9 for instance")

        focal_length *= 2.54/50

        cam_info = nd.active_camera.info(transform_space='RELATIVE')

        rot = cam_info.rotation.invert()
        pos = rot @ (nd.position - cam_info.location)

        behind = pos.z > 0

        #ratio = focal_length/(focal_length - pos.z)
        ratio = focal_length/(focal_length + pos.length)


        proj = Vector((pos.x*ratio, pos.y*ratio, 0))

        pos.out("Position")
        proj.out("Projection")
        ratio.out("Ratio")
        behind.out("Behind")

        # Sensor Size
        aspect_ratio.out("Sensor Width")
        Float(1.).out("Sensor Height")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Position Culling

    with GeoNodes("Point Culling", prefix="Camera"):

        cloud = Cloud(Geometry())

        node = G.camera.relative(link_from='TREE').node

        radius = Float(0, "Radius", min=0, tip="Point radius")

        # Sensor Size
        half_width  = node.sensor_width/2
        half_height = node.sensor_height/2

        # Out of the sensor
        ignore = node.position.z > radius
        proj   = node.projection

        size = radius * node.ratio

        ignore |= proj.x < -half_width - size
        ignore |= proj.x > half_width + size
        ignore |= proj.y < -half_height - size
        ignore |= proj.y > half_height + size

        cloud.points[ignore].delete().out()

        ignore.out("Ignore")
        (-ignore).out("Keep")
        node.position.out("Position")
        node.projection.out("Projection")
        node.ratio.out("Ratio")
        size.out("Apparent Size")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Edge Culling

    with GeoNodes("Edge Culling", prefix="Camera") as tree:

        mesh = Mesh()

        node = G.camera.relative(link_from='TREE').node

        # Both indices are behind
        i1 = nd.edge_vertices.vertex_index_1
        i2 = nd.edge_vertices.vertex_index_2
        ignore = mesh.points.sample_index(node.behind, i1) & mesh.points.sample_index(node.behind, i2)

        # Edges positions
        A = mesh.points.sample_index(node.projection, i1)
        B = mesh.points.sample_index(node.projection, i2)

        # Closest point C is the projection of origin on AB line: AO.AB

        AB = B - A
        t = -(A.dot(AB))

        l = AB.length
        C = A.switch(t > 0, B.switch(t < l, A + AB*(t/l)))

        diag2 = node.sensor_width**2 + node.sensor_height**2
        ignore |= C.dot(C) > diag2


        mesh.edges[ignore].delete().out()

        ignore.out("Ignore")
        (-ignore).out("Keep")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Face Culling

    with GeoNodes("Face Culling", prefix="Camera") as tree:

        mesh = Mesh()

        use_normal = Boolean(True, "Use Normal", tip="Delete faces facing outwards the camera direction")

        # ----- Normal

        with Layout("Normal"):

            cam_info = nd.active_camera.info(transform_space='RELATIVE')

            normal = mesh.faces.sample_index(nd.normal, nd.index)
            pos = nd.position - cam_info.location

            mesh.faces.store("Ignore", pos.dot(normal).greater_than(0.1).switch(-use_normal))

        # ----- Points on the surface

        node = G.camera.relative().node
        flat = Mesh(mesh)
        flat.points.store("Behind Count", Integer(node.behind))
        flat.points.position = node.projection

        # Sensor Size
        half_width  = node.sensor_width/2
        half_height = node.sensor_height/2

        with Repeat(mesh=mesh, iterations=mesh.faces.count) as rep:

            flat_face = Mesh(flat).faces[nd.index.not_equal(rep.iteration)].delete()

            delete = flat_face.points.attribute_statistic(Integer.Named("Behind Count")).sum.equal(flat_face.points.count)

            area = flat_face.faces.sample_index(nd.face_area, 0)
            subdiv = 7

            cloud = flat_face.subdivide(subdiv).points.to_points()

            x, y = nd.position.x, nd.position.y
            delete |= x < -half_width
            delete |= x >  half_width
            delete |= y < -half_height
            delete |= y >  half_height

            cloud.points[delete].delete_all()

            rep.mesh.faces[rep.iteration].store("Ignore", Boolean.Named("Ignore") | cloud.points.count.equal(0))

        mesh = rep.mesh

        mesh.faces[Boolean.Named("Ignore")].delete()

        mesh.out()

# =============================================================================================================================
# Sierpinski triangle

def sierpinski():

    with GeoNodes("Sierpinski Triangle"):

        print("="*10, "Sierpinski")

        size        = Float(1, "Size", min=1)
        iterations  = Integer(5, "Iterations", min=0, max=20)
        precision   = Integer(2, "Precision", min=1, max=7)
        material    = Material(None, "Material")

        iterations += gnmath.log(size, 2).to_integer()

        iterations += Integer(1).switch(nd.is_viewport)
        total_max = Integer(10000000).switch(nd.is_viewport, 1000000)

        prec = Float(.1)**precision
        prec *= Float(.1).switch(nd.is_viewport, 1)

        cloud = Cloud.Points(1, position=0)
        cloud.points.radius = size


        with Repeat(cloud=cloud, iterations=iterations) as rep:

            node = G.camera.relative().node

            total = rep.cloud.points.count

            with rep.cloud.points.for_each(position=nd.position, radius=nd.radius, ratio=node.ratio) as feel:

                new_points = Mesh.Circle(3, radius=feel.radius).points.to_points()
                new_points.transform(translation=feel.position)
                new_points.points.radius = feel.radius/2

                feel.generated.geometry = new_points.switch( (feel.ratio*feel.radius < prec) | (total > total_max), feel.element)

            cloud = Cloud(feel.generated.geometry)

            rep.cloud = G.camera.point_culling(geometry=cloud, radius=nd.radius*2, link_from='TREE')

            #rep.cloud = feel.generated.geometry

        # ----- Finalization

        cloud = Cloud(rep.cloud)

        fractal = Mesh(cloud.points.instance_on(instance=Mesh.Circle(3, fill_type='NGON'), scale=nd.radius*2).realize())

        fractal.set_material(material)

        fractal.out()

# =============================================================================================================================
# Multi res grid

def multires_grid():

    with GeoNodes("Multires Grid"):

        size_x = Float(10, "Size X", min=1)
        size_y = Float(10, "Size Y", min=1)
        size_z = Float(1,  "Size Z", min=0)
        prec   = Float(10, "Precision", min=0, tip="Precision in 1000th")/1000 * Integer(1).switch(nd.is_viewport, 10)

        size = gnmath.sqrt(size_x**2 + size_y**2)

        cloud = Cloud.Points(1)
        cloud.points.store("Size", (size_x, size_y, size_z))
        cloud.points.store("Stop", False)

        max_points = 10000000 * Integer(10).switch(nd.is_viewport, 1)

        with Repeat(cloud=cloud, iterations=15, iter_scale=1.) as rep:

            count = rep.cloud.points.count

            keep   = Cloud(rep.cloud).points[Boolean.Named("Stop")].separate()
            divide = Cloud(keep.inverted_)

            divide.points.store("Size", rep.iter_scale)

            rep.iter_scale /= 2

            # Hidden points
            radius = size*rep.iter_scale
            node = G.camera.point_culling(divide, radius=radius, link_from='TREE').node

            divide.points.store("Stop", node.ignore)

            # Small apparent size
            remote_size = radius*node.ratio
            divide.points.store("Stop", Boolean.Named("Stop") | (count > max_points) | (remote_size < prec))

            keep_ = divide.points[Boolean.Named("Stop")].separate()
            keep += keep_

            divide = Cloud(keep_.inverted_)

            # Now, we can divide
            square = Mesh.Grid(size_x=size_x, size_y=size_y, vertices_x=2, vertices_y=2).points.to_points()

            new_squares = Cloud(divide.points.instance_on(instance=square, scale=rep.iter_scale).realize())

            rep.cloud = keep + new_squares

        cloud = rep.cloud

        square = Mesh.Grid(size_x=size_x, size_y=size_y, vertices_x=2, vertices_y=2)

        surface = Mesh(cloud.points.instance_on(instance=square, scale=Float.Named("Size")).realize())
        surface = surface.merge_by_distance()


        surface.out()

# =============================================================================================================================
# Fractals

def romanesco():
    """ Some fractals such as Romanesco Cabbage

    These 3D fractals replace a single point by other points.
    Each point has a radius allowing to cull points outside the camera and to
    limit the fractal depth.

    A point has the following attributes:
    - radius (Float) : size
    - Up (Vector) : upwards direction

    A fractal iteration replaces each point by other points applying the fractal specific shrink factor.

    Deform Shape
    ============

    Deforms the point to be less annoying

    Arguments
    ---------
    - Geometry : Geometry with points
    - Twist (Angle) : twist angle per meter
    - Bend (Angle) : ben angle per meter
    """

    with GeoNodes("Deform Shape", prefix="Fractal"):

        cloud = Cloud(Geometry())

        twist          = Float.Angle(0, "Twist")
        bend           = Float.Angle(0, "Bend")
        bend_direction = Float.Angle(0, "Bend Direction")
        scale          = Float(1,       "Scale")

        x, y, z = nd.position.xyz

        twist_rot = Rotation((0, 0, twist*z))

        bend_rot  = Rotation((bend*z, 0, 0)) @ Rotation((0, 0, bend_direction))

        rot = twist_rot @ bend_rot

        transform = Matrix.Transform(rotation=rot, scale=scale)

        cloud.points.position = transform @ nd.position
        cloud.points.store("Up", transform @ Vector.Named("Up"))

        cloud.out()

    # ====================================================================================================
    # Points Iterator
    #
    # Replace points by a set of points

    with GeoNodes("Points Iterator", prefix="Fractal", is_group=True):

        model      = Cloud(None,    "Model", tip="Cloud of points with 'Up' Vector attribute")
        mesh       = Mesh(None,     "Final Mesh")
        keep_iter  = Boolean(False, "Keep Iterated")
        use_normal = Boolean(False, "Use Normal")
        prec       = Float(10,      "Precision", min=0, tip="Precision in 1000th")/1000 * Integer(1).switch(nd.is_viewport, 10)
        rot_scale  = Float(0,       "Rotation Scale")
        disp_scale = Float(0,       "Displacement Scale", min=0)
        iterations = Integer(5,     "Iterations", min=0, max=20, tip="Number of iterations (CAUTION !)")
        seed       = Integer(0,     "Seed")

        twist      = Float.Angle(0, "Twist")
        bend       = Float.Angle(0, "Bend")

        # ===== Model size

        bbox = model.bounding_box

        p0, p1 = bbox.min_, bbox.max_
        size = (p1 - p0).length

        z0, z1 = p0.z, p1.z
        height = z1 - z0

        # ===== Control random seed for each point

        model.points.store("Seed",     seed.hash_value(nd.index))
        model.points.store("Normal",   Vector((0, 0, 1)).switch(use_normal, Vector.Named("Normal")))
        model.points.store("Rotation", Rotation().switch(use_normal, Rotation.AlignToVector(Vector.Named("Normal"))))

        # ===== Twist and bending

        x, y, z = nd.position.xyz

        twist_rot = Rotation((0, 0, twist*z))
        bend_rot  = Rotation((bend*z, 0, 0)) @ Rotation((0, 0, bend_direction))
        rot = twist_rot @ bend_rot

        model.points.store("Deform", rot)

        # ===== Base point

        cloud = Cloud.Points(1)

        cloud.points.radius = 1.
        cloud.points.store("Iterate",  True)
        cloud.points.store("Seed",     seed)
        cloud.points.store("Normal",   (0, 0, 1))
        cloud.points.store("Rotation", Rotation())

        # ===== Maximum points

        max_points = 10000000 * Integer(10).switch(nd.is_viewport, 1)

        # ===== Iteration loop

        with Repeat(cloud = cloud, iterations=iterations, iteration_max=0) as rep:

            cloud = rep.cloud

            # ===== We continue only if the max number of points is not reached

            npoints = cloud.points.count
            still_ok = npoints < max_points

            # ===== Visible points to iterate

            with Layout("Visible points to iterate"):
                node = G.camera.point_culling(cloud, radius=nd.radius*size, link_from='TREE').node
                cloud.points[Boolean.Named("Iterate")].store("Iterate", still_ok & node.keep & (node.apparent_size > prec))

            # ===== Keep track when iterations finishes

            with Layout("Where iteration terminates"):
                rep.iteration_max = rep.iteration.switch(cloud.points.attribute_statistic(Boolean.Named("Iterate")).sum.equal(0), rep.iteration_max)

            # ===== Fractal iteration

            with Layout("Iterate: replace points by the model"):

                with Layout("Copy attributes"):
                    cloud.points.store("Main Seed",     Integer.Named("Seed"))
                    cloud.points.store("Main Radius",   nd.radius)
                    cloud.points.store("Main Normal",   Rotation.Named("Deform"))
                    cloud.points.store("Main Rotation", (Rotation((0, 0, twist)) @ Rotation((bend, 0, 0))) @ Rotation.Named("Rotation"))

                with Layout("Replacement"):
                    new_cloud = Cloud(cloud.points[Boolean.Named("Iterate")].instance_on(instance=model, rotation=Rotation.Named("Main Rotation"), scale=nd.radius).realize())

                with Layout("Attributes of next iteration"):
                    new_cloud.points.store("Seed", Integer.Named("Main Seed").hash_value(Integer.Named("Seed")))
                    new_cloud.points.radius = nd.radius * Float.Named("Main Radius")

                    new_cloud.points.store("Normal",   Rotation.Named("Main Rotation") @ Vector.Named("Normal"))
                    new_cloud.points.store("Rotation", Rotation.Named("Rotation") @ Rotation.Named("Main Rotation"))

                with Layout("Displacement Noise"):
                    new_cloud.points.position += G.random.normal_vector(0, disp_scale*nd.radius, id=Integer.Named("Seed"), seed=Integer.Named("Seed"))

                # Done

                del_points  = Cloud(cloud).points[Boolean.Named("Iterate")].delete()
                keep_points = Cloud(cloud).points.store("Iterate", False)

                rep.cloud = del_points.switch(keep_iter, keep_points) + new_cloud

        cloud = rep.cloud

        Boolean(True).info("Points: " + cloud.points.count.to_string() + " after " + rep.iteration_max.to_string() + " iterations.")

        # ===== Set a mesh to each remaining point

        with Layout("Remove attributes"):
            cloud.remove_named_attribute("Iterate")
            cloud.remove_named_attribute("Main Seed")
            cloud.remove_named_attribute("Main Radius")
            cloud.remove_named_attribute("Main Deform")
            cloud.remove_named_attribute("Main Rotation")

        cloud.points.store("Random", Float.Random(0, 1, Float.Named("Seed")))

        fractal = Mesh(cloud.points.instance_on(instance=mesh, rotation=Rotation.Named("Rotation"), scale=nd.radius).realize())

        with Layout("Remove attributes"):
            fractal.remove_named_attribute("Deform")
            fractal.remove_named_attribute("Rotation")

        cloud.out("Points")
        fractal.out("Mesh")

    # ====================================================================================================
    # Mesh iterator

    with GeoNodes("Mesh Iterator", prefix="Fractal"):

        mesh         = Mesh()
        size         = Float(100, "Size")
        model_shrink = Float.Factor(1, "Model Shrink", min=0, max=10)
        shrink       = Float.Factor(.5, "Shrink Factor", min=.001, max=.999)
        use_faces    = Boolean(True, "Use Faces", tip="Use faces rather than points")
        add_central  = Boolean(False, "Add Central Points")
        material     = Material(None, "Material")
        smooth       = Boolean(False, "Shade Smooth")

        # ===== Build the model from the input mesh

        with Layout("Build the model from the input mesh"):

            mesh.transform(scale=size)

            point_model = mesh.points.to_points()
            point_model.points.store("Normal", mesh.points.sample_index(nd.normal, nd.index))

            face_model = mesh.faces.to_points()
            face_model.points.store("Normal", mesh.faces.sample_index(nd.normal, nd.index))

            model = point_model.switch(use_faces, face_model)

            central_point = Cloud.Points(1)
            central_point.points.store("Normal", (0, 0, 1))

            model = model.switch(add_central, model + central_point)
            model.points.radius = shrink

            model.transform(scale=model_shrink)

        if False:
            test = model.points.instance_on(Mesh.Line(), rotation=Rotation.AlignToVector(Vector.Named("Normal")))
            test.out()

        # ===== Iterates

        node = G.fractal.points_iterator(model=model, final_mesh=mesh, link_from='TREE').node

        fractal = node.mesh
        fractal.faces.smooth = smooth
        fractal.faces.material = material

        fractal.out()


    # ====================================================================================================
    # Mesh iterator








































def face_fractals():
    """ Fractals built by replacing a face by several ones
    """

    with GeoNodes("Faces Iterator"):

        iterator      = Mesh()
        iterations    = Integer(5, "Iterations", min=0, max=10)
        scale         = Float(.5, "Scale Factor")

        cam_culling   = Boolean(True,     "Camera Culling")
        aspect_ratio  = Float(16/9,       "Aspect Ratio", tip="Camera aspect ratio, 16/9 for instance")
        focal_length  = Float.Distance(1, "Focal Length", min=0.01)


        iterations = (iterations + 1).switch(nd.is_viewport, iterations)

        # ::::: The mesh to iterate

        iterator.faces.store("Scale", scale)

        fractal = Mesh.Grid(size_x=1, size_y=1, vertices_x=2, vertices_y=2)
        fractal.faces.store("Scale", 1)

        with Repeat(fractal=fractal, iterations=iterations) as rep:

            fractal = rep.fractal
            fractal.faces.store("Pos", nd.position)
            fractal.faces.store("rot", Rotation.AlignToVector(nd.normal))

            cloud = Cloud.Points(rep.fractal.faces.count)
            cloud.points.position = fractal.faces.sample_index(Vector.Named("Pos"), nd.index)
            cloud.points.store("rot", fractal.faces.sample_index(Rotation.Named("rot"), nd.index))
            cloud.points.store("old_scale", fractal.faces.sample_index(Float.Named("Scale"), nd.index))

            step = Mesh(cloud.points.instance_on(instance=iterator, scale=Float.Named("old_scale"), rotation=Rotation.Named("rot")).realize())

            step.faces.store("Scale", Float.Named("old_scale") * Float.Named("Scale"))

            # Camera culling

            culled = Mesh(step).points.store("invisible", Float(culled_position(nd.position, aspect_ratio, focal_length)))
            culled.faces.store("delete", Float.Named("invisible"))
            culled.faces[Float.Named("delete").equal(1)].delete_all()
            step = step.switch(cam_culling, culled)

            rep.fractal = step

        fractal = rep.fractal

        fractal.out()




# =============================================================================================================================
# Split segments

def split_segments():

    with GeoNodes("Split Segments"):

        sides       = Integer(3, "Sides", min=3, max=10)
        iterations  = Integer(5, "Iterations", min=0, max=10)
        external    = Boolean(True, "External")
        noise_scale = Float(0, "Noise Scale")
        seed        = Integer(0, "Seed")

        triangle = Mesh.Circle(vertices=sides)
        angle = Float(pi/3).switch(external, -pi/3)

        with Repeat(triangle=triangle, seed=seed, iterations=iterations) as rep:

            rep.seed = rep.seed.hash_value(rep.iteration)

            node = nd.edge_vertices
            with rep.triangle.edges.for_each(p1=node.position_1, p2=node.position_2) as feel:

                new_edges = Mesh.Line(start_location=feel.p1, end_location=feel.p2, count=5)
                v = (feel.p2 - feel.p1)/3

                ns = noise_scale * v.length
                noise_vector = Vector((ns, ns, 0))

                new_edges.points[1].position = feel.p1 + v + Float.Random(-noise_vector, noise_vector, rep.seed)
                new_edges.points[3].position = feel.p2 - v  + Float.Random(-noise_vector, noise_vector, rep.seed + 1)

                w = Rotation((0, 0, angle)) @ v
                new_edges.points[2].position = feel.p1 + v + w  + Float.Random(-noise_vector, noise_vector, rep.seed + 2)

                feel.generated.geometry = new_edges

            rep.triangle = feel.generated.geometry

        rep.triangle.out()

# =============================================================================================================================
# Fern

def fern():

    with GeoNodes("Fern"):

        iterations   = Integer(5, "Iterations", min=0, max=10)
        angle        = Float.Angle(pi/20, "Grow Angle")
        grow_factor  = Float.Factor(.9, "Grow Factor", min=.01, max=.99)
        sub_angle    = Float.Angle(pi/5, "Sub Angle")
        sub_factor   = Float.Factor(.3, "Sub Factor", min=.01, max=.99)
        angle_noise  = Float(0, "Angle Noise")
        factor_noise = Float(0, "Factor Noise")
        seed         = Integer(0, "Seed")

        leaf = Mesh.Line(start_location=0, end_location=(1, 0, 0), count=2)
        leaf.edges.store("Use", True)

        with Repeat(leaf=leaf, seed=seed, iterations=iterations) as rep:

            rep.seed = rep.seed.hash_value(rep.iteration)

            node = nd.edge_vertices
            with rep.leaf.edges.for_each(p1=node.position_1, p2=node.position_2, seed=rep.seed) as feel:

                hv = rep.seed.hash_value(feel.index)

                v = feel.p2 - feel.p1
                l = v.length

                edge = Mesh(feel.element)
                extrude = edge.edges.sample_index(Boolean.Named("Use"), 0)

                loop_angle  = angle       + Float.Random(-angle*angle_noise, angle*angle_noise, hv)
                loop_ag     = sub_angle   + Float.Random(-sub_angle*angle_noise, sub_angle*angle_noise, hv + 1)
                loop_factor = grow_factor + Float.Random(-factor_noise, factor_noise, hv + 2)
                loop_fac    = sub_factor  + Float.Random(-factor_noise, factor_noise, hv + 3)

                edge.points[1].extrude(Rotation((0, 0, loop_angle)) @ (v*loop_factor))
                edge.points[1].extrude(Rotation((0, 0, -loop_angle - loop_ag)) @ (v*loop_fac))
                edge.points[1].extrude(Rotation((0, 0,  loop_angle + loop_ag)) @ (v*loop_fac))

                edge.edges.store("Use", True)
                edge.edges[0].store("Use", False)
                feel.generated.geometry  = feel.element.switch(extrude, edge)

            leaf = feel.generated.geometry #.merge_by_distance()
            rep.leaf = leaf

        rep.leaf.out()

def points_fractal():

    with GeoNodes("Points Fractal"):

        iterations   = Integer(1,  "Iterations", min=0, max=10)
        radius       = Float(  1,  "Radius", min=.1)
        ratio        = Float(  3,  "Height Ratio", min=.2)
        peak         = Float(  3,  "Peak", min=.5)
        turns        = Float(  5,  "Turns")
        count        = Integer(10,  "Children Count", min=2)
        scale        = Float( .8,  "Scale")
        twist        = Float.Angle(0, "Twist")
        input_model  = Object(None, "Points to Iterate")

        # ----- Model to iterate

        num_model = 3

        if num_model == 0:
            model = Curve.Circle(count, radius=radius)
            model.points.store("Direction", nd.position.normalize())
            model.points.store("Scale",     1/count)
            model = model.to_points()

        elif num_model == 1:
            model = Mesh.UVSphere(segments=3, rings=2, radius=1)
            model.points[nd.position.z < -.1].delete()
            model.points.store("Direction", nd.position.normalize())
            model.points.store("Scale",     1)
            model = model.points.to_points()

        elif num_model == 2:
            model = Cloud(input_model.info().geometry)

        elif num_model == 3:
            model = Cloud(Geometry())

        # ----- Start from one single point

        fractal = Cloud.Points(1)
        fractal.points.store("Radius", radius)
        fractal.points.store("Direction", (0, 0, 1))
        fractal.points.store("Scale", 1)
        fractal.points.store("Twist", twist)

        # ----- Fractal iteration loop

        with Repeat(fractal=fractal, iterations=iterations) as rep:

            # ----- Loop on the current points

            with rep.fractal.points.for_each(
                    position  = nd.position,
                    scale     = Float.Named("Scale"),
                    direction = Vector.Named("Direction"),
                    twist     = Float.Named("Twist")) as feel:

                rotation = Rotation.AlignToVector(feel.direction)
                rotation = Rotation((0, 0, feel.twist)) @ rotation

                replace = Cloud(model).transform(translation=feel.position, scale=feel.scale, rotation=rotation)

                replace.points.store("Direction", rotation @ Vector.Named("Direction"))
                replace.points.store("Scale", feel.scale * Float.Named("Scale"))
                replace.points.store("Twist", feel.twist + twist)

                feel.generated.geometry = replace

            rep.fractal = feel.generated.geometry

        # ----- Get the generated fractal

        fractal = Cloud(rep.fractal)

        # ----- Geometry on each point

        #rotation = Rotation.AlignToVector(Vector.Named("Direction"))
        #fractal = fractal.points.instance_on(instance=leaf_object.info().geometry, rotation=rotation, scale=Float.Named("Scale"))

        fractal.out()


def romanesco1():

    with GeoNodes("Romanesco1"):

        iterations   = Integer(1,        "Iterations", min=0, max=4)
        npoints      = Integer(100,      "Number of points", min=10, max=500)
        base_radius  = Float(  1,        "Base Radius", min=.1)
        sub_radius_f = Float.Factor(.2,  "Sub Radius Factor", min=.01, max=.9)

        size_factor  = Float.Factor(.99, "Size Factor", min=.9, max=.999)
        up_factor    = Float.Factor(.1,  "Up Factor", min=0, max=1)
        rho_factor   = Float.Factor(.1,  "Radius Factor", min=0, max=1)
        angle_factor = Float.Factor(1,   "Angle Factor", min=.1, max=10)

        # ----- We build the base model by turning around a cone

        pyramid = Cloud.Points(npoints)

        with Repeat(pyramid=pyramid, rho=base_radius, theta=0., z=0., size=base_radius*sub_radius_f, iterations=npoints) as rep:

            pos = Vector((rep.rho*gnmath.cos(rep.theta), rep.rho*gnmath.sin(rep.theta), rep.z))

            cur_point = nd.index.equal(rep.iteration)

            rep.pyramid.points[cur_point].position = pos
            rep.pyramid.points[cur_point].store("Size",  rep.size)
            rep.pyramid.points[cur_point].store("Scale", rep.size)

            dz     = up_factor*rep.size
            drho   = rho_factor*rep.size
            dtheta = angle_factor*rep.size/rep.rho

            normal = Rotation((0, 0, rep.theta)) @ Vector((dz, 0, drho))
            rep.pyramid.points[cur_point].store("Direction", normal.normalize())

            rep.size *= size_factor

            rep.rho -= drho
            rep.theta += dtheta
            rep.z += dz

        rep.pyramid.out()

# =============================================================================================================================
# Logarithmic spiral

def log_spiral():

    with GeoNodes("Logarithmic Spiral"):

        count      = Integer(500, "Count")
        radius     = Float(1,     "Radius")
        omega      = Float(.8,    "Omega")
        rotations  = Float(3,     "Rotations")
        height     = Float(0,     "Height")

        # ----- Profile curve

        if False:
            profile_obj = Object(None, "Profile Curve", tip="Curve in (x, z): x -> z")

            def_profile = Curve.Line(start=(0, 0, height), end=(radius, 0, 0))
            profile = profile_obj.info().geometry.curve
            profile = profile.switch(profile.points.count < 2, def_profile)

        # ----- Logarithmic spiral

        slope = height/radius

        curve = Curve.Line().resample(count)

        theta =  tau*rotations/count*nd.index
        rho = radius*gnmath.abs(omega)**theta
        theta *= gnmath.sign(omega)

        curve.points.position = (rho*gnmath.cos(theta), rho*gnmath.sin(theta), height - rho*slope)

        # ----- Normal to the cone

        normal = curve.points.position*(1, 1, 0)
        normal = Rotation((0, 0, theta)) @ Vector((height, 0, radius))
        curve.points.store("Normal", normal.normalize())

        curve.out()

# =============================================================================================================================
# Romanesco cabbage

def romanesco2():

    with GeoNodes("Romanesco Cabbage"):

        iterations   = Integer(1,        "Iterations", min=0, max=3)
        nspirals     = Integer(6,        "Number of spirals", min=3, max=12)
        radius       = Float(1,          "Radius", min=.1)
        height       = Float(2,          "Height", min=.1)
        omega        = Float(.7,         "Omega")
        rotations    = Float(4,          "Rotations")
        upwards      = Float(4,          "Upwards factor")

        npoints      = Integer(30,       "Number of points", min=3, max=200)
        q            = Float.Factor(.9,  "Shrink Factor", min=.01, max=.99)

        sub_radius_f = Float.Factor(.2,  "Sub Radius Factor", min=.1, max=3)
        f            = Float.Factor(.9,  "Shrink Factor", min=.01, max=.99)
        noise_scale  = Float(0,          "Noise scale")
        seed         = Integer(0,        "Seed")


        iterations = iterations.switch(nd.is_viewport, iterations - 1)

        # ::::: Base Spiral

        with Layout("Base Spiral"):

            spiral = Curve(Group("Logarithmic Spiral", radius=radius, height=height, omega=omega, rotations=rotations).geometry)

            # ::::: Extract points following a geometric series

            # Geometric series:
            # length = size*(1 - q^n)/(1 - q) => size = length*(1 - q)/(1 - q^n)

            length = spiral.length
            size = length*(1 - q)/(1 - q**npoints)

            curve = Curve.Line().resample(npoints)
            l = size*(1 - q**nd.index)/(1 - q)

            curve.points.position = spiral.sample(nd.position, length=l)
            curve.points.store("Scale",  size*q**nd.index)

            # Orient progressively the normal to z
            f = (nd.index/(npoints - 1))**upwards


            normal = spiral.sample(Vector.Named("Normal"), length=l)
            normal = normal.mix(f, (0, 0, 1))
            curve.points.store("Normal", normal)

        #curve.points.store("Normal", spiral.sample(Vector.Named("Normal"), length=l))

        if False:
            curve = curve.points.instance_on(instance=Curve.Line().transform(scale=.3), rotation=Rotation.AlignToVector(Vector.Named("Normal")))
            curve.out()
            return

        # ::::: Duplicate nspirals times

        with Layout("Duplicates"):
            cloud = Cloud.Points(nspirals, position=0)
            cloud.points.store("rot", Rotation((0, 0, tau/nspirals*nd.index)))

            spirals = Curve(cloud.points.instance_on(instance=curve, rotation=Rotation.Named("rot")).realize())
            spirals.points.store("Normal", Rotation.Named("rot") @ Vector.Named("Normal"))
            spirals.remove_named_attribute("rot")

            spirals = spirals.to_points()

        if False:
            spirals = spirals.points.instance_on(instance=Curve.Line().transform(scale=.3), rotation=Rotation.AlignToVector(Vector.Named("Normal")))
            spirals.out()
            return

        # ::::: Iterations

        with Layout("Initial Point"):
            cabbage = Cloud.Points(1)
            cabbage.points.store("Normal", (0, 0, 1))
            cabbage.points.store("Scale", 1.)

        with Repeat(cabbage=cabbage, iterations=iterations) as rep:

            rep_seed = seed.hash_value(rep.iteration)

            cab = rep.cabbage

            rot = Rotation.AlignToVector(Vector.Named("Normal"))
            cab.points.store("rot", rot)
            cab.remove_named_attribute("Normal")

            cab.points.store("old_scale", Float.Named("Scale"))
            cab.remove_named_attribute("Scale")

            with Layout("Instantiate"):
                new_cabbage = Cloud(cab.points.instance_on(instance=spirals,
                    scale     = Float.Named("old_scale"),
                    rotation  = Rotation.Named("rot")
                    ).realize())

            with Layout("Update Scale and Normal attributes"):
                scale = Float.Named("old_scale")*Float.Named("Scale")
                scale *= val_noise(1, noise_scale/5, rep_seed)
                new_cabbage.points.store("Scale",  scale)

                normal = Rotation.Named("rot") @ Vector.Named("Normal")
                normal += vect_noise(0, noise_scale, seed=rep_seed + 1)
                new_cabbage.points.store("Normal", normal.normalize())

            rep.cabbage = new_cabbage

        # ::::: Finalisation

        cabbage = rep.cabbage

        if False:
            spirals = cabbage.points.instance_on(instance=Curve.Line().transform(scale=.3), rotation=Rotation.AlignToVector(Vector.Named("Normal")))
            spirals.out()
            return

        cabbage.points.radius = Float.Named("Scale")

        # ::::: Cone

        with Layout("Complete with cones"):
            cone = Mesh.Cone(radius_bottom=radius, depth=height)
            cone.corners.store("UV Map", cone.uv_map_)
            cone.corners.store("Z", nd.position.z/height)
            cone.faces.material = "Romanesco"

            if False:
                cone.out()
                return

            rot = Rotation.AlignToVector(Vector.Named("Normal"))
            cabbage = Mesh(cabbage.points.instance_on(instance=cone, scale=nd.radius*1, rotation=rot).realize())

            cabbage.faces.smooth = True

        cabbage.out()





def demo():

    # ----- Growing Mesh

    with GeoNodes("Branch"):

        iterations = Integer(10, "Iterations", min=2, max=10)
        extr_scale = Float.Factor(.3, "Extrude Scale", min=.1, max=2)
        branches   = Integer(2, "Branches", min=2, max=6)

        seed       = Integer(0, "Seed")

        line = Mesh.Line(end_location=(0, 0, 1), count=2)

        with Repeat(tree=line, iterations=iterations) as rep:

            rep_seed = rep.iteration.hash_value(seed)

            with rep.tree.edges.for_each() as feel:

                edge = Mesh(feel.element)

                with Layout("Edge direction and length"):
                    p0 = edge.points.sample_index(nd.position, index=0)._lc("P0")
                    p1 = edge.points.sample_index(nd.position, index=1)._lc("P1")
                    direction = (p1 - p0)._lc("Direction")
                    length = direction.length._lc("Length")
                    direction = direction.normalize()

                with Repeat(edge=edge, iterations=branches) as br_rep:

                    br_seed = rep_seed.hash_value(br_rep.iteration)

                    br_length = length*extr_scale*Float.Random(.8, 1.2, id=feel.index, seed=br_seed)
                    br_dir = direction + Vector.Random(-.4, .4, id=feel.index, seed=br_seed + 1)

                    br_rep.edge.points[1].extrude(br_dir*br_length)

                feel.generated.geometry = br_rep.edge

            rep.tree = feel.generated.geometry

        rep.tree.out()

    # ----- Mesh 1

    with GeoNodes("Branch 1"):

        iterations = Integer(10, "Iterations")
        trunk_fac  = Float.Factor(.3, "Trunk Factor", min=0, max=1)
        seed       = Integer(0, "Seed")

        line = Mesh.Line(end_location=(0, 0, 1), count=2)
        line.edges.store_named_attribute("Split", True)

        with Repeat(tree=line, iterations=iterations) as rep:

            rep_seed = rep.iteration.hash_value(seed)

            with rep.tree.edges.for_each() as feel:

                edge = Mesh(feel.element)

                with Layout("Edge direction and length"):
                    p0 = edge.points.sample_index(nd.position, index=0)._lc("P0")
                    p1 = edge.points.sample_index(nd.position, index=1)._lc("P1")
                    direction = (p1 - p0)._lc("Direction")
                    length = direction.length._lc("Length")

                with Layout("First edge: from start to point located around trunk factor"):
                    c  = (p0 + p1)*trunk_fac
                    c += Vector.Random(-.1*length, .1*length, id=feel.index, seed=rep_seed)._lc("Center")

                    new_edges = Mesh.Line(start_location=p0, end_location=c, count=2)
                    new_edges.edges.store_named_attribute("Split", False)

                with Layout("Extrude till end point"):
                    new_edges.points[1].extrude(p1 - c)
                    new_edges.edges[1].store_named_attribute("Split", True)

                with Layout("Extrude in another direction"):
                    direction += Vector.Random(-.4*length, .4*length, id=feel.index, seed=rep_seed + 1)
                    length *= (1 - trunk_fac)*Float.Random(.8, 1.2, id=feel.index, seed=rep_seed + 2)

                    new_edges.points[1].extrude(direction.normalize()*length)
                    new_edges.edges[2].store_named_attribute("Split", True)

                with Layout("Keep element if not split"):
                    feel.generated.geometry = edge.switch(edge.edges.sample_index(Boolean.Named("Split"), 0), new_edges)

            rep.tree = feel.generated.geometry

        rep.tree.out()


    # ----- Curve

    with GeoNodes("Branch Curve"):

        iterations = Integer(10, "Iterations")
        seed       = Integer(0, "Seed")

        fr = Curve.Line(end=(0, 0, 1))

        with Repeat(curve=fr, iterations=iterations) as rep:

            rep_seed = rep.iteration.hash_value(seed)

            with rep.curve.splines.for_each() as feel:

                segment = Curve(feel.element)
                p0 = segment.points.sample_index(nd.position, index=0)
                p1 = segment.points.sample_index(nd.position, index=1)

                segment.resample(3)

                segment.points[1].offset = Vector.Random(-.1, .1, id=feel.index, seed=rep_seed)

                direction = p1 - p0
                length = direction.length

                direction += Vector.Random(-.3, .3, id=feel.index, seed=rep_seed + 1)
                length *= Float.Random(.8, 1.2, id=feel.index, seed=rep_seed + 2)


                new_segment = Curve.Line(start=segment.points.sample_index(nd.position, index=1), direction=direction.normalize(), length=length)

                feel.generated.geometry = segment + new_segment


            rep.curve = feel.generated.geometry

        rep.curve.out()
