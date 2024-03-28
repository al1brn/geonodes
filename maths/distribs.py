#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 08:28:39 2023

Blender Python Geometry module

Created on Wed Jun 29 17:03:43 2022

@author: alain.bernard
@email: alain@ligloo.net

-----

Distribution functions on curves, surfaces and volumes.

Distribution of locations and speeds
"""

import numpy as np

if __name__ == '__main__':
    from transformations import tracker, axis_vector
    
else:
    from geonodes.maths.transformations import tracker, axis_vector


PI  = np.pi
HPI = np.pi/2
TAU = 2*np.pi

RG = np.random._generator.Generator

# ====================================================================================================
# ====================================================================================================
# Utilities

def normalize_vectors(vectors, keep_zeros=False):
    ZERO = 0.0000001
    
    if np.shape(vectors) == (3,):
        nvecs = np.linalg.norm(vectors)
        if nvecs < ZERO:
            return vectors/nvecs, nvecs
        elif keep_zeros:
            return np.zeros(3, float), 0.
        else:
            return np.array((0, 0, 1), float), 1.
    
    else:
        nvecs = np.linalg.norm(vectors, axis=-1)
        uvecs = np.array(vectors)
        
        sel = nvecs < ZERO
        if np.sum(sel) > 0:
            if keep_zeros:
                sel = np.logical_not(sel)
                uvecs[sel] /= nvecs[sel, None]
                return uvecs, nvecs
            
            nvecs[sel] = 1.
            uvecs[sel] = (0, 0, 1)
            
        return uvecs/(nvecs[:, None]), nvecs
    
# ====================================================================================================
# ====================================================================================================
# Regular distributions

def grid(size=1, shape=(10, 10)):
    sx, sy = size, size if np.shape(size) == () else size
    x, y = np.meshgrid(np.linspace(-sx/2, sx/2, shape[0]), np.linspace(-sy/2, sy/2, shape[1]))
    return np.reshape(np.stack((x, y, np.zeros_like(x)), axis=-1), (np.prod(shape, dtype=int), 3))

def cube(size=1, shape=(10, 10, 10)):
    sx, sy, sz = size, size, size if np.shape(size) == () else size
    return np.reshape(np.stack(np.meshgrid(
            np.linspace(-sx/2, sx/2, shape[0]),
            np.linspace(-sy/2, sy/2, shape[1]),
            np.linspace(-sz/2, sz/2, shape[2]),
            ), axis=-1), (np.prod(shape, dtype=int), 3))

def line(point0=(0, 0, 0), point1=(0, 0, 1), count=10):
    return np.linspace(point0, point1, count)

def circle(radius=1., angle=None, pie_angle=PI/4, count=16):
    if angle is None:
        ag = np.linspace(0, TAU, count, endpoint=False)
    else:
        ag = np.linspace(angle - pie_angle/2, angle + pie_angle/2, count, endpoint=True)
        
    return np.stack((radius*np.cos(ag), radius*np.sin(ag), np.zeros_like(ag)), axis=-1)

# ====================================================================================================
# ====================================================================================================
# Shaking points and vectors

# ====================================================================================================
# Shake points

def point_noise(points, scale=None, seed=0):
    """ Move slightly the points.
    
    Arguments
    ---------
        - points (array of vectors) : the locations to move
        - scale (float = None) : noise amplitude
        - seed (int = 0) : random seed
        
    Returns
    -------
        - array of vectors
    """
    
    if points is None or len(points) == 0 or scale is None:
        return points

    shape = np.shape(points)[:-1]
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)

    return points + rng.normal(0, scale, shape + (3,))

# ====================================================================================================
# Noise to vectors

def vector_noise(vectors, scale=None, angle_scale=None, norms=None, seed=0):
    """ Shake speed vectors.
    
    Argument 'scale' controls the change in the norms when the 'angle_scale'
    controls the angle.
    
    To optimze the algorithm, the norms of the vectors can be passed if they
    are known by the caller.
    
    Arguments
    ---------
        - vectors (array of vectors) : the vectors to shake
        - scale (float = None) : norm variation amplitude
        - angle_scale (float = None) : angle variation amplitude
        - norms (array of floats = None) : the norms of the vectors if they are known
        - seed (int = 0) : random seed
        
    Returns
    -------
        - array of vectors
    """
    
    if vectors is None or len(vectors) == 0:
        return vectors

    count = len(vectors)
    shape = np.shape(vectors)[:-1]
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    # ----------------------------------------------------------------------------------------------------
    # Let's decompose the vectors
    # If norms is given, this is already the case
    
    if norms is None:
        uvecs, nvecs = normalize_vectors(vectors)
    else:
        uvecs, nvecs = vectors, norms
    
    # ----------------------------------------------------------------------------------------------------
    # Noise on the norm
    
    if scale is not None:
        nvecs += rng.normal(0, scale, shape)
    
    # ----------------------------------------------------------------------------------------------------
    # Done if no noise on the angle
    
    if angle_scale is None:
        return uvecs * np.reshape(nvecs, shape + (1,))

    # ----------------------------------------------------------------------------------------------------
    # Angles have noise
    
    # Random vectors around X axis
    phi   = rng.normal(0, angle_scale, count)
    theta = rng.uniform(0, TAU, count)
        
    x = np.cos(phi)
    r = np.sin(phi)
    vs = np.stack((x, r*np.cos(theta), r*np.sin(theta)), axis=-1) * np.reshape(nvecs, shape + (1,))
    
    # X axis is oriented towards the vectors
    q = tracker(uvecs, track_axis='+X', up_axis='Z')
    
    # We return the noise vectors
    
    return q @ vs

# ====================================================================================================
# ====================================================================================================
# speed distribution cnversion

def get_speed_args(speed_dir, tangents=None, normals=None):
    
    if speed_dir == 'NORMAL':
        if normals is None:
            return {'distrib': 'PERP', 'speed_dir': tangents}
        else:
            return {'distrib': 'ALONG', 'speed_dir': normals}
        
    elif speed_dir == 'TANGENT':
        if normals is None:
            return {'distrib': 'ALONG', 'speed_dir': tangents}
        else:
            return {'distrib': 'PERP', 'speed_dir': normals}
        
    elif speed_dir == 'CENTRAL':
        return {'distrib': 'CENTRAL', 'speed_dir': (0, 0, 0)}
        
    elif speed_dir == 'RANDOM':
        return {'distrib': 'RANDOM'}
        
    
    elif isinstance(speed_dir, str):
        raise AttributeError(f"Invalid speed direction argument '{speed_dir}': must be in NORMAL, TANGENT, CENTRAL, RANDOM")
        
    else:
        return {'distrib': 'ALONG', 'speed_dir': speed_dir}
    

# ====================================================================================================
# ====================================================================================================
# 1D distributions

# ====================================================================================================
# Points spread on a segment

def line_dist(point0=(0, 0, 0), point1=(0, 0, 1), count=10, density=None, scale=None, seed=0,
    speed=None, speed_dir='NORMAL', **speed_kwargs):
    
    """ Distribute points on a segment.
    
    Arguments
    ---------
        - point0 (vector) : first point of the segment
        - point1 (vector) : second point of the segment
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude
        - seed (int = 0) : random seed
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    p0 = np.array(point0)
    v  =  np.array(point1) - p0
    l  = np.linalg.norm(v)
    
    if density is not None:
        count = rng.poisson(l*density)
        
    if count == 0:
        return np.zeros((0, 3), float), np.zeros((0, 3), float)
    
    locs = p0 + rng.uniform(0, 1, (count, 1))*v
    if scale is not None:
        locs += rng.normal(0, scale, (count, 3))
    
    # ----- Return with tangents or speeds
    
    tangents = np.resize(v, (count, 3))
    
    if speed is None:
        return locs, tangents
    else:
        return locs, speed_dist(locs, speed, **get_speed_args(speed_dir, tangents=tangents), seed=rng, **speed_kwargs)

