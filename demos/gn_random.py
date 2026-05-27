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

module : random module
----------------------

Random generator

updates
-------
- created : 2025/01/12
- updated : 2026/04/07

This module provides a random data generator for floats, vectors and rotations


## Modifiers:

> - Random Uniform Value
> - Random Uniform Vector
> - Random Normal Value
> - Random Normal Vector
> - Random Rotation
"""

from geonodes import *

def demo():

    # ====================================================================================================
    # Random uniform
    # ====================================================================================================

    with GeoNodes("Random Uniform Value", is_group=True):

        min_value = Float(0, "Min")
        max_value = Float(1, "Max")
        ID        = Integer(0, "ID", hide_value=True, default_input='ID_OR_INDEX')
        seed      = Integer(0, "Seed")

        value  = Float.Random(min_value, max_value, ID, seed=seed)
        single = Cloud.Points(count=1).points.sample_index(value, index=0)
        
        value.out("Value")
        single.out("Single")
        (seed + 1).out("Seed")


    with GeoNodes("Random Uniform Vector", is_group=True):

        min_value = Vector(0, "Min")
        max_value = Vector(1, "Max")
        ID        = Integer(0, "ID", hide_value=True, default_input='ID_OR_INDEX')
        seed      = Integer(0, "Seed")

        vector = Vector.Random(min_value, max_value, ID, seed=seed)
        single = Cloud.Points(count=1).points.sample_index(Vector.Random(min_value, max_value, seed=seed + 1), index=0)
        
        vector.out("Vector")
        single.out("Single")
        (seed + 2).out("Seed")

    # ====================================================================================================
    # Random normal
    # ====================================================================================================

    with GeoNodes("Random Normal Value", is_group=True):

        value = Float(0,   "Value")
        scale = Float(1,   "Scale")
        ID    = Integer(0, "ID", hide_value=True, default_input='ID_OR_INDEX')
        seed  = Integer(0, "Seed")

        x1 = Float.Random(0, 1, id=ID, seed=seed)
        x2 = Float.Random(0, 1, id=ID, seed=seed + 1)

        y1 = gnmath.sqrt(-2*gnmath.log(x1, e))*gnmath.cos(2*pi*x2)

        y = value + scale*y1
        single = Cloud.Points(count=1).points.sample_index(y, index=0)

        y.out("Value")
        single.out("Single")
        (seed + 2).out("Seed")

    # ----------------------------------------------------------------------------------------------------
    # Normal vector
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Random Normal Vector", is_group=True):

        length = Float(1,       "Length",   tip="Vector average length")
        scale  = Float(0,       "Scale",    tip="Length scale")
        two_d  = Boolean(False, "2D", tip="2D Vectors (Z = 0)")
        ID     = Integer(0,     "ID", hide_value=True, default_input='ID_OR_INDEX')
        seed   = Integer(0,     "Seed")
    
        # ---------------------------------------------------------------------------
        # 2D normalized vectors
        # ---------------------------------------------------------------------------

        with Layout("Unit 2D vector"):
            theta    = Float.Random(0, 2*pi, id=ID, seed=seed)
            normal2D = Vector((gnmath.cos(theta), gnmath.sin(theta), 0))

        # ---------------------------------------------------------------------------
        # 3D normalized vectors
        # ---------------------------------------------------------------------------

        with Layout("Unit 3D vector"):
            z = Float.Random(-1, 1, id=ID, seed=seed + 1)
            r = gnmath.sqrt(gnmath.min(1, 1 - z*z))
            normal3D = Vector((r*gnmath.cos(theta), r*gnmath.sin(theta), z))

        # ---------------------------------------------------------------------------
        # Length
        # ---------------------------------------------------------------------------

        with Layout("Random length"):
            l = G().random_normal_value(length, scale, id=ID, seed = seed + 2)

        vector = normal3D.switch(two_d, normal2D).scale(l)
        single = Cloud.Points(count=1).points.sample_index(vector, index=0)

        vector.out("Vector")
        single.out("Single")
        (seed + 3).out("Seed")

    # ----------------------------------------------------------------------------------------------------
    # Random rotation
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Random Rotation", is_group=True):

        angle  = Float.Angle(0, "Angle",   tip="Average rotation")
        scale  = Float.Angle(0, "Scale",   tip="Rotation scale")
        ID     = Integer(0,     "ID", hide_value=True, default_input='ID_OR_INDEX')
        seed   = Integer(0,     "Seed")

        axis  = G().random_normal_vector(id=ID, seed=seed)
        ag    = G().random_normal_value(angle, scale, id=ID, seed=seed + 1)

        rotation = Rotation.FromAxisAngle(axis, ag)
        single = Cloud.Points(count=1).points.sample_index(rotation, index=0)

        rotation.out("Rotation")
        single.out("Single")
        (seed + 2).out("Seed")

    # ----------------------------------------------------------------------------------------------------
    # Random Noise
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Random Noise", is_group=True):

        pos = Vector(None, "Position", default_input='Position')
        seed = Integer(0, "Seed")

        offset = G("Random").uniform_vector(-1000, 1000, seed=seed).single
        seed = offset.seed
        
        noise = Texture.Noise(vector=pos + offset).node.link_inputs()
        
        v = Vector(noise.color).scale(2) - 1
        
        v.out("Position")
        noise.factor.out("Factor")
        noise.color.out("Color")
        seed.out("Seed")

    # ----------------------------------------------------------------------------------------------------
    # Random Row
    # ----------------------------------------------------------------------------------------------------

    with GeoNodes("Random Row", is_group=True):

        length    = Float(1., "Length", 0.001)
        part      = Float(.1, "Part", 0.001)
        scale     = Float(.01, "Scale", 0)
        use_count = Boolean(False, "Use Count")
        count     = Integer(10, "Count", 1)
        seed      = Integer(0, "Seed")

        n = gnmath.max(1, (length/part).to_integer())
        count.switch_false(use_count, n)
        part.switch(use_count, length/n)

        pts = Cloud.Points(count=count)
        parts = G("Random").normal_value(value=part, scale=scale, seed=seed)
        seed = parts.seed

        pts.points.Length = parts        
        total = pts.points.attribute_statistic(Float("Length")).sum_
        pts.points.Length = Float("Length") * (length/total)

        for rep in repeat(pts.points.count, pts=pts, z=0.0):
            pts = Cloud(rep.pts)
            pts.points[nd.index == rep.iteration].position = (0, 0, rep.z)
            rep.pts = pts
            rep.z += pts.points.sample_index(Float("Length"))

        pts = rep.pts

        with Layout("Single"):
            spt = Cloud.Points(1)
            spt.points.Length = length

        pts.switch(count == 1, spt)

        pts.out()
        seed.out("Seed")












        


        



