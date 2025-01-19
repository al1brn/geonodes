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

module : demo fractal
-------------------

Fractals and linked things.

updates
-------
- created :   2025/01/12

$ DOC transparent = False

$ DOC START

[Source Code](../demos/fractal.py)

> [!CAUTION]
> This module is still work in progress

This module provides several independant features:
- Random normal: normal law implementation for values and vectors
- Camera culling: culls points, edges and faces which are not visible in the field of view of the camera
- Multi resolution: surfaces with a resolution depending on the distance to the camera
- Fractals: diving into fractals

All the modifiers can be generated using demo function.
Specific modifiers can be generated using specic functions:
- random_normal : random modifiers
- camera_culling : camera culling modifiers
- multires_surface : multi resolution modifiers
- sierpinski : sierpinski fractal
- romanesco : other fractals



> [!NOTE]
> Modifiers:
> - Random Normal Value
> - Random Normal Vector
> - Random Shake Vectors
> - Camera Projection
> - Camera Point Culling
> - Camrea Edge Culling
> - Camera Face Culling
> - Sierpinski Triangle
> - Multires Surface
> - Multires Faces
> - DEMO Multires Faces
> - Fractal Cloud Iterator
> - Fractal Mesh Iterator
> - Fractal Cone Iterator
> - Logarithmic Spiral
> - Romanesco Cabbage (In progress)