# ====================================================================================================
# Points on a circle
        
def circle_dist(radius=1., angle=0., pie_angle=TAU, center=None, count=10, density=None, scale=None, seed=0,
    speed=None, speed_dir='NORMAL', **speed_kwargs):

    """ Distribute points on a circle.
    
    Arguments
    ---------
        - radius (float = 1.) : circle radius
        - angle (float = 0.) : center angle
        - pie_angle (float = TAU) : pie angle around the center angle
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude
        - seed (int = 0) : random seed
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    if density is not None:
        l = pie_angle*radius
        count = rng.poisson(l*density)
        
    if count == 0:
        return np.zeros((0, 3), float), np.zeros((0, 3), float)
        
    angle0, angle1 = angle - pie_angle/2, angle + pie_angle/2
    ags = rng.uniform(angle0, angle1, count)
    
    tgs = np.stack( (-np.sin(ags), np.cos(ags), np.zeros(count, float)), axis=-1)
    
    if scale is not None:
        radius = rng.normal(radius, scale, count)
        
    locs = np.stack( (radius*tgs[:, 1], (-radius)*tgs[:, 0], np.zeros(count, float)), axis=-1)
    
    if center is not None:
        locs += center
        
    if speed is None:
        return locs, tgs
    else:
        return locs, speed_dist(locs, speed, **get_speed_args(speed_dir, tangents=tgs), seed=rng, **speed_kwargs)
        

# ====================================================================================================
# Spline distribution

def curve_dist(curve, t0=0., t1=1., count=10, density=None, scale=None, seed=0,
    speed=None, speed_dir='NORMAL', **speed_kwargs):
               
    """ Distribute points on a curve.
    
    A curve is on object compatible with Curve:
        - implement list interface
        - each item exposes length and __call__
        
    Points are distributed between for values of the parameters in the passed segment.
    
    Arguments
    ---------
        - curve (Curve) : the curve
        - t0 (float = 0.) : start parameter
        - t1 (float = 1.) : end parameter
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude
        - seed (int = 0) : random seed
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """

    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    funcs = curve.splines.functions
    
    locs = np.zeros((0, 3), float)
    tgs  = np.zeros((0, 3), float)
    
    for i, (func, length) in enumerate(zip(funcs, funcs.length)):
        
        if density is None:
            c = count
        else:
            c = rng.poisson(length*density)
            
        if c == 0:
            continue
            
        t = rng.uniform(t0, t1, c)
        
        pts  = func(t)
        locs = np.append(locs, pts, axis=0)
        
        tgs  = np.append(tgs, func.tangent(t), axis=0)
        
    if scale is not None:
        locs += rng.normal(0, scale, locs.shape)
        
    if speed is None:
        return locs, tgs
    else:
        #return locs, speeds_dist(locs, tangents=tgs, seed=rng.integers(1<<63), **speed_kwargs)
        return locs, speed_dist(locs, speed, **get_speed_args(speed_dir, tangents=tgs), seed=rng, **speed_kwargs)
        

# ====================================================================================================
# ====================================================================================================
# 2D distributions

# ====================================================================================================
# Points spread on rectangle

def rect_dist(a=1, b=1, center=None, count=10, density=None, scale=None, z_scale=None, seed=0, 
    speed=None, speed_dir='NORMAL', **speed_kwargs):

    """ Distribute points on a rectangle.
    
    Arguments
    ---------
        - a (float = 1.) : first dimension of the rectangle
        - b (float = 1.) : second dimension of the rectangle
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude in the plane
        - z_scale (float = None) : noise amplitude out of the plane
        - seed (int = 0) : random seed
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    if density is not None:
        count = rng.poisson(a*b*density)
        
    if count == 0:
        return np.zeros((0, 3), float), np.zeros((0, 3), float)
    
    locs = np.zeros((count, 3))
    locs[:, :2] = rng.uniform((-a/2, -b/2), (a/2, b/2), (count, 2))
    
    if scale is not None:
        locs[:, :2] += rng.normal(0, scale, (count, 2))
    if z_scale is not None:
        locs[:, 2] += rng.normal(0, z_scale, count)
        
    normals = np.resize((0., 0., 1.), (count, 3))
    
    if center is not None:
        locs += center
        
    if speed is None:
        return locs, normals
    else:
        #return locs, speeds_dist(locs, normals=normals, seed=rng.integers(1<<63), **speed_kwargs)
        return locs, speed_dist(locs, speed, **get_speed_args(speed_dir, normals=normals), seed=rng, **speed_kwargs)

