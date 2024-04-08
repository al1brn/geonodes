#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:33:43 2024

@author: alain
"""

import numpy as np
import matplotlib.pyplot as plt

Q      = -.5
v      = .1
c      = 1
beta   = v/c
gamma  = 1/np.sqrt(1 - beta**2)

# ====================================================================================================
# Solver

def solve(f, t0, t1):
    
    # ----- Look for two acceptable bounds
    
    count = 1000
    vs = f(np.linspace(t0, t1, count))
    ds = vs[:-1]*vs[1:]
    i = np.argmin(ds)
    dt = (t1 - t0)/(count-1)
    t0, t1 = t0 + i*dt, t0 + (i+1)*dt
    
    v0 = f(t0)
    v1 = f(t1)
    assert(v0*v1 < 0)
    
    # ----- Proper order
    
    if v0 > v1:
        v, t   = v1, t1
        v1, t1 = v0, t0
        v0, t0 = v, t
        
    assert(v0<=0)
    assert(v1>=0)
    
    # ----- Loop
    
    for _ in range(50):
        t = (t0 + t1)/2
        v = f(t)
        if abs(v) < 1e-6:
            return t
        elif v < 0:
            v0, t0 = v, t
        else:
            v1, t1 = v, t
    return t

# ====================================================================================================
# Particle location

def part_loc(t):
    x = v*t
    if np.shape(x) == ():
        return np.array((x, 0))
    else:
        a = np.zeros((len(x), 2), float)
        a[:, 0] = x
        return a

# ====================================================================================================
# Field at time t 

def field(t, M):
    
    xp, yp = np.array(M) - part_loc(t)
    
    r2 = xp**2 + yp**2
    e = Q/r2
    return np.array((xp*e, yp*e))

# ====================================================================================================
# Relativist field at time t 

def rel_field(t, M):
    
    def f(tau):
        v = M - part_loc(tau)
        d2 = v[..., 0]**2 + v[..., 1]**2
        return c**2*(t-tau)**2 - d2
    
    tau = solve(f, t - 10, t)
    
    return field(tau, M)

    
    xp, yp = np.array(M) - part_loc(tau)
    
    r2 = xp**2 + yp**2
    e = Q/r2
    return np.array((xp*e, yp*e))



def traj(t0, t1, x0=0, y0=5, count=100, sub_steps=10):
    
    for the_field in [field, rel_field]: 
        M    = np.empty((count+1, 2), float)
        M[0] = (x0, y0)
        vs = np.empty((count+1, 2), float)
        vs[0] = (0, 0)
        
        dt  = (t1 - t0)/(count-1)
        dt_ = dt/sub_steps
        for i in range(count):
            loc = M[i]
            v   = vs[i]
            t   = dt*i
            for j in range(sub_steps):
                f       = the_field(t+j*dt_, loc)
                new_v   = v + f*dt_
                loc    += (v + new_v)/2*dt_
                v       = new_v
                
            M[i+1]  = loc
            vs[i+1] = v
            
        plt.plot(M[:, 0], M[:, 1])
        
        
    p = part_loc(np.linspace(t0, t1, count))
    plt.plot(p[:, 0], p[:, 1], 'o')

    plt.show()
    
traj(-5, 5, x0=0, y0=3)
        
    


    
    


    
    
    