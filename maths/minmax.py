#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 19:13:23 2024

@author: alain
"""

import numpy as np

# ====================================================================================================
# Function:
# x < 0 : f(x) = x
# x > 0 : f(x) = 0
# Rounded on the interval ]-delta, delta[

def max_0(x, delta=0):
    r = np.minimum(x, 0)
    if delta > 0:
        sel = np.logical_and(x > -delta, x < delta)
        v   = x[sel]
        if len(v):
            r[sel] = v*v/(-4*delta) + v/2 - delta/4
    return r

# ====================================================================================================
# Continuous minimum and maximum

def minimum(x, max_value=None, delta=0):
    if max_value is None:
        return x
    return max_value + max_0(x - max_value, delta)

def maximum(x, min_value, delta=0):
    if min_value is None:
        return x
    return min_value - max_0(min_value - x, delta)

def clip(x, min_value=None, max_value=None, delta=0):
    return minimum(maximum(x, min_value, delta=delta), max_value, delta=delta)

# ====================================================================================================
# Vector norm minimization

def maximize_vectors(v, max_norm=None, delta=0):
    if max_norm is None:
        return v
    
    norm = np.linalg.norm(v, axis=-1)
    new_norm = minimum(norm, max_norm, delta=delta)
    
    sel = np.abs(norm) > .001
    v[sel] = v[sel]*(new_norm[sel]/norm[sel])[:, None]
    
    return v
    
def minimize_vectors(v, min_norm=None, delta=0):
    if min_norm is None:
        return v
    
    norm = np.linalg.norm(v, axis=-1)
    new_norm = maximum(norm, min_norm, delta=delta)
    
    sel = np.abs(norm) > .001
    v[sel] = v[sel]*(new_norm[sel]/norm[sel])[:, None]
    
    return v

def clip_vectors(v, min_norm=None, max_norm=None, delta=0):
    if min_norm is None and max_norm is None:
        return v

    norm = np.linalg.norm(v, axis=-1)
    new_norm = clip(norm, min_norm, max_norm, delta=delta)
    
    sel = np.abs(norm) > .001
    w = np.array(v)
    w[sel] = v[sel]*(new_norm[sel]/norm[sel])[:, None]
    
    return w

# ====================================================================================================
# Demo / Test

def demo():
    import matplotlib.pyplot as plt
    
    t = np.linspace(-1, 2, 100)
    
    title = 'max_0'
    plt.plot(t, max_0(t, .1))
    plt.title(label=title)
    plt.show()

    title = 'min_0'
    plt.plot(t, -max_0(-t, .1))
    plt.title(label=title)
    plt.show()

    t = np.linspace(-10, 30, 100)
    
    title = 'minimum'
    plt.plot(t, minimum(t, 20, 1))
    plt.title(label=title)
    plt.show()
    
    title = 'maximum'
    plt.plot(t, maximum(t, 10, 1))
    plt.title(label=title)
    plt.show()
    
    title = 'clip'
    plt.plot(t, clip(t, None, None, delta=1) + 0)
    plt.plot(t, clip(t,   10, None, delta=1) + 2)
    plt.plot(t, clip(t, None,   20, delta=1) + 4)
    plt.plot(t, clip(t,   10,   20, delta=1) + 6)
    plt.title(label=title)
    plt.show()
    
    title = 'clip vectors'
    
    v = np.random.uniform(-12, 12, (100, 3))
    n0 = np.linalg.norm(v, axis=-1)
    
    w = clip_vectors(v, None, None, delta=1)
    n1 = np.linalg.norm(w, axis=-1)
    plt.plot(n0, n1, '.')
    
    w = clip_vectors(v, 5, None, delta=1)
    n1 = np.linalg.norm(w, axis=-1)
    plt.plot(n0, n1 + 2, '.')
    
    w = clip_vectors(v, None, 11, delta=1)
    n1 = np.linalg.norm(w, axis=-1)
    plt.plot(n0, n1 + 4, '.')
    
    w = clip_vectors(v, 5, 11, delta=1)
    n1 = np.linalg.norm(w, axis=-1)
    plt.plot(n0, n1 + 6, '.')
    
    plt.title(label=title)
    plt.show()

