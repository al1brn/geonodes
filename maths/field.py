#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 09:50:24 2024

@author: alain
"""

import numpy as np

# =============================================================================================================================
# Local base

def local_base(vectors):
    e0 = vectors/np.linalg.norm(vectors, axis=-1)[..., None]
    e1 = np.cross(e0, (0, 0, 1))
    ne1 = np.linalg.norm(e1, axis=-1)
    msk = ne1 < 0.01
    e1[msk] = np.cross(e0[msk], (1, 0, 0))
    e1 /= np.linalg.norm(e1, axis=-1)[..., None]
    return e0, e1, np.cross(e0, e1)

# =============================================================================================================================
# Simple fields

def constant_field(points, vector=(1, 0, 0)):
    return np.resize(vector, np.shape(points))*1.

def radial_field(points, power=1, factor=1.):
    points = np.array(points, float)
    if power == 0:
        return points
    else:
        norm = np.linalg.norm(points, axis=-1)
        norm[norm < 0.0001] = 1.
        return (points*(factor/norm**power)[..., None])

# =============================================================================================================================
# Electric field

def electric_field(points, locations=(0, 0, 0), charges=1., epsilon0=1.):
    """ Compute the electric field produced by charges at locations.

    Arguments
    ---------
    - points (array of vectors) : points where to compute the field
    - locations (array of vectors = (0., 0., 0.)) : locations of the electric charges
    - charges (array of floats = 1.) : electric charges
    - epsilon0 (float = 1.) : epsilon0 constant

    Returns
    -------
    - array of vectors, array of floats or vector, float
    """

    K = 1/4/np.pi/epsilon0

    # ====================================================================================================
    # Single point algorithm

    if np.shape(points) == (3,):

        # ----- Single charge

        if np.shape(locations) == (3,):
            v = np.array(points) - np.array(locations)
            n = max(np.linalg.norm(v), 1e-4)
            return v*(K*charges/n**3), charges/n**2

        # ----- Multiple charges

        v = points - np.array(locations, float)
        n = np.linalg.norm(v, axis=-1)
        v /= n[:, None]**3

        if np.shape(charges) == (1,):
            v *= charges
            charges = np.resize(charges, len(locations))
        elif isinstance(charges, np.ndarray):
            v *= charges[:, None]
        else:
            v *= np.array(charges)[:, None]

        E = np.sum(v, axis=0)

        E_pos = np.sum(v[charges > 0], axis=0)
        return E*K, np.linalg.norm(E_pos) - np.linalg.norm(E - E_pos)

    # ====================================================================================================
    # Multiple points algorithm

    # ----- Make sure locations is a proper array

    locations = np.array(locations, float)
    if len(locations.shape) == 1:
        locations = np.reshape(locations, (1,) + np.shape(locations))

    # ----- Compute the electric field separating negative and positive charges to
    # compute the "color" attribute

    charges_count = len(locations)
    if np.shape(charges) in [(), (1,), (charges_count,)]:
        charges = np.resize(charges, charges_count)
    else:
        raise AttributeError(f"electric_field error: 'locations' attributes has {charges_count} locations which is not compatible with the number of charges {np.shape(charges)}")

    E_pos = np.zeros((len(points), 3), float)
    E_neg = np.array(E_pos)
    for location, charge in zip(locations, charges):
        v = points - location
        n = np.maximum(np.linalg.norm(v, axis=-1), 1e-4)
        v /= (n**3)[:, None]
        if charge > 0:
            E_pos += v*charge
        else:
            E_neg += v*charge

    # ----------------------------------------------------------------------------------------------------
    # Color attribute

    return (E_pos + E_neg)*K, np.linalg.norm(E_pos) - np.linalg.norm(E_neg)

# =============================================================================================================================
# Electric field

def electric_field_NP(points, locations=(0, 0, 0), charges=1, epsilon0=1.):
    """ Compute the electric field produced by charges at locations.

    -------------------------------------------------------------------------------------
    NUMPY version which is less efficient than the naive implementation with python loops
    -------------------------------------------------------------------------------------

    Arguments
    ---------
    - points (array of vectors) : points where to compute the field
    - locations (array of vectors = (0., 0., 0.)) : locations of the electric charges
    - charges (array of floats = 1.) : electric charges
    - epsilon0 (float = 1.) : epsilon0 constant
    - return_color (bool = False) : return color attribute in an AttrVectors array of True

    Returns
    -------
    - array of vectors and, if return_color is True, an array of floats
    """

    # ----- Field at a single point

    if np.shape(points) == (3,):
        E, color = electric_field_NP([points], locations=locations, charges=charges, epsilon0=epsilon0)
        return E[0], color[0]

    # ----- Make sure locations and charges are proper arrays

    locations = np.array(locations, float)
    if len(locations.shape) == 1:
        locations = np.reshape(locations, (1,) + np.shape(locations))

    if np.shape(charges) == ():
        charges_ = charges
        charges = np.zeros(len(locations), float)
        charges[:] = charges_

    elif np.shape(charges) == (1,):
        charges = np.resize(charges, len(locations)).astype(float)

    elif not isinstance(charges, np.ndarray):
        charges = np.array(charges)

    # ----- Compute posive and negative fields separately to compare them

    i_neg = charges < 0
    i_pos = np.logical_not(i_neg)

    E = np.zeros((2, len(points), 3), float)
    indices = i_neg
    for i_E in range(2):
        if np.sum(indices) == 0:
            indices = i_pos
            continue

        locs = locations[indices]
        chgs = charges[indices]

        # All vectors form charge locations to points
        v = np.array(points)[:, None] - locs[None]

        # Vector norms
        norm = np.linalg.norm(v, axis=-1)
        norm[norm < .001] = 1.
        v /= (norm**3)[..., None]

        # Multiply by the charges
        v *= chgs[None, :, None]

        # Electric field
        E[i_E] = np.sum(v, axis=1)

        # ----- Neg to pos
        indices = i_pos

    # ----- Resulting field

    colors = np.linalg.norm(E[1], axis=-1) - np.linalg.norm(E[0], axis=-1)

    return (E[0] + E[1])*(1/4/np.pi/epsilon0), colors

    """
    if return_color:

        # Compute the field
        v = electric_field(points, locations=locations, charges=charges, return_color=False)

        from geonodes import AttrVectors

        if np.shape(charges) == ():
            color = -1. if charges < 0 else 1.
        else:
            # Compute field from negative charges
            charges = np.array(charges, float)
            neg_sel = charges < 0
            if np.sum(neg_sel) > 0:
                neg_locs = locations[neg_sel]
                neg_charges = charges[neg_sel]
                neg_v = electric_field(points, locations=neg_locs, charges=neg_charges, return_color=False)
                pos_v = v - neg_v
                neg_norm = np.linalg.norm(neg_v, axis=-1)
                pos_norm = np.linalg.norm(pos_v, axis=-1)
                color = pos_norm - neg_norm
            else:
                color = 1.

            return AttrVectors(v, color=color)

    # ----- Field computation

    # All vectors form charge locations to points
    v = np.array(points)[:, None] - locations[None]

    # Vector norms
    norm = np.linalg.norm(v, axis=-1)
    norm[norm < .001] = 1.
    v /= (norm**3)[..., None]

    # Multiply by the charges
    if np.shape(charges) == ():
        v *= charges
    else:
        v *= np.array(charges)[None, :, None]

    # Return vectors
    return np.sum(v, axis=1)*(1/4/np.pi/epsilon0)
    """

# =============================================================================================================================
# Magnetic field

def magnetic_field(points, locations=(0, 0, 0), moments=(1, 0, 0), mu0=1.):
    """ Compute the magnetic field produced by magnetic moments at locations.

    Arguments
    ---------
    - points (array of vectors) : points where to compute the field
    - locations (array of vectors = (0., 0., 0.)) : locations of the magnetic moments
    - moments (array of vectors = (1., 0., 0.)) : magnetic moments
    - mu0 (float = 1.) : mu0 constant

    Returns
    -------
    - array of vectors and, if return_color is True, an array of floats
    """

    # ----- Field at a single point

    if np.shape(points) == (3,):
        v, col = magnetic_field([points], locations=locations, moments=moments, mu0=mu0)
        return v[0], col[0]

    if not isinstance(points, np.ndarray):
        points = np.array(points)

    # ---------------------------------------------------------------------------
    # Normalize inputs

    locations = np.array(locations, float)
    if len(locations.shape) == 1:
        locations = np.reshape(locations, (1,) + np.shape(locations))

    moments_ = np.array(locations)
    moments_[:] = moments
    moments = moments_

    # ---------------------------------------------------------------------------
    # Compute field

    B = np.zeros((len(points), 3), float)
    color = np.zeros(len(points), float)
    for location, moment in zip(locations, moments):

        v = points - location
        n = np.maximum(np.linalg.norm(v, axis=-1), 1e-4)

        er = v/n[:, None]
        n2 = 1/(n*n)

        f_r = np.einsum('...i, ...i', er, moment)*n2
        f_n = np.cross(er, np.cross(er, moment))*n2[:, None]

        del n2

        B += (er*f_r[:, None] + f_n)*(mu0/4/np.pi)
        color += f_r

    return B, color

# =============================================================================================================================
# Magnetic field

def magnetic_field_NP(points, locations=(0, 0, 0), moments=(1, 0, 0), mu0=1.):
    """ Compute the magnetic field produced by magnetic moments at locations.

    -------------------------------------------------------------------------------------
    NUMPY version which is less efficient than the naive implementation with python loops
    -------------------------------------------------------------------------------------

    Arguments
    ---------
    - points (array of vectors) : points where to compute the field
    - locations (array of vectors = (0., 0., 0.)) : locations of the magnetic moments
    - moments (array of vectors = (1., 0., 0.)) : magnetic moments
    - mu0 (float = 1.) : mu0 constant

    Returns
    -------
    - array of vectors or AttrVectors if return_color is True
    """

    # ----- Field at a single point

    if np.shape(points) == (3,):
        v, col = magnetic_field([points], locations=locations, moments=moments, mu0=mu0)
        return v[0], col[0]

    # ---------------------------------------------------------------------------
    # Normalize inputs

    locations = np.array(locations, float)
    if len(locations.shape) == 1:
        locations = np.reshape(locations, (1,) + np.shape(locations))

    moments_ = np.array(locations)
    moments_[:] = moments
    moments = moments_

    # ---------------------------------------------------------------------------
    # Compute field

    v = np.array(points)[:, None] - locations[None, :]

    norm = np.linalg.norm(v, axis=-1)
    norm[norm < .001] = 1.
    er = v/norm[..., None]

    norm2 = (1/norm**2)

    f_r = np.einsum('...i, ...i', er, moments[None, :])*norm2
    f_n = np.cross(er, np.cross(er, moments[None, :]))*norm2[..., None]

    del norm2

    color = np.sum(f_r, axis=1)

    vect = np.sum(er*f_r[..., None] + f_n, axis=1)*(mu0/4/np.pi)

    return vect, color

# -----------------------------------------------------------------------------------------------------------------------------
# A a dipole : uses the electric field

def magnetic_field_FROM_ELECTRIC(points, locations=(0, 0, 0), moments=(1, 0, 0), distance=.1, mu0=1., return_color=False):

    n = 1 if len(np.shape(locations)) == 1 else len(locations)
    charge_locations = np.empty((2*n, 3), float)
    dirs = np.resize(moments, (n, 3))
    norms = np.linalg.norm(dirs, axis=-1)
    dirs *= ((distance/2)/norms)[:, None]

    charge_locations[:n] = locations - dirs
    charge_locations[n:] = locations + dirs

    return electric_field(points, locations=charge_locations, charges=np.append(norms, -norms), epsilon0=1/mu0, return_color=return_color)

# =============================================================================================================================
# Derivatives

# -----------------------------------------------------------------------------------------------------------------------------
# Partial derivative along an axis

def partial_der(points, field, axis=0, dt=.01, **kwargs):
    dv = (dt, 0, 0) if axis==0 else (0, dt, 0) if axis==1 else (0, 0, dt)
    return (field(points + dv, **kwargs) - field(points - dv, **kwargs))*(.5/dt)

# -----------------------------------------------------------------------------------------------------------------------------
# Gradient

def grad(points, field, dt=.01, **kwargs):
    g = np.array(points, float)
    g[..., 0] = partial_der(points, field, axis=0, dt=dt, **kwargs)
    g[..., 1] = partial_der(points, field, axis=1, dt=dt, **kwargs)
    g[..., 2] = partial_der(points, field, axis=2, dt=dt, **kwargs)
    return g

# -----------------------------------------------------------------------------------------------------------------------------
# Divergence

def div(points, field, dt=.01, **kwargs):
    points = np.array(points, float)
    return ((field(points + (dt, 0, 0), **kwargs) - field(points - (dt, 0, 0), **kwargs))[..., 0] +
            (field(points + (0, dt, 0), **kwargs) - field(points - (0, dt, 0), **kwargs))[..., 1] +
            (field(points + (0, 0, dt), **kwargs) - field(points - (0, 0, dt), **kwargs))[..., 2])*(.5/dt)

# -----------------------------------------------------------------------------------------------------------------------------
# Curl

def curl(points, field, dt=.01, **kwargs):

    points = np.array(points, float)

    partial_x = partial_der(points, field, axis=0, dt=dt, **kwargs)
    partial_y = partial_der(points, field, axis=1, dt=dt, **kwargs)
    partial_z = partial_der(points, field, axis=2, dt=dt, **kwargs)

    points[..., 0] = partial_y[2] - partial_z[1]
    points[..., 1] = partial_z[0] - partial_x[2]
    points[..., 2] = partial_x[2] - partial_z[0]

    return points

# -----------------------------------------------------------------------------------------------------------------------------
# Laplacian

def laplacian(points, field, dt=.1, **kwargs):

    points = np.array(points, float)

    lap  = field(points - (2*dt, 0, 0), **kwargs) + field(points + (2*dt, 0, 0), **kwargs)
    lap += field(points - (0, 2*dt, 0), **kwargs) + field(points + (0, 2*dt, 0), **kwargs)
    lap += field(points - (0, 0, 2*dt), **kwargs) + field(points + (0, 0, 2*dt), **kwargs)

    return (lap - 6*field(points, **kwargs))*(.5/dt)**2


# -----------------------------------------------------------------------------------------------------------------------------
# "In the flow" divergence computation
# Just for fun

def div2(field, points, dt=.01):

    points = np.array(points, float)
    v = field(points)

    e0, e1, e2 = local_base(v)

    da = np.einsum('...i, ...i', field(points + dt*e0) - field(points - dt*e0), e0)
    db = np.einsum('...i, ...i', field(points + dt*e1) - field(points - dt*e1), e1)
    dc = np.einsum('...i, ...i', field(points + dt*e2) - field(points - dt*e2), e2)

    return (da + db + dc)*(.5/dt)


# ====================================================================================================
# Field lines

# ----------------------------------------------------------------------------------------------------
# Compute starting points around charge locations
# Return start_points and backwards arguments

def get_start_points(locations, charges=1, count=100, distance=.1, electric=True, seed=0):
    """ Compute field line starting points around the charges or magnetic moment locations.

    Arguments
    ---------
    - location (arrayc of vectors) : charges / moments locations
    - charges (float or array of floats or vector or array of vectors) : the charges or moments
    - count (int = 100) : number of starting points to create
    - distance (float = .1) : distance to the centers
    - electric (bool = True) : locations are electric charges (True) or magnetic moments (False)
    - seed (any = 0) : random seed

    Returns
    -------
    - Array of vectors, array of bools : line strat points and backwards flag
    """

    from geonodes.maths import distribs

    points, _ = distribs.sphere_dist(radius=distance, count=count, seed=seed)

    # ----- One single location

    if np.shape(locations) == (3,):
        if electric:
            return locations + points, [charges < 0] * count
        else:
            charges = np.reshape(charges, (3,))
            return locations + points, np.einsum('i, ...i', charges, points) < 0

    # ----- Several locations

    # Move points around random locations

    n = len(locations)
    rng = np.random.default_rng(seed+1)
    inds = rng.integers(0, n, count)

    # Charges as a proper array

    if electric:
        if np.size(charges) == 1:
            charges = np.resize(charges, len(locations))
        elif not isinstance(charges, np.ndarray):
            charges = np.array(charges)

        return points + np.array(locations)[inds], charges[inds] < 0

    else:
        if np.size(charges) == 3:
            charges = np.resize(charges, (len(locations), 3))
        elif not isinstance(charges, np.ndarray):
            charges = np.array(charges)

        return points + np.array(locations)[inds], np.einsum('...i, ...i', charges[inds], points) < 0


# ----------------------------------------------------------------------------------------------------
# Compute the lines of field

def field_lines(field_func, start_points, backwards=False, return_color=False, max_length=None, length_scale=None, end_points=None, zero=1e-6, max_points=1000, precision=.1, sub_steps=10, seed=0, **kwargs):

    """ Com pute the lines of field

    ---------------------------------------------------------------
    NUMPY VERSION : seams to be better than the python loop version
    ---------------------------------------------------------------

    Arguments :
    -----------
        - field_func (function of template (array of vectors, **kwargs) -> array of vectors) : the field function
        - start_points (array of vectors) : lines starting points
        - backwards (bool = False) : build lines backwards
        - return_color (bool = False) : manage 'color' attribute along the field
        - max_length (float = None) : max line lengths
        - length_scale (float = None) : line length scale if random length scale around central value
        - end_points (array of vectors) : points where lines must end
        - zero (float = 1e-6) : value below which the field is null
        - max_points (int = 1000) : max number of points per spline
        - precision (float = 0.1) : step length
        - sub_steps (int = 10) : number of sub steps

    Returns :
    ---------
        - Splines dictionary with keys {'types': [], 'cyclic':  [], 'splines': [{'points':, 'radius':, 'tilt': }]}
    """

    # ----------------------------------------------------------------------------------------------------
    # Field function can return a couple (vectors, colors) or just vectors

    def call_field_func(points, **kwargs):
        a = field_func(points, **kwargs)
        if isinstance(a, tuple):
            return a
        else:
            return a, 0.

    # ----------------------------------------------------------------------------------------------------
    # Prepare variables

    rng = np.random.default_rng(seed)

    if not isinstance(start_points, np.ndarray):
        start_points = np.array(start_points, float)

    single = np.shape(start_points) == (3,)
    if single:
        start_points = np.reshape(start_points, (1, 3))

    count = len(start_points)

    max_lengths = None
    if length_scale is not None:
        max_lengths = rng.normal(max_length, length_scale, count)

    if not isinstance(end_points, np.ndarray):
        end_points = np.array(end_points, float)

    sub_steps = max(sub_steps, 1)
    prec = precision / sub_steps

    backs = np.empty(count, bool)
    backs[:] = backwards
    has_backwards = np.sum(backs) > 0
    if has_backwards:
        rev = np.ones((count, 1), int)
        rev[backs, 0] = -1

    # ----------------------------------------------------------------------------------------------------
    # Loop variables

    points = np.zeros((count, max_points, 3), float)
    points[:, 0] = start_points

    # ----- Radius and colors
    radius = np.ones((count, max_points), float)
    colors = np.zeros((count, max_points), float)

    vect, col = call_field_func(start_points, **kwargs)
    radius[:, 0] = np.linalg.norm(vect, axis=-1)
    colors[:, 0] = col

    # ----- Lengths and counts
    lengths = np.zeros(count, float)
    counts  = np.ones(count, int)

    # ----- Lines which are not finished

    alive  = np.ones(count, bool)

    # ---------------------------------------------------------------------------
    # Add a point with its attributes

    def add_points(point_index, pts, norm, cols):

        points[:, point_index] = pts
        radius[:, point_index] = norm
        colors[:, point_index] = cols
        lengths[alive] += np.linalg.norm(pts - points[:, point_index-1], axis=-1)[alive]
        counts[alive] += 1

        sel = None
        if length_scale is None:
            if max_length is not None:
                sel = lengths >= max_length
        else:
            sel = lengths >= max_lengths
        if sel is not None:
            alive[sel] = False

    # ----------------------------------------------------------------------------------------------------
    # Loop

    pts  = np.array(start_points)
    norm = None
    cols = 0
    for point_index in range(1, max_points):

        # ----- Sub steps

        for _ in range(sub_steps):

            # ----- Vector at current location
            v0, cols = call_field_func(pts, **kwargs)

            if has_backwards:
                v0 *= rev

            # ----- Precision along this vector
            norm   = np.linalg.norm(v0, axis=-1)

            sel = norm < zero
            alive[sel] = False
            norm[sel] = 1

            factor = prec/norm
            v0 *= factor[..., None]

            # ----- Average with target vector for more accurracy
            v1, _ = call_field_func(pts + v0, **kwargs)
            v1 *=(factor[..., None])
            if has_backwards:
                v1 *= rev
            v  = (v0 + v1)/2

            # ----- Next point
            pts += v

            # ----- Lines are back to the starting point
            if point_index > 2:
                ds = np.linalg.norm(pts - start_points, axis=-1)
                alive[ds < precision] = False

            # ----- Lines reach one starting point

            if end_points is not None:
                ds       = np.linalg.norm(pts[:, None] - end_points[None], axis=-1)
                min_inds = np.argmin(ds, axis=1)
                min_ds   = ds[np.arange(count), min_inds]

                alive[min_ds < precision] = False

        # ----- Add the point

        add_points(point_index, pts, norm, cols)

    # ----------------------------------------------------------------------------------------------------
    # Return the lines as a dict

    splines = {'types': [1]*len(counts), 'cyclic': [False]*len(counts), 'splines': []}

    for line_index, n in enumerate(counts):

        splines['cyclic'] = np.linalg.norm(points[line_index, n-1] - points[line_index, 0]) <= precision
        if has_backwards and rev[line_index]:
            splines['splines'].append({
                'points': points[line_index, :n],
                'radius': radius[line_index, :n],
                'tilt'  : colors[line_index, :n],
            })
        else:
            splines['splines'].append({
                'points': np.flip(points[line_index, :n]),
                'radius': np.flip(radius[line_index, :n]),
                'tilt'  : np.flip(colors[line_index, :n]),
            })

    return splines


# -----------------------------------------------------------------------------------------------------------------------------
# Compute the lines of field with loops in python

def field_lines_PY_LOOP(field_func, start_points, backwards=False, max_length=None, length_scale=None, end_points=None, zero=1e-6, max_points=1000, precision=.1, sub_steps=10, seed=0, **kwargs):

    """ Compute the lines of field

    ---------------------------------------------------------------
    PYTHON LOOP Version : seams to be slower than the numpy version
    ---------------------------------------------------------------

    Arguments :
    -----------
        - field_func (function of template (array of vectors, **kwargs) -> array of vectors) : the field function
        - start_points (array of vectors) : lines starting points
        - backwards (bool = False) : build lines backwards
        - max_length (float = None) : max line lengths
        - length_scale (float = None) : line length scale if random length scale around central value
        - end_points (array of vectors) : points where lines must end
        - zero (float = 1e-6) : value below which the field is null
        - max_points (int = 1000) : max number of points per spline
        - precision (float = 0.1) : step length
        - sub_steps (int = 10) : number of sub steps

    Returns :
    ---------
        - Splines dictionary with keys {'types': [], 'cyclic':  [], 'splines': [{'points':, 'radius':, 'tilt': }]}
    """

    # ----------------------------------------------------------------------------------------------------
    # Prepare variables

    rng = np.random.default_rng(seed)

    if not isinstance(start_points, np.ndarray):
        start_points = np.array(start_points, float)

    single = np.shape(start_points) == (3,)
    if single:
        start_points = np.reshape(start_points, (1, 3))

    count = len(start_points)

    if max_length is not None and length_scale is not None:
        rng = np.random.default_rng(seed)
        max_lengths = rng.normal(max_length, length_scale, count)
    else:
        max_lengths = [max_length]*count

    if not isinstance(end_points, np.ndarray):
        end_points = np.array(end_points, float)

    sub_steps = max(sub_steps, 1)
    prec = precision / sub_steps

    backs = np.empty(count, bool)
    backs[:] = backwards
    has_backwards = np.sum(backs) > 0
    if has_backwards:
        rev = np.ones((count, 1), int)
        rev[backs, 0] = -1

    # ====================================================================================================
    # Core function building a line in a given direction
    # Makes use of global arrays verts, radius and colors to avoid multiple array creations
    # - arrays are created one at max size
    # - copied at the final size for each spline

    verts  = np.empty((max_points, 3), float)
    radius = np.empty(max_points, float)
    colors = np.empty(max_points, float)

    def build_spline(start_point, max_length, back):

        # ----- Initial point

        vect, col = field_func(start_point, return_color=True, **kwargs)
        verts[0], radius[0], colors[0] = np.array(start_point), np.linalg.norm(vect), col

        length  = 0.
        cyclic  = False
        cur_loc = np.array(start_point)
        count   = 0
        stop    = False

        for i_vertex in range(1, max_points):

            # ----------------------------------------------------------------------------------------------------
            # Sub steps

            for _ in range(sub_steps):

                # Vector at current location

                v0 = field_func(cur_loc, return_color=False, **kwargs)

                # Factor to have a length equal to prec

                norm = np.linalg.norm(v0)
                if norm < zero:
                    stop = True
                    break

                factor = -prec/norm if back else prec/norm
                v0 *= factor

                # Vector at next location

                v1 = field_func(cur_loc + v0, return_color=False, **kwargs)*factor

                # Actuel step is the average of these two vectors

                cur_loc += (v0 + v1)/2

            # ----------------------------------------------------------------------------------------------------
            # Add the point

            vect, col = field_func(cur_loc, return_color=True, **kwargs)
            verts[i_vertex], radius[i_vertex], colors[i_vertex] = np.array(cur_loc), np.linalg.norm(vect), col
            length += precision

            # ----------------------------------------------------------------------------------------------------
            # Exit loop conditions

            if i_vertex > 2:
                ds = np.linalg.norm(cur_loc - start_point)
                if ds <= precision:
                    cyclic = True
                    stop   = True

            # ----- Line reaches one starting point

            if end_points is not None:
                ds  = np.linalg.norm(cur_loc - end_points, axis=-1)
                if np.any(ds <= precision):
                    stop   = True

            # ----- Max length is reached

            if max_length is not None and length >= max_length:
                stop = True

            # ----- Stop condition is reached

            count = i_vertex + 1
            if stop:
                break

        # ----------------------------------------------------------------------------------------------------
        # Return the result

        if back:
            return {'spline' : {
                        'points' : np.flip(np.array(verts[:count])),
                        'radius' : np.flip(np.array(radius[:count])),
                        'tilt'   : np.flip(np.array(colors[:count])),
                        },
                    'cyclic' : cyclic,
                    }
        else:
            return {'spline': {
                        'points' : np.array(verts[:count]),
                        'radius' : np.array(radius[:count]),
                        'tilt'   : np.array(colors[:count]),
                        },
                    'cyclic' : cyclic,
                    }

    # ====================================================================================================
    # Loop on the field lines

    splines = {'splines': [], 'cyclic': []}

    for start_point, max_length, back in zip(start_points, max_lengths, backs):

        spline = build_spline(start_point, max_length, back)
        if len(spline['spline']['points']) > 2:
            splines['cyclic'].append(spline['cyclic'])
            splines['splines'].append(spline['spline'])

    splines['types'] = [1]*len(splines['cyclic'])

    return splines

# -----------------------------------------------------------------------------------------------------------------------------
# Compute the lines of field as bezier curves
# Less precise but quicker (hope so)

def bezier_field_lines(field_func, start_points, backwards=False, max_length=None, length_scale=None, end_points=None, zero=1e-6, max_points=1000, factor=1., seed=0, **kwargs):

    """ Compute the lines of field as Bezier curves

    Arguments :
    -----------
        - field_func (function of template (array of vectors, **kwargs) -> array of vectors) : the field function
        - start_points (array of vectors) : lines starting points
        - backwards (bool = False) : build lines backwards
        - max_length (float = None) : max line lengths
        - length_scale (float = None) : line length scale if random length scale around central value
        - end_points (array of vectors) : points where lines must end
        - zero (float = 1e-6) : value below which the field is null
        - max_points (int = 1000) : max number of points per spline
        - factor (float = 1.) : step length

    Returns :
    ---------
        - Splines dictionary with keys {'types': [], 'cyclic':  [], 'splines': [{'points':, 'radius':, 'tilt': }]}
    """

    # ----------------------------------------------------------------------------------------------------
    # Prepare variables

    # Start points

    if not isinstance(start_points, np.ndarray):
        start_points = np.array(start_points, float)

    single = np.shape(start_points) == (3,)
    if single:
        start_points = np.reshape(start_points, (1, 3))

    count = len(start_points)

    # Max lengths

    if max_length is not None and length_scale is not None:
        rng = np.random.default_rng(seed)
        max_lengths = rng.normal(max_length, length_scale, count)
    else:
        max_lengths = [max_length]*count

    # End points

    if not isinstance(end_points, np.ndarray):
        end_points = np.array(end_points, float)

    # Backwards directions

    backs = np.empty(count, bool)
    backs[:] = backwards
    has_backwards = np.sum(backs) > 0
    if has_backwards:
        rev = np.ones((count, 1), int)
        rev[backs, 0] = -1

    # ----------------------------------------------------------------------------------------------------
    # Core function building a line in a given direction
    # Makes use of global arrays verts, radius and colors to avoid multiple array creations
    # - arrays are created one at max size
    # - copied at the final size for each spline

    verts    = np.empty((max_points, 3), float)
    radius   = np.empty(max_points, float)
    colors   = np.empty(max_points, float)

    def build_spline(start_point, max_length, back):

        # ----------------------------------------------------------------------------------------------------
        # Compute the shift vector from the field vector
        # Returns : shift vector, norm

        def shift_vector(vect):
            n = np.linalg.norm(vect)
            if n < zero:
                return (0., 0., 0.), 0.

            if back:
                vect = -vect

            if True or n > 1:
                return vect*(factor/n), factor
            else:
                return vect*factor, n*factor

        # ----------------------------------------------------------------------------------------------------
        # Is a segment [cur_loc, next_loc] close to points (end points or start_point)

        def segment_close_to(cur_loc, next_loc, points):

            # ----- Unary vector on the segment
            vect = next_loc - cur_loc
            norm = np.linalg.norm(vect)
            null_segment = norm < 1e-6
            if not null_segment:
                vect /= norm

            dmin = max(factor, norm)

            # ----- Loop on the points
            if np.shape(points) == (3,):
                points = [points]

            for point in points:
                v = point - cur_loc
                n = np.linalg.norm(v)
                if null_segment:
                    if n < dmin:
                        return point
                else:
                    dist = np.dot(vect, v)
                    if dist < 0 or dist > dmin:
                        continue

                    perp = np.linalg.norm(np.cross(vect, v))
                    if perp < dmin:
                        return point

            # ----- No close point found

            return None

        # ----------------------------------------------------------------------------------------------------
        # Build core

        # ----- Initial point

        vect, col = field_func(start_point, **kwargs)
        v0, norm = shift_vector(vect)
        verts[0], radius[0], colors[0] = np.array(start_point), norm, col

        if norm < zero:
            return {}

        # ----- Loop variables

        length  = 0.
        cyclic  = False
        cur_loc = np.array(start_point)
        count   = 0

        # ----- Loop

        for i_vertex in range(1, max_points):

            # First approx : let's shift of v0 and let's compute the field at that location
            v1, _ = shift_vector(field_func(cur_loc + v0, **kwargs)[0])

            # Second approx let's use the average tangent

            next_loc = cur_loc + (v0 + v1)/2

            vect, col = field_func(next_loc, **kwargs)
            v0, norm = shift_vector(vect)
            verts[i_vertex], radius[i_vertex], colors[i_vertex] = np.array(cur_loc), norm, col

            length += norm
            count = i_vertex + 1

            # ----------------------------------------------------------------------------------------------------
            # Exit loop conditions

            # ----- Vector is null

            if norm < zero:
                break

            # ----- Line back to the starting point

            if i_vertex > 2:
                pt = segment_close_to(cur_loc, next_loc, start_point)
                if pt is not None:
                    cyclic = True
                    break

            # ----- Line reaches and end point

            if end_points is not None:
                pt = segment_close_to(cur_loc, next_loc, end_points)
                if pt is not None:
                    v = pt - next_loc
                    verts[count], radius[count], colors[count] = np.array(pt), np.linalg.norm(v), col
                    count += 1
                    break

            # ----- Max length is reached

            if max_length is not None and length >= max_length:
                break

            # ----- Update location

            cur_loc = next_loc

        # ----------------------------------------------------------------------------------------------------
        # Return the result

        return {'spline' : {
                    'points'      : np.array(verts[:count]),
                    'radius'      : np.array(radius[:count]),
                    'tilt'        : np.array(colors[:count]),
                    },
                'cyclic' : cyclic,
                }

    # ----------------------------------------------------------------------------------------------------
    # Main : loop on the field lines

    splines = {'splines': [], 'cyclic': []}

    for start_point, max_length, back in zip(start_points, max_lengths, backs):

        spline = build_spline(start_point, max_length, back)
        if len(spline['spline']['points']) > 2:
            splines['cyclic'].append(spline['cyclic'])
            splines['splines'].append(spline['spline'])

    splines['types'] = [0]*len(splines['cyclic'])

    return splines

# =============================================================================================================================
# Tests

# -----------------------------------------------------------------------------------------------------------------------------
# Different field tests
# def electric_field(points, locations=(0, 0, 0), charges=1., epsilon0=1.):
# def electric_field_NP(points, locations=(0, 0, 0), charges=1, epsilon0=1.):
# def magnetic_field(points, locations=(0, 0, 0), moments=(1, 0, 0), mu0=1.):
# def magnetic_field_NP(points, locations=(0, 0, 0), moments=(1, 0, 0), mu0=1.):
#
# def field_lines(field_func, start_points, backwards=False, return_color=False, max_length=None, length_scale=None, end_points=None, zero=1e-6, max_points=1000, precision=.1, sub_steps=10, seed=0, **kwargs):
# def bezier_field_lines(field_func, start_points, backwards=False, max_length=None, length_scale=None, end_points=None, zero=1e-6, max_points=1000, factor=1., seed=0, **kwargs):

def test_fields(electric=True, base_tests=True, perf_tests=True):

    import geonodes as gn
    from time import time

    # ----------------------------------------------------------------------------------------------------
    # Test a field function to build poly and bezier lines

    def test_func(name, field_func, start_points, backs, locations, lines_algo='BOTH', **kwargs):

        ok_poly   = lines_algo in ['BOTH', 'POLY']
        ok_bezier = lines_algo in ['BOTH', 'BEZIER']

        if ok_poly:
            t0 = time()
            poly = field_lines(field_func,
                start_points = start_points,
                backwards    = backs,
                max_length   = None,
                length_scale = None,
                end_points   = locations,
                zero         = 1e-6,
                max_points   = 1000,
                precision    = .1,
                sub_steps    = 10,
                seed         = 0,
                locations    = locations,
                **kwargs)

            duration = time() - t0
            print(f"{name} : poly   = {duration:.1f}")

            gn.Curve(**poly).to_object(  f"{name} {len(start_points)} - Poly")

        if ok_bezier:
            t0 = time()
            bezier = bezier_field_lines(field_func,
                start_points = start_points,
                backwards    = backs,
                max_length   = None,
                length_scale = None,
                end_points   = locations,
                zero         = 1e-6,
                max_points   = 1000,
                factor       = 1.,
                seed         = 0,
                locations    = locations,
                **kwargs)

            duration = time() - t0
            print(f"{name} : bezier = {duration:.1f}")

            gn.Curve(**bezier).to_object(  f"{name} {len(start_points)} - Bezier")


    rng = np.random.default_rng(0)

    # ----------------------------------------------------------------------------------------------------
    # Electric field

    CHARGES_MAX = 50
    locations = rng.uniform(-10, 10, (CHARGES_MAX, 3))

    sphere = gn.Mesh.UVSphere(radius=.5) * CHARGES_MAX
    sphere.points.translate(locations)
    sphere.to_object("Charges")

    if electric:
        print("Electric field")
        prefix = 'EL'

        charges   = rng.uniform(-10, 10, CHARGES_MAX)
        charges[0] = -1
        charges[1] = 1

        kwargs  = {'epsilon0': 1., 'charges': None}
        ch_name = 'charges'
        fstd    = electric_field
        f_np    = electric_field_NP
        dist    = .1

    else:
        print("Magnetic field")
        prefix = 'MG'

        charges = rng.uniform(-1, 1, (CHARGES_MAX, 3))

        kwargs  = {'mu0': 1., 'moments': None}
        ch_name = 'moments'
        fstd    = magnetic_field
        f_np    = magnetic_field_NP
        dist    = 1.

    if base_tests:
        print("Base test : does it work ?")
        print()

        for q_count, lines_count in zip([1, 2, 5], [100, 100, 100]):
            start_points, backs = get_start_points(locations[:q_count], charges[:q_count], distance=dist, count=lines_count, electric=electric)
            kwargs[ch_name] = charges[:q_count]
            test_func(f"{prefix} {q_count} STD {lines_count} lines", fstd, start_points, backs, locations[:q_count], **kwargs)
            test_func(f"{prefix} {q_count} NPY {lines_count} lines", f_np, start_points, backs, locations[:q_count], **kwargs)

    if perf_tests:
        print("\nPerformance test")
        for lines_count in [1, 10, 100, 500, 1000]:
            for q_count in [1, 2, 5, 10, 25, 50]:
                start_points, backs = get_start_points(locations[:q_count], charges[:q_count], distance=dist, count=lines_count, electric=electric)
                kwargs[ch_name] = charges[:q_count]
                test_func(f"{prefix} {q_count} STD {lines_count} lines", fstd, start_points, backs, locations[:q_count], lines_algo='POLY', **kwargs)
                test_func(f"{prefix} {q_count} NPY {lines_count} lines", f_np, start_points, backs, locations[:q_count], lines_algo='POLY', **kwargs)
