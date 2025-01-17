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

module : demo curly
-------------------

Playing with curve topology

updates
-------
- creation : 2024/07/23
- update :   2024/09/04
- update :   2025/01/12

$ DOC START

[Source Code](../demos/curly.py)

In this demo we play with curve topology

> [!NOTE]
> Modifiers:
> - Frise
> - Abs

``` python
from geonodes.demos import curly

curly.demo()
```
"""

from geonodes import *

def demo():

    with GeoNodes("Frise"):

        with Layout("Frise"):

            count       = Integer(10,   "Patterns Count", 1)
            use_circle  = Boolean(True, "Circular Shape")
            rot_handles = Boolean(True, "Rotate handles")

            resol = 2

            frise = Curve.Line(0, (count, 0, 0)).resample(count*resol + 1)
            frise.splines.type = 'BEZIER'
            frise.splines.resolution = 32

            frise[(nd.index % resol).equal(1)].offset = (-.6, 0, .5)

            frise[(nd.index % resol).equal(0)].set_both_handle_type(handle_type='ALIGN')
            frise[(nd.index % resol).equal(1)].set_both_handle_type(handle_type='FREE')

            frise[(nd.index % resol).equal(0)].left_handle_offset = (-.1, 0, 0)
            frise[(nd.index % resol).equal(0)].right_handle_offset = (.3, 0, 0)

            frise[(nd.index % resol).equal(1)].left_handle_offset = (0.5, 0, .5)
            frise[(nd.index % resol).equal(1)].right_handle_offset = (.2, 0, .9)

            radius = (count/tau)._lc("radius")
            theta = (nd.position.x/radius)._lc("theta")

            frise.points._Theta = theta
            frise.points._Left  = frise.left_handle_position  - nd.position
            frise.points._Right = frise.right_handle_position - nd.position

            straight = Curve(frise)

        with Layout("Circle"):

            frise.position = radius*gnmath.cos(theta), radius*gnmath.sin(theta), nd.position.z

            unrotated = Curve(frise)

            theta = Float("Theta") + pi/2

            p = Vector("Left")
            frise.left_handle_position = nd.position + (p.x*gnmath.cos(theta), p.x*gnmath.sin(theta), p.z)

            p = Vector("Right")
            frise.right_handle_position = nd.position + (p.x*gnmath.cos(theta), p.x*gnmath.sin(theta), p.z)

            frise = unrotated.switch(rot_handles, frise)

        straight.switch(use_circle, frise).out()

    with GeoNodes("Abs"):

        count = Integer(10, "Resolution")
        x_loc = 0

        with Layout("A"):
            A = Curve.Line(0, (.8, 0, 0)).resample(3)

            A[1].position = (.4, 0, 1)

            A += Curve.Line((.2, 0, .5), (.6, 0, .5))


        A.offset = (x_loc, 0, 0)
        x_loc += 1

        alphabet = A

        with Layout("B"):

            B = Curve.Line(0, (1, 0, 0)).resample(4)
            B.splines.type = 'BEZIER'

            B[1].position = (0, 0, 1)
            B[2].position = (0, 0, .6)
            B[3].position = (0, 0, 0)

            B[1].right_handle_position = (.5, 0, 1)

            B[2].left_handle_position = (.5, 0, .6)
            B[2].right_handle_position = (.7, 0, .6)

            B[3].left_handle_position = (.7, 0, 0)

        B.offset = (x_loc, 0, 0)
        x_loc += 1

        alphabet += B

        with Layout("S"):
            S = Curve.Line(end = (0, 0, 1)).resample(3)
            S.splines.type = 'BEZIER'
            #S.splines.resolution = 30

            delta = .4

            S[0].offset = (-.2, 0, .1)
            S[2].offset = (.2, 0, -.1)


            S[0].right_handle_position = (.3, 0, -.3)
            S[2].left_handle_position  = (-.3, 0, 1.3)

            S[1].left_handle_position = (.6, 0, .5)
            S[1].right_handle_position = S[1].left_handle_position * (-1, 1, 1)


        S.offset = (x_loc, 0, 0)
        x_loc += 1

        alphabet += S
        alphabet.splines.resolution = 24


        alphabet.out()
