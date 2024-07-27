def demo(material="Material"):

    import geonodes.script as gn

    # The Geometry Nodes modifier

    with gn.GeoNodes("Hello World"):

        # Let's get the parameters from the user

        count   = gn.Integer(100, "Resolution", 10, 300, "Figure resolution, dont't be too greedy")
        size    = gn.Float.Distance(20, "Map size", .1, 100, "Map size in meters")
        omega   = gn.Float(2., "Omega")
        height  = gn.Float(2., "Height")

        # The base (x, y) grid
        grid = gn.Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)

        # We compute z
        with gn.Layout("Computing the wave"):

            distance = (gn.nd.position * (1, 1, 0)).length
            z = height * gn.gnmath.sin(distance*omega)/distance


        # Let's change the z coordinate of our vertices
        grid.offset = (0, 0, z)

        # The color of the surface depends upon the orientation of the faces
        # towerd a control object

        target_object = gn.Object(name="Direction")
        loc = target_object.info().location

        hue = ((grid.faces.normal @ loc)/2 + .5)**2
        grid.points.store_named_attribute("Color", gn.Vector(gn.Color.CombineHSV(hue, .9, .7)))

        # We smooth the grid
        grid.faces.smooth = True

        # We set the material created above
        grid.faces.material = material

        # We are done: plugging the deformed grid as the modified geometry
        grid.to_output()