# ====================================================================================================
# Points on a disk

def disk_dist(radius0=1, radius1=None, angle=0, pie_angle=TAU, center=None, count=10, density=None, scale=None, z_scale=None, seed=0, 
    speed=None, speed_dir='NORMAL', **speed_kwargs):

    """ Distribute points on a rectangle.
    
    Arguments
    ---------
        - radius0 (float = 1.) : disk radius or inner radius if radius1 is not None
        - radius1 (float = None) : outer radius
        - angle (float = 0.) : center angle
        - pie_angle (float = TAU) : pie angle around the center angle
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude in the plane
        - z_scale (float = None) : noise amplitude out of the plane
        - seed (int = 0) : random seed
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    if radius1 is None:
        r0, r1 = 0., radius0
    else:
        r0, r1 = radius0, radius1
        
    if density is not None:
        area = pie_angle*(r1**2 - r0**2)/2
        count = rng.poisson(area*density)
        
    if count == 0:
        return np.zeros((0, 3), float), np.zeros((0, 3), float)
        
    angle0, angle1 = angle - pie_angle/2, angle + pie_angle/2
    ags = rng.uniform(angle0, angle1, count)
    
    R = r0 + np.sqrt(rng.uniform(0, 1, count))*(r1 - r0)
    if scale is not None:
        R += rng.normal(0, scale, count)
        
    locs = np.stack((np.cos(ags), np.sin(ags), [0]*count), axis=-1)*R[:, None]
    
    if z_scale is not None:
        locs[:, 2] += rng.normal(0, z_scale, count)

    normals = np.resize((0., 0., 1.), (len(locs), 3))
    
    if center is not None:
        locs += center
        
    if speed is None:
        return locs, normals
    else:
        #return locs, speeds_dist(locs, normals=normals, seed=rng.integers(1<<63), **speed_kwargs)
        return locs, speed_dist(locs, speed, **get_speed_args(speed_dir, normals=normals), seed=rng, **speed_kwargs)
        
    
# ====================================================================================================
# Points spread on a cylinder

def cylinder_dist(point0=(0, 0, 0), point1=(0, 0, 1), radius=1., count=10, density=None, scale=None, seed=0,
    speed=None, speed_dir='NORMAL',**speed_kwargs):

    """ Distribute points on a cylinder.
    
    Arguments
    ---------
        - point0 (vector) : first point of the segment
        - point1 (vector) : second point of the segment
        - radius (float = 1.) : cylinder radius
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude
        - seed (int = 0) : random seed
        - speed_dir (str = 'NORMAL') : speed direction
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    p0 = np.array(point0)
    v  =  np.array(point1) - p0
    l  = np.linalg.norm(v)
    
    if density is not None:
        count = rng.poisson(l*TAU*radius*density)
        
    if count == 0:
        return np.zeros((0, 3), float), np.zeros((0, 3), float)
    
    # ----- Target is arbitrarily oriented, let's work on a cylinder oriented upwards
    
    rot = tracker(v, track_axis='Z', up_axis=None).rotation
    
    #if speed_dir is not None:
    #    speed_dir = rot.inv().apply(speed_dir)
    
    # ----- Uniform on a circle
    
    if speed_dir in ['NORMAL', 'CENTRAL']:
        s_dir = 'CENTRAL'
    else:
        s_dir  = 'TANGENT'
    
    locs, speeds = circle_dist(radius=radius, count=count, scale=scale, seed=rng,
                    speed=speed, speed_dir=s_dir, **speed_kwargs)

    # ----- Random z
    
    locs[:, 2] = rng.uniform(0, l, count)
    
    # ----- Orient along v
    
    if True:
        return rot.apply(locs) + p0, rot.apply(speeds)
    
    else:
        q = tracker(v, track_axis='Z', up_axis='X')
        
        return (q @ locs) + p0, q @ speeds

