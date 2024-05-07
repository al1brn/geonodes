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

def electric_field(points, locations=(0, 0, 0), charges=1, epsilon0=1., return_color=False):

    # ----- Field at a single point

    if np.shape(points) == (3,):
        v = electric_field([points], locations=locations, charges=charges, epsilon0=epsilon0, return_color=return_color)
        if return_color:
            return v
        else:
            return v[0]

    # ----- Make sure locations is a proper array

    locations = np.array(locations, float)
    if len(locations.shape) == 1:
        locations = np.reshape(locations, (1,) + np.shape(locations))

    # ----- Return color : need to compute posive and negative field to compare them

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

# =============================================================================================================================
# Magnetic field

def magnetic_field(points, locations=(0, 0, 0), moments=(1, 0, 0), mu0=1., return_color=False):

    # ----- Field at a single point

    if np.shape(points) == (3,):
        v = magnetic_field([points], locations=locations, moments=moments, mu0=mu0, return_color=return_color)
        if return_color:
            return v
        else:
            return v[0]

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

    if return_color:
        from geonodes import AttrVectors
        return AttrVectors(vect, color=color)

    else:
        return vect



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








# OLD VERSION

def magnetic_field_OLD(points, locations=(0, 0, 0), moments=(1, 0, 0), mu0=1., return_color=False):

    # ----- Field at a single point

    if np.shape(points) == (3,):
        v = magnetic_field([points], locations=locations, moments=moments, mu0=mu0, return_color=return_color)
        if return_color:
            return v
        else:
            return v[0]

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

    if True:
        norm2 = (1/norm**2)

        f_r = np.einsum('...i, ...i', er, moments[None, :])*norm2
        f_n = np.cross(er, np.cross(er, moments[None, :]))*norm2[..., None]

        del norm2

        color = np.sum(f_r, axis=1)

        vect = np.sum(er*f_r[..., None] + f_n, axis=1)*(mu0/4/np.pi)

        if return_color:
            from geonodes import AttrVectors
            return AttrVectors(vect, color=color)

        else:
            return vect


    else:
        f_r = np.einsum('...i, ...i', er, moments[None, :])
        f_n = np.cross(er, np.cross(er, moments[None, :]))

        vect = np.sum((er*f_r[..., None] + f_n)/((norm**2)[..., None]), axis=1)*(mu0/4/np.pi)

        if return_color:

            from geonodes import AttrVectors

            return AttrVectors(vect, color=1)

            #return vect, np.sum(f_r/norm**2, axis=-1)
        else:
            return vect

        #return np.sum((er*f_r[..., None] + f_n)/((norm**2)[..., None]), axis=1)*(mu0/4/np.pi)

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

def field_lines(field_func, start_points, backwards=False, return_color=False, max_length=None, length_scale=None, end_points=None, zero=1e-6, max_points=1000, precision=.1, sub_steps=10, seed=0, **kwargs):

    """ Compute the lines of field

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
        - list of (AttrVectors, bool) : (points with attributes 'radius' and 'color', is_cyclic)
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

    if return_color:
        avects = field_func(start_points, return_color=True, **kwargs)

        radius[:, 0] = np.linalg.norm(avects.co, axis=-1)
        colors[:, 0] = avects.color
    else:
        radius[:, 0] = np.linalg.norm(field_func(start_points, **kwargs), axis=-1)

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
            if return_color:
                avects = field_func(pts, return_color=True, **kwargs)
                v0, cols = np.array(avects.co), avects.color
            else:
                v0 = field_func(pts, **kwargs)

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
            v1 = field_func(pts + v0, **kwargs)*(factor[..., None])
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
    # Return the lines

    from geonodes import AttrVectors

    lines = []
    for line_index, n in enumerate(counts):

        closed = np.linalg.norm(points[line_index, n-1] - points[line_index, 0]) <= precision
        v_co     = points[line_index, :n]
        v_radius = radius[line_index, :n]
        v_color = colors[line_index, :n]

        ok_flip = has_backwards and rev[line_index]

        if ok_flip:
            v_co     = np.flip(v_co, axis=0)
            v_radius = np.flip(v_radius)
            v_color  = np.flip(v_color)

        lines.append((AttrVectors(v_co, radius=v_radius, color=v_color), closed))

        if False:
            if ok_flip:
                lines.append((np.flip(points[line_index, :n], axis=0), np.flip(radius[line_index, :n]), closed, cols))
            else:
                lines.append((points[line_index, :n], radius[line_index, :n], closed, cols))

    if single:
        return lines[0]
    else:
        return lines

# =============================================================================================================================
# Tests

def test_div(r=1.):

    def print_a(title, a):
        print(title, ":\n", ", ".join([f"{v:.3f}" for v in a]), "\n")

    count = 12
    ag = np.linspace(0, 2*np.pi, count, endpoint=False)
    pts = np.zeros((count, 3), float)
    pts[:, 0] = r*np.cos(ag)
    pts[:, 1] = r*np.sin(ag)

    a = div(constant_field, pts)
    print_a("Constant field", a)

    for power, expected in zip([0, 1, 3], ["3", f"{2/r:.3f}", "0"]):
        print('-'*70)
        a = div(lambda v: radial_field(v, power=power), pts)
        print_a(f"Radial field, power={power}, expected: {expected}", a)

        a = div2(lambda v: radial_field(v, power=power), pts)
        print_a(f"Radial field, power={power}, expected: {expected}", a)









def tests():
    import matplotlib.pyplot as plt

    def draw_field(points, vectors, fmt='-'):
        for p, v in zip(points, vectors):
            plt.plot([p[0], p[0] + v[0]], [p[1], p[1] + v[1]], fmt)


    charges = ((-1, 0, 0, -1), (1, 0, 0, 1))
    #charges = charges[0]


    for r in np.linspace(2, 5, 3):
        count = 30
        ag = np.linspace(0, 2*np.pi, count, endpoint=False)
        pts = np.zeros((count, 3), float)
        pts[:, 0] = r*np.cos(ag)
        pts[:, 1] = r*np.sin(ag)

        if False:
            E = electric_field(pts, charges=charges, epsilon0=.01)
        else:
            E = radial_field(pts, power=2, factor=2)

        draw_field(pts, E, fmt='-k')

    plt.show()

#tests()
#test_div(r=10)
