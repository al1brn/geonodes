print('-'*100)

from geonodes import *

def demo():

    # ====================================================================================================
    # Shaders

    with ShaderNodes("Trunk"):

        ped = Shader.Principled(base_color=(.097, .036, .008), roughness=.9)
        ped.out()


    with ShaderNodes("Foliage"):

        # Green color

        tex = Texture.Noise(scale=37)
        fac = tex.fac.map_range(0.3, .7)
        col0 = Color((0.002, 0.035, 0.015)).mix(fac, (0.001, 0.427, 0.015))

        # Brown read color

        tex = Texture.Noise(scale=20)
        fac = tex.fac.map_range(0.3, .7)
        col1 = Color((0.209, 0.168, 0.004)).mix(fac, (0.264, 0.033, 0.013))

        # Mix green brown

        tex = Texture.Noise(scale=5)
        fac = tex.fac.map_range(0.4, .6)
        col = col0.mix(fac, col1)

        ped = Shader.Principled(base_color=col, roughness=.9)
        ped.out()


    # ====================================================================================================
    # A single tree

    with GeoNodes("A Tree", is_group=True):

        # ----- Tree parameters

        base          = Float(.3, "Base width")
        height        = Float(7, "Tree Height")
        width         = Float(.5, "Tree Width")*height
        trunk         = Float.Factor(.2, "Trunk height", min=0, max=.9)
        conic         = Float.Factor(.4, "Conic shape", min=-1, max=1)

        # ----- Seed

        seed = Integer(0, "Seed")

        with Layout("Trunk"):
            cone = Mesh.Cone(radius_bottom=base/2, radius_top=base/6, depth=height*.9)
            cone.faces.material = "Trunk"
            cone.faces.shade_smooth = True

        with Layout("Foliage"):
            sphere = Mesh.IcoSphere(radius=.5, subdivisions=3)
            sphere.faces.material = "Foliage"
            sphere.faces.smooth = True

            trunk = 1 - trunk
            h = height*trunk
            w = nd.position.z.map_range(-.5, .5, width*(1 + conic), width*(1 - conic))
            sphere.points.position *= (w, w, h)*Vector.Random(.8, 1.2, seed=seed)
            sphere.points.offset = (0, 0, height - h/2)

            cone += sphere

        cone.out()

    # ====================================================================================================
    # A collection or randomly generated trees

    with GeoNodes("Trees Collection", is_group=True):

        count = Integer(10, "Count")

        seed  = Integer(0, "Seed")

        grid = Mesh.Line(end_location=(2*count, 0, 0), count=count)

        with grid.points.for_each(position=nd.position) as feel:

            hv = feel.index.hash_value(seed)
            tree = Mesh(Group("A Tree",
                base_width    = Float.Random(.1, .6, id=feel.index, seed=hv + 1),
                tree_height   = Float.Random( 1, 10, id=feel.index, seed=hv + 2),
                tree_width    = Float.Random( .2,  .5, id=feel.index, seed=hv + 3),
                trunk_height  = Float.Random(.1, .3, id=feel.index, seed=hv + 4),
                conic_shape   = Float.Random( .2,  1, id=feel.index, seed=hv + 5),

                seed          = hv,
                ).geometry)

            #tree.points.offset = feel.position

            feel.generated.geometry = tree.to_instance()


        feel.generated.geometry.out()

    # ====================================================================================================
    # A forest

    with GeoNodes("Forest"):

        surface = Mesh()
        density = Float(.3, "Density")*Float(1).switch(nd.is_viewport, .1)
        seed    = Integer(0, "Seed")

        cloud = surface.faces.distribute_points(distance_min=1, density_factor=density, seed=seed)

        trees = Group("Trees Collection", count=10, seed=seed + 1)
        forest = cloud.points.instance_on(
            instance=trees, pick_instance=True,
            scale=Float.Random(.5, 1.5, seed=seed + 2),
            rotation=(0, 0, Float.Random(0, tau, seed=seed + 3)),
            )

        forest.out()


    # ====================================================================================================
    # Demo

    with GeoNodes("Forest Demo"):

        density = Float(1, "Density")
        seed    = Integer(0, "Seed")

        plane = Mesh.Grid(vertices_x=50, vertices_y=50, size_x=100, size_y=100)
        plane.points.offset = (0, 0, Texture.Noise(scale=.03).fac*10)
        plane.faces.smooth = True

        forest = Group("Forest", mesh=plane, density=density, seed=seed + 1)

        (plane + forest).out()
