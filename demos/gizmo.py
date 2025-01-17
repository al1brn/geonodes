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

module : demo gizmo
-------------------

Working with Gizmo

updates
-------
- created :   2025/01/12

$ DOC START

[Source Code](../demos/gizmo.py)

Playing with gizmos


> [!NOTE]
> Modifiers:
> - Gizmo Demo

``` python
from geonodes.demos import gizmo

gizmo.demo()
```
"""

from geonodes import *

def demo():

    with GeoNodes("Gizmo Demo"):

        geo = Geometry()

        with Layout("Cube size"):

            x, y, z = Float(1, "X"), Float(1, "Y"), Float(1, "Z")

            scale = Float(1, "Scale")

            size = Vector((x, y, z))*scale

        with Layout("Size gizmos"):

            val1, val2, val3 = Float(1), Float(2), Float(3)
            gizmo = val1.linear_gizmo(val2, val3)

            xg = x.linear_gizmo(position=(x/2*scale, 0, 0), direction=(1, 0, 0), color_id='X')
            x.pin_gizmo = True

            yg = y.linear_gizmo(position=(0, y/2*scale, 0), direction=(0, 1, 0), color_id='Y')
            y.pin_gizmo = True

            zg = z.linear_gizmo(position=(0, 0, z/2*scale), direction=(0, 0, 1), color_id='Z')
            z.pin_gizmo = True

            sg = scale.linear_gizmo(position=size/2, direction=(1, 1, 1))
            scale.pin_gizmo=True

        with Layout("Cube"):
            cube = Mesh.Cube(size=size) + (xg, yg, zg, sg)

        with Layout("Transformation Gizmo"):

            matrix = Matrix(None, name="Transformation")
            matrix = Matrix() #None, name="Transformation")
            matrix.transform_gizmo(use_translation_x=False, use_translation_y=False, use_translation_z=False, use_scale_x=False, use_scale_y=False, use_scale_z=False)
            matrix.pin_gizmo = True

            cube.transform(transform=matrix)

        cube.out()
