from geonodes import *

def demos():

    # ====================================================================================================
    # Hello World
    # ====================================================================================================


    # Create the Geometry Nodes named "Hello World"

    with GeoNodes("Doc Hello World"):
        
        height = 3
        omega  = 2

        # The surface is basically a grid 20 x 20 with a resolution 200 x 200
        grid = Mesh.Grid(vertices_x=200, vertices_y=200, size_x=20, size_y=20)
        

        # z is computed using gnmath library and operators as in pure python
        with Layout("Computing the wave"):
            pos = nd.position
            distance = gnmath.sqrt(pos.x**2 + pos.y**2)
            z = height*gnmath.sin(distance*omega)/distance

        # Let's change the z coordinate of our vertices
        with Layout("Point offset and smoothness"):
            grid.offset = (0, 0, z)
            grid.faces.smooth = True

        # We are done: plugging the deformed grid as the modified geometry
        grid.out()

    # ====================================================================================================
    # Socket classes
    # ====================================================================================================

    with GeoNodes("Doc Socket Init"):

        # Get the Group Input geometry
        geometry = Geometry()

        # Plug the geometry to the Group output node
        geometry.out()

        # Create sockets from their node primitives
        with Layout("Primitives"):
            i = Integer(123)
            f = Float(3.14)
            s = String("A string")
            b = Boolean(True)
            v = Vector((1, 2, 3))
            red = Color("Red")
            green = Color("#00FF00")
            blue = Color((0, 0, 1))
            r = Rotation((pi, pi, pi/2))

        # The key word argument name indicates these are Group input sockets
        # The value is the default value
        i = Integer(123, name = "Integer")
        f = Float(3.14, name = "Float")
        s = String("A string", name = "String")
        b = Boolean(True, name = "Boolean")
        v = Vector((1, 2, 3), name = "Vector")
        red = Color("Red", name = "Color 0")
        green = Color("#00FF00", name = "Color 1")
        blue = Color((0, 0, 1), name = "Color 2")
        r = Rotation((pi, pi, pi/2), name = "Rotation")

        # If the initial value is a string, the value is a named attribute
        # Named Attribute 'Integer'
        with Layout("Named Attributes"):
            i = Integer("Integer")
            # Named Attribute 'Float'
            f = Float("Float")

        # Creating Geometries
        with Layout("Creating geometries"):
            cube = Mesh.Cube()
            curve = Curve.Spiral()

    # ====================================================================================================
    # gnmath
    # ====================================================================================================

    with GeoNodes("Doc gnmath"):

        with Layout("gnmath"):
            a = Float(1)
            b = gnmath.sin(a)
            
            # Add between two Floats
            c = gnmath.add(b, 7.5)

            i = Integer(123)
            # Greater Common Divisor exists only for Integers
            j = gnmath.gcd(i, 17) 
            
            # Add exists also for Floats
            k = gnmath.iadd(j, 7)
            
            u = Vector((1, 2, 3))
            # Cross product exists only for vectors
            v = gnmath.cross(u, (7, 8, 9))
            # Add axists also for Floats
            w = gnmath.vadd(v, (5, 6,7))

            # Bitwise functions
            j = gnmath.bw_and(i, 7)

            a = Boolean(True)
            b = gnmath.xor(a, False)
            c = gnmath.band(b, False)
            d = gnmath.band(b, False)

        with Layout("Alternative Syntax"):
            a = Float(1)
            b = a.sin()
            c = b + 7.5

            i = Integer(123)
            j = i.gcd(17) 
            k = j + 7
            
            u = Vector((1, 2, 3))
            v = u.cross((7, 8, 9))
            w = v + (5, 6,7)
            
            
            a = Boolean(True)
            b = a.xor(False)
            # and operator is implemented with & 
            c = b & False
            # or operator is implemented with |
            d = b | False  

    # ====================================================================================================
    # operators
    # ====================================================================================================

    with GeoNodes("Doc Operators"):

        # Float operators
        a = Float(10)
        c = a*pi # Math node, operation 'MULTIPLY'
        c += 1 # Math node, operation 'ADD'
        ok = a <= c # Compare node, operation 'LESS_EQUAL'

        # Integer operators
        a = Integer(10)
        c = a*42 # Operation between two Integers : Integer Math node is used
        c += 1 # Integer Math node, operation 'ADD'
        d = -c # Integer Math node, operation 'NEGATE'

        # Bitwise operators
        a = Integer(1) << 3
        a |= Integer(7) & 1

        # Vector operators
        u = Vector((1, 2, 3))
        v = u + (7, 8, 9) # Vector Math node, operation 'ADD'
        w = u*3 # Vector Math node, operation 'SCALE'

        # Boolean operators
        b = Boolean(True)
        c = b | False # Boolean Math node, operation 'OR'

        # String operators
        s = String("A string")
        s += ": this is something added. "
        s += String(" ") * ("This", "is", "a", String("sentence."))

        # Join Geometry
        geo = Geometry() # Input geometry
        geo += Mesh.Cube(), Curve.Spiral() # Join with two other geometries

        # Mesh boolean
        cube = Mesh.Cube()
        ico  = Mesh.IcoSphere(radius=.8)

        mesh = cube - ico # Difference
        mesh = cube * ico # Union
        mesh = cube / ico # Intersect   

    # ====================================================================================================
    # Method names
    # ====================================================================================================

    with GeoNodes("Doc Method names"):

        # ----------------------------------------------------------------------------------------------------
        # RULE 2 : Constructor nodes in CamelCase
        #
        # Primitive nodes 'Cube', 'Points' and 'Bézier Segment' are
        # implemented as constructors of their Geometry

        cube = Mesh.Cube()
        cloud = Cloud.Points()
        bezier = Curve.BezierSegment()

        # ----------------------------------------------------------------------------------------------------
        # RULE 2 : Constructor nodes in CamelCase
        # RULE 3 : Omit class name
        #
        # Primitive nodes 'Mesh Line' and  'Curve Line' are implemented as
        # constructors of their Geometry, omitting the name of the class

        mesh_line = Mesh.Line()
        curve_line = Curve.Line()

        # ----------------------------------------------------------------------------------------------------
        # RULE 1 : Nodes name in snake_case
        #
        # Nodes 'Subdivision Surface', 'Triangulate', 'Set Position' are implemented as method
        # of their geometry using the snake_case version for their name

        cube.subdivision_surface()
        cube.triangulate()
        curve_line.set_position()

        # ----------------------------------------------------------------------------------------------------
        # RULE 1 : Nodes name in snake_case
        # RULE 3 : Omit class name
        #
        # In the snake_case version of the nodes 'Fill Curve', 'Deform Curves on Surface',
        # 'Subdivide Mesh' the name of the geometry is omitted

        mesh = Curve.Circle().fill()
        curve_line.resample(count=17)
        cube.subdivide()

        # ----------------------------------------------------------------------------------------------------
        # RULE 4 : setters and getters are properties
        #
        # The nodes 'Set Position' and 'Set Radius' are also implemented as properties

        mesh.position += (1, 2, 3)
        mesh.offset = (1, 2, 3)
        cloud.radius = 1.

        # Join the geometries and to output
        Geometry.Join(cube, cloud, bezier, mesh_line, curve_line, mesh).out()

    # ====================================================================================================
    # Argument names
    # ====================================================================================================

    with GeoNodes("Doc Argument names"):

        # ----------------------------------------------------------------------------------------------------
        # RULE A : socket arguments in snake_case

        sphere = Mesh.UVSphere(segments=16, rings=12, radius=1.)
        sphere.merge_by_distance(distance=.1)

        # ----------------------------------------------------------------------------------------------------
        # RULE B : sockets ordered as in the node, parameters are placed after

        sphere.merge_by_distance(distance=.1, mode='All')

        # ----------------------------------------------------------------------------------------------------
        # RULE C : Selection socket is set by item index
        #
        # Don't write:
        # sphere.set_position(selection=nd.index < 5, position=(1, 2, 3))

        sphere[nd.index < 5].set_position(position=(1, 2, 3))

        # ----------------------------------------------------------------------------------------------------
        # RULE D : parameter arguments take the parameter name
        #
        # Node 'Merge by Distance' owns a parameter named 'mode'

        sphere.merge_by_distance(mode='All')

        # ----------------------------------------------------------------------------------------------------
        # RULE E : domain parameter is taken from the calling domain
        #
        # Don't write:
        # sphere.set_shade_smooth(shade_smooth=True, domain='FACE')

        sphere.faces.set_shade_smooth(True)

        # ----------------------------------------------------------------------------------------------------
        # RULE F : data_type parameter is omitted, it is deduced from the argument type
        #
        # Don't write
        # b = sphere.sample_uv_surface(value=a, data_type='VECTOR')
        # data_type will be deduced from the type of variable a

        a = Vector()
        b = sphere.sample_uv_surface(value=a)

        # ----------------------------------------------------------------------------------------------------
        # RULE G : nodes having a _mode_ like parameter are implemented once per possible value
        
        # Mix Color
        col1, col2 = Color(), Color()
        
        # You can mix using the factor_mode parameter
        col = col1.mix(col2, factor_mode='UNIFORM')
        
        # You can alternatively used the methods suffixed by the mode
        col = col1.mix_darken(col2)
        col = col1.mix_multiply(col2)
        col = col1.mix_burn(col2)

        sphere.out() 

    # ====================================================================================================
    # Returned values
    # ====================================================================================================

    with GeoNodes("Doc Returned Values"):

        # ---------------------------------------------------------------------------
        # Simple example
        # ---------------------------------------------------------------------------

        #  Node 'Cube' returns two output sockets:
        # - Mesh
        # - UV Map
        # The returned value has a property named uv_map_

        cube = Mesh.Cube()
        
        # The following lines are equivalent
        uv_map = cube.node.uv_map
        uv_map = cube.uv_map

        # ---------------------------------------------------------------------------
        # Reading info
        # ---------------------------------------------------------------------------
        
        # The returned socket is the first one: point_count
        # Let's name if info for the sake of clarity
        info = cube.domain_size()

        # The other socket can be read
        face_count = info.face_count
        edge_count = info.edge_count

        # Peer sockets can be read from any socket
        point_count = face_count.point_count
        # The two sockets wrap the same blender socket
        assert info._bsocket == point_count._bsocket

        # ---------------------------------------------------------------------------
        # Names collision
        # ---------------------------------------------------------------------------

        # The returned socket is the first one : 'Transform'
        # Let's name if info for the ssake of clarity
        transfo = nd.self_object.info()

        # Location peer socket
        loc = transfo.location

        # But rotation and scale are properties of Transformation class
        rot0 = transfo.rotation # rotation property of transfo

        # To read the peer socket, we need to suffix the name with _
        rot1 = transfo.rotation_
        assert rot0._bsocket != rot1._bsocket

        # ---------------------------------------------------------------------------
        # Example
        # ---------------------------------------------------------------------------

        #  Node 'Extrude Mesh' returns three output sockets:
        # - Mesh
        # - Top
        # - Side

        ico = Mesh.IcoSphere(subdivisions=2)

        # Extrude 30% of the faces
        ico.faces[Boolean.Random(probability=.3)].extrude(offset_scale=.4)

        # Duplicate extruded faces with a 0 scale extrusion
        ico.faces[ico.top_].extrude(offset_scale=0)

        # --- ico.top_ is needed twice, let's use an intermediary variable

        top = ico.top
        ico.faces[top].scale(scale=.5)

        # Another extrusion
        ico.faces[top].extrude(offset_scale=1)

        # --- Let's now dig the sides

        ico.faces[ico.side].extrude(offset_scale=0)
        top = ico.top
        ico.faces[top].scale(.8)
        ico.faces[top].extrude(offset_scale=-.01)

        # Output
        (ico + cube.set_position(offset=(5, 0, 0))).out()  

    # ====================================================================================================
    # Panels
    # ====================================================================================================

    with GeoNodes("Doc Panels"):
        
        # Create two options in a panel named Options

        with Panel("Options"):
            shade_smooth = Boolean(True, "Shade Smooth")
            subdiv = Integer(1, "Subdivision", 0, 5)
            
        # Create a third value in this panel using the argument syntax
        change_mat = Boolean(True, "Change Material", panel="Options")

        # Methods can be combined
        with Panel("Options"):
            count = Integer(5, "Count", 1, 10, panel="Sub options")

        # The panels can be chained with > char
        Factor = Float.Factor(.5, "Factor", 0, 1, panel="Options > Sub options")

    # ====================================================================================================
    # Creating geometries
    # ====================================================================================================

    with GeoNodes("Doc Creating Geometries"):

        # Geometry group input node is used if it exists,
        # Otherwise a group input node named 'Mesh' is created
        mesh = Mesh()

        # Node 'Cube'
        cube = Mesh.Cube()

        # In Groups, other geometries can be created
        curve = Curve(name="Curve")

        # Gemetries can be converted
        spiral = Curve.Spiral().to_mesh(profile_curve=Curve.Circle(radius=.1))

        # Volume
        cube_vol = Volume.Cube()
        
        (cube + mesh + curve + spiral + cube_vol).out()

    # ====================================================================================================
    # Input
    # ====================================================================================================

    with GeoNodes("Doc Input"):

        # ---------------------------------------------------------------------------
        # Initial creation
        # ---------------------------------------------------------------------------

        # Node input sockets can ge creating first to make clear the interface
        # of the node

        height = Float(3., "Height", 0, 10)

        with Panel("Helix Params"):
            resol   = Integer(12, "Resolution", 5, 100)
            rots    = Float(2, "Rotations", 0.1, 10)
            radius  = Float(1., "Radius", 0.01, 2)

        helix = Curve.Spiral(resolution=resol, rotations=rots, start_radius=radius, end_radius=radius,height=height)

        # ---------------------------------------------------------------------------
        # Using Inputs
        # ---------------------------------------------------------------------------

        # Input special socket create a socket of the proper and name and type

        with Panel("Cube Params"):
            cube = Mesh.Cube(size=Input(), vertices_x=Input(), vertices_y=Input(), vertices_z=2)

        # ---------------------------------------------------------------------------
        # Linking several sockets
        # ---------------------------------------------------------------------------

        spiral = Curve.Spiral()
        # Link all the inputs but the height
        spiral.node.link_inputs(None, "Spiral", exclude=["Height"])
        # The height is fixed
        spiral.height = Float.Input("Height")

        Geometry.join(helix, spiral, cube).out()

    # ====================================================================================================
    # Closure
    # ====================================================================================================

    with GeoNodes("Doc Closure"):

        # Create a closure adding to two entries 
        with Closure() as cl0:
            a = Float(1.0, "A")
            b = Float(1.0, "B")
            (a + b).out("Sum")

        # If evaluated immediately, the signature is read from the previous nodes.
        cl0.evaluate().out(panel = "Separate 0")

        # We can get the closure signature for future use
        sig = cl0.get_signature()

        # We can evaluate a closure using this signature
        cl1 = Closure(name="Closure 1")
        cl1.evaluate(signature=sig).out(panel="Signature 1")

        # We can evaluate another closure using a manual signature:
        # a couple of dicts for input and output
        sig = (
            {'A': 'Float', 'B': 'Float'},
            {'Sum': 'Float'})

        cl2 = Closure(name="Closure 2")
        cl2.evaluate(signature=sig).out(panel="Signature 2")
        
        with Closure.MenuSwitch() as cl:
            cl0.out("Closure 0")
            cl1.out("Closure 1")
            cl2.out("Closure 2")

        cl.node.menu = Input(default_value="Closure 0")
        cl.out()

    # ====================================================================================================
    # Simulation
    # ====================================================================================================

    with GeoNodes("Doc Simulation"):
        
        # Two input parameters
        count  = Integer(10, "Count", 1, 100)
        radius = Float(.1, "Radius", 0, 2)

        
        # Cloud of points
        cloud = Cloud.Points(count=count, position=Vector.Random((-5, -5, 5), (5, 5, 15)))
        
        # Gravity simulation with initial random speed
        for sim in cloud.simulation(Speed=Vector.Random(-1, 1)):
            
            # One speed per point
            speed = cloud.points.capture_attribute(sim.speed)
            
            # Increment the posiion
            cloud.position += speed*sim.delta_time
            
            # Acceleration
            speed += sim.delta_time*(0, 0, -9.81)
            
            # Bounce onfloor
            x, y, z = speed.xyz
            speed = speed.switch(nd.position.z.less_than(radius), (.9*x, .9*y, -.7*z))
            
            # Next iteration
            speed.out("Speed")
            
            # Within for loop, out to Zone Output Node
            cloud.out()
            
        mesh = Mesh.Grid(20, 20)
        mesh += cloud.instance_on(instance=Mesh.UVSphere(radius=radius))
            
        # Outside de the loop, out yo Group Output Node
        mesh.out()

    # ====================================================================================================
    # Repeat
    # ====================================================================================================

    with GeoNodes("Doc Repeat"):

        # Parameters
        levels = Integer(5, "Levels", 1, 10)
        size = Float(5, "Size", .1, 10)
        
        delta = size/levels
        
        cube = Mesh.Cube(size=(size, size, 1))
        
        for rep in cube.repeat(levels):
            
            sz = size - rep.iteration*delta
            floor = Mesh.Cube(size=(sz, sz, 1))
            floor.transform(translation=(0, 0, rep.iteration ))
            
            (cube + floor).out()
            
        cube.out()


    