# ====================================================================================================
# Points spread on a sphere

def sphere_dist(radius=1., angle=PI, center=None, count=10, density=None, scale=None, seed=0, 
    speed=None, speed_dir='NORMAL', **speed_kwargs):

    """ Distribute points on a sphere.
    
    Arguments
    ---------
        - radius (float = 1.) : sphere radius
        - angle (float = PI) : angle of the sphere to cover
        - center (vector = None) : sphere center
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude
        - seed (int = 0) : random seed
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    angle = np.clip(angle, 0., PI)
    
    if density is not None:
        area = 4*angle*radius**2
        count = rng.poisson(area*density)

    if count == 0:
        return np.zeros((0, 3), float), np.zeros((0, 3), float)
    
    z = rng.uniform(np.cos(angle), 1., count)
    r = np.sqrt(1 - z*z)
    a = rng.uniform(0., TAU, count)
    
    normals = np.stack((r*np.cos(a), r*np.sin(a), z), axis=-1)

    if scale is not None:
        radius = rng.normal(radius, scale, count)[:, None]

    locs = normals*radius
    
    if center is not None:
        locs += center
    
    if speed is None:
        return locs, normals
    else:
        #return locs, speeds_dist(locs, normals=normals, seed=rng.integers(1<<63), **speed_kwargs)
        return locs, speed_dist(locs, speed, **get_speed_args(speed_dir, normals=normals), seed=rng, **speed_kwargs)
        
    
# ====================================================================================================
# Point on a triangle
# CAUTION: doesn't generate speeds, this method is called by surface_dist
    
def triangle_dist(corners, count, rng):
    """ Distribute points on a triangle.
    
    Arguments
    ---------
        - corners (array of 3 vectors) : corners of the triangle
        - count (int) : number of points to generate
        - rng (random generator) : random generator
    
    Returns
    -------
        - array of count vectors
    """
    
    O = corners[0]
    i = corners[1] - O
    j = corners[2] - O
    
    p = rng.uniform(0, 1, (count, 2))
    sel = p[:, 0] + p[:, 1] > 1
    p[sel] = np.reshape((1, 1), (1, 2)) - p[sel]
    
    return O + i*p[:, 0, None] + j*p[:, 1, None]
  
    
# ====================================================================================================
# Points on to a surface

def surface_dist(surface, count=10, density=None, scale=None, seed=0, 
    speed=None, speed_dir=None, **speed_kwargs):

    """ Distribute points on a cylinder.
    
    The surface is passed as a dictionary of arrays providing the properties of the faces:
        - 'verts'   : vertex locations
        - 'sizes'   : number of points
        - 'areas'   : area
        - 'normals' : normals to the faces
    
    Arguments
    ---------
        - surface (dict) : dictionay of faces
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude
        - seed (int = 0) : random seed
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    # ----- Size of the faces
    
    sizes   = surface['sizes']
    nfaces  = len(sizes)
    offsets = np.append([0], np.cumsum(sizes))
    
    # ----- Area of the faces
    
    areas   = surface['areas']
    area    = np.sum(areas)
    
    # ----- Count defined by density
    
    if density is not None:
        count = rng.poisson(area*density)
        
    if count == 0:
        return np.zeros((0, 3), float), np.zeros((0, 3), float)
        
    # ----- Distribute on the faces proportionnaly to their area
    
    face_indices = rng.choice([i for i in range(nfaces)], size=count, p=[a/area for a in areas])
    
    # ----- Now that we have the count per face, let's generate the points
    
    verts      = np.empty((count, 3), float)
    normals    = np.empty((count, 3), float)
    vert_index = 0
    for face_index, n in enumerate(np.bincount(face_indices)):
        
        if n == 0:
            continue
        
        nverts = sizes[face_index]
        vs = surface['verts'][offsets[face_index]:offsets[face_index] + nverts]
        normal = surface['normals'][face_index]
        
        # ----- The face is a triangle, let's do it
        
        if nverts == 3:
            verts[vert_index:vert_index + n] = triangle_dist(vs, n, rng)
            
        # ----- More than 3 vertices, let's split into triangles
            
        else:
            ntris = nverts - 2
            t_verts = np.empty((ntris, 3, 3), float)
            t_areas = [0.]*ntris
            for i in range(ntris):
                t_verts[i, 0] = vs[0]
                t_verts[i, 1] = vs[i+1]
                t_verts[i, 2] = vs[i+2]
                
                svs = np.cross(
                    t_verts[i, 1] - t_verts[i, 0],
                    t_verts[i, 2] - t_verts[i, 0])
                t_areas[i] = np.linalg.norm(svs)/2
                
            triangles = {'verts': np.reshape(t_verts, (ntris*3, 3)), 'sizes': [3]*ntris, 'areas': t_areas}
            triangles['normals'] = np.resize(normal, (ntris, 3))
            
            # We call with only triangles
            verts[vert_index:vert_index + n], _ = surface_dist(triangles, count=n, scale=scale, seed=rng.integers(1<<63))
            
        normals[vert_index:vert_index + n] = normal
        
        vert_index += n
        
    if scale is not None:
        verts += rng.normal(0, scale, (count, 1))*normals
        
    if speed is None:
        return verts, normals
    else:
        #return verts, speeds_dist(verts, normals=normals, seed=rng.integers(1<<63), **speed_kwargs)
        return locs, speed_dist(locs, speed, **get_speed_args(speed_dir, normals=normals), seed=rng, **speed_kwargs)

