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

module : demo boids (WIP)
-------------------

Create utilities to manage neighbords in a cloud of points

updates
-------
- creation :   2025/02/07

$ DOC START

[Source Code](../demos/boids.py)

Boids utilities WIP

"""

from geonodes import *

primes = [100007, 100009, 10037]
USE_PRIMES = True
TO_INT_MODE = 'FLOOR'

# =============================================================================================================================
# Macros

def grid_coords(pos, radius):
    """ Returns the grid int coordinates of a position
    """
    with Layout("Cube Coords"):
        v = pos.scale(1/radius)
        x, y, z = v.xyz
        return x.to_integer(TO_INT_MODE), y.to_integer(TO_INT_MODE), z.to_integer(TO_INT_MODE)

def int_coord_hash(i, j, k=0, _2D=True):
    """ Compute the unique id of a int coordinates couple
    """
    with Layout("Unique ID"):
        if USE_PRIMES:
            if _2D:
                return i*primes[0] + j*primes[1]
            else:
                return i*primes[0] + j*primes[1] + k*primes[2]

        else:
            if _2D:
                return i.hash_value(j)
            else:
                return i.hash_value(j).hash_value(k)

def position_hash(pos, radius, _2D=True):
    """ Hash of a space position
    """
    with Layout("Position Hash"):
        return int_coord_hash(*grid_coords(pos, radius), _2D=_2D)

def neighbor_hashes(i, j, k=0, _2D=True):
    """ Hashes of neigbors
    """
    with Layout("Neighbor hashes"):
        res = []

        for i_ in [-1, 0, 1]:
            for j_ in [-1, 0, 1]:
                if _2D:
                    res.append(int_coord_hash(i+i_, j+j_, _2D=True))
                else:
                    for k_ in [-1, 0, 1]:
                        res.append(int_coord_hash(i+i_, j+j_, k+k_, _2D=False))

        return res

# =============================================================================================================================
# Maximize a speed

with GeoNodes("Max Speed", is_group=True):

    speed = Vector(None, "Speed")
    max_speed = Float(10, "Max Speed", 0)

    s = speed.length()
    v = (max_speed*4)*(1/(1 + gnmath.exp(-s/max_speed)) - .5)

    speed.scale((v/s).switch(s.equal(0), 1)).out()

# =============================================================================================================================
# Mark the neighbors of a point in a cloud

with GeoNodes("Neighbors"):

    cloud  = Cloud()
    index  = Integer(0, "Index", single_value=True)
    radius = Float(.1, "Radius", single_value=True)
    _2D    = Boolean(True, "2D")

    pos = cloud.points.sample_index(nd.position, index=index)
    i, j, k = grid_coords(pos, radius)
    named_hash = Integer("Hash")

    # ----------------------------------------------------------------------------------------------------
    # 2D

    with If(Cloud, _2D) as res:
        for ih, h in enumerate(neighbor_hashes(i, j, _2D=True)):
            if ih == 0:
                sel = named_hash.equal(h)
            else:
                sel |= named_hash.equal(h)

        sel &= nd.index != index

        res.option = Cloud(cloud).points[sel.bnot()].delete()

    # ----------------------------------------------------------------------------------------------------
    # 3D

    with Else(res):
        for ih, h in enumerate(neighbor_hashes(i, j, k, _2D=False)):
            if ih == 0:
                sel = named_hash.equal(h)
            else:
                sel |= named_hash.equal(h)

        sel &= nd.index != index

        res.option = Cloud(cloud).points[sel.bnot()].delete()

    res.out("Cloud")
    pos.out("Position")

# =============================================================================================================================
# Bounce within a domain

with GeoNodes("Domain Bounce"):

    cloud  = Cloud()
    domain = Geometry(None, "Domain")
    damp   = Float.Factor(.95, "Damp", 0, 1)
    _2D    = Boolean(True, "2D")

    bbox = domain.bounding_box()

    vmin = bbox.min_
    vmax = bbox.max_

    x, y, z = nd.position.xyz
    sx, sy, sz = Vector("Speed").xyz

    cloud.transform(translation= -vmin)

    with Layout("X, Y"):
        sel = x < 0
        cloud.points[sel]._Speed   = (-sx*damp, sy, sz)
        cloud.points[sel].position = (-x, y, z)

        sel = y < 0
        cloud.points[sel]._Speed = (sx, -sy*damp, sz)
        cloud.points[sel].position = (x, -y, z)

    with Layout("Z If 3D"):
        cl = Cloud(cloud)

        sel = z < 0
        cl.points[sel]._Speed = (sx, sy, -sz*damp)
        cl.points[sel].position = (x, y, -z)

        cloud = cloud.switch_false(_2D, cl)

    cloud.transform(translation = vmin - vmax)

    with Layout("X, Y"):
        sel = x > 0
        cloud.points[sel]._Speed = (-sx*damp, sy, sz)
        cloud.points[sel].position = (-x, y, z)

        sel = y > 0
        cloud.points[sel]._Speed = (sx, -sy*damp, sz)
        cloud.points[sel].position = (x, -y, z)

    with Layout("Z If 3D"):
        cl = Cloud(cloud)

        sel = z > 0
        cl.points[sel]._Speed = (sx, sy, -sz*damp)
        cl.points[sel].position = (x, y, -z)

        cloud = cloud.switch_false(_2D, cl)

    cloud.transform(translation=vmax)

    cloud.out()

# =============================================================================================================================
# Simulation

def gen_simulation(calc_acc_group, cloud, radius=1, max_speed=20., gravity=0., domain=None, _2D=True):

    speed = Vector("Speed")
    cloud.points[-speed.exists_]._Speed = Vector()

    with Simulation(cloud=cloud) as sim:

        # ----- Into the grid
        with If(Float, _2D) as hash:
           hash.option = position_hash(nd.position, radius, _2D=True)

        with Else(hash):
            hash.option = position_hash(nd.position, radius, _2D=False)
        #
        cloud.points._Hash = hash

        # ----- Loop

        with Repeat(cloud=sim.cloud, iterations=cloud.points.count) as rep:

            neighbors = Cloud(G().neighbors(rep.cloud, index=rep.iteration, radius=radius, _2d=_2D))

            node = Group(calc_acc_group, cloud=neighbors, position=neighbors.position_, speed=rep.cloud.points.sample_index(speed, index=rep.iteration)).link_from()

            rep.cloud.points[rep.iteration]._A = node.acceleration + gravity

        # ----- Update speed and position

        cloud = rep.cloud
        cloud.points._Speed  = G().max_speed(speed + Vector("A").scale(sim.delta_time), max_speed=max_speed)
        cloud.position += speed.scale(sim.delta_time)

        if domain is not None:
            cloud = G().domain_bounce(cloud, domain=domain, damp=.95, _2d=_2D)

        sim.cloud = cloud

    return sim.cloud

# =============================================================================================================================
# Density acceleration
#
# Acceleration from neighbors is computed as an acceleration decreasing with distance

with GeoNodes("Fluid Repulsion", is_group=True):

    cloud = Cloud()
    pos   = Vector(None, "Position", single_value=True)
    speed = Vector(None, "Speed", single_value=True)

    with Panel("Fluid"):
        dist = Float(.5, "Distance", 0)
        fac  = Float(3, "Factor", 0)

    dist_vect = pos - nd.position
    d = dist_vect.length()

    f = gnmath.max(0, dist**2 - d**2)
    f = 1/f**fac
    a = dist_vect.scale(f/d)

    acceleration = cloud.points.attribute_statistic(a).sum
    acceleration.out("Acceleration")


# =============================================================================================================================
# Calc forces within a cloud of points

with GeoNodes("Fluid Demo"):

    count       = Integer(100, "Count", 10)
    radius      = Float(.1, "Radius", single_value=True)
    max_speed   = Float(20, "Max Speed", 0, single_value=True)
    gravity     = Vector(0, "Gravity")
    size        = Float(5, "Domain Size")
    _2D         = Boolean(True, "2D")
    seed        = Integer(0, "Seed")

    domain = Mesh.Cube(size=size)
    size2 = size/2
    size2_ = -size2

    with If(Cloud, _2D) as cloud:
        cloud.option = Cloud.Points(count, position=Vector.Random((size2_, size2_, 0), (size2, size2, 0), seed=seed))
    with Else(cloud):
        cloud.option = Cloud.Points(count, position=Vector.Random(size2_, size2, seed=seed))

    sp = max_speed/10
    sp_ = -sp

    with If(Vector, _2D) as speed:
        speed.option = Vector.Random((sp_, sp_, 0), (sp, sp, 0), seed=seed + 1)
    with Else(speed):
        speed.option = Vector.Random((sp_, sp_, sp_), (sp, sp, sp), seed=seed + 1)

    cloud.points._Speed = speed

    cloud = gen_simulation("Fluid Repulsion", cloud, radius=radius, max_speed=max_speed, gravity=gravity, domain=domain, _2D=_2D)

    cloud.out()

def OLD():

    # ----- DEBUG


    if False:
        index = Integer(0, "Index", panel="Debug")

        cloud = G().neighbors(cloud, index=index, radius=radius)
        cloud.out()
        raise Break()

        cloud.points.radius=.1
        cloud.points[index].radius=.3


        pos = cloud.points.sample_index(nd.position, index=index)
        i, j, k = cube_coords(pos, radius)

        neighbors = neighbor_hashes(i, j, k)


        with Layout("Neigbors selection"):
            ok = Boolean(False)
            named_hash = Integer("Hash")

            for h in neighbors:
                ok |= named_hash.equal(h)

        cloud.points[ok.bnot()].delete()

        cloud.out()
        raise Break()


    # ----- Simulation

    cloud.points._Speed = Vector()
    cloud.points._Speed = Vector.Random(-1, 1, seed=1)


    with Simulation(cloud=cloud) as sim:

        sim.cloud.points._A = Vector()

        # ----- Loop

        with Repeat(cloud=sim.cloud, iterations=cloud.points.count) as rep:

            neighbors = Cloud(G().neighbors(rep.cloud, index=rep.iteration, radius=radius))

            pos = neighbors.position_

            dist_vect = pos - nd.position
            d = dist_vect.length()

            rel_speed = rep.cloud.points.sample_index(Vector("Speed"), index=rep.iteration) - Vector("Speed")
            speed_fac = rel_speed.length()

            f = gnmath.max(0, radius**2 - d**2)
            f = dist_vect.scale(speed_fac*d**3/10)

            A = neighbors.points.attribute_statistic(f).sum

            rep.cloud.points[rep.iteration]._A = A + (0, 0, g)

        cloud = rep.cloud

        cloud.points._Speed += Vector("A")*sim.delta_time
        cloud.points.offset = Vector("Speed")*sim.delta_time

        sim.cloud = G().bounce(cloud, domain=domain)

    cloud = sim.cloud

    #cloud = Cloud(G().bounce(cloud))

    cloud.out()
