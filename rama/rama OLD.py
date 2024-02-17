#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 08:01:54 2022

@author: alain
"""

import bpy

import numpy as np

from geopy.core.multiresgrid import MultiResGrid
from geopy.core.noise import Perlin
from geopy.core.noise import noise, terrain

# ====================================================================================================
# Rama dimensions

cyl_length     = 50.
cyl_radius     = 8.   # Sea level
north_altitude = .05  #  50 m above the sea level
south_altitude = .5   # 500 m above sea level
sea_length_raw = 10.  # sea_length is sea_length_raw minus cliff lengths
cliff_slope    = .1   # Factor giving the length of the cliff from its height

# ----- Computed parameters

cyl_x0         = -cyl_length/2
cyl_x1         =  cyl_length/2

north_cliff_length = north_altitude * cliff_slope
south_cliff_length = south_altitude * cliff_slope

north_length   = (cyl_length - sea_length_raw)/2 - north_cliff_length
south_length   = (cyl_length - sea_length_raw)/2 - south_cliff_length

north_x0       = cyl_x0
north_x1       = north_x0 + north_length

south_x1       = cyl_x1
south_x0       = south_x1 - south_length

sea_x0         = north_x1 + north_cliff_length
sea_x1         = south_x0 - south_cliff_length
sea_length     = sea_x1 - sea_x0

# ----- For reference

print(f"North: {int(north_x0*1000):6d} to {int(north_x1*1000): 6d}: {int(north_length*1000):6d}")
print(f"Sea  : {int(sea_x0*1000):6d} to {int(sea_x1*1000): 6d}: {int(sea_length*1000):6d}")
print(f"South: {int(south_x0*1000):6d} to {int(south_x1*1000): 6d}: {int(south_length*1000):6d}")

# ====================================================================================================
# Get rama cylinder

def get_cylinder(factor=1, scale=1000, select=None):
    
    if isinstance(select, str):
        select = {select}
    
    cylinder = {}
    
    # ----- Rama cylinder

    name = "Rama Cylinder"
    if select is None or name in select:

        nx = int(rama_land)*3
        ny = int(rama_circ)*3
        
        ncuts = 4

        cuts = [
            {'axis': 'x', 'at': north_x1 - .00, 'to': sea_x0 + .00, 'cuts': 15},
            {'axis': 'x', 'at': sea_x1   - .00, 'to': south_x0 + .00, 'cuts': 15},

            #{'axis': 'x', 'at': rama_north_light_X0, 'to': rama_north_light_x0, 'cuts': ncuts},
            #{'axis': 'x', 'at': rama_north_light_x1, 'to': rama_north_light_X1, 'cuts': ncuts},
            ]
        
        #cuts = None
        
        #for y_light in rama_light_ys:
        #    cuts.append({'axis': 'y', 'at': y_light + rama_north_light_Y0, 'to': y_light + rama_north_light_y0, 'cuts': ncuts})
        #    cuts.append({'axis': 'y', 'at': y_light + rama_north_light_y1, 'to': y_light + rama_north_light_Y1, 'cuts': ncuts})
    
        func = lambda x, y: rama_cylinder(x, y, factor=factor, scale=scale)
        cylinder[name] = MultiResGrid(nx, ny, bounds=((cyl_x0, -rama_ymax), (cyl_x1, rama_ymax)), func=func, cuts=cuts)
    
    
    # ----- North land

    name = "Rama Land North"
    if select is None or name in select:

        nx = int(rama_land)*3
        ny = int(rama_circ)*3
        
        ncuts = 4

        cuts = [
            {'axis': 'x', 'at': rama_north_x1-.2, 'to': rama_north_x1, 'cuts': 15},

            {'axis': 'x', 'at': rama_north_light_X0, 'to': rama_north_light_x0, 'cuts': ncuts},
            {'axis': 'x', 'at': rama_north_light_x1, 'to': rama_north_light_X1, 'cuts': ncuts},
            ]
        
        for y_light in rama_light_ys:
            cuts.append({'axis': 'y', 'at': y_light + rama_north_light_Y0, 'to': y_light + rama_north_light_y0, 'cuts': ncuts})
            cuts.append({'axis': 'y', 'at': y_light + rama_north_light_y1, 'to': y_light + rama_north_light_Y1, 'cuts': ncuts})
    
        func = lambda x, y: north_land(x, y, factor=factor, scale=scale)
        cylinder[name] = MultiResGrid(nx, ny, bounds=((-rama_land - rama_sea/2, -rama_ymax), (-rama_sea/2, rama_ymax)), func=func, cuts=cuts)

    # ----- south land

    name = "Rama Land South"
    if select is None or name in select:

        nx = int(rama_land)
        ny = int(rama_circ)
        
        ncuts = 4

        cuts = [
            {'axis': 'x', 'at': rama_south_x0, 'to': rama_south_x0 + .25, 'cuts': 20},

            {'axis': 'x', 'at': rama_south_light_X0, 'to': rama_south_light_x0, 'cuts': ncuts},
            {'axis': 'x', 'at': rama_south_light_x1, 'to': rama_south_light_X1, 'cuts': ncuts},
            ]
        
        for y_light in rama_light_ys:
            cuts.append({'axis': 'y', 'at': y_light + rama_south_light_Y0, 'to': y_light + rama_south_light_y0, 'cuts': ncuts})
            cuts.append({'axis': 'y', 'at': y_light + rama_south_light_y1, 'to': y_light + rama_south_light_Y1, 'cuts': ncuts})
        
    
        func = lambda x, y: south_land(x, y, factor=factor, scale=scale)
    
        cylinder[name] = MultiResGrid(nx, ny, bounds=((rama_sea/2, -rama_ymax), (rama_sea/2 + rama_land, rama_ymax)), func=func, cuts=cuts)

    # ----- sea

    name = "Rama Sea"
    if select is None or name in select:

        nx = int(rama_sea)
        ny = int(rama_circ)
    
        func = lambda x, y: sea(x, y, factor=factor, scale=scale)
    
        cylinder[name] = MultiResGrid(nx, ny, bounds=((rama_sea_x0, -rama_ymax), (rama_sea_x1, rama_ymax)), func=func)
    
    # ----- North Hemisphere

    name = "Rama North Hemi"
    if select is None or name in select:

        nx = 8
        ny = 16
    
        func = lambda x, y: north_hemisphere(x, y, scale=scale)
    
        cylinder[name] = MultiResGrid(nx, ny, bounds = ((-np.pi/2, -np.pi), (0, np.pi)), func=func)
        
    if True:
        for i, phi, width in zip(range(3), rama_platform_phis, rama_platform_phis):

            name = f"Rama Platform {i}"
            if select is None or name in select or "Rama Platform" in select:
                cylinder[name] = north_platform_grid(4, 360, phi=phi, width=width, scale=scale)

    # ----- South hemisphere
    
    name = "Rama South Hemi"
    if select is None or name in select:

        nx = 8
        ny = 16
    
        func = lambda x, y: south_hemisphere(x, y, scale=scale)
    
        cylinder[name] = MultiResGrid(nx, ny, bounds = ((0, -np.pi), (np.pi/2, np.pi)), func=func)
        
    # ----- South cones
    
    for i_cone in range(7):
        
        name = f"Rama Cone {i_cone}"
        
        if select is None or name in select:
            
            if i_cone == 0:
                
                cylinder[name] = main_cone_grid(scale)
                
            else:
                
                cylinder[name] = small_cone_grid(i_cone, scale)
        
        
    return cylinder



































# ====================================================================================================
# OLD


rama_length    = 50.
rama_radius    = 8.
rama_circ      = rama_radius*2*np.pi
rama_ymax      = rama_circ / 2
rama_sea       = 10.
rama_land      = (rama_length - rama_sea)/2

rama_north_x1  = -rama_sea/2
rama_north_x0  = rama_north_x1 - rama_land
rama_north_riff_width = .25  
rama_north_riff_slope = .01

rama_south_x0  = rama_sea/2
rama_south_x1  = rama_south_x0 + rama_land
rama_south_riff_width = .5
rama_south_riff_slope = .03

rama_sea_x0 = -rama_sea/2 - .2
rama_sea_x1 =  rama_sea/2 + .2

# ----- Hemispheres

rama_hemi_flatten = 1

rama_north_hemi_center = np.array((rama_north_x0, 0., 0.))

rama_platform_widths = [.1, .15, .2]
rama_platform_phis   = [np.pi/2*.75, np.pi/2*.5, np.pi/2*.25]

rama_south_hemi_center = np.array((rama_south_x1, 0., 0.))

rama_cone_length = 10
rama_cone_radius = 1
rama_cones_scale = .6
rama_cones_y0    = rama_radius*rama_hemi_flatten*.9

# ----- Lights chanels

rama_light_length = 8.0
rama_light_width  = 0.1
rama_light_slope  = 0.3
rama_light_ys     = [-rama_circ/3, 0, rama_circ/3]

rama_north_light_x0 = rama_north_x0 + (rama_land - rama_light_length)/2
rama_north_light_x1 = rama_north_light_x0 + rama_light_length
rama_north_light_y0 = -rama_light_width/2
rama_north_light_y1 = +rama_light_width/2

rama_north_light_X0 = rama_north_light_x0 - rama_light_slope
rama_north_light_X1 = rama_north_light_x1 + rama_light_slope
rama_north_light_Y0 = rama_north_light_y0 - rama_light_slope
rama_north_light_Y1 = rama_north_light_y1 + rama_light_slope

rama_north_light_zs = [.66, .1, .76]

rama_south_light_x0 = rama_south_x0 + (rama_land - rama_light_length)/2
rama_south_light_x1 = rama_south_light_x0 + rama_light_length
rama_south_light_y0 = -rama_light_width/2
rama_south_light_y1 = +rama_light_width/2

rama_south_light_X0 = rama_south_light_x0 - rama_light_slope
rama_south_light_X1 = rama_south_light_x1 + rama_light_slope
rama_south_light_Y0 = rama_south_light_y0 - rama_light_slope
rama_south_light_Y1 = rama_south_light_y1 + rama_light_slope

rama_south_light_zs = [.7, .4, .7]

# ====================================================================================================
# Utilities

def lerp(t, a, b):
    return a + t*(b - a)

def smooth_factor(t):
    return t * t * (3. - 2. * t)

def smooth_interp(t, a, b):
    return lerp(smooth_factor(t), a, b)


# ====================================================================================================
# Curvature
# - From plane to cylinder with a scale
#
# - x : any
# - y : from -rama_ymax to rama_ymax
# - z : any
#
# Let's note C = rama_ymax
#
# ----- Curvature only
#
# For an angle A in [0, pi], radius R is such as RA = C
# - R = C/A , A = 0 will be addressed later
#
# At distance y, we have the angle a:
# a = Ay/C
# 
# Point with altitude z will give radius r:
# - r = R - z
#
# Transformation is:
# x' = x
# y' = r.sin(a)
# z' = R - r.cos(a)
#
# For small values of A:
# y' = Ra - za = C/A.Ay/c -  za = y - za
# z' = R(1 - cos(a)) + z = z + 1/2.C/A.A2y2/C2 = z + 1/2y2A/C2
#
# ----- Centering on z=0
#
# z'' = z' - A/pi*RADIUS 

def to_cylinder(points, factor=0, scale=1):
    
    if factor == 0:
        return points*scale
    
    if len(np.shape(points)) == 1:
        return to_cylinder(np.expand_dims(points, axis=0), factor, scale)[0]

    x = points[..., 0]
    y = points[..., 1]
    z = points[..., 2]
    
    A = factor*np.pi
    a = (factor*np.pi/rama_ymax)*y

    cyl = np.array(points)
    
    if A < 0.001:
        
        cyl[..., 1] = y - a*z
        cyl[..., 2] = z + y*y*(A/C/C/2) - factor*rama_radius
                        
    else:
        
        R = rama_ymax/A
        r = R - z

        cyl[..., 1] = r*np.sin(a)
        cyl[..., 2] = R - r*np.cos(a) - factor*rama_radius
    
    return cyl*scale

# ----------------------------------------------------------------------------------------------------
# Return the angle

def get_angle(points, factor):
    
    if len(np.shape(points)) == 1:
        return get_angle(np.expand_dims(points, axis=0), factor)[0]
    
    return (factor*np.pi/rama_ymax)*points[..., 1]

# ----------------------------------------------------------------------------------------------------
# Get the normal

def get_normal(points, factor):
    
    if len(np.shape(points)) == 1:
        return get_normal(np.expand_dims(points, axis=0), factor)[0]
    
    vs = np.zeros(np.shape(points)[:-1] + (3,), float)
    
    a = get_angle(points, factor)
    vs[..., 1] = np.sina(a)
    vs[..., 2] = np.cos(a)
    
    return vs
    
    

# ====================================================================================================
# Surface continuity
#
# Ensure the continuity when closing the strip into a cylinder
#
# To make sure f(L) = f(-L), we compute f(L + y) and f(L - y) for y < W
# Then:
# - f( L - y) = smooth(f( L - y), f(-L - y), p)
# - f(-L + y) = smooth(f(-L + y), f( L + y), p)


def continuity(verts, func, overlap=2):
    
    i_lefts  = verts[..., 1] < -rama_ymax + overlap
    i_rights = verts[..., 1] >  rama_ymax - overlap
    
    # ----- Compute left stripe after right end
    
    lefts = np.array(verts[i_lefts])
    lefts[..., 2] = 0
    
    # Shift left to [ymax, ymax + overlap]
    lefts[..., 1] += rama_circ
    
    lefts[..., 2] = func(lefts)
    
    # ----- Compute right stripe befre left start
    
    rights = np.array(verts[i_rights])
    rights[..., 2] = 0
    
    # Shift rights to [-ymax-overlap, -ymax]
    rights[..., 1] -= rama_circ
    
    rights[..., 2] = func(rights)
    
    # ----- Smoothly combine the stripes
    
    # p:
    # - 0   at -ymax
    # - 0.5 at -ymax + overlap
    p = (lefts[..., 1] - rama_ymax)/(overlap*2)
    
    verts[i_lefts, 2] = smooth_interp(.5 + p, lefts[..., 2], verts[i_lefts, 2])
    
    # p:
    # - 0   at ymax - overlap
    # - 0.5 at ymax
    p = (-rama_ymax - rights[..., 1])/(overlap*2)
    
    verts[i_rights, 2] = smooth_interp(.5 - p, verts[i_rights, 2], rights[..., 2])

# ====================================================================================================
# Build a section from a function
#
# Ensure the continuity when closing the strip into a cylindre
#
# To make sure f(L) = f(-L), we compute f(L + y) and f(L - y) for y < W
# Then:
# - f( L - y) = smooth(f( L - y), f(-L - y), p)
# - f(-L + y) = smooth(f(-L + y), f( L + y), p)


def cylinder_section(verts, func, factor=1, scale=1, overlap=2):
    
    verts[..., 2] = func(verts)
    
    continuity(verts, func, overlap)
    
    return to_cylinder(verts, factor=factor, scale=scale)

# ====================================================================================================
# Carve (or elevate a rectangle)
# Used to buiild the light channels
#
# - X0, X1, Y0, Y1 : the external rectangle
# - x0, x1, y0, y1 : the internal rectangle
# - altitude       : the target altitude
#
# Some heavy code...


def carve_rectangle(xy, zs, X0, X1, Y0, Y1, x0, x1, y0, y1, altitude):
    
    # ----- Work in the external rectangle

    i_inside = np.arange(len(zs))[np.logical_and(
            np.logical_and(xy[..., 0] >= X0, xy[..., 0] <= X1),
            np.logical_and(xy[..., 1] >= Y0, xy[..., 1] <= Y1),
        )]
    
    xs = xy[i_inside, 0]
    ys = xy[i_inside, 1]
    z  = zs[i_inside]
    ref_z = np.array(z)
    
    # ----- Inner rectangle
    
    z[np.logical_and(
        np.logical_and(xs >= x0, xs <= x1),
        np.logical_and(ys >= y0, ys <= y1),
        )] = altitude
    
    # ---------------------------------------------------------------------------
    # Left x

    # ----- Slope x down from terrain to altitude
        
    selection = np.logical_and(
            np.logical_and(xs >= X0, xs <= x0),
            np.logical_and(ys >= y0, ys <= y1),
        )
    
    p = (xs[selection] - X0)/(x0 - X0)
    z[selection] = smooth_interp(p, ref_z[selection], altitude)
    
    # ----- Bottom half corner
    
    diag = X0 + (ys-Y0)*((x0-X0)/(y0-Y0))
    
    selection = np.logical_and(
            np.logical_and(xs >= X0, xs <= diag),
            np.logical_and(ys >= Y0, ys <= y0),
        )
    
    p = (xs[selection] - X0)/(x0 - X0)
    z[selection] = smooth_interp(p, ref_z[selection], altitude)
    
    # ----- Top half corner
    
    diag = X0 + (ys-Y1)*((x0-X0)/(y1-Y1))
    
    selection = np.logical_and(
            np.logical_and(xs >= X0, xs <= diag),
            np.logical_and(ys >= y1, ys <= Y1),
        )
    
    p = (xs[selection] - X0)/(x0 - X0)
    z[selection] = smooth_interp(p, ref_z[selection], altitude)
    
    
    # ---------------------------------------------------------------------------
    # Right x

    # ----- Slope x from altitude up to terrain
        
    selection = np.logical_and(
            np.logical_and(xs >= x1, xs <= X1),
            np.logical_and(ys >= y0, ys <= y1),
        )
    
    p = (xs[selection] - x1)/(X1 - x1)
    z[selection] = smooth_interp(p, altitude, ref_z[selection])
    
    # ----- Bottom half corner
    
    diag = x1 + (ys-y0)*((X1-x1)/(Y0-y0))
    
    selection = np.logical_and(
            np.logical_and(xs >= diag, xs <= X1),
            np.logical_and(ys >= Y0, ys <= y0),
        )
    
    p = (xs[selection] - x1)/(X1 - x1)
    z[selection] = smooth_interp(p, altitude, ref_z[selection])
    
    # ----- Top half corner
    
    diag = x1 + (ys-y1)*((X1-x1)/(Y1-y1))
    
    selection = np.logical_and(
            np.logical_and(xs >= diag, xs <= X1),
            np.logical_and(ys >= y1, ys <= Y1),
        )
    
    p = (xs[selection] - x1)/(X1 - x1)
    z[selection] = smooth_interp(p, altitude, ref_z[selection])
    
    # ---------------------------------------------------------------------------
    # Bottom y
    
    # ----- Slope y down from terrain to altitude
        
    selection = np.logical_and(
            np.logical_and(xs >= x0, xs <= x1),
            np.logical_and(ys >= Y0, ys <= y0),
        )
    
    p = (ys[selection] - Y0)/(y0 - Y0)
    z[selection] = smooth_interp(p, ref_z[selection], altitude)
    
    # ----- Left half corner
    
    diag = Y0 + (xs-X0)*((y0-Y0)/(x0-X0))
    
    selection = np.logical_and(
            np.logical_and(xs >= X0, xs <= x0),
            np.logical_and(ys >= Y0, ys <= diag),
        )
    
    p = (ys[selection] - Y0)/(y0 - Y0)
    z[selection] = smooth_interp(p, ref_z[selection], altitude)
    
    # ----- Right half corner
    
    diag = y0 + (xs-x1)*((Y0-y0)/(X1-x1))
    
    selection = np.logical_and(
            np.logical_and(xs >= x1, xs <= X1),
            np.logical_and(ys >= Y0, ys <= diag),
        )
    
    p = (ys[selection] - Y0)/(y0 - Y0)
    z[selection] = smooth_interp(p, ref_z[selection], altitude)
    
    # ---------------------------------------------------------------------------
    # Top y

    # ----- Slope y from altitude up to terrain
        
    selection = np.logical_and(
            np.logical_and(xs >= x0, xs <= x1),
            np.logical_and(ys >= y1, ys <= Y1),
        )
    
    p = (ys[selection] - y1)/(Y1 - y1)
    z[selection] = smooth_interp(p, altitude, ref_z[selection])
    
    # ----- Left half corner
    
    diag = Y1 + (xs-X0)*((y1-Y1)/(x0-X0))
    
    selection = np.logical_and(
            np.logical_and(xs >= X0, xs <= x0),
            np.logical_and(ys >= diag, ys < Y1),
        )
    
    p = (ys[selection] - y1)/(Y1 - y1)
    z[selection] = smooth_interp(p, altitude, ref_z[selection])
    
    # ----- Right half corner
    
    diag = y1 + (xs-x1)*((Y1-y1)/(X1-x1))
    
    selection = np.logical_and(
            np.logical_and(xs >= x1, xs <= X1),
            np.logical_and(ys >= diag, ys < Y1),
        )
    
    p = (ys[selection] - y1)/(Y1 - y1)
    z[selection] = smooth_interp(p, altitude, ref_z[selection])
    
    # ---------------------------------------------------------------------------
    # Result in z
    
    zs[i_inside] = z
    
# ====================================================================================================
# rama whole cylinder:

def rama_cylinder(x, y, factor=1, scale=1000):

    if not hasattr(x, '__len__'):
        return rama_cylinder([x], [y])[0]
    
    def rama(verts):
        
        x = verts[..., 0]
        z = np.zeros_like(x)
        
        # ----- North land: growing from 0 to north_altitude
        
        sel = x < north_x1
        z[sel] = lerp((x[sel]-north_x0)/north_length, 0, north_altitude)
        
        # ----- North cliff: down from north_altitude to 0

        sel = np.logical_and(x >= north_x1, x <= sea_x0)
        z[sel] = lerp((x[sel]-north_x1)/north_cliff_length, north_altitude, 0)
        
        # ----- South cliff: growing from 0 to south_altitude

        sel = np.logical_and(x >= sea_x1, x <= south_x0)
        z[sel] = lerp((x[sel]-sea_x1)/south_cliff_length, 0, south_altitude)

        # ----- North land: donw from south_altitude to 0
        
        sel = x >= south_x0
        z[sel] = lerp((x[sel]-south_x0)/south_length, south_altitude, 0)
        
        return z

    
    # ----------------------------------------------------------------------------------------------------
    # Main function
    
    vs = np.stack((x, y, np.zeros(len(x), float))).T

    return cylinder_section(vs, rama, factor=factor, scale=scale)


# ====================================================================================================
# The north land terrain function

def north_land(x, y, factor=1, scale=1000):

    if not hasattr(x, '__len__'):
        return north_land([x], [y])[0]
    
    def north_terrain(verts):
        
        # ----- Mountains locations
        
        perlin = Perlin(2, amp=1000, scale=1., contrast=1., rng=5)
        
        # ----- Altitudes
        
        frequence = 1/40
        amplitude = 18
        
        altitudes = (perlin.noise(verts[..., :2]*frequence) - .47)*amplitude
        if False:
            test = perlin.noise(verts[..., :2]*frequence)
            if len(test) > 0:
                print(f"verts: {np.shape(verts)} --> min={np.min(test):.2f}, max={np.max(test):.2f}, amplitude={(np.max(test) - np.min(test)):.2f}")
                
        # ----- Smooth to almost zero when reaching x limits
        
        margin = 3

        i = verts[..., 0] < rama_north_x0 + margin
        p = (verts[i, 0] - rama_north_x0)/margin
        altitudes[i] = smooth_interp(p, altitudes[i]*.01, altitudes[i])
        
        i = verts[..., 0] > rama_north_x1 - margin
        p = (verts[i, 0] - rama_north_x1 + margin)/margin
        altitudes[i] = smooth_interp(p, altitudes[i], .05 + altitudes[i]*.01)
        
        amps = np.array(altitudes)*1.5
        
        # ----- Octaves
        
        octaves   = 4
        frq_fac   = 2
        amp_fac   = .8
        for octave in range(octaves):
            frequence *= frq_fac
            amplitude *= amp_fac
            
            perlin = Perlin(2, amp=1000, scale=1., contrast=1., rng=octave+10)
            z = (perlin.noise(verts[..., :2]*frequence) - .3)*amps
            
            if octave == 0:
                zs = z
            else:
                zs += z
                
            amps *= amp_fac
            
        # ----- Northen riff
        # riff is a curve along y representing the riff border
        
        riff  = rama_north_x1 - (Perlin(1, amp=1000, scale=1., contrast=2., rng=100).noise(verts[..., 1]*10) - .2) *rama_north_riff_width
        slope = (Perlin(1, amp=1000, scale=1., contrast=2, rng=101).noise(verts[..., 1]*1) - .2) * rama_north_riff_slope
        
        p = np.clip((verts[..., 0] - riff)/slope, 0, 1)
        
        zs[:] = smooth_interp(p, zs, 0)
        
        # ----- Light chanels
        
        for y_light, z_light in zip(rama_light_ys, rama_north_light_zs):
            
            carve_rectangle(verts, zs,
                rama_north_light_X0, rama_north_light_X1, y_light + rama_north_light_Y0, y_light + rama_north_light_Y1,
                rama_north_light_x0, rama_north_light_x1, y_light + rama_north_light_y0, y_light + rama_north_light_y1,
                z_light)
            
        # ----- Return the zs
            
        return zs
    
    # ----------------------------------------------------------------------------------------------------
    # Main function
    
    vs = np.stack((x, y, np.zeros(len(x), float))).T

    return cylinder_section(vs, north_terrain, factor=factor, scale=scale)


# ====================================================================================================
# The south land terrain function

def south_land(x, y, factor=1, scale=1000):

    if not hasattr(x, '__len__'):
        return south_land([x], [y])[0]
    
    def south_terrain(verts):

        # ----- Mountains locations
        
        perlin = Perlin(2, amp=1000, scale=2., contrast=1., rng=51)
        
        # ----- Altitudes
        
        frequence = 1/20
        amplitude = 3
        
        # min=0.33, max=0.66, amplitude=0.33
        altitudes = (perlin.noise(verts[..., :2]*frequence) - .3)*amplitude
        
        if False:
            test = perlin.noise(verts[..., :2]*frequence)
            if len(test) > 0:
                print(f"verts: {np.shape(verts)} --> min={np.min(test):.2f}, max={np.max(test):.2f}, amplitude={(np.max(test) - np.min(test)):.2f}")
                
        # ----- Smooth to almost zero when reaching x limits
        
        margin = 3

        i = verts[..., 0] < rama_south_x0 + margin
        p = (verts[i, 0] - rama_south_x0)/margin
        altitudes[i] = smooth_interp(p, altitudes[i]*.01 + .5, altitudes[i])
        
        i = verts[..., 0] > rama_south_x1 - margin
        p = (verts[i, 0] - rama_south_x1 + margin)/margin
        altitudes[i] = smooth_interp(p, altitudes[i], altitudes[i]*.01)
        
        amps = np.array(altitudes)*1.5
        
        #return amps
        
        # ----- Octaves
        
        octaves   = 4
        frq_fac   = 2
        amp_fac   = .8
        for octave in range(octaves):
            frequence *= frq_fac
            amplitude *= amp_fac
            
            perlin = Perlin(2, amp=1000, scale=1., contrast=1., rng=octave+60)
            z = (perlin.noise(verts[..., :2]*frequence) - .3)*amps
            
            if octave == 0:
                zs = z
            else:
                zs += z
                
            amps *= amp_fac
            
        # ----- Southern riff
        # riff is a curve along y representing the riff border
        
        riff  = rama_south_x0 + (Perlin(1, amp=1000, scale=1., contrast=2., rng=100).noise(verts[..., 1]*1) - .2) *rama_south_riff_width
        slope = (Perlin(1, amp=1000, scale=1., contrast=2, rng=101).noise(verts[..., 1]*1) - .2) * rama_south_riff_slope
        
        p = np.clip((verts[..., 0] - riff)/slope, 0, 1)
        
        zs[:] = smooth_interp(p, 0, zs)
        
        # ----- Light chanels
        
        for y_light, z_light in zip(rama_light_ys, rama_south_light_zs):
            
            carve_rectangle(verts, zs,
                rama_south_light_X0, rama_south_light_X1, y_light + rama_south_light_Y0, y_light + rama_south_light_Y1,
                rama_south_light_x0, rama_south_light_x1, y_light + rama_south_light_y0, y_light + rama_south_light_y1,
                z_light)
        
        # ----- Return the zs
            
        return zs
    
    
    # ----------------------------------------------------------------------------------------------------
    # Main function
    
    vs = np.stack((x, y, np.zeros(len(x), float))).T

    return cylinder_section(vs, south_terrain, factor=factor, scale=scale)    

# ====================================================================================================
# The sea

def sea(x, y, factor=1, scale=1000):
    
    if not hasattr(x, '__len__'):
        return sea([x], [y])[0]
    
    
    func = lambda xy: 0.003
    
    vs = np.stack((x, y, np.zeros(len(x), float))).T

    return cylinder_section(vs, func, factor=factor, scale=scale)


# ====================================================================================================
# North hemisphere
#
# For hemispheres
# - x : hemi angle
# - y : circle angle

# ----------------------------------------------------------------------------------------------------
# The north hemisphere

def north_hemisphere(x, y, scale=1000):
    
    R = rama_radius*scale
    C = rama_north_hemi_center*scale
    
    r = R*np.sin(x)
    return np.stack((-R*np.cos(x), r*np.cos(-y), r*np.sin(-y))).T + C

# ----------------------------------------------------------------------------------------------------
# A plateforme

def north_platform_func(x, y, phi, width, scale=1000):
    
    R  = rama_radius*scale
    x0 = -R*np.sin(phi)
    r  = R*np.cos(phi)
    
    if hasattr(x, '__len__'):
        rs = np.array(x)
        rs[:] = r
        rs[x>.99] *= 1.05
        
    else:
        rs = r*1.05 if x > .99 else r
    
    return np.stack((x0+x*(width*scale), rs*np.cos(-y), rs*np.sin(-y))).T + rama_north_hemi_center*scale

def north_platform_grid(nx, ny, phi, width, scale=1000):

    func = lambda x, y: north_platform_func(x, y, phi=phi, width=width, scale=scale)
    
    cuts = {'axis': 'x', 'at': .98}
    
    return MultiResGrid(nx, ny, bounds = ((0, -np.pi), (1, np.pi)), func=func, cuts=cuts) 


# ====================================================================================================
# North hemisphere

# ----------------------------------------------------------------------------------------------------
# The south hemisphere

def south_hemisphere(x, y, scale=1000):
    
    R = rama_radius*scale
    C = rama_south_hemi_center*scale
        
    r = R*np.sin(x)
    return np.stack((R*np.cos(x), r*np.cos(-y)*rama_hemi_flatten, r*np.sin(-y))).T + C

# ----------------------------------------------------------------------------------------------------
# A cone
# - x : length % (0 to 1)
# - y : circle angle

def south_cone(x, y, O=(0, 0, 0), length=10, radius=3, scale=1):
    z = x*length*scale
    r = abs((1 - x)*radius*scale)
    C = np.array(O)*scale
    return np.stack((z, r*np.cos(y), r*np.sin(y))).T + C

def main_cone_grid(scale=1000):
    
    nx = 8
    ny = 16
    
    func = lambda x, y: south_cone(x, y,
                 O      =  rama_south_hemi_center + (rama_hemi_flatten*rama_radius, 0, 0),
                 length = -rama_cone_length,
                 radius =  rama_cone_radius,
                 scale  = scale)
    
    return MultiResGrid(nx, ny, bounds = ((0, -np.pi), (1, np.pi)), func=func)    
    
def small_cone_grid(index, scale=1000):
    
    nx = 8
    ny = 16
    
    ag     = np.pi*index/3
    r      = rama_radius/2
    
    func = lambda x, y: south_cone(x, y,
                 O      =  rama_south_hemi_center + (rama_cones_y0, r*np.cos(ag), r*np.sin(ag)),
                 length = -rama_cone_length*rama_cones_scale,
                 radius =  rama_cone_radius*rama_cones_scale,
                 scale  = scale)
    
    return MultiResGrid(nx, ny, bounds = ((0, -np.pi), (1, np.pi)), func=func)    



# ====================================================================================================
# Get rama cylinder

def get_cylinder(factor=1, scale=1000, select=None):
    
    if isinstance(select, str):
        select = {select}
    
    cylinder = {}
    
    # ----- Rama cylinder

    name = "Rama Cylinder"
    if select is None or name in select:

        nx = int(rama_land)*3
        ny = int(rama_circ)*3
        
        ncuts = 4

        cuts = [
            {'axis': 'x', 'at': north_x1 - .00, 'to': sea_x0 + .00, 'cuts': 15},
            {'axis': 'x', 'at': sea_x1   - .00, 'to': south_x0 + .00, 'cuts': 15},

            #{'axis': 'x', 'at': rama_north_light_X0, 'to': rama_north_light_x0, 'cuts': ncuts},
            #{'axis': 'x', 'at': rama_north_light_x1, 'to': rama_north_light_X1, 'cuts': ncuts},
            ]
        
        #cuts = None
        
        #for y_light in rama_light_ys:
        #    cuts.append({'axis': 'y', 'at': y_light + rama_north_light_Y0, 'to': y_light + rama_north_light_y0, 'cuts': ncuts})
        #    cuts.append({'axis': 'y', 'at': y_light + rama_north_light_y1, 'to': y_light + rama_north_light_Y1, 'cuts': ncuts})
    
        func = lambda x, y: rama_cylinder(x, y, factor=factor, scale=scale)
        cylinder[name] = MultiResGrid(nx, ny, bounds=((cyl_x0, -rama_ymax), (cyl_x1, rama_ymax)), func=func, cuts=cuts)
    
    
    # ----- North land

    name = "Rama Land North"
    if select is None or name in select:

        nx = int(rama_land)*3
        ny = int(rama_circ)*3
        
        ncuts = 4

        cuts = [
            {'axis': 'x', 'at': rama_north_x1-.2, 'to': rama_north_x1, 'cuts': 15},

            {'axis': 'x', 'at': rama_north_light_X0, 'to': rama_north_light_x0, 'cuts': ncuts},
            {'axis': 'x', 'at': rama_north_light_x1, 'to': rama_north_light_X1, 'cuts': ncuts},
            ]
        
        for y_light in rama_light_ys:
            cuts.append({'axis': 'y', 'at': y_light + rama_north_light_Y0, 'to': y_light + rama_north_light_y0, 'cuts': ncuts})
            cuts.append({'axis': 'y', 'at': y_light + rama_north_light_y1, 'to': y_light + rama_north_light_Y1, 'cuts': ncuts})
    
        func = lambda x, y: north_land(x, y, factor=factor, scale=scale)
        cylinder[name] = MultiResGrid(nx, ny, bounds=((-rama_land - rama_sea/2, -rama_ymax), (-rama_sea/2, rama_ymax)), func=func, cuts=cuts)

    # ----- south land

    name = "Rama Land South"
    if select is None or name in select:

        nx = int(rama_land)
        ny = int(rama_circ)
        
        ncuts = 4

        cuts = [
            {'axis': 'x', 'at': rama_south_x0, 'to': rama_south_x0 + .25, 'cuts': 20},

            {'axis': 'x', 'at': rama_south_light_X0, 'to': rama_south_light_x0, 'cuts': ncuts},
            {'axis': 'x', 'at': rama_south_light_x1, 'to': rama_south_light_X1, 'cuts': ncuts},
            ]
        
        for y_light in rama_light_ys:
            cuts.append({'axis': 'y', 'at': y_light + rama_south_light_Y0, 'to': y_light + rama_south_light_y0, 'cuts': ncuts})
            cuts.append({'axis': 'y', 'at': y_light + rama_south_light_y1, 'to': y_light + rama_south_light_Y1, 'cuts': ncuts})
        
    
        func = lambda x, y: south_land(x, y, factor=factor, scale=scale)
    
        cylinder[name] = MultiResGrid(nx, ny, bounds=((rama_sea/2, -rama_ymax), (rama_sea/2 + rama_land, rama_ymax)), func=func, cuts=cuts)

    # ----- sea

    name = "Rama Sea"
    if select is None or name in select:

        nx = int(rama_sea)
        ny = int(rama_circ)
    
        func = lambda x, y: sea(x, y, factor=factor, scale=scale)
    
        cylinder[name] = MultiResGrid(nx, ny, bounds=((rama_sea_x0, -rama_ymax), (rama_sea_x1, rama_ymax)), func=func)
    
    # ----- North Hemisphere

    name = "Rama North Hemi"
    if select is None or name in select:

        nx = 8
        ny = 16
    
        func = lambda x, y: north_hemisphere(x, y, scale=scale)
    
        cylinder[name] = MultiResGrid(nx, ny, bounds = ((-np.pi/2, -np.pi), (0, np.pi)), func=func)
        
    if True:
        for i, phi, width in zip(range(3), rama_platform_phis, rama_platform_phis):

            name = f"Rama Platform {i}"
            if select is None or name in select or "Rama Platform" in select:
                cylinder[name] = north_platform_grid(4, 360, phi=phi, width=width, scale=scale)

    # ----- South hemisphere
    
    name = "Rama South Hemi"
    if select is None or name in select:

        nx = 8
        ny = 16
    
        func = lambda x, y: south_hemisphere(x, y, scale=scale)
    
        cylinder[name] = MultiResGrid(nx, ny, bounds = ((0, -np.pi), (np.pi/2, np.pi)), func=func)
        
    # ----- South cones
    
    for i_cone in range(7):
        
        name = f"Rama Cone {i_cone}"
        
        if select is None or name in select:
            
            if i_cone == 0:
                
                cylinder[name] = main_cone_grid(scale)
                
            else:
                
                cylinder[name] = small_cone_grid(i_cone, scale)
        
        
    return cylinder

# ====================================================================================================
# Locate parts

def locate_parts(factor:0, scale=1):
    
    # ----------------------------------------------------------------------------------------------------
    # Light chanels
    
    for i, y_light, z_light in zip(range(3), rama_light_ys, rama_north_light_zs):
        
        loc = np.array((rama_north_x0 + rama_land/2, y_light, z_light))
        
        lch = bpy.data.objects[f"Light Chanel N{i}"]
        lch.location = to_cylinder(loc, factor=factor, scale=scale)
        lch.scale = (scale, scale, scale)
        lch.rotation_euler.x = get_angle(loc, factor)
        
    for i, y_light, z_light in zip(range(3), rama_light_ys, rama_south_light_zs):
        
        loc = np.array((rama_south_x0 + rama_land/2, y_light, z_light))
        
        lch = bpy.data.objects[f"Light Chanel S{i}"]
        lch.location = to_cylinder(loc, factor=factor, scale=scale)
        lch.scale = (scale, scale, scale)
        lch.rotation_euler.x = get_angle(loc, factor)
        
        
        




        
    


