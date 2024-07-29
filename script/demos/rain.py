from geonodes.script import *

def demo():

    with GeoNodes("Rain"):

        resolution     = Integer(100, "Resolution", 10, 500)
        size           = Float.Distance(20, "Map size", .1, 100, "Map size in meters")
        terrain_scale  = Float(.2, "Terrain Scale")
        terrain_height = Float(1., "Terrain Height")
        terrain_mat    = Material(None, "Terrain")
        density        = Float(1, "Density")
        omega          = Float(10, "Omega")
        height         = Float(.01, "Height")
        c              = Float(1, "Celerity")

        """

        omega    = Float(2., "Omega")
        height   = Float(2., "Height")
        material = Material(None, "Material")

        """

        with Layout("Terrain with puddles"):
            grid = Mesh.Grid(size_x=size, size_y=size, vertices_x=resolution, vertices_y=resolution)

            noise = Texture.Noise(vector=grid.position, scale=terrain_scale)
            z = (noise.fac - .5)*terrain_height
            water = z.less_equal(0)
            grid.points.offset = (0, 0, gnmath.max(0, z))
            water.store(grid.points, "Water")
            grid.faces.material = terrain_mat
            grid.faces.smooth = True

        with Simulation(geometry=None) as sim:

            with Layout("Dips"):
                dips = grid.faces.distribute_points(density=density*sim.delta_time, seed=nd.frame)
                dips.points.store("Age", 0)

            with Layout("Delete the dips not in a puddle"):
                grid_index = grid.points.sample_nearest(nd.position)
                water = grid.points.sample_index(Boolean.Named("Water"), grid_index)
                dips = dips.points[-water].delete()

            with Layout("Add to the current dips"):
                sim.geometry += dips

            with Layout("Update age"):
                pts = Points(sim.geometry)
                age = Float.Named("Age")
                pts.points.store("Age", age + sim.delta_time)
                sim.geometry = pts.points[age.greater_than(2)].delete()

        pts = Points(sim.geometry)

        with Repeat(z=0., index=0, iterations=pts.points.count) as rep:

            center = pts.points.sample_index(nd.position, index=rep.index)
            age    = pts.points.sample_index(Float.Named("Age"), index=rep.index)
            rep.index += 1

            dist = gnmath.max(.1, nd.position.distance(center))
            z = gnmath.sin(omega*dist - age*c)*height*/dist*(2 - age)

            rep.z += z

        with Layout("Update water height"):
            #grid.points.position = (nd.position*(1, 1, 0)) + (0, 0, rep.z)
            grid.points[Boolean.Named("Water")].offset = (0, 0, rep.z)
            pass

        (grid + pts).out()
        return

        (grid + pts).out()












        grid.out()
