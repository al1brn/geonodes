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

module : demo forest
--------------------

ForEach zone

updates
-------
- creation :   2025/01/12

$ DOC START

[Source Code](../demos/forest.py)

A simple parameterized forest.


> [!NOTE]
> Modifiers:
> - A Tree
> - Trees Collection
> - Forest
> - Forest Demo

``` python
from geonodes.demos import forest

forest.demo()
```
"""

from geonodes import *

def demo():

    # ====================================================================================================
    # Shaders

    with ShaderNodes("Trunk"):

        ped = Shader.Principled(base_color=(.097, .036, .008), roughness=.9)
        ped.out()


    with ShaderNodes("Foliage"):

        # Green color

        fac = Texture.Noise(scale=37)
        fac = fac.map_range(0.3, .7)
        col0 = Color((0.002, 0.035, 0.015)).mix((0.001, 0.427, 0.015), fac)

        # Brown read color

        fac = Texture.Noise(scale=20)
        fac = fac.map_range(0.3, .7)
        col1 = Color((0.209, 0.168, 0.004)).mix((0.264, 0.033, 0.013), fac)

        # Mix green brown

        fac = Texture.Noise(scale=5)
        fac = fac.map_range(0.4, .6)
        col = col0.mix(col1, fac)

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

        grid = Mesh.LineEndPoints(end_location=(2*count, 0, 0), count=count)

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

        cloud = surface.faces.distribute_points_poisson(distance_min=1, density_factor=density, seed=seed)

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
        plane.points.offset = (0, 0, Texture.Noise(scale=.03)*10)
        plane.faces.smooth = True

        forest = Group("Forest", mesh=plane, density=density, seed=seed + 1)

        (plane + forest).out()
