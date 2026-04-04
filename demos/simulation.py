from geonodes import GeoNodes, Vector, Integer, Float, Mesh, simulation, repeat, nd, gnmath, Closure, Group
from geonodes import Layout, Curve, ShaderNodes, Material, snd, Shader, Color, Panel, String

def demo():

    with ShaderNodes("Curve Color", replace_material=True):
        col = snd.attribute("Color").color
        ped = Shader.Principled(base_color=col)
        ped.out()

    with GeoNodes("Trajectory", is_group=True):

        pos = Vector(0, "Start Location")
        iterations = Integer(10, "Iterations", 1)
        f = Closure(None, "Function")

        line = Mesh.Line(start_location=pos).points[nd.index.greater_than(0)].delete()
        for sim in simulation(mesh=line, pos=pos, t=0.):

            dt = sim.delta_time/iterations

            for rep in repeat(pos=sim.pos, t=sim.t, iterations=iterations):

                v = f.evaluate(t=rep.t, signature=({"t": Float}, {"Speed": Float})).speed
                dx = v*dt

                rep.pos += (dx, 0, dt)
                rep.t += dt

            count = sim.mesh.points.count
            sim.mesh = sim.mesh.points[nd.index.equal(count-1)].extrude(rep.pos - sim.pos)
            sim.pos = rep.pos
            sim.t = rep.t

        sim.mesh.out()

    with GeoNodes("Transformation"):

        w   = Float(1., "Omega")
        amp = Float(1., "Amplitude")
        c   = 1.

        with Closure() as traj_e:
            t = Float(0, "t")
            v = w*amp*gnmath.cos(w*t)

            v.out("Speed")


        with Closure() as traj_m:
            t = Float(0, "t")
            v = traj_e.evaluate(t=t)
            gamma = gnmath.sqrt(c**2 + v**2)/c**2
            beta = v/gamma

            beta.out("Speed")


        mesh = Group("Trajectory", function=traj_e)._out
        mesh += Group("Trajectory", function=traj_m)._out

        mesh.to_curve().out()


    with GeoNodes("Add Legends"):
        curves = Curve()
        radius = Float(.05, "Radius")
        mat = Material("Curve Color", "Material")

        with Panel("Legend"):
            names = String("Curve 1\nCurve 2", "Names")
            pos = Vector(0, "Position")
            delta = Float(1, "Delta")
            length = Float(1, "Length")

        seed = Integer(0, "Seed")

        for feel in curves.splines.for_each():

            cur = Curve(feel.element)
            leg_pos = pos + (0, 0, delta + feel.index*delta)
            leg = Curve.Line(start=leg_pos, end=leg_pos + (length, 0, 0))
            cur += leg

            mesh = Curve(cur).to_mesh(profile_curve=Curve.Circle(radius=radius))
            mesh.faces.Color = Color.CombineHSV(Float.Random(0, 1, seed=feel.index.hash_value(seed=seed), id=0), .9, .9)
            feel.geometry = mesh

        mesh = Mesh(feel.generated)
        mesh.faces.material = mat
        mesh.faces.shade_smooth = True

        mesh.out()




        






        

