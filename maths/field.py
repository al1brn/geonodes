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

def electric_field(points, charges=(0, 0, 0, 1), epsilon0 = 1.):
    
    charges = np.array(charges, float)
    if len(charges.shape) == 1:
        charges = np.reshape(charges, (1,) + np.shape(charges))
    
    v = np.array(points)[:, None] - charges[None, :, :-1]
    
    norm = np.linalg.norm(v, axis=-1)
    norm[norm < .001] = 1.
    v /= (norm**3)[..., None]
    v *= charges[None, :, -1][..., None]
    
    return np.sum(v, axis=1)*(1/4/np.pi/epsilon0)

# =============================================================================================================================
# Magnet field

def magnetic_field(points, dipoles=[(0., 0., 0.), (1., 0., 0.)], mu0=1.):
    
    # ---------------------------------------------------------------------------
    # Normalize inputs
    
    count = 1 if len(np.shape(dipoles)) == 2 else len(dipoles)
    n = 1 if len(np.shape(points)) == 1 else len(points)
        
    dipoles = np.reshape(dipoles, (count, 2, 3))
    points  = np.reshape(points, (n, 3))
    
    # ---------------------------------------------------------------------------
    # Compute field
    
    v = np.array(points)[:, None] - dipoles[None, :, 0]
    
    norm = np.linalg.norm(v, axis=-1)
    norm[norm < .001] = 1.
    er = v/norm[..., None]

    f_r = np.einsum('...i, ...i', er, dipoles[None, :, 1])
    f_n = np.cross(er, np.cross(er, dipoles[None, :, 1]))
    
    return np.sum((er*f_r[..., None] + f_n)/((norm**2)[..., None]), axis=1)*(mu0/4/np.pi)



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
    