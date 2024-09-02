from bpy.types import Attribute, SEQUENCER_PT_view_safe_areas
from ..geonodes import *
from .. import shadernodes as sh

def demo():

    # =============================================================================================================================
    # Float Math

    with GeoNodes("Test Float Math"):

        Geometry().out()


        with Layout("Base operators"):
            a, b, c = Float(10), Float(20), Float(pi)

            a += b*c/123 - 789
            A = gnmath.multiply_add(a, b, c)

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

            A += b*c/123 - 789
            A = gnmath.multiply_add(a, b, c)


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
    # Mesh

    with GeoNodes("Mesh Operations"):

        mesh = Mesh()

        with Layout("Primitives"):

            cone   = Mesh.Cone(vertices=32, side_segments=3, fill_segments=3, radius_top=.5, radius_bottom=2, depth=2, fill_type='TRIANGLE_FAN')
            cube   = Mesh.Cube(size=(1, 2, 3), vertices_x=2, vertices_y=3, vertices_z=3)
            cyl    = Mesh.Cylinder(vertices=32, side_segments=3, fill_segments=3, radius=.5, depth=5, fill_type='NGON')
            grid   = Mesh.Grid(size_x=2, size_y=1, vertices_x=2, vertices_y=2)
            ico    = Mesh.IcoSphere(radius=2, subdivisions=2)
            sphere = Mesh.UVSphere(segments=6, rings=7, radius=1.5)
            # ----- Start end line
            line0  = Mesh.Line(count=100, end_location=2)
            # ----- Start offset line
            line1  = Mesh.Line(count=100, offset=-1)
            circle = Mesh.Circle(vertices=8, radius=.5, fill_type='TRIANGLE_FAN')

            meshes = [cone, cube, cyl, grid, ico, sphere, line0, line1, circle]

        with Layout("Extrusion"):

            cube = cube.faces.extrude(nd.normal, .5)
            cube = cube.faces[cube.top_].extrude(offset_scale=0)
            top = cube.top_
            cube = cube.faces[top].scale(scale=.8, uniform=False)
            cube = cube.faces[top].scale(scale=.6, uniform=True)
            cube = cube.faces[top].extrude(offset_scale=.5)
            cube = cube.faces[cube.top_].flip()
            meshes.append(cube)

            meshes.append(cube.dual())

        with Layout("Boolean"):
            meshes.append(cyl.intersect(cone))
            meshes.append(cyl.union(cone))
            meshes.append(cyl.difference(cone))
            meshes.append(cone.intersect(cyl))
            meshes.append(cone.union(cyl))
            meshes.append(cone.difference(cyl))


        with Layout("Transformation Join"):
            node = nd.join_geometry().node
            locs = Mesh.Grid(size_x=20, size_y=20, vertices_x=5, vertices_y=5)
            for i, mesh in enumerate(meshes):
                node.geometry = mesh.transform(translation=locs.points.sample_index(nd.position, index=i))

            node.geometry.out()

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
        a.plug_node_into(rename={'Vertices X': 'Vertices', 'Vertices Y': 'Vertices'})

        a = Node("Math")

        # Connect the 'Value' output socket to the 'Value' input socket
        # The third socket is exclude by its index
        # Input values are renamed 'First' and 'Second'
        a.plug_node_into(exclude=2, rename={'Value': 'First', 'Value_001': 'Second'})

        b = Node("Math", operation='SQRT')

        # Plug the previous math node on a single socket
        b.plug_node_into(a, include='Value')
