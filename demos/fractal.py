import numpy as np

#from random import Random

from .. import nd, snd, gnmath, GeoNodes, ShaderNodes, Group, G
from .. import Geometry, Mesh, Curve, Cloud, Material
from .. import Repeat, Simulation, Layout
from .. import Boolean, Integer, Float, Vector, Rotation, Matrix, Color
from .. import pi, tau

SENSOR_SIZE = .1

# =============================================================================================================================
# Utilities and macros

# -----------------------------------------------------------------------------------------------------------------------------
# Random normal

def random_normal():

    with GeoNodes("Random Normal Value", is_group=True):

        value = Float(0,   "Value")
        scale = Float(1,   "Scale")
        seed  = Integer(0, "Seed")

        x1 = Float.Random(0, 1, seed=seed)
        x2 = Float.Random(0, 1, seed=seed.hash_value(seed))

        y1 = gnmath.sqrt(-2*gnmath.log(x1))*gnmath.cos(2*np.pi*x2)

        y = value + scale*y1

        y.out("Value")

    with GeoNodes("Random Normal Vector", is_group=True):

        vector = Vector(0,   "Vector")
        scale  = Vector(1,   "Scale")
        seed   = Integer(0,  "Seed")

        v = Vector((
            G.random_normal_value(vector.x, scale.x, seed),
            G.random_normal_value(vector.y, scale.y, seed + 1),
            G.random_normal_value(vector.z, scale.z, seed + 2),
        ))

        v.out("Vector")

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

        focal_length *= 2.54/50*SENSOR_SIZE

        cam_info = nd.active_camera.info(transform_space='RELATIVE')

        rot = cam_info.rotation.invert()
        pos = rot @ (nd.position - cam_info.location)

        behind = pos.z > - focal_length

        t = -focal_length/pos.z

        proj = Vector((pos.x*t, pos.y*t, 0))

        pos.out("Position")
        proj.out("Projection")
        t.out("Ratio")
        behind.out("Behind")

        # Sensor Size
        height = SENSOR_SIZE
        width  = aspect_ratio*height

        width.out("Sensor Width")
        Float(height).out("Sensor Height")

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
        ignore = node.behind
        proj   = node.projection

        size = radius * node.ratio

        ignore |= proj.x < -half_width - size
        ignore |= proj.x > half_width + size
        ignore |= proj.y < -half_height - size
        ignore |= proj.y > half_height + size

        cloud.points[ignore].delete().out()

        ignore.out("Ignore")
        (-ignore).out("Keep")

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
            subdiv = 7 #gnmath.max(5, gnmath.log(area, 2)/SENSOR_SIZE)

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
        material    = Material(None, "Material")

        iterations += gnmath.log(size, 2).to_integer()

        cloud = Cloud.Points(1, position=0)
        cloud.points.radius = size

        with Repeat(cloud=cloud, iterations=iterations) as rep:

            node = G.camera.relative().node

            total = rep.cloud.points.count

            with rep.cloud.points.for_each(position=nd.position, radius=nd.radius, ratio=node.ratio) as feel:

                new_points = Mesh.Circle(3, radius=feel.radius).points.to_points()
                new_points.transform(translation=feel.position)
                new_points.points.radius = feel.radius/2

                feel.generated.geometry = new_points.switch( (feel.ratio*feel.radius < .01*SENSOR_SIZE) | (total > 1000000), feel.element)

            cloud = Cloud(feel.generated.geometry)

            rep.cloud = G.camera.point_culling(geometry=cloud, radius=nd.radius*2, link_from='TREE')

            #rep.cloud = feel.generated.geometry

        # ----- Finalization

        cloud = Cloud(rep.cloud)

        fractal = Mesh(cloud.points.instance_on(instance=Mesh.Circle(3, fill_type='NGON'), scale=nd.radius*2).realize())

        fractal.set_material(material)

        fractal.out()

        return




        # ::::: The mesh to iterate

        triangle = Mesh.Circle(vertices=3, fill_type='NGON').transform(rotation=(0, 0, pi/2))

        iterator = Mesh(triangle.points.instance_on(instance=triangle).realize())
        iterator = iterator.merge_by_distance().transform(scale=2/3)

        fractal = Group("Faces Iterator", mesh=iterator, iterations=iterations, scale_factor=.5, camera_culling=cam_culling, aspect_ratio=aspect_ratio, focal_length=focal_length).geometry

        fractal.out()



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
# Sierpinski triangle

def sierpinski_OLD():

    with GeoNodes("Sierpinski OLD"):

        iterations  = Integer(5, "Iterations", min=0, max=10)
        rotation    = Float.Factor(0, "Rotation", min=-1, max=1)
        noise_scale = Float(0, "Noise Scale")
        seed        = Integer(0, "Seed")

        triangle = Mesh.Circle(vertices=3, fill_type='NGON')

        with Repeat(triangle=triangle, seed=seed, iterations=iterations) as rep:

            rep.seed = rep.seed.hash_value(rep.iteration)

            i0 = nd.offset_corner_in_face(nd.corners_of_face().corner_index, offset=0)
            i1 = nd.offset_corner_in_face(nd.corners_of_face().corner_index, offset=1)
            i2 = nd.offset_corner_in_face(nd.corners_of_face().corner_index, offset=2)

            p0 = rep.triangle.points.sample_index(nd.position, nd.vertex_of_corner(i0))
            p1 = rep.triangle.points.sample_index(nd.position, nd.vertex_of_corner(i1))
            p2 = rep.triangle.points.sample_index(nd.position, nd.vertex_of_corner(i2))

            with rep.triangle.faces.for_each(p0=p0, p1=p1, p2=p2, seed=rep.seed) as feel:

                sn = (p1 - p0).length*noise_scale
                nv1 = Vector((sn, sn, 0))
                nv0 = -nv1

                #p0 = feel.p0 + Vector.Random(nv0, nv1, feel.seed)
                #p1 = feel.p1 + Vector.Random(nv0, nv1, feel.seed + 1)
                #p2 = feel.p2 + Vector.Random(nv0, nv1, feel.seed + 2)

                p0, p1, p2 = feel.p0, feel.p1, feel.p2

                f = .5 + rotation/2
                f_ = 1 - f

                q0 = (f*p0 + f_*p1)._lc("q0")
                q1 = (f*p1 + f_*p2)._lc("q1")
                q2 = (f*p2 + f_*p0)._lc("q2")

                q0 += Vector.Random(nv0, nv1, feel.seed)
                q1 += Vector.Random(nv0, nv1, feel.seed + 1)
                q2 += Vector.Random(nv0, nv1, feel.seed + 2)

                tri0 = Mesh.Circle(vertices=3, fill_type='NGON')
                tri0.points[0].position = p0
                tri0.points[1].position = q0
                tri0.points[2].position = q2

                tri1 = Mesh(tri0)
                tri1.points[0].position = q0
                tri1.points[1].position = p1
                tri1.points[2].position = q1

                tri2 = Mesh(tri0)
                tri2.points[0].position = q1
                tri2.points[1].position = p2
                tri2.points[2].position = q2


                feel.generated.geometry = tri0.join(tri1, tri2)


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

def romanesco():

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
