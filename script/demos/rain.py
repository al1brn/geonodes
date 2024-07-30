from geonodes.script import *


def dip_wave(center, t, c=5, falloff=30, omega=4, height=1, amp_only=False):
    with Layout("Dip Wave", color='MACRO'):
        dist = nd.position.distance(center)
        fac  = gnmath.max(0, c*t - dist)
        amp = height*gnmath.sin(2*gnmath.atan(falloff*fac))/gnmath.max(.5, dist)
        z = amp*gnmath.sin(omega*fac)
        #return height*gnmath.sin(2*omega*gnmath.atan(fac))
        return z.switch(amp_only, amp)

def single_wave():

    with GeoNodes("Single Wave"):
        grid = Mesh.Grid(20, 20, 200, 200)
        grid.faces.smooth = True

        z = dip_wave(0, Float(0, "Time"), Float(5, "c"), Float(30, "Falloff"), Float(4, "Omega"), Float(1, "Height"), amp_only=Boolean(False, "Amplitude Only"))
        grid.points.offset = (0, 0, z)

        grid.out()



def demo():

    with GeoNodes("Rain"):

        resolution     = Integer(100, "Resolution", 10, 500)
        size           = Float.Distance(20, "Map size", .1, 100, "Map size in meters")
        terrain_scale  = Float(.2, "Terrain Scale")
        terrain_height = Float(1., "Terrain Height")
        terrain_mat    = Material(None, "Terrain")
        density        = Float(1, "Density")
        omega          = Float(4, "Omega")
        height         = Float(.01, "Height")
        c              = Float(5, "Celerity")
        falloff        = Float(30, "Falloff", 0)

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

            with Layout("Dip location and age"):
                center = pts.points.sample_index(nd.position, index=rep.index)
                age    = pts.points.sample_index(Float.Named("Age"), index=rep.index)
                rep.index += 1

            if True:
                z = dip_wave(center, t=age, c=c, falloff=falloff, omega=omega, height=height)

            else:
                dist = gnmath.max(.1, nd.position.distance(center))._lc("Distance")

                with Layout("Amplitude decreases with time and distance"):

                    fac = falloff*gnmath.max(c*age - dist, 0)
                    amp = height*gnmath.sin(2*gnmath.atan(fac))

                with Layout("The wave"):
                    #z = gnmath.sin(omega*dist - age*c)*amp
                    z = amp*gnmath.sin(omega*fac)

            rep.z += z

        with Layout("Update water height"):
            #grid.points.position = (nd.position*(1, 1, 0)) + (0, 0, rep.z)
            grid.points[Boolean.Named("Water")].offset = (0, 0, rep.z)
            pass

        (grid + pts).out()
        return

        (grid + pts).out()












        grid.out()