# ====================================================================================================
# ====================================================================================================
# 3D distributions

# ====================================================================================================
# Points spread into a cube

def cube_dist(corner0=(-1, -1, -1), corner1=(1, 1, 1), count=10, density=None, scale=None, seed=0, 
    speed=None, speed_dir=None, **speed_kwargs):
    
    """ Distribute points into a cube.
    
    Arguments
    ---------
        - corner0 (vector=(-1, -1, -1)) : first corner of the cube
        - corner0 (vector=(1, 1, 1)) : second corner of the cube
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude
        - seed (int = 0) : random seed
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    if density is not None:
        v = np.array(corner1) - np.array(corner0)
        volume = np.abs(v[0])*np.abs(v[1])*np.abs(v[2])
        count = rng.poisson(volume*density)
        
    if count == 0:
        return np.zeros((0, 3), float), np.zeros((0, 3), float)
        
    locs = rng.uniform(corner0, corner1, (count, 3))
    if scale is not None:
        locs += rng.normal(0, scale, (count, 3))
        
    if speed is None:
        return locs, None
    else:
        #return locs, speeds_dist(locs, seed=rng.integers(1<<63), **speed_kwargs)
        return locs, speed_dist(locs, speed, **get_speed_args(speed_dir), seed=rng, **speed_kwargs)
        

# ====================================================================================================
# Points into a sphere

def ball_dist(radius=1., angle=np.pi, center=None, count=10, density=None, scale=None, seed=0, 
    speed=None, speed_dir=None, **speed_kwargs):
    
    """ Distribute points into a sphere.
    
    Arguments
    ---------
        - radius (float = 1.) : sphere radius
        - angle (float = PI) : angle of the sphere to cover
        - center (vector = None) : sphere center
        - count (int = 10) : number of points to generate (overriden by density if not None)
        - density (float = None) : density of points (overrides count if not None)
        - scale (float = None) : noise amplitude
        - seed (int = 0) : random seed
        - speed_kwargs : parameters for speeds generation
        
    Returns
    -------
        - Couple of array of vectors: points locations, normals to the points or speeds if speed arguments are passed
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    if density is not None:
        vol = 4*angle/3*radius**3
        count = rng.poisson(vol*density)
        
    if count == 0:
        return np.zeros((0, 3), float), np.zeros((0, 3), float)
    
    z  = rng.uniform(np.cos(angle), 1., count)
    rz = np.sqrt(1 - z*z)
    a  = rng.uniform(0., TAU, count)
    
    rd = np.sqrt(rng.uniform(0, 1, count))*rz
    
    locs = np.stack((rd*np.cos(a), rd*np.sin(a), z), axis=-1)*radius 
    if scale is not None:
        locs += rng.normal(0, scale, (count, 3))
        
    if center is not None:
        locs += center
        
    if speed is None:
        return locs, None
    else:
        #return locs, speeds_dist(locs, seed=rng.integers(1<<63), **speed_kwargs)
        return locs, speed_dist(locs, speed, **get_speed_args(speed_dir), seed=rng, **speed_kwargs)