``` python
from geonodes.demos import fractal

fractal.demo()
```
"""

import numpy as np

from geonodes import *

if False:
    from .. import nd, snd, gnmath, GeoNodes, ShaderNodes, Group, G
    from .. import Geometry, Mesh, Curve, Cloud, Material, String, Texture, Shader
    from .. import Face
    from .. import Repeat, Simulation, Layout, Panel
    from .. import Boolean, Integer, Float, Vector, Rotation, Matrix, Color
    from .. import pi, tau

# Prefixes

random_   = G("Random")
camera_   = G("Camera")
fractal_  = G("Fractal")
multires_ = G("Multires")


FOCAL_FACTOR = .04939

def test():

    from geonodes.core.socket_class import Switch

    with GeoNodes("Test"):

        geo = Geometry()
        cone = Mesh.Cone()
        cond = Boolean(True, "Cone")

        res = Switch(cone) if cond else geo

        res.out()

# =============================================================================================================================
# Demo

def demo(clear=False):
    if clear:
        GeoNodes.remove_groups()

    random_normal()
    camera_culling()
    sierpinski()
    multires_surface()
    romanesco()
    growing()


# =============================================================================================================================
# Utilities and macros

# -----------------------------------------------------------------------------------------------------------------------------
# Random normal

def random_normal():

    # Macro
    def expand_seed(seed, n):

        MAX_INT = 1 << 31 - 1

        with Layout(f"Expand Seed {n} Times"):

            cloud = Cloud.Points(n)
            values = Integer.Random(0, MAX_INT, seed=seed)

            seeds = ()
            for i in range(n):
                seeds = seeds + (cloud.points.sample_index(values, i)._lc(f"Seed {i}"),)

        return seeds

    with GeoNodes("Normal Value", is_group=True, prefix=random_):

        value = Float(0,   "Value")
        scale = Float(1,   "Scale")
        ID    = Integer(0, "ID")
        seed  = Integer(0, "Seed")

        seed0, seed1 = expand_seed(seed, 2)

        x1 = Float.Random(0, 1, id=ID, seed=seed0)
        x2 = Float.Random(0, 1, id=ID, seed=seed1)

        y1 = gnmath.sqrt(-2*gnmath.log(x1))*gnmath.cos(2*np.pi*x2)

        y = value + scale*y1

        y.out("Value")

    with GeoNodes("Normal Vector", is_group=True, prefix=random_):

        length = Float(1,       "Length",   tip="Vector average length")
        scale  = Float(0,       "Scale",    tip="Length scale")
        two_d  = Boolean(False, "2D", tip="2D Vectors (Z = 0)")
        ID     = Integer(0,      "ID")
        seed   = Integer(0,      "Seed")

        # ===== We need 3 different seeds

        seed0, seed1, seed2 = expand_seed(seed, 3)

        # ===== 2D normalized vectors

        with Layout("Unit 2D vector"):
            theta    = Float.Random(0, 2*pi, seed=seed0)
            normal2D = Vector((gnmath.cos(theta), gnmath.sin(theta), 0))

        # ===== 3D normalized vectors

        with Layout("Unit 3D vector"):
            phi = Float.Random(-pi/2, pi/2, seed=seed1)
            cphi = gnmath.cos(phi)
            normal3D = Vector((cphi*gnmath.cos(theta), cphi*gnmath.sin(theta), gnmath.sin(phi)))

        # ===== Length

        with Layout("Random length"):
            l = random_.normal_value(length, scale, id=ID, seed=seed2)

        normal = normal3D.switch(two_d, normal2D)
        (normal * l).out("Vector")
        normal.out("Direction")

    with GeoNodes("Shake Vectors", is_group=True, prefix=random_):

        vector   = Vector(None,   "Vector")
        c_scale  = Float.Angle(0, "Angle Scale",  tip="Angle scale")
        l_scale  = Float(0,       "Length Scale", tip="Length scale")
        seed  = Integer(0,        "Seed")

        # ===== We need 3 seeds from in the input seed

        seed0, seed1, seed2 = expand_seed(seed, 3)

        # ===== Change the angle

        with Layout("Change the orientation"):
            theta = Float.Random(0, 2*pi, seed=seed0)
            phi   = random_.normal_value(0, c_scale, id=nd.id, seed=seed1)

            rot = Rotation.AlignToVector(vector=vector)
            shake = Rotation((phi, 0, theta))
            vector = ((rot.invert() @ shake) @ rot) @ vector

        # ===== Change the length

        with Layout("Change the length"):
            vector = vector.scale(random_.normal_value(1, l_scale, id=nd.id, seed=seed2))

        # ===== Done

        vector.out()

def iterations_panel(def_iter=3, def_prec=10):
    with Panel("Iterations"):
        iterations = Integer(def_iter, "Iterations", min=0, max=20, tip="Maximum number of iterations (use with care)")
        prec       = Float(def_prec,   "Precision", min=0, tip="Precision in 1000th (use with care)")/1000 * Integer(1).switch(nd.is_viewport, 10)

    return iterations, prec

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

    with GeoNodes("Projection", is_group=True, prefix=camera_):

        FOCAL_FACTOR = .04939

        # ===== Arguments

        position     = Vector(0,   "Position", tip="Point position", default_input='POSITION')
        radius       = Float(0,    "Radius", min=0, tip="Position radius")
        normal       = Vector(0,   "Normal", tip="Point direction", default_input='NORMAL')

        with Panel("Camera Culling"):
            ok_cc        = Boolean(True, "Camera Culling")
            focal_length = Float(50,   "Focal Length", min=1, tip="Focal length in mm")
            aspect_ratio = Float(16/9, "Aspect Ratio", tip="Camera aspect ratio, 16/9 for instance")

        focal_length *= FOCAL_FACTOR

        # ===== In the camera frame

        cam_info = nd.active_camera.info(transform_space='RELATIVE')

        with Layout("Projection in Camera Space"):
            vect     = position - cam_info.location
            rot      = cam_info.rotation.invert()
            pos      = rot @ vect
            distance = pos.length()

        # ===== Position above sensor are behind the camera
        # Taking into account the radius

        with Layout("Behind the Sensor"):
            z_pos = pos.z._lc("Z Position")
            behind = (z_pos - radius > 0) & ok_cc

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

            outside_left  = (proj.x < -half_width) & ok_cc
            outside_right = (proj.x >  half_width) & ok_cc
            outside_bot   = (proj.y < -half_height) & ok_cc
            outside_top   = (proj.y >  half_height) & ok_cc

            outside = outside_left | outside_right | outside_bot | outside_top

        # ===== Returns

        proj.out(         "Projection")
        behind.out(       "Behind")
        outside.out(      "Outside")
        outwards.out(     "Outwards")
        app_radius.out(   "Radius")
        distance.out(     "Distance")
        ratio.out(        "Ratio")
        outside_left.out( "Outside Left")
        outside_right.out("Outside Right")
        outside_bot.out(  "Outside Bot")
        outside_top.out(  "Outside Top")

        pos.out(          "Position")

    # -----------------------------------------------------------------------------------------------------------------------------
    # Position Culling

    with GeoNodes("Point Culling", prefix=camera_):

        cloud = Cloud(Geometry())

        # ===== Projection into the camera space

        if True:
            node = camera_.projection(radius=nd.radius).node.link_from(exclude=['Position', 'Normal'])
        else:
            node = camera_.projection(position=nd.position, radius=nd.radius, link_from={'exclude': 'Normal'}).node

        cloud.points[node.behind | node.outside].delete()

        cloud.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Edge Culling

    with GeoNodes("Edge Culling", prefix=camera_) as tree:

        mesh = Mesh()

        # ===== Projection

        if True:
            node = camera_.projection().node.link_from(exclude=['Normal', 'Normal'])
        else:
            node = camera_.projection(position=nd.position, link_from={'exclude': 'Normal'}).node


        # Get the created input sockets
        radius = Float.Input("Radius")
        aspect_ratio = Float.Input("Aspect Ratio")

        # ===== Both indices are behind

        with Layout("Sensor halt sizes and diagonal"):
            half_width = (aspect_ratio/2)._lc("Width/2")
            half_height = Float(.5)._lc("Height/2")
            diag = (half_height*gnmath.sqrt(1 + aspect_ratio**2))._lc("Diagonal/2")

        with Layout("Edge's vertex indices"):
            i1 = nd.edge_vertices().vertex_index_1
            i2 = nd.edge_vertices().vertex_index_2

        with Layout("A, B: Edge's vertex projected positions"):
            A  = mesh.points(node.projection, i1)._lc("A")
            rA = mesh.points(node.radius,     i1)._lc("A Radius")
            B  = mesh.points(node.projection, i2)._lc("B")
            rB = mesh.points(node.radius,     i2)._lc("B Radius")

        with Layout("Projection the origin on the edge line"):
            # Line equation is: OM = OA + tAB
            # Projection H is such as: OH.AB = 0 ==> (A + tAB).AB = 0 <=> t = -A.AB/AB**2
            AB = B - A
            l2 = AB.x**2 + AB.y**2
            t = -(A.dot(AB))/l2

            C  =  A.switch(t > 0,  B.switch(t < 1,  A + AB*t))._lc("C")
            rC = rA.switch(t > 0, rB.switch(t < 1, rA + (rB - rA)*t))._lc("C Radius")

        # DEBUG
        if False:
            debugA = Mesh(mesh).edges.to_points(position=A).points.instance_on(instance=Mesh.Cube(size=.1))
            #debugA = None
            debugB = Mesh(mesh).edges.to_points(position=B).points.instance_on(instance=Mesh.Cone(radius_bottom=.1, depth=.3))
            debugB = None
            debugC = Mesh(mesh).edges.to_points(position=C).points.instance_on(instance=Mesh.UVSphere(radius=.05))
            #debugC = None
            mesh.points.position = node.projection
            mesh.join(debugA, debugB, debugC).out()
            return

        with Layout("Both vertices are behind"):
            ignore = mesh.points(node.behind, i1) & mesh.points(node.behind, i2)

        with Layout("Both vertices are outside but on the same side"):
            ignore |= mesh.points(node.outside_left,  i1) & mesh.points(node.outside_left,  i2)
            ignore |= mesh.points(node.outside_right, i1) & mesh.points(node.outside_right, i2)
            ignore |= mesh.points(node.outside_bot,   i1) & mesh.points(node.outside_bot,   i2)
            ignore |= mesh.points(node.outside_top,   i1) & mesh.points(node.outside_top,   i2)

        with Layout("Nearest point farer than diagonal"):
            ignore |= C.length() > diag + rC
            pass

        mesh.edges[ignore].delete()
        mesh.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Face Culling

    with GeoNodes("Face Culling", prefix=camera_) as tree:

        mesh = Mesh()

        back_faces = Float.Factor(1, "Back Faces Culling", min=0, max=1, tip="Ignore points whose 'Normal' vector points outwards the camera position (1: keep all).")

        # ===== Faces facing outwards

        dual = Mesh(mesh).dual()
        dual.points.store("Normal", mesh.faces.sample_index(nd.normal, nd.index))
        node = camera_.projection(position=nd.position, radius=None, normal=Vector.Named("Normal")).node

        mesh.faces[dual.points.sample_index(node.outwards, nd.index) > back_faces].delete()

        # ===== All the corners behind

        # Points projection
        if True:
            node = camera_.projection().node.link_from(include="Camera Culling")
        else:
            node = camera_.projection(position=nd.position, link_from={'exclude': ['Radius', 'Normal']}).node

        with Layout("Faces with all vertices behind the sensor"):
            mesh.points.store("TEMP Vertex Behind", Float(node.behind))
            mesh.faces.store("TEMP Face Behind", Float.Named("TEMP Vertex Behind"))

            #ignore = Float.Named("TEMP Face Behind") > 1 - 1/nd.corners_of_face(face_index=nd.index).total
            ignore = Float.Named("TEMP Face Behind") > 1 - 1/Face.corners_total(nd.index)
            mesh.faces[ignore].delete()

        # ===== Faces outside the sensor

        projected = Mesh(mesh)
        projected.points.position = node.projection

        half_width  = Float(None, "Aspect Ratio")/2
        half_height = .5

        inside = -Boolean.Named("TEMP Outside")

        with projected.faces.for_each() as feel:
            bbox = feel.element.bounding_box()

            outside =  bbox.max_.x < -half_width
            outside |= bbox.min_.x >  half_width
            outside |= bbox.max_.y < -half_height
            outside |= bbox.min_.y >  half_height

            feel.generated.geometry = feel.element
            feel.generated.outside = outside

        mesh.faces[Mesh(feel.generated.geometry).faces.sample_index(feel.generated.outside, nd.index)].delete()

        # ===== Done

        mesh.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Camera debug

    with ShaderNodes("DBG Face"):

        col = snd.attribute(attribute_name="RGB")
        ped = Shader.Principled(base_color=col)
        ped.out()

    with GeoNodes("Debug", prefix=camera_):

        mesh = Mesh(Geometry())
        mesh.faces.material = "DBG Face"
        prec = Float(10,     "Precision", min=0, tip="Precision in 1000th (use with care)")/1000 * Integer(1).switch(nd.is_viewport, 10)
        show_grid     = Boolean(False, "Grid")
        show_original = Boolean(True, "Show Mesh")

        node = camera_.projection(position=nd.position, radius=None, normal=None, link_from='TREE').node

        # ===== Sensor

        sensor = Mesh.Grid(size_x=Float(None, "Aspect Ratio"), size_y=1, vertices_x=2, vertices_y=2)
        sensor.faces.delete_only_face()

        grid = Mesh.Grid(size_x=10*prec, size_y=10*prec, vertices_x=11, vertices_y=11)
        grid.faces.delete_only_face()

        sensor += grid.switch(-show_grid)

        # ===== Projected Mesh

        proj = Mesh(mesh)
        proj.points.position = node.projection
        proj.faces.delete_only_face()

        # ==== Points

        hidden = Boolean.MenuSwitch({'Behind': node.behind, 'Outside': node.outside, 'All': (node.behind | node.outside)}, name='Hidden Points')

        mesh.points.store("RGB", Color((0, 1, 0)).switch(hidden, (1, 0, 0)))
        pts = Mesh(mesh.points.instance_on(instance=Mesh.UVSphere(radius=.02)).realize())
        pts.faces.material = "DBG Face"

        geo = sensor + proj
        cam_info = nd.active_camera.info()

        geo.transform(translation=(0, 0, Float(None, "Focal Length")*(-FOCAL_FACTOR)))
        geo.transform(translation=cam_info.location, rotation=cam_info.rotation)

        # ===== Faces

        node = camera_.projection(position=nd.position, radius=gnmath.sqrt(nd.face_area), normal=nd.normal).node

        face_behind = node.behind
        face_outside = node.outside
        face_back = node.outwards > 0
        face_size = node.radius < prec
        face_all = face_behind | face_outside | face_size | face_back

        hidden = Boolean.MenuSwitch({'All': face_all, 'Behind': face_behind, 'Outside': face_outside, 'Backwards': face_back, 'Radius': face_size}, name='Hidden Surfaces')
        mesh.faces.store("RGB", Color((0, 1, 0)).switch(hidden,  (1, 0, 0)))

        mesh.switch(-show_original).join(geo, pts).out()


# =============================================================================================================================
# Sierpinski triangle

def sierpinski():

    with GeoNodes("Sierpinski Triangle", prefix=fractal_):

        # ===== Macro : build a triangle from points

        def new_triangle(p0, p1, p2):
            with Layout("Triangle From Points"):
                triangle = Mesh.Circle(3, fill_type='NGON')
                triangle.points[0].position = p0
                triangle.points[1].position = p1
                triangle.points[2].position = p2
                return triangle

        # ===== Triangulate the input Mesh

        triangles  = Mesh(None,    "Geometry").triangulate()
        iterations, prec = iterations_panel(3, 10)

        # ===== Size of the faces

        with Panel("Iterations"):
            triangles.faces.store("Size", gnmath.sqrt(nd.face_area))
            triangles.faces.store("Iterate", True)

        with Repeat(triangles=triangles, max_iteration=0, iterations=iterations) as rep:

            # ===== The coordinates of the triangle corners

            with Layout("The 3 triangle corners"):
                pts = [rep.triangles.points.sample_index(nd.position, nd.vertex_of_corner(nd.offset_corner_in_face(nd.corners_of_face(), i))) for i in range(3)]

            if True:
                node = camera_.projection(radius=Float.Named("Size")).node.link_from(include='Camera Culling')
            else:
                node = camera_.projection(position=nd.position, radius=Float.Named("Size"), link_from={'exclude': 'Normal'}).node

            rep.triangles.faces[Boolean("Iterate")].store("Iterate", -(node.behind | node.outside | (node.radius < prec)))
            rep.triangles.faces.store("Size", Float.Named("Size")/2)

            with rep.triangles.faces.for_each(iterate=Boolean.Named("Iterate"), p0=pts[0], p1=pts[1], p2=pts[2]) as feel:

                p0, p1, p2 = feel.p0, feel.p1, feel.p2

                q0, q1, q2 = (p0 + p1).scale(.5), (p1 + p2).scale(.5), (p2 + p0).scale(.5)

                feel.generated.geometry = feel.element.switch(feel.iterate, new_triangle(q0, p1, q1) + new_triangle(q1, p2, q2) + new_triangle(q2, p0, q0))

            rep.triangles = feel.generated.geometry

        triangles = Mesh(rep.triangles)

        triangles.faces.material = Material(None, "Material")
        triangles.out()

    with GeoNodes("DEMO Sierpinski"):

        ico = Mesh.IcoSphere(subdivisions=2, radius=10)

        fractal = Mesh(fractal_.sierpinski_triangle(ico, link_from='TREE'))

        fractal.points.position = fractal.points.position.normalize().scale(10)

        fractal.out()


# =============================================================================================================================
# Multi resolution surface

def multires_surface():

    # -----------------------------------------------------------------------------------------------------------------------------
    # Multi resolution surface
    #
    # An UV Map is divided according the dimension of the faces
    #
    # An initial division is performed to compute the face sizes and normals
    # During the fractal iteration, the size if the faces is estimated by tdividing the initial surface by 2
    #
    # The surface is computed by a group taking (position.x, position.y) as uv map coordinates in space (0, 1), (0, 1)
    # (See DEMO Multires Surface)

    with GeoNodes("Surface", is_group=True, prefix=multires_):

        position   = Vector(None,  "Position")

        iterations, prec = iterations_panel(3, 10)
        with Panel("Iterations"):
            init_split = Integer(3,    "Initial UV Subdivisions", min=0, max=5)

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
            outwards = camera_.projection(position=position, normal=Vector.Named("Normal"), link_from={'exclude': 'Radius'}).outwards_
            uv.points.store("Iterate", outwards < back_faces)

        # ===== Division loop

        max_points = 10000000 * Integer(10).switch(nd.is_viewport, 1)

        with Repeat(uv=uv,iterations=iterations, iter_scale=.5/segments, max_iteration=0) as rep:

            iterate = Boolean.Named("Iterate")

            # ===== Number max of points is reached

            with Layout("Max number of points is reached"):
                count = rep.uv.points.count
                stop = count > max_points
                iterate = iterate & (-stop)
                rep.max_iteration = rep.iteration.switch(stop, rep.max_iteration)

            # ===== Camera projection

            if True:
                node = camera_.projection(position=position, radius=Float.Named("Size")).node.link_from(include="Camera Culling")
            else:
                node = camera_.projection(position=position, radius=Float.Named("Size"), link_from={'exclude':'Normal'}).node

            # ===== Stop iteration for hidden points or small apparent size

            with Layout("Stop Iteration conditions"):
                iterate = iterate & -(node.behind | node.outside | (node.radius < prec))

            # ===== We can divide remaining points

            with Layout("Divide remaining points"):
                square = Mesh.Grid(size_x=1, size_y=1, vertices_x=2, vertices_y=2).points.to_points()
                new_squares = Cloud(rep.uv.points[iterate].instance_on(instance=square, scale=rep.iter_scale).realize())
                new_squares.points.store("Size",  Float.Named("Size")/2)
                new_squares.points.store("Scale", Float.Named("Scale")/2)

            with Layout("Replace iterated points"):

                rep.uv.points[iterate].delete()
                rep.uv += new_squares

            rep.iter_scale /= 2

        uv = Cloud(rep.uv)

        # ----- Finalize the uv grid

        with Layout("Build the final surface"):
            square  = Mesh.Grid(vertices_x=2, vertices_y=2)
            surface  = Mesh(uv.points.instance_on(instance=square, scale=Float.Named("Scale")).realize()).merge_by_distance(rep.iter_scale)

            surface.corners.store("UV Map", nd.position)
            surface.points.position = position

        surface.out()

        Boolean(True).info("Faces: " + surface.faces.count.to_string() + ", Iterations: " + rep.max_iteration.to_string())

    # -----------------------------------------------------------------------------------------------------------------------------
    # Multires plane

    with GeoNodes("Faces", prefix=multires_):

        mesh = Mesh()

        iterations, prec = iterations_panel(3, 10)

        with Panel("Camera Culling"):
            back_faces = Float.Factor(.1, "Back Faces Culling", min=0, max=1, tip="Don't iterate initial backward faces (-1: iterate all).")

        # ===== Prepare the mesh

        mesh.faces.store("Iterate", True)

        max_points = 1000000 * Integer(10).switch(nd.is_viewport, 1)

        # ===== Subdivision loop

        with Repeat(mesh=mesh, iterations=iterations) as rep:

            iterate = Boolean.Named("Iterate")

            # ----- Max number of points is reached

            npoints = rep.mesh.points.count
            iterate = iterate & npoints < max_points

            # ----- Face projection

            radius = 4*gnmath.sqrt(nd.face_area)
            #radius = nd.face_area
            if True:
                node = camera_.projection(radius=radius, normal=nd.normal).node.link_from(include="Camera Culling")
            else:
                node = camera_.projection(position=nd.position, radius=radius, normal=nd.normal).node

            iterate = iterate & -(node.behind | node.outside | (node.radius < prec) | (node.outwards > back_faces))
            #iterate = iterate & -(node.radius < prec)

            rep.mesh.faces[Boolean.Named("Iterate")].store("Iterate", iterate)

            subdiv = rep.mesh.faces[Boolean.Named("Iterate")].separate()
            keep   = subdiv.inverted_

            subdiv.subdivide(1)

            rep.mesh = keep + subdiv

        mesh = rep.mesh

        mesh.remove_named_attribute("Iterate")

        mesh.out()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Demo on how to use the Multires Surface group

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


        position = Vector.MenuSwitch({'Plane': plane, 'Sphere': sphere}, name="Surface")

        surface = Mesh(multires_.surface(position=position, link_from='TREE'))

        with Layout("Finalize"):
            surface.faces.smooth = True
            surface.faces.material = Material(None, "Material")

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

    with GeoNodes("Deform Shape", prefix=fractal_):

        cloud = Cloud(Geometry())

        with Panel("Deformation"):
            twist          = Float.Angle(0, "Twist")
            bend           = Float.Angle(0, "Bend")
            bend_direction = Float.Angle(0, "Bend Direction")
            scale          = Float(1,       "Scale")

        x, y, z = nd.position.xyz

        twist_rot = Rotation((0, 0, twist*z))

        bend_rot  = Rotation((bend*z, 0, 0)) @ Rotation((0, 0, bend_direction))

        rot = twist_rot @ bend_rot

        transform = Matrix.CombineTransform(rotation=rot, scale=scale)

        cloud.points.position = transform @ nd.position
        cloud.points.store("Up", transform @ Vector.Named("Up"))

        cloud.out()

    # ====================================================================================================
    # Points Iterator
    #
    # Replace points by a set of points

    with GeoNodes("Cloud Iterator", prefix=fractal_):

        model        = Cloud(Geometry(None,       "Geometry", tip="Geometry with points"))
        normal       = Vector((0, 0, 1),    "Normal",  tip="Normal to the points")

        iterations, prec = iterations_panel(5, 10)

        with Panel("Parameters"):
            scale        = Float(.5,            "Scale", min=.01, max=.999, tip="Iteration scale")
            trans        = Float.Factor(0,      "Translate", min=-1, max=1, tip="Translation factor along the normal")
            size_scale   = Float.Factor(0,      "Size Scale", min=0, max=1, tip="Size Scale")
            twist        = Float.Angle(0,       "Twist", tip="Rotation around the normal the normal")
            bend         = Float.Angle(0,       "Bend",  tip="Bending angle")
            thread_ratio = Float.Factor(1,      "Thread Ratio", min=0, max=1, tip="Ratio applied to thread scale at each iteration")

        with Panel("Noise"):
            twist_scale  = Float.Angle(0,       "Twist Scale", tip="Twist noise at each iteration")
            bend_scale   = Float.Angle(0,       "Bend Scale",  tip="Bending noise at each iteration")
            thread_scale = Float.Factor(.1,     "Thread Scale", min=0, max=1, tip="Thread scale along divisions")
            seed          = Integer(0,           "Seed")

        with Panel("Options"):
            keep_iter    = Boolean(False,       "Keep Iterated", tip="Keep the points once iterated or delete them")
            back_faces   = Float.Factor(1,      "Back Faces Culling", min=0, max=1, tip="Tolerance for points pointing outwards the camera")


        # ===== Model size

        with Layout("Model size"):

            bbox = model.bounding_box()

            p0, p1 = bbox.min_, bbox.max_
            size = (p1 - p0).length()._lc("Model Size")

            z0, z1 = p0.z, p1.z
            height = (z1 - z0)._lc("Model Height")

        # ===== Control random seed for each point

        with Layout("Setup the model"):
            model.points._Seed     = seed.hash_value(nd.index)
            #model.points._Scale    = scale
            model.points._Scale    = model.points.radius
            model.points._Normal   = normal
            model.points._Rotation = Rotation.AlignToVector(normal)
            model.points._Z        = nd.position.z - z0

            Z = Float("Z")

            # Base twisting around Z axis
            with Layout("Twisting around Z"):
                twist_angle = random_.normal_value(twist, twist_scale, id=seed, seed=seed)
                twist_rot = Rotation((0, 0, twist_angle*Z))
                no_twist  = twist_scale.equal(0, epsilon=.001)

            # Base bending
            with Layout("Bending"):
                no_bend    = bend.equal(0, epsilon=0) & bend_scale.equal(0, epsilon=0)

            # Knowing if twisting or bending is not required will avoid
            # some matrices multiplications
            no_deform = no_twist & no_bend

            # Apply to the model
            rot = twist_rot
            model.points.position  = rot @ model.points.position
            model.points._Normal   = rot @ Vector("Normal")
            model.points._Rotation = Rotation("Rotation") @ rot

        # ===== Base point

        with Layout("Initial point"):
            cloud = Cloud.Points(1)

            cloud.points._Iterate  = True
            cloud.points._Seed     = seed
            cloud.points._Scale    = 1.
            cloud.points._Normal   = (0, 0, 1)
            cloud.points._Rotation = Rotation()

            cloud.points._Depth  = 0
            cloud.points._Thread = 1.

        # ===== Maximum points

        with Layout("Maximum number of points"):
            max_points = 10000000 * Integer(10).switch(nd.is_viewport, 1)


        # ===== Iteration loop

        with Repeat(cloud = cloud, iterations=iterations, thread_scale=thread_scale, iteration_max=0) as rep:

            cloud = rep.cloud

            # ===== We continue only if the max number of points is not

            with Layout("Stop iteration when maximum number of points is reached"):
                npoints = cloud.points.count
                still_ok = npoints < max_points
                rep.iteration_max = rep.iteration_max.switch(still_ok, rep.iteration_max + 1)

            # ===== Visible points to iterate

            with Layout("Projection"):
                if True:
                    node = camera_.projection(radius=Float("Scale")*size, normal=Vector("Normal")).node.link_from(include="Camera Culling")
                else:
                    node = camera_.projection(position=nd.position, radius=Float("Scale")*size, normal=Vector("Normal"), link_from='TREE').node

                iterate = Boolean("Iterate") & still_ok
                iterate &= -(node.behind | node.outside | (node.radius < prec) | (node.outwards > back_faces))

                cloud.points[Boolean("Iterate")]._Iterate = iterate

            # ===== Fractal iteration

            with Layout("Copy attributes"):
                cloud.points._Main_Seed     = Integer("Seed")
                cloud.points._Main_Scale    = Float("Scale")
                cloud.points._Main_Normal   = Vector("Normal")
                cloud.points._Main_Rotation = Rotation("Rotation")
                cloud.points._Main_Position = nd.position

            with Layout("Replacement"):
                inst_scale = Float("Main Scale")
                seed = Integer("Seed")
                inst_scale = random_.normal_value(inst_scale, inst_scale*size_scale, id=seed, seed=seed + 1000)
                instances = cloud.points[Boolean("Iterate")].instance_on(instance=model,
                    #scale    = Float("Main Scale"))
                    scale    = inst_scale)

                # Set the instance @ origin to perform deformations
                instances.position = 0

                # Now we realize
                new_cloud = Cloud(instances.realize())

            with Layout("Attributes of next iteration"):
                new_cloud.points._Seed  = Integer("Main Seed").hash_value(Integer("Seed"))
                new_cloud.points._Scale = Float("Main Scale") * Float("Scale")
                new_cloud.points._Depth = Integer("Depth") + 1

                seed = Integer("Seed")
                new_cloud.points._Thread = Float("Thread")*random_.normal_value(1, rep.thread_scale, id=seed, seed=seed+100)
                rep.thread_scale *= thread_ratio

            with Layout("Deformation"):

                seed = Integer("Main Seed")
                Z = Float("Z")

                # Instance origin
                O = Vector("Main Position")

                # Twisting around Z axis
                with Layout("Twist"):
                    twist_rot = Rotation((0, 0, random_.normal_value(0, twist_scale, id=seed, seed=seed)*Z)).switch(no_twist)

                # Bending
                with Layout("Bend"):
                    bend_angle = random_.normal_value(bend, bend_scale, id=seed, seed=seed + 1)
                    bend_dir   = Float.Random(0, 2*np.pi, id=seed, seed=seed + 2)
                    bend_rot   = Rotation((bend_angle*Z, 0, 0)) @ Rotation((0, 0, bend_dir)).switch(no_bend)

                # Apply to vertices
                with Layout("Apply"):
                    rot = ((twist_rot @ bend_rot) @ Rotation.Named("Main Rotation")).switch(no_deform, Rotation.Named("Main Rotation"))
                    new_cloud.points.position  = O + rot @ new_cloud.position
                    new_cloud.points._Normal   = rot @ Vector("Normal")
                    new_cloud.points._Rotation = Rotation("Rotation") @ rot

                if False:
                    rot = Rotation.Named("Main Rotation")
                    pos = nd.position - O

                    pos = rot.invert() @ pos
                    nrm = rot.invert() @ Float.Named("Normal")

                    z = Float.Named("Z")
                    deform = Rotation((0, 0, twist*z)) @ (Rotation((bend*z, 0, 0)) @ Rotation((0, 0, 0)))

                    new_cloud.points.position  = O + (rot @ deform) @ pos
                    new_cloud.points.store("Normal", (rot @ deform) @ nrm)

                new_cloud.points.offset = Vector("Normal").scale(trans*height*Float.Named("Scale"))

                # Done

                del_points  = Cloud(cloud).points[Boolean("Iterate")].delete()
                cloud.points._Iterate = False
                keep_points = cloud

                rep.cloud = del_points.switch(keep_iter, keep_points) + new_cloud

        cloud = Cloud(rep.cloud)

        Boolean(True).info("Points: " + cloud.points.count.to_string() + " after " + rep.iteration_max.to_string() + " iterations.")

        with Layout("Scale to radius and seed to id"):
            cloud.points.radius = Float("Scale")
            cloud.id     = Float("Seed")

        # ===== Remove

        with Layout("Remove attributes but Normal and Rotation"):
            cloud.remove_names("Main *")
            for na in ("Iterate", "Scale", "Seed", "Z"):
                cloud.remove_named_attribute(na)

        with Layout("Add a random number"):
            cloud.points._Random = Float.Random(0, 1, id=nd.index, seed=nd.id)

        cloud.out("Points")

    # ====================================================================================================
    # Mesh iterator

    with GeoNodes("Mesh Iterator", prefix=fractal_):

        mesh         = Mesh()

        with Panel("Options"):
            use_faces = Boolean(True, "Use Faces", tip="Use faces rather than points")

        # ===== Build the model from the input mesh

        with Layout("Model from points"):
            point_model = mesh.points.to_points()
            point_model.points._Normal = mesh.points.sample_index(nd.normal, nd.index)

        with Layout("Model from Faces"):
            face_model = mesh.faces.to_points()
            face_model.points._Normal = mesh.faces.sample_index(nd.normal, nd.index)

        model = point_model.switch(use_faces, face_model)

        with Layout("Fractal"):

            cloud = Cloud(fractal_.cloud_iterator(geometry=model, normal=Vector("Normal"), link_from='TREE'))

        mesh = Mesh(cloud.points.instance_on(instance=mesh, scale=nd.radius, rotation=Rotation("Rotation")).realize())

        mesh.out()

    with GeoNodes("Cone Iterator", prefix=fractal_):

        with Panel("Cone"):
            sides   = Integer(3,  "Sides", min=3, max=20, tip="Number of sides")
            n       = Integer(5,  "Instances per side", min=3, max=50, tip="Number of instances per side")
            height  = Float(2,    "Height", min=.1, max=10, tip="Cabbage heigth")

        # ===== Cone Side

        with Layout("Cone Side"):

            width = 1.
            line = Cloud.Points(count=n)
            line.points._Normal = Vector((height, 0, width)).normalize()

            # index 0 at bottom

            # q**n = eps ==> q = eps**(1/n)
            eps = .01
            q = eps**(1/n)

            # 1 = shrink*(1 - q**n)/(1 - q) => shrink = (1 - q)/(1 - eps)
            shrink = 2*(1 - q)/(1 -eps) # Diameter

            # ratio from 1 to q**n
            # CAUTION : missing the top node because index == n doesn't exist
            ratio = q**nd.index
            ratio0, ratio1 = 1, q**n
            ratio = (ratio - ratio0)/(ratio1 - ratio0)

            line.points.position = (-width*ratio, 0, ratio*height)
            line.points.radius   = shrink*q**nd.index

        # ===== Duplicate

        with Layout("Duplicate to form a cone"):

            circle = Mesh.Circle(radius=width, vertices=sides)
            rot = Rotation((0, 0, (2*np.pi)*nd.index/sides))
            model = circle.points.instance_on(instance=line, rotation=rot)

            model = Cloud(model.realize())

            rot = Rotation((0, 0, (2*np.pi)*(nd.index// n)/sides))
            model.points._Normal = rot @ Vector("Normal")

        # ===== Point at the top

        with Layout("Summit"):
            summit = Cloud.Points(1, position=(0, 0, height))
            summit.points._Normal = (0, 0, 1)
            summit.points.radius = shrink*q**n

            model += summit

        # ===== Let's iterate

        cloud = Cloud(fractal_.cloud_iterator(geometry=model, scale=nd.radius, normal=Vector("Normal"), link_from='TREE'))

        # ===== Finalize

        cone = Mesh.Cone(radius_bottom=width, depth=height)
        mesh = Mesh(cloud.points.instance_on(instance=cone, scale=nd.radius, rotation=Rotation("Rotation")).realize())

        mesh.faces.smooth = True
        mesh.faces.material = Material(None, "Material")

        mesh.out()

    # ====================================================================================================
    # Logarithmic Spiral

    with GeoNodes("Logarithmic Spiral"):

        with Panel("Spiral"):
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

        with Layout("Base Logarihmic Spiral"):
            curve = Curve.Line().resample(count)

            theta =  tau*rotations/count*nd.index
            rho = radius*gnmath.abs(omega)**theta
            theta *= gnmath.sign(omega)

            #slope = height/count
            slope = height/radius

            #curve.points.position = (rho*gnmath.cos(theta), rho*gnmath.sin(theta), slope*nd.index)
            curve.points.position = (rho*gnmath.cos(theta), rho*gnmath.sin(theta), slope*(radius - rho))

        # ----- Normal to the cone

        with Layout("Normal"):
            normal = curve.points.position*(1, 1, 0)
            normal = Rotation((0, 0, theta)) @ Vector((height, 0, radius))
            curve.points._Normal = normal.normalize()

        curve.out()

    # ====================================================================================================
    # Romanesco Cabbage

    with GeoNodes("Romanesco Cabbage", prefix=fractal_):

        iterations, prec = iterations_panel(1, 10)

        with Panel("Debug"):
            show_spiral  = Boolean(False, "Show Initial Spiral")
            show_spirals = Boolean(False, "Show Spirals")
            show_cones   = Boolean(False, "Show Cones")

        with Panel("Cabbage"):
            nspirals      = Integer(6,           "Number of spirals", min=3, max=12)
            radius        = Float(10,            "Size", min=1)
            height_factor = Float(1.5,           "Height Factor", min=0)
            upwards       = Float(4,             "Upwards factor")
            npoints       = Integer(30,          "Number of points", min=3, max=200)
            q             = Float.Factor(.9,     "Shrink Factor", min=.01, max=.999)
            size_factor   = Float.Factor(.2,     "Size Factor", min=.01, max=.999)
            cone_segms    = Integer(7,           "Cone Segments", 3, 32)

        #omega         = Float(.8,            "Omega")
        #rotations     = Float(3,             "Rotations")
        #seed          = Integer(0,           "Seed")

        # ===== Base Spiral

        with Layout("Base Spiral"):

            height = radius*height_factor

            spiral = Curve(G().logarithmic_spiral(count=500, radius=radius, height=height, link_from='TREE'))

            # ::::: Extract points following a geometric series

            # Geometric series:
            # length = size*(1 - q^n)/(1 - q) => size = length*(1 - q)/(1 - q^n)

            length = spiral.length()
            size = length*(1 - q)/(1 - q**npoints)

            curve = Curve.Line().resample(npoints)
            l = size*(1 - q**nd.index)/(1 - q)

            curve.points.position = spiral.sample_length(nd.position, length=l)

            with Layout("Radius"):
                curve.points._Radius = size_factor*q**nd.index

            # Orient progressively the normal to z
            f = (nd.index/(npoints - 1))**upwards

            normal = spiral.sample_length(Vector("Normal"), length=l)
            #normal = normal.mix(f, (0, 0, 1))
            curve.points._Normal = normal.normalize()

            with Layout("Debug Initial Spiral"):
                normals = curve.points.instance_on(instance=Curve.Line(), rotation=Rotation.AlignToVector(Vector("Normal")))
                initial_spiral = curve + normals


        # ===== Duplicate nspirals times

        with Layout("Duplicates"):
            cloud = Cloud.Points(nspirals, position=0)
            cloud.points.store("rot", Rotation((0, 0, tau/nspirals*nd.index)))

            spirals = Curve(cloud.points.instance_on(instance=curve, rotation=Rotation.Named("rot")).realize())
            spirals.points._Normal = Rotation.Named("rot") @ Vector("Normal")
            spirals.remove_named_attribute("rot")

            # DEBUG : keep curves
            if False:
                normals = spirals.points.instance_on(instance=Curve.Line(), rotation=Rotation.AlignToVector(Vector("Normal")))
                (spirals + normals).out()
                return

        with Layout("Show Spirals"):
            normals = spirals.points.instance_on(instance=Curve.Line(), rotation=Rotation.AlignToVector(Vector("Normal")))
            debug_spirals = spirals + normals

        with Layout("Spirals to points"):
            spirals = spirals.to_points_evaluated()
            spirals.points.radius = Float.Named("Radius")

        # ===== Iterates

        cone = Mesh.Cone(radius_bottom=radius, vertices=cone_segms, depth=height)

        cloud = fractal_.cloud_iterator(geometry=spirals, normal=Vector("Normal"), link_from='TREE')

        if False:
            cloud.out()
            return


        cabbage = Mesh(Cloud(cloud).instance_on(instance=cone, scale=nd.radius, rotation=Rotation("Rotation")))
        geo = cloud.switch(show_cones, cabbage)
        geo += debug_spirals.switch_false(show_spirals)
        geo = geo.switch(show_spiral, initial_spiral)
        geo.out()












































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

            node = nd.edge_vertices()
            with rep.triangle.edges.for_each(p1=node.position_1, p2=node.position_2) as feel:

                new_edges = Mesh.Line(start_location=feel.p1, end_location=feel.p2, count=5)
                v = (feel.p2 - feel.p1)/3

                ns = noise_scale * v.length()
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

            node = nd.edge_vertices()
            with rep.leaf.edges.for_each(p1=node.position_1, p2=node.position_2, seed=rep.seed) as feel:

                hv = rep.seed.hash_value(feel.index)

                v = feel.p2 - feel.p1
                l = v.length()

                edge = Mesh(feel.element)
                extrude = edge.edges.sample_index(Boolean.Named("Use"), 0)

                loop_angle  = angle       + Float.Random(-angle*angle_noise, angle*angle_noise, hv)
                loop_ag     = sub_angle   + Float.Random(-sub_angle*angle_noise, sub_angle*angle_noise, hv + 1)
                loop_factor = grow_factor + Float.Random(-factor_noise, factor_noise, hv + 2)
                loop_fac    = sub_factor  + Float.Random(-factor_noise, factor_noise, hv + 3)

                #edge.points[1].extrude(Rotation((0, 0, loop_angle)) @ (v*loop_factor))
                #edge.points[1].extrude(Rotation((0, 0, -loop_angle - loop_ag)) @ (v*loop_fac))
                #edge.points[1].extrude(Rotation((0, 0,  loop_angle + loop_ag)) @ (v*loop_fac))
                edge[1].extrude_vertices(Rotation((0, 0, loop_angle)) @ (v*loop_factor))
                edge[1].extrude_vertices(Rotation((0, 0, -loop_angle - loop_ag)) @ (v*loop_fac))
                edge[1].extrude_vertices(Rotation((0, 0,  loop_angle + loop_ag)) @ (v*loop_fac))

                edge.edges.store("Use", True)
                edge.edges[0].store("Use", False)
                feel.generated.geometry  = feel.element.switch(extrude, edge)

            leaf = feel.generated.geometry #.merge_by_distance()
            rep.leaf = leaf

        rep.leaf.out()

def points_fractal():

    return

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
        normal = Rotation((0, 0, theta)) @ Vector((height, 0, radius)).normalize()
        curve.points._Normal = normal

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

            length = spiral.length()
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





def growing():

    # ----- Growing Mesh

    with GeoNodes("Branch"):

        iterations = Integer(10, "Iterations", min=2, max=10)
        extr_scale = Float.Factor(.3, "Extrude Scale", min=.1, max=2)
        branches   = Integer(2, "Branches", min=2, max=6)

        seed       = Integer(0, "Seed")

        line = Mesh.LineEndPoints(end_location=(0, 0, 1), count=2)

        with Repeat(tree=line, iterations=iterations) as rep:

            rep_seed = rep.iteration.hash_value(seed)

            with rep.tree.edges.for_each() as feel:

                edge = Mesh(feel.element)

                with Layout("Edge direction and length"):
                    p0 = edge.points.sample_index(nd.position, index=0)._lc("P0")
                    p1 = edge.points.sample_index(nd.position, index=1)._lc("P1")
                    direction = (p1 - p0)._lc("Direction")
                    length = direction.length()._lc("Length")
                    direction = direction.normalize()

                with Repeat(edge=edge, iterations=branches) as br_rep:

                    br_seed = rep_seed.hash_value(br_rep.iteration)

                    br_length = length*extr_scale*Float.Random(.8, 1.2, id=feel.index, seed=br_seed)
                    br_dir = direction + Vector.Random(-.4, .4, id=feel.index, seed=br_seed + 1)

                    #br_rep.edge.points[1].extrude(br_dir*br_length)
                    br_rep.edge[1].extrude_vertices(br_dir*br_length)

                feel.generated.geometry = br_rep.edge

            rep.tree = feel.generated.geometry

        rep.tree.out()

    # ----- Mesh 1

    with GeoNodes("Branch 1"):

        iterations = Integer(10, "Iterations")
        trunk_fac  = Float.Factor(.3, "Trunk Factor", min=0, max=1)
        seed       = Integer(0, "Seed")

        line = Mesh.LineEndPoints(end_location=(0, 0, 1), count=2)
        line.edges.store_named_attribute("Split", True)

        with Repeat(tree=line, iterations=iterations) as rep:

            rep_seed = rep.iteration.hash_value(seed)

            with rep.tree.edges.for_each() as feel:

                edge = Mesh(feel.element)

                with Layout("Edge direction and length"):
                    p0 = edge.points.sample_index(nd.position, index=0)._lc("P0")
                    p1 = edge.points.sample_index(nd.position, index=1)._lc("P1")
                    direction = (p1 - p0)._lc("Direction")
                    length = direction.length()._lc("Length")

                with Layout("First edge: from start to point located around trunk factor"):
                    c  = (p0 + p1)*trunk_fac
                    c += Vector.Random(-.1*length, .1*length, id=feel.index, seed=rep_seed)._lc("Center")

                    new_edges = Mesh.LineEndPoints(start_location=p0, end_location=c, count=2)
                    new_edges.edges.store_named_attribute("Split", False)

                with Layout("Extrude till end point"):
                    #new_edges.points[1].extrude(p1 - c)
                    new_edges[1].extrude_vertices(p1 - c)
                    new_edges.edges[1].store_named_attribute("Split", True)

                with Layout("Extrude in another direction"):
                    direction += Vector.Random(-.4*length, .4*length, id=feel.index, seed=rep_seed + 1)
                    length *= (1 - trunk_fac)*Float.Random(.8, 1.2, id=feel.index, seed=rep_seed + 2)

                    #new_edges.points[1].extrude(direction.normalize()*length)
                    new_edges[1].extrude_vertices(direction.normalize()*length)
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
                length = direction.length()

                direction += Vector.Random(-.3, .3, id=feel.index, seed=rep_seed + 1)
                length *= Float.Random(.8, 1.2, id=feel.index, seed=rep_seed + 2)

                new_segment = Curve.LineDirection(start=segment.points.sample_index(nd.position, index=1), direction=direction.normalize(), length=length)

                feel.generated.geometry = segment + new_segment


            rep.curve = feel.generated.geometry

        rep.curve.out()
