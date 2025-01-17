#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/29

@author: alain

-----------------------------------------------------
geonodes module
- Scripting Geometry Nodes
-----------------------------------------------------

module : macros
---------------
- Some macros

classes
-------

functions
---------
- Solidify

updates
-------
- creation : 2024/07/29
"""

from geonodes import *

# =============================================================================================================================
# Solidify a mesh

def solidify(mesh, thickness=.01, individual=False, merge_distance=.001):
    """ Solidify a mesh

    Arguments
    ---------
    - thickness (Float = .01) : thickness
    - individual (Boolean = False) : extrude individual faces
    - merge_distance (Float = .001) : distance to use to merge intial faces and the extruded mesh

    Returns
    -------
    - Mesh : the solidified mesh
    """

    with Layout("Macro - Solidify", color='MACRO'):

        mesh = Mesh(mesh)
        solidified = Mesh(mesh).flip_faces() + mesh.extrude_faces(offset_scale=thickness, individual=individual)
        solidified = solidified.switch(Float(merge_distance).greater_than(0), solidified.merge_by_distance(distance=merge_distance))

        return solidified.switch(Float(thickness).less_than(0), solidified.flip_faces())

# =============================================================================================================================
# Impulse : combine 2 map ranges
# The impulse can optionnally move at speed c and falloff with both time and distance

def impulsion(value, from_min=0, from_max=1, amplitude=1., increase=.5, decrease=.5, c=0, t=0, dist_falloff=0, time_falloff=0, smooth=True):
    """ Create an impulse varying with time and distance.

    The function returns a value in the interval [0, amplitude]
    The increase interval is [from_min, from_min + increase]
    The decrease interval is [to_max - decreare, to_max]

    Motion is taken into account by moving the intervals with c*t
    Falloff can take place with time and/or time. The fall is exp(-falloff * x^2))

    Arguments
    ---------
    - value (Float) : the input value
    - from_min (Float = 0) : value where the impulse starts
    - from_max (Float = 1) : value where the impulse ends
    - amplitude (Float = 1) : max returned value
    - increase (Float = .5) : increase length
    - decrease (Float = .5) : ecrease length
    - c (Float = 0) : impulse celerity
    - t (Float = 0) : time
    - dist_falloff (Float = 0) : distance falloff
    - time_falloff (Float = 0) : time falloff
    - smooth (Boolean = True) : use map_range smooth option
    """

    with Layout("Macro - Inpulse Factor", color='MACRO'):

        with Layout("Bounds"):
            ct = c*t
            fmin_up = (from_min + ct)._lc("From Min Up")
            fmax_up = (fmin_up + increase)._lc("From Max Up")

            fmax_dn = (from_max + ct)._lc("From Min Down")
            fmin_dn = (fmax_dn - decrease)._lc("From Max Down")

        with Layout("Two map ranges in smooth / linear version"):
            a0 = Float(value).map_range_smooth_step(from_min = fmin_up, from_max = fmax_up)
            b0 = Float(value).map_range_smooth_step(from_min = fmin_dn, from_max = fmax_dn, to_min=1, to_max=0)
            v0 = a0*b0

            a1 = Float(value).map_range_linear(from_min = fmin_up, from_max = fmax_up)
            b1 = Float(value).map_range_linear(from_min = fmin_dn, from_max = fmax_dn, to_min=1, to_max=0)
            v1 = a1*b1
            v = v1.switch(smooth, v0)._lc("Factor")

        with Layout("Amlitude with falloff"):
            v *= amplitude*gnmath.exp(-(time_falloff/100)*t**2 - (dist_falloff/100*value**2))

    return v

# =============================================================================================================================
# Integral

def integrals(x0=0, x1=1, count=100, **values):
    """ Compute integrals of a function on the interval [x0, x1]

    Plural version : several integrals are computed by the same macro
    Values are computed using nd.position.x

    For instance:
    ``` python
    count = 100

    # Integral of x in interval [0, 1]
    x = nd.position.x

    # Integral of sine in interval [0, pi]
    sin = gnmath.sin(x)

    integrals = macros.integrals(0, pi, count, x=x, sin=sin)

    mesh = Mesh()
    mesh.points.store("x", integrals["x"])
    mesh.points.store("sin", integrals["sin"])

    mesh.out()
    ```

    Arguments
    ---------
    - x0 (Float = 0) : Left bound of the integration interval
    - x1 (Float = 1) : Right bound of the integration interval
    - count (Integer = 100) : number of intervals
    - values (keyword arguments) : named argument

    Returns
    -------
    - dict keyed by values keys : the integrals
    """

    with Layout("Macro - Integrals", color='MACRO'):

        cloud = Mesh.LineEndPoints(count=count + 1, start_location=(x0, 0, 0), end_location=(x1, 0, 0))

        capture = cloud.points.capture_attribute(**{name: value for name, value in values.items()})

        factor = (x1 - x0)/(count + 1)

        return {name: (cloud.points.attribute_statistic(capture[name]).sum*factor)._lc(name) for name in values.keys()}

def integral(value, x0=0, x1=1, count=100):

    return integrals(x0=x0, x1=x1, count=count, integral=value)['integral']

# =============================================================================================================================
# Double integral

def double_integrals(x0=0, x1=1, y0=0, y1=1, count_x=100, count_y=100, **values):
    """ Compute double integrals of a function on the intervals [x0, x1], [y0, y1]

    Plural version : several integrals are computed by the same macro
    The values must be computed using:
    - variable 1 : nd.position.x
    - variable 2 : nd.position.y

    For instance:
    ``` python
    count = 100

    x = nd.position.x
    y = nd.position.y

    # Integral of x*y
    xy = nd.position.x * nd.position.y

    # Integral of x*sine in interval [0, 10],[0, pi]
    sin = (nd.position.x*10)*gnmath.sin(nd.position.y*pi)

    integrals = macros.double_integrals(x0=0, x1=10, y0=-pi/2, y1=pi/2, count=count, xy=x*y, sin=x*gnmath.cos(y))

    mesh = Mesh()
    mesh.points.store("xy", integrals["xy"])
    mesh.points.store("sin", integrals["sin"])

    mesh.out()
    ```

    Arguments
    ---------
    - x0 (Float = 0) : Left bound of the x integration interval
    - x1 (Float = 1) : Right bound of the x integration interval
    - y0 (Float = 0) : Left bound of the y integration interval
    - y1 (Float = 1) : Right bound of the y integration interval
    - count_x (Integer = 100) : number of intervals on x
    - count_y (Integer = 100) : number of intervals on y
    - values (keyword arguments) : named argument

    Returns
    -------
    - dict keyed by values keys : the integrals
    """

    with Layout("Macro - Double integrals", color='MACRO'):

        delta_x = x1 - x0
        delta_y = y1 - y0

        grid = Mesh.Grid(size_x=delta_x, size_y=delta_y, vertices_x=count_x, vertices_y=count_y)
        grid.points.offset = (x0 + delta_x/2, y0 + delta_y/2, 0)

        capture = grid.points.capture_attribute(**{name: value for name, value in values.items()})

        factor = delta_x*delta_y/count_x/count_y

        return {name: (grid.points.attribute_statistic(capture[name]).sum*factor)._lc(name) for name in values.keys()}

def double_integral(value, x0=0, x1=1, y0=0, y1=1, count_x=100, count_y=100):

    return double_integrals(x0=x0, x1=x1, y0=y0, y1=y1, count_x=count_x, count_y=count_y, integral2=value)['integral2']