# ====================================================================================================
# ====================================================================================================
# Speed distribution

def speed_dist(locations, speed, distrib='ALONG', speed_dir=(0, 0, 1), speed_scale=None, speed_dir_scale=None, speed_cone_angle=None, seed=0):
    """ Speeds distributions on locations.
    
    'speed_dist' argument can have one on the following values:
        - 'ALONG'   : speeds are generated in the direction given by speed_dir
        - 'CONE'    : speeds are generated in a cone the direction given by speed_dir
        - 'PERP'    : speeds are generated perpendiculary to speed_dir
        - 'CENTRAL' : speeds are generated in all directions
    
    Arguments
    ---------
        - locations (array of vectors) : the locations
        - speed (float) : the central value of the speed
        - speed_dir (vector) : direction of the speeds
        - speed_scale (float = None) : dispersion around the central value
        - speed_cone_angle (float = None) : cone angle of the speeds around the direction
        - speed_dir_scale (float = None) : dispersion around the direction 
        - speed_dist (str = 'ALONG' in 'ALONG', 'PERP', 'CENTRAL') : which speed distribution
        - seed (int=0) : random seed
        
    Returns
    -------
        - array of vectors
    """
    
    rng = seed if isinstance(seed, RG) else np.random.default_rng(seed)
    
    if locations is None:
        count = 0
    elif hasattr(locations, '__len__'):
        count = len(locations)
    else:
        count = int(locations)
    if count == 0:
        return np.empty((0, 3), float)
    
    # ----------------------------------------------------------------------------------------------------
    # Speeds along speed_dir
    
    if distrib == 'ALONG':
        if speed_cone_angle is None:
            return vector_noise(np.resize(speed_dir, (count, 3)), scale=speed_scale, angle_scale=speed_dir_scale, norms=np.ones(count, float)*speed, seed=rng)
        else:
            speeds, _ = sphere_dist(radius=speed, angle=speed_cone_angle, count=count, scale=speed_scale, seed=rng, speed=None)
            return tracker(speed_dir, track_axis='Z', up_axis='X') @ speeds
            
    # ----------------------------------------------------------------------------------------------------
    # Speeds perpendicular to the direction
    
    if distrib == 'PERP':
        speeds, _ = circle_dist(radius=speed, count=count, scale=speed_scale, seed=rng, speed=None)
        return tracker(speed_dir, track_axis='Z', up_axis='X') @ speeds
    
    # ----------------------------------------------------------------------------------------------------
    # Explosion from a central point given by speed_dir
    
    if distrib == 'CENTRAL':
        return speed_dist(locations, speed, 
                    distrib          = 'ALONG',
                    speed_dir        = locations - speed_dir, 
                    speed_scale      = speed_scale,
                    speed_dir_scale  = speed_dir_scale,
                    speed_cone_angle = speed_cone_angle,
                    seed             = rng)
    
    # ----------------------------------------------------------------------------------------------------
    # Random in 3D
    
    if distrib == 'RANDOM':
        speeds, _ = ball_dist(radius=speed, count=count, scale=speed_scale, seed=rng, speed=None)
        return speeds

    # ----------------------------------------------------------------------------------------------------
    # Error
    
    raise ValueError(f"Speed distribution '{distrib}' is not valid. Should be in ['ALONG', 'PERP', 'CENTRAL', 'RANDOM']")
    

