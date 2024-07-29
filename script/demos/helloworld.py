from geonodes.script import *

def demo(material="Material"):

    # The Geometry Nodes modifier

    with GeoNodes("Hello World"):

        # Let's get the parameters from the user

        count    = Integer(100, "Resolution", 10, 500, "Figure resolution, dont't be too greedy")
        size     = Float.Distance(20, "Map size", .1, 100, "Map size in meters")
        omega    = Float(2., "Omega")
        height   = Float(2., "Height")
        material = Material(None, "Material")

        # The base (x, y) grid
        grid = Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)

        # We compute z
        with Layout("Computing the wave"):

            distance = (nd.position * (1, 1, 0)).length
            z = height * gnmath.sin(distance*omega)/distance

        # Let's change the z coordinate of our vertices
        with Layout("Changing the z coordinate"):
            grid.offset = (0, 0, z)

        with Layout("Finalize"):
            # We smooth the grid
            grid.faces.smooth = True

            # We set the material created above
            grid.faces.material = material

        # We are done: plugging the deformed grid as the modified geometry
        grid.out()
