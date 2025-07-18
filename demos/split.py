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

module : demo split
--------------------

Split mesh in half and mord

updates
-------
- creation : 2025/05/24

$ DOC START

[Source Code](../demos/split.py)

This demo provides four modifiers:
- Split Half :
  Split a mesh in two parts along X, Y or Z plane
- Split Eight :
  Split a mesh in eight parts along the 3 planes
- Split Fractal :
  Split recursively in eight parts : 8, 64, 512,... parts
- Explode Islands :
    Convert islands into instances and explode them with a factor


``` python
from geonodes.demos import split

split.demo()
```
"""

from geonodes import *

def demo():

    # =============================================================================================================================
    # Split in two parts

    with GeoNodes("Split Half"):

        mesh  = Mesh()
        dir   = Integer.MenuSwitch({'X': 0, 'Y': 1, 'Z': 2}, menu='Z', name="Direction")
        mat   = Material(None, "Material")

        with Layout("Dimensions"):
            node = mesh.points.attribute_statistic(attribute=nd.position).node
            center = (node.min + node.max)/2

            size = (node.max - node.min)*2
            sx, sy, sz = size.xyz

            trans = Vector.Switch(dir.equal(0), Vector.Switch(dir.equal(1), (0, 0, sz), (0, sy, 0)), (sx, 0, 0))

        with Layout("Split Cube"):
            cube = Mesh.Cube(size=size)
            cube.set_material(mat)

        with Layout("Top half"):
            cube.transform(translation=center + trans.scale(-.5))
            top = Mesh(mesh).intersect(cube, solver='EXACT')

        with Layout("Bottom half"):
            cube.transform(translation=trans)
            bot = Mesh(mesh).intersect(cube, solver='EXACT')

        splitten = top + bot


        splitten.out()
        bot.out("Half 1")
        top.out("Half 2")

    # =============================================================================================================================
    # Split in eight parts

    with GeoNodes("Split Eight"):

        mesh  = Mesh()
        mat   = Material(None, "Material")

        z_node     = G().split_half(mesh,            direction='Z', material=mat).node
        y_node_1   = G().split_half(z_node.half_1,   direction='Y', material=mat).node
        y_node_2   = G().split_half(z_node.half_2,   direction='Y', material=mat).node
        x_node_1_1 = G().split_half(y_node_1.half_1, direction='X', material=mat).node
        x_node_1_2 = G().split_half(y_node_1.half_2, direction='X', material=mat).node
        x_node_2_1 = G().split_half(y_node_2.half_1, direction='X', material=mat).node
        x_node_2_2 = G().split_half(y_node_2.half_2, direction='X', material=mat).node


        splitten = x_node_1_1.half_1 + (x_node_1_1.half_2,
                x_node_1_2.half_1, x_node_1_2.half_2,
                x_node_2_1.half_1, x_node_2_1.half_2,
                x_node_2_2.half_1, x_node_2_2.half_2)

        splitten.out()

        x_node_1_1.half_1.out("Part 1")
        x_node_1_1.half_2.out("Part 2")
        x_node_1_2.half_1.out("Part 3")
        x_node_1_2.half_2.out("Part 4")
        x_node_2_1.half_1.out("Part 5")
        x_node_2_1.half_2.out("Part 6")
        x_node_2_2.half_1.out("Part 7")
        x_node_2_2.half_2.out("Part 8")


    # =============================================================================================================================
    # Split fractal

    with GeoNodes("Split Fractal"):

        mesh  = Mesh()
        count = Integer(2, "Count", 1, 6)
        mat   = Material(None, "Material")

        with Repeat(mesh=mesh, iterations=count) as rep:

            insts = rep.mesh.points.split_to_instances(group_id=nd.mesh_island().island_index)

            with insts.insts.for_each() as feel:

                island = feel.element.realize()

                feel.generated.geometry = G().split_eight(island, material=mat)

            rep.mesh = feel.generated.geometry

        mesh = rep.mesh

        mesh.out()

    # =============================================================================================================================
    # Explode islandes

    with GeoNodes("Explode Islands"):

        mesh = Mesh()
        factor = Float(1, "Factor", 0)

        insts = mesh.points.split_to_instances(group_id=nd.mesh_island().island_index)
        with insts.insts.for_each() as feel:

            island = Mesh(feel.element.realize())
            node = island.points.attribute_statistic(attribute=nd.position).node
            center = (node.max + node.min)/2
            island.transform(translation=-center)
            inst = island.to_instance()
            inst.position = center

            feel.generated.geometry = inst

        insts = Instances(feel.generated.geometry)

        insts.position *= factor

        insts.out()