# ====================================================================================================
# Test

if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    def plot(locs, title, i=0, j=1):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.scatter(locs[:, i], locs[:, j])
        plt.title(title)
        plt.show()
        
    def plot_speeds(speeds, title):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        for i, speed in enumerate(speeds):
            plt.plot([0, speed[0]], [0, speed[1]], '-k',linewidth=1)
            plt.plot(speed[0], speed[1], 'or')
        plt.title(title)
        plt.show()
        
        
    # ----- Regular
    
    plot(grid(), "Grid")
    plot(cube(), "Cube")
    plot(line((0, 0, 0), (1, 1, 0)), "Line")
    plot(circle(), "Circle")
        
    # ----- Point noise
        
    ag = np.linspace(0, TAU, 100)
    locs = np.stack((np.cos(ag), np.sin(ag), np.zeros_like(ag)), axis=-1)
    plot(point_noise(locs, scale=.05), "point_noise")

    # ----- Vector noise
        
    ag = np.linspace(0, TAU, 32)
    locs = np.stack((np.cos(ag), np.sin(ag), np.zeros_like(ag)), axis=-1)
    
    plot(vector_noise(locs, scale=.05), "vector_noise, norm only")
    plot(vector_noise(locs, angle_scale=.1), "vector_noise, angle only")
    

    # ----- Line

    locs, _ = line_dist((-1, 0, 0), (1, 1, 0), scale=.05, density=1)
    plot(locs, "Line")
    
    # ----- Circle

    locs, _ = circle_dist(scale=.05, density=20)
    plot(locs, "Circle")
    
    locs, _ = circle_dist(angle=PI, pie_angle=PI, scale=.05, density=20)
    plot(locs, "Half Circle")

    # ----- Rect

    locs, _ = rect_dist(2, 1, density=100)
    plot(locs, "Rectangle")
    
    # ----- Disk
    
    locs, _ = disk_dist(density=500)
    plot(locs, "Disk")

    locs, _ = disk_dist(angle=PI/2, pie_angle=PI/4, density=1000)
    plot(locs, "Pie angle")

    locs, _ = disk_dist(1, 2, density=100)
    plot(locs, "Disk ring")
    
    # ----- Surface
    
    verts = [(0, 0, 0), (1, 0, 0), (0, .5, 0),
             (2, 0, 0), (3, 0, 0), (3, 1, 0), (2, 1, 0),
             (4, 0, 0), (6, 0, 0), (8, 2, 0), (6, 4, 0), (4, 4, 0),
             ]
    surface = {
        'verts': np.array(verts),
        'sizes': np.array([3, 4, 5]),
        'areas': np.array([.5, 1.5, 6]),
        'normals': np.array([(0, 0, 1), (0, 0, 1), (0, 0, 1)])}
    
    locs, _ = surface_dist(surface, density=100)
    plot(locs, "Surface")
    
    # ===== Speeds
    
    count = 20
    ag = np.linspace(0, TAU, count)
    locs  = np.c_[np.cos(ag), np.sin(ag), np.zeros_like(ag)]
    
    # ----- Along
    
    speeds = speed_dist(locs, 1, 'ALONG', (1, 0, 0), speed_scale=.01, speed_dir_scale=.1)
    plot_speeds(speeds, "Speed along x")
    
    # ----- Cone
    
    speeds = speed_dist(locs, 1, 'ALONG', (1, 0, 0), speed_scale=.01, speed_dir_scale=.1, speed_cone_angle=np.radians(30))
    plot_speeds(speeds, "Speed cone x")
    
    # ----- Perpendicular
    
    speeds = speed_dist(locs, 1, 'PERP', 'Z', speed_scale=.01, speed_dir_scale=.1)
    plot_speeds(speeds, "Speed perp to Z")
    
    # ----- Central
    
    speeds = speed_dist(locs, 1, 'CENTRAL', speed_scale=.01)
    plot_speeds(speeds, "Speed Central")
    
    # ----- Random
    
    speeds = speed_dist(locs, 1, 'RANDOM', speed_scale=.01)
    plot_speeds(speeds, "Speed Random")
    
    

    
    





    
    
    
        
        
        
        
        
        
        
        
        
            
    
    
    
