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

module : demo helloworld
------------------------

This basic demo creates a onludlated surface.

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12

$ DOC START

[Source Code](../demos/helloworld.py)

This first demo creates an ondulated surface.

You will see:
- Creating a Geometry Nodes modifier
- Creating input sockets
- Creating a Mesh Grid
- Computing
- Changing the grid verices positions
- Outputing the resulting grid

> [!NOTE]
> Modifiers:
> - Hello World

``` python
from geonodes.demos import helloworld

helloworld.demo()
```
"""

__author__ = "Alain Bernard"
__email__  = "lesideesfroides@gmail.com"
__copyright__ = "Copyright (c) 2025, Alain Bernard"
__license__ = "GNU GPL V3"
__version__ = "3.0.0"
__blender_version__ = "4.3.0"


from geonodes import *

def demo():

    # The Geometry Nodes modifier

    with GeoNodes("Hello World"):

        # Let's get the parameters from the user

        count    = Integer(100, "Resolution", 10, 500, "Figure resolution, dont't be too greedy")
        size     = Float.Distance(20, "Map size", .1, 100, "Map size in meters")
        omega    = Float(2., "Omega", single_value=True)
        height   = Float(2., "Height",single_value=True)
        material = Material(None, "Material")

        # The base (x, y) grid
        grid = Mesh.Grid(vertices_x=count, vertices_y=count, size_x=size, size_y=size)

        # We compute z
        with Layout("Computing the wave"):

            distance = (nd.position * (1, 1, 0)).length()
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
