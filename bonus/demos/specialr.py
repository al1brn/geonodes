#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Sat Nov  6 19:14:47 2021

@author: alain.bernard
@email: alain@ligloo.net

-----

Special relativity
"""

import numpy as np
from scipy.spatial.transform import Rotation

ZERO = 0.0001

# =============================================================================================================================
# Utilities

def sevt(e):
    return f"([{e[0]:.3f}, {e[1]:.3f}, {e[2]:.3f}], {e[3]:.3f})"




# ====================================================================================================
# Events
#
# Events are 4D vectors implemented as (x, y, z, ct)
#
# Speeds are 3D vectors (x, y, z) with a norm beta less than 1
#
# A frame of reference is:
# - An event O take as the origin
# - A spatial transformation matrix M
# - A speed 

# ====================================================================================================
# Speed

class Speed:
    def __init__(self, direction=(0, 0, 0), beta=None, alpha=None, gamma=None):
        nrm = np.linalg.norm(direction)
        if nrm < ZERO:
            self.direction = np.array((1, 0, 0), float)
        else:
            self.direction = np.array(direction)/nrm
            
        self.beta  = nrm if beta is None else beta
        self.alpha = np.sqrt(1 - self.beta*self.beta) if alpha is None else alpha
        self.gamma = 1/self.alpha if gamma is None else gamma
        
    def __str__(self):
        return f"<beta: {self.beta:.3f}, alpha: {self.alpha:.3f}, {self.direction}>"
    
    def __pos__(self):
        return Speed(self.direction, self.beta, self.alpha, self.gamma)
    
    def __neg__(self):
        return Speed(-self.direction, self.beta, self.alpha, self.gamma)
    
        
# ====================================================================================================
# Frame
#
# A frame is defined relatively to another one named World
# A frame has the same axis direction as the World
# The speed has an arbitrary direction, not necessarily along x axis
# The origin Event of the Frame is not necessarily (0, 0, 0, 0)

class Frame:
    """ Frame of reference.
    
    Arguments
    ---------
        - O (Event) : Origin event expressed in the main frame
        - speed (Speed) : Speed of the frame expressed in the main frame
    """
    
    def __init__(self, O=(0, 0, 0, 0), speed=Speed()):
        self.O     = np.array(O)
        self.speed = speed
            
    def __str__(self):
        return f"<Frame {sevt(self.O)}, speed: {self.speed}>"
            
    # ----------------------------------------------------------------------------------------------------
    # Transformation of an Event expressed in the World into the Frame
        
    def transform(self, e):
        
        if np.shape(e) == (4,):
            return self.transform([e])[0]
        
        # ----- Change origin
        
        e_ = e - self.O
        
        # ----- Lorentz transformation
        
        t = np.array(e_[..., 3])
        x = np.dot(e_[..., :3], self.speed.direction)
        v = e_[..., :3] - x[:, None]*self.speed.direction
        
        # t' <- gamma(t - beta.x)
        e_[..., 3] = self.speed.gamma*(t - self.speed.beta*x)
        # x' <- gamma(x - beta.t)
        x_ = self.speed.gamma*(x - self.speed.beta*t)
        # Add perpendicular vector
        e_[..., :3] = v + x_*self.speed.direction
        
        # ----- Space rotation
        
        #e_[..., :3] = np.einsum('ij, ...i', self.M, e_[..., :3])
        
        return e_
    
    # ----------------------------------------------------------------------------------------------------
    # Reverse transformation
    
    def rev_transform(self, e_):
        
        if np.shape(e_) == (4,):
            return self.rev_transform([e_])[0]
        
        # ----- Space rotation
        
        e = np.array(e_)
        #e[..., :3] = np.einsum('ij, ...i', self.M_, e[..., :3])
        
        # ----- Lorentz transformation
        
        t_ = np.array(e[..., 3])
        x_ = np.dot(e[..., :3], self.speed.direction)
        v = e[..., :3] - x_[:, None]*self.speed.direction
        
        # t <- gamma(t' + beta.x')
        e[..., 3] = self.speed.gamma*(t_ + self.speed.beta*x_)
        # x <- gamma(x' + beta.t')
        x = self.speed.gamma*(x_ + self.speed.beta*t_)
        # Add perpendicular vector
        e[..., :3] = v + x*self.speed.direction 
        
        # ----- Change origin
        
        return e + self.O
    
    # ----------------------------------------------------------------------------------------------------
    # Inverse Frame
    #
    # Transformation is : e' = L(e - O)
    # Hence:
    # e - O = L'(e')
    # e = L'(e' - L(-O)) 
    #
    # note: L(-O) = L(0 - O) = T(0) 
    
    @property
    def inverse(self):
        return Frame(O=self.transform((0, 0, 0, 0)), speed=-self.speed)
    
# ====================================================================================================
# Trajectory
#
# A trajectory defines the location and speed of a body at each time t in the World
#
# traj(t) = M, s, t_ (location, velocity, proper time)
#
# A point emits permanently rays in all directions. A time t, a mobile receiver receives a ray coming from
# an emitter. We want to know the time t - dt when the received ray was emitted.
#
# f : emitter trajectory
# g : receiver trajectory
#
# Let's name R the location of the receiver. The ray was emitted when the emitter was at location M such as
# the distance d between R and M is equal to c.dt:
#
# MR = c.dt

# ---------------------------------------------------------------------------
# Find the location of the emitter
    
def emitter_location(f, location, t, dt_max=100, prec=.001, c=1):
    
    # ----- Loops count
    
    loops = int(np.log(dt_max/prec)/np.log(2)) + 1
    
    # ----- Shape
    
    shape = np.shape(f(t))[:-1]
    dt0 = np.ones(shape, float)*dt_max
    dt1 = np.zeros(shape, float)
    
    d0 = np.linalg.norm(f(t - dt0) - location, axis=-1) - c*dt0
    d1 = np.linalg.norm(f(t - dt1) - location, axis=-1) - c*dt1
    
    for _ in range(loops):
        
        dt = (dt0 + dt1)/2
        d  = np.linalg.norm(f(t - dt) - location, axis=-1) - c*dt
        
        inds = d < 0
        dt0[inds] = dt[inds]  
        dt1[np.logical_not(inds)] = dt[np.logical_not(inds)]
        
    # ---------------------------------------------------------------------------
    # Return the result     
    
    return t - dt

# ====================================================================================================
# Body
#
# A body is an animated mesh
#
class Body:
    def __init__(self):
        pass
    
    def capture(self, spec, frames):
        
        import bpy
        from geopy.core import blender
        import geopy as gp
        
        mesh = gp.Mesh.FromObject(spec)
        n = len(frames)
        self.verts = np.zeros((n, len(mesh.points), 3), float)
        
        index = 0
        for frame in frames:
            bpy.context.scene.frame_current = frame
            mesh = gp.Mesh.FromObject(spec, evaluated=False)
            self.verts[index] = mesh.points.position
            index += 1
            
        print(self.verts)
        print(np.shape(self.verts))
        
        
        
        










        


        


# ====================================================================================================
# Main
    
if __name__ == '__main__':
    
    def frame_test():
        
        print("Frame test")

        R = Frame(O=(5, -5, 7, 10), speed=Speed(beta=.8))
        print(R)
    
        S = R.inverse
        print(S)
    
        e = (1, 2, 3, 4.)
    
        e_ = R.transform(e)
        print(f"R: {sevt(e)} --> {sevt(e_)} --> {sevt(R.rev_transform(e_))}")
        
        e = S.transform(e_)
        print(f"S: {sevt(e_)} --> {sevt(e)} --> {sevt(S.rev_transform(e))}")
        
        print()
        
    def emitter_test():
        
        rng = np.random.default_rng(0)
        n = 3
        
        locs   = np.array(([0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]), float)
        speeds = np.array(([.5, 0, 0], [.5, 0, 0], [.5, 0, 0], [.5, 0, 0]), float)
        
        def f(t):
            if np.shape(t) == ():
                return locs + speeds*t
            else:
                return locs + speeds*t[:, None]
            
        location = (1, 1, 1)
        t0 = 10
        
        t = emitter_location(f, location, t0)
        
        print("Emitter test")
        print("t", t)
        d = np.linalg.norm(f(t) - location, axis=-1) - (t0 - t)
        print("precision", d)
        
        
    #frame_test()
    
    emitter_test()
    
    
        
        
            







def event(location, time):
    
    shape = arrays_shape(location, time, (3,)) + (4,)
        
    e = np.zeros(shape, float)
    if np.shape(location) == ():
        e[..., 0] = location
    else:
        e[..., :3] = location
    e[..., 3] = time
    
    return e






def str_v(v, space=""):
    s = space + "["
    
    if np.shape(v) == ():
        return f"{space}{v:6.2f}"

    if len(np.shape(v)) > 1:
        if len(v) == 1:
            s += str_v(v[0], "")
        else:
            for vv in v:
                s += "\n" + str_v(vv, space + "    ")
    else:
        for x in v:
            s += f" {x:6.2f}"
            
    return s + "]"

def str_e(e, only_x=False):
    if only_x:
        return f"({e[0]:6.2f} ct={e[3]:6.2f})"
    else:
        return f"({str_v(e[:3])} ct={e[3]:6.2f})"
    
# ---------------------------------------------------------------------------
# Dicchotomy solver    
    
def dichotomy(f, target=0, start=0, prec=0.0001, v_min=None, v_max=None, debug=None):
    
    shape = np.shape(target)
    size  = np.size(target)
    
    if np.size(start) > size:
        shape = np.shape(start)
        size  = np.size(start)
        
    v0 = f(start)
    if np.size(v0) > size:
        shape = np.shape(v0)
        size  = np.size(v0)
        
    single = shape == ()
    if single:
        shape = (1,)
        
    # ----- The target
        
    vt = np.empty(shape, float)
    vt[:] = target
    
    v1 = np.array(v0)
    
    # ----- Lowest limit
        
    if v_min is None:
        t0 = np.empty(shape, float)
        t0[:] = start
        
        e = 1
        for i in range(30):
            inds = np.where(v0 > vt)[0]
            if len(inds) == 0:
                break
            t0[inds] -= e
            e *= 2
            v0 = f(t0)
    else:
        t0 = np.empty(shape, float)
        t0[:] = v_min
        
    # ----- Highest limit
        
    if v_max is None:
        t1 = np.empty(shape, float)
        t1[:] = start
        
        e = 1
        for i in range(30):
            inds = np.where(v1 < vt)[0]
            if len(inds) == 0:
                break
            t1[inds] += e
            e *= 2
            v1 = f(t1)
    else:
        t1 = np.empty(shape, float)
        t1[:] = v_max
        
    # ---------------------------------------------------------------------------
    # Dichotomy loop
    
    max_loops = 40
    loops = max_loops
    
    for i in range(max_loops):
        
        t = (t0 + t1)/2
        
        v = f(t)
        
        if len(np.where(abs(v - vt) > prec)[0]) == 0:
            loops = i+1
            break
        
        inds = np.where(v < vt)
        t0[inds] = t[inds]
        
        
        inds = np.where(v > vt)
        t1[inds] = t[inds]
        

    if debug is not None:
        print(f"Dichotomy {debug}: {loops:2d}")
        
    # ---------------------------------------------------------------------------
    # Return the result        
        
    if single:
        return t[0]
    else:
        return t    
    
# ---------------------------------------------------------------------------
# Utility which shapes two arrays into the same global shape

def arrays_shape(a1, a2, item1=(), item2=()):
    
    if len(np.shape(a1)) <= len(item1):
        shape1 = ()
    else:
        shape1 = np.shape(a1)[:len(np.shape(a1))-len(item1)]

    if len(np.shape(a2)) <= len(item2):
        shape2 = ()
    else:
        shape2 = np.shape(a2)[:len(np.shape(a2))-len(item2)]
        
    return shape2 if len(shape2) > len(shape1) else shape1
    
    
# ---------------------------------------------------------------------------
# Initialize an event, or an array of events from location and time
#
# An event if is 4D vector. For consistency, time is place at the fourth location:
#
# (ct, x, y, z) = np.array((x, y, z, ct))
#
# If location is a single evalue, it is interpreted as (x, 0, 0)

def event(location, time):
    
    shape = arrays_shape(location, time, (3,)) + (4,)
        
    e = np.zeros(shape, float)
    if np.shape(location) == ():
        e[..., 0] = location
    else:
        e[..., :3] = location
    e[..., 3] = time
    
    return e

# ---------------------------------------------------------------------------
# Space-time interval
    
def st_interval(e0, e1):
    d = np.array(e1) - np.array(e0)
    d *= d
    
    return np.sum(d[:3], axis=-1) - d[3]

# ---------------------------------------------------------------------------
# Rotation matrix around an axis

def rot_matrix(angle, axis='Z'):
    
    ca = np.cos(angle)
    sa = np.sin(angle)
    
    if axis.upper() == 'X':
        return np.array((
            (1,  0,   0),
            (0,  ca, sa),
            (0, -sa, ca)
            ))
    
    elif axis.upper() == 'Y':
        return np.array((
            ( ca, 0, -sa),
            (  0, 1,   0),
            ( sa, 0,  ca)
            ))
    
    return np.array((
        ( ca, sa, 0),
        (-sa, ca, 0),
        (  0,  0, 1)
        ))


# ---------------------------------------------------------------------------
# Rotation matrix to align an axis along a direction

def orient_matrix(vector, axis='Z'):
    
    # ----- Normalize the direction
    
    v = np.array(vector) / np.linalg.norm(vector)

    # ----- Spherical components (theta, phi)
    
    theta = np.arctan2(v[1], v[0])
    nh    = np.linalg.norm(v[:2])
    phi   = np.arctan2(v[2], nh)   # nh >= 0 --> phi between -pi/2 and pi/2
    
    # ----- Align along the required axis
    
    if axis.upper() == 'X':
        return np.matmul(
                rot_matrix(-phi,  axis='Y'),
                rot_matrix(theta, axis='Z')
                )
    
    elif axis.upper() == 'Y':
        return np.matmul(
                rot_matrix(phi,             axis='X'),
                rot_matrix(theta - np.pi/2, axis='Z')
                )

    return np.matmul(
                rot_matrix(np.pi/2 - phi, axis='Y'),
                rot_matrix(theta,         axis='Z')
                )

# ---------------------------------------------------------------------------
# Some tests

def rm_test():
    for axis in ['X', 'Y', 'Z']:
        for ag in [30, 120]:
            for u in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                print(f"axis: {axis}, angle: {ag:3d}°: u {str_v(u)}", str_v(np.dot(u, rot_matrix(np.radians(ag), axis))))
        print()
        
def om_test():
    
    for axis, a in zip(['X', 'Y', 'Z'], [(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
        for theta in np.linspace(0, 2*np.pi, 12, False):
            for phi in np.linspace(-np.pi/2, np.pi/2, 6):
                v = (np.cos(phi)*np.cos(theta), np.cos(phi)*np.sin(theta), np.sin(phi))
                m = orient_matrix(v, axis)
                b = np.dot(a, m)
                diff = np.linalg.norm(v - b)
                
                thd = np.degrees(theta)
                phd = np.degrees(phi)
                print(f"axis={axis}: theta: {thd:4.0f}°, phi: {phd:4.0f}° {str_v(v)} --> {str_v(b)} {diff:.4f}")
        print()
    
# ---------------------------------------------------------------------------
# Lorentz transformation
#
# Standard transformation generally uses:
# - (0, 0, 0, 0) for both origin events
# - Speed along x axis
#
# Compute the general transformation with no constraint
#
# Global event0 is transformed in local event1.
#
# e' - e1 = L(e - e0)
#
# Pivot event p is such as :
#
# p - e1 = L(p - p0)
#
# p(x, t) is solution of
#
# x = x1 + g(x - x0 - b(t - t0)) = x1 - g(x0 - bt0) + g(x - bt)
# t = t1 + g(t - t0 - b(x - x0)) = t1 - g(t0 - bx0) + g(t - bx)
#
# Which solves in:
#
# x = (x0 + x1)/2 + 1/2.bg/(1-g)(t0 - t1)
# t = (t0 + t1)/2 + 1/2.bg/(1-g)(x0 - x1)



class Lorentz():
    
    def __init__(self, speed=0, event0=0, event1=0):
        
        if np.shape(speed) == ():
            self.speed = np.array((speed, 0., 0.))
        else:
            self.speed = np.empty(3, float)
            self.speed[:] = speed
        
        self.beta = np.linalg.norm(self.speed)
        if self.beta >= .99999999:
            raise RuntimeError(f"Special relativity error: speed can't be higher than light velocity: {speed}")
            
        self.alpha = np.sqrt(1 - self.beta*self.beta)
        self.gamma = 1/self.alpha
        
        self.event0 = np.empty(4, float)
        self.event1 = np.empty(4, float)
        
        self.event0[:] = event0
        self.event1[:] = event1
        
        # ---------------------------------------------------------------------------
        # Spacial rotation to orient x along the speed
        
        if self.beta < 1e-6:
            self.x_to_speed  = np.identity(3)
            self.x_to_speed_ = np.identity(3)
        else:
            self.x_to_speed  = orient_matrix(self.speed, axis='X')
            self.x_to_speed_ = np.linalg.inv(self.x_to_speed)
        
        mat  = np.identity(4)
        mat[:3, :3] = self.x_to_speed
        mat_ = np.linalg.inv(mat)
    
        # ---------------------------------------------------------------------------
        # Combine with standard Lorentz transformation
        
        # mat  : X --> speed
        # mat_ : speed --> X 
        
        self.mat = np.matmul(mat_, np.matmul(np.array((
            (           self.gamma, 0, 0, -self.gamma*self.beta),
            (                    0, 1, 0,                     0),
            (                    0, 0, 1,                     0),
            (-self.gamma*self.beta, 0, 0,            self.gamma)
            )), mat))
        
        # And inverse transformation
        
        self.mat_ = np.linalg.inv(self.mat)
        
    def __repr__(self):
        s = f"<Lorentz transformation: beta= {self.beta:.3f}, gamma= {self.gamma:.2f}"
        s += f"\n   event0: {str_e(self.event0)}"
        s += f"\n   event1: {str_e(self.event1)}"
        return s + "\n>"
    
      
    # ---------------------------------------------------------------------------
    # Transformation
    
    def raw_transformation(self, e, inv=False):
        if inv:
            return np.dot(e, self.mat_)
        else:
            return np.dot(e, self.mat)
        
    def __call__(self, e, inv=False):
        if inv:
            return self.event0 + np.dot(e - self.event1, self.mat_)
        else:
            return self.event1 + np.dot(e - self.event0, self.mat)
        
    def inverse(self):
        
        lz = Lorentz()
        
        lz.mat    = np.array(self.mat_)
        lz.mat_   = np.array(self.mat)
        lz.beta   = self.beta
        lz.alpha  = self.alpha
        lz.gamma  = self.gamma
        lz.event0 = np.array(self.event1)
        lz.event1 = np.array(self.event0)
        
        return lz
    
    # ---------------------------------------------------------------------------
    # At global time, we want to known where a location point is globally located
    #
    # - global_times (t) : global times when the question is asked
    # - local_locs   (x'): local locations we search the global location of
    #
    # Lorentz transformation gives:
    # - (x', t') = L(x, t)
    # where t and x' are the parameters and x, t' are the unknowns
    #
    # Resolution with standard Lorentz transformation
    # -----------------------------------------------
    #
    # x' = g(x - b.t)  ==> x  = x'/g + b.t
    # t' = g(t - b.x)  ==> t' = g(t - b.x'/g - b^2.t) = -b.x' + t/g
    #
    # Hence:
    # - x  = x'/g + b.t
    # - t' = -b.x' + t/g 
    #
    # Resolution with different origins
    # ------------------------------------------
    #
    # Same by replacing formalley each value by v - v0 and v' - v1
    #
    # Resolution with speed in any direction
    # --------------------------------------
    #
    # e' = R.L.R_.e
    #
    # Which gives:
    #
    # R_.e' = L.R_.e
    #
    # Hence the previsous equations apply with steps before and after:
    #
    # BEFORE
    # - Rotation R_ on local location
    #
    # RESOLUTION
    #
    # AFTER
    # - Rotation R on global location
    #
    

    def sim_location(self, global_times, local_points):
        
        # ---------------------------------------------------------------------------
        # Shape the input into numpy arrays
        
        if np.shape(local_points) == ():
            locs = np.array((local_points, 0, 0), float)
        else:
            locs = np.array(local_points)
            
        shape = arrays_shape(locs, global_times, (3,))
        if shape == (): shape = (1,)
        
        l_loc = np.empty(shape + (3,), float)
        l_loc[:] = locs
        l_loc -= self.event1[:3]
        
        g_t = np.empty(shape, float)
        g_t[:] = global_times
        g_t -= self.event0[3]
        
        # ---------------------------------------------------------------------------
        # Step before = inverse rotation of local points
        
        l_loc = np.matmul(l_loc, self.x_to_speed_)
        
        #print("l_loc", str_v(l_loc))
        
        # ---------------------------------------------------------------------------
        # General resolution
        # - x  = x'/g + b.t
        # - t' = t/g - b.x'
        # Change only x
        
        g_loc = np.array(l_loc)
        g_loc[..., 0] = l_loc[..., 0]*self.alpha + self.beta*g_t
        l_t           = g_t*self.alpha           - self.beta*l_loc[..., 0]
        
        # ---------------------------------------------------------------------------
        # Step after = rotation of global points
        
        g_loc = np.matmul(g_loc, self.x_to_speed)
        
        # ---------------------------------------------------------------------------
        # Done without forgetting takes the origin into account
        
        return g_loc + self.event0[:3], l_t + self.event1[3]
        
        
    # ---------------------------------------------------------------------------
    # Twins story
    # 
    # Tells the twins story
    
    @staticmethod
    def twins(beta=.8, distance=8):
        
        # ----- Journey Lorentz transformation
        
        lz = Lorentz(beta)
        e0 = event(0, 0)
        duration = distance/beta
        e1 = event(distance, duration)
        e2 = event(0, 2*duration)
        
        f0 = lz(e0)
        f1 = lz(e1)
        
        # ----- At U-turn event, where is the earth for the Traveler ?
        
        # Traveler Lorentz transformation
        
        lz_ = lz.inverse()
        
        # Earth is at location 0 in the earth frame, with proper time age
        x, age   = lz_.sim_location(f1[3], 0)
        
        # ----- The transformation for the way back
        # the e1 / f1 is chosen as the origin for the frame
        
        wb = Lorentz(-beta, event0=e1, event1=f1)
        
        # We compute the arrival event for the travaler
        
        f2 = wb(e2)
        
        # ----- Let's write the full story
        
        print("Journey")
        print("-------")
        print("    start event : ", str_e(e0, True), str_e(f0, True))
        print("    U-turn event: ", str_e(e1, True), str_e(f1, True))
        print("    Earth location for traveler:", f"{x[0]:6.2f}")
        print("    Earth twin age for traveler:", f"{age:6.2f}")
        print()
        print("Way back")
        print("--------")
        print("    U-turn event :", str_e(e1, True), str_e(wb(e1), True))
        print("    Arrival event:", str_e(e2, True), str_e(f2, True))
        print()
        print("Earth twin age:", f"{e2[3]:6.2f}")
        print("Traveler age  :", f"{f2[3]:6.2f}")
        print()
        
    # ---------------------------------------------------------------------------
    # Random speeds
    
    @staticmethod
    def rand_speed(count=10, norm=None, seed=None):
        
        if seed is not None:
            np.random.seed(seed)
            
        if norm is None:
            nspeed = np.random.uniform(0, .999, (count, 1))
        else:
            nspeed = np.empty((count, 1), float)
            nspeed[:] = norm
            
            
        speeds = np.random.uniform(-1, 1, (count, 3))
        ns = np.linalg.norm(speeds, axis=-1)
        speeds = speeds / np.expand_dims(ns, axis=-1)
        speeds *= nspeed
        
        return speeds
    
    # ---------------------------------------------------------------------------
    # Test
    
    @staticmethod
    def tests(count=100, seed=0):
        
        np.random.seed(0)
        
        speeds = Lorentz.rand_speed(count)
        evs0   = np.random.uniform(-10, 10, (count, 4))
        evs1   = np.random.uniform(-10, 10, (count, 4))
        es     = np.random.uniform(-10, 10, (100, 4))
        
        # Inverse test
        
        error = 0.
        for i in range(count):
            L = Lorentz(speeds[i], evs0[i], evs1[i])
            les = L(es)
            bes = L(les, True)
            error += np.linalg.norm(bes-es)

        print("Transformation and inv transformation")
        print(f"Error after {count} tests: {error:.5f}\n")
            
        def test_simloc(L, count=10):
            np.random.seed(0)
            locs = np.random.uniform(-10, 10, (count, 3))
            tims = np.random.uniform(-10, 10, count)
            x, tp = L.sim_location(tims, locs)
            
            e = event(locs, tp)
            c = event(x, tims)
            t = L(e, inv=True)
            return np.linalg.norm(c-t)
                
            
        error= 0.
        for i in range(count):
            error += test_simloc(Lorentz(speeds[i], evs0[i], evs1[i]))
            
        print("Sim_location test")
        print(f"Error after {count} tests: {error:.5f}\n")
            

        
# ---------------------------------------------------------------------------
# Add two speeds
# One is expressed in the ref frame of the other
#
# Let's consider a time dt in ref 0
# Speed s1 ins ref 0 means that during dt, location with change of s1.dt
# Two events : (0, 0) --> (s1.dt, dt)
# These two events are transformed 
# - (0, 0)      --> (0, 0)
# - (s1.dt, dt) --> (g.s1.dt + g.b.dt, g.b.s1.dt + g.dt)
#
# Speed is : s = g.s1.dt + g.b.

def speeds_add(speed0, speed1):
    #if np.size(speed0) > np.size(speed1):
    #    shape = np.shape(speed0)
    #else:
    #    shape = np.shape(speed1)
        
    #if shape == ():
    #    shape = (3,)
        
    shape = arrays_shape(speed0, speed1, (3,), (3,)) + (3,)
        
    s0 = np.zeros(shape, float)
    s1 = np.zeros(shape, float)
    
    if np.shape(speed0) == ():
        s0[0] = speed0
    else:
        s0[:] = speed0

    if np.shape(speed1) == ():
        s1[0] = speed1
    else:
        s1[:] = speed1
        
    # ---------------------------------------------------------------------------
    # Motion in the frame moving at speed 0 during dt = 1
    
    e = event(s1, 1)
    
    # ---------------------------------------------------------------------------
    # Referentiel frame 0
    
    f = Lorentz(speed=s0)(e, inv=True)
    
    return f[:3]/f[3]


# ---------------------------------------------------------------------------
# Solid

class Solid():
    
    def __init__(self, location=0, speed=0, omega=None, rot_axis=(0, 1, 0)):
        
        self.lorentz = Lorentz(speed, event0=event(location, 0))
        
        self.omega    = omega
        self.rot_axis = rot_axis
        
    # ---------------------------------------------------------------------------
    # Origin location
    
    def origin(self, t):
        return self.lorentz.event0[:3] + self.lorentz.speed*t
    
    # ---------------------------------------------------------------------------
    # Origin speed
    
    @property
    def speed(self):
        return self.lorentz.speed
    
    # ---------------------------------------------------------------------------
    # Global speed of pts with a local speed
    #
    # We consider points at origin. After a proper time tau, they will be located
    # at (v.tau, tau)
    # Transforming this event will give the speed
    # tau can be chosen to value 1
    #
    # Raw transformation is used since we don't need the origin events event0 and event1
    
    def global_speed(self, speeds):
        e = self.lorentz.raw_transformation(event(speeds, 1), inv=True)
        return e[..., :3]/np.expand_dims(e[..., 3], axis=-1)
    
    # ---------------------------------------------------------------------------
    # Rotation property
    
    @property
    def rot_axis(self):
        return self.rot_axis_
    
    @rot_axis.setter
    def rot_axis(self, value):
        self.rot_axis_    = np.empty(3, float)
        self.rot_axis_[:] = value
        self.rot_axis_    = self.rot_axis_ / np.linalg.norm(self.rot_axis_) 
        self.rot_matrix   = orient_matrix(self.rot_axis_, axis='Z')
        self.rot_matrix_  = np.linalg.inv(self.rot_matrix)
        
    # ---------------------------------------------------------------------------
    # If rotation exists, compute locations and speeds at given proper times
        
    def rotation(self, tau, locs):
        
        # ---------------------------------------------------------------------------
        # Shape the arrays
        
        shape   = arrays_shape(locs, tau, (3,))
        
        taus    = np.zeros(shape, float)
        taus[:] = tau
        
        lcs     = np.zeros(shape+(3,), float)
        lcs[:]  = locs
        
        # ---------------------------------------------------------------------------
        # No rotation : nothing to rotate
        
        if self.omega is None:
            return lcs, np.zeros(shape + (3,), float)
        
        # ---------------------------------------------------------------------------
        # Rotation
        
        m    = np.zeros(shape + (3, 3), float)
        m[:] = np.identity(3)
        
        ag   = self.omega*taus
        
        ca   = np.cos(ag)
        sa   = np.sin(ag)
        
        m[..., 0, 0] =  ca
        m[..., 1, 1] =  ca
        m[..., 0, 1] =  sa
        m[..., 1, 0] = -sa
        
        # ----- Computation
        
        pts = np.einsum('...ij,...i', # Einsum to rotate locations
              np.matmul(self.rot_matrix_, np.matmul(m, self.rot_matrix)),
              lcs)

        speeds = np.cross(self.omega*self.rot_axis, locs)
        speeds = np.einsum('...ij,...i', # Einsum to rotate locations
              np.matmul(self.rot_matrix_, np.matmul(m, self.rot_matrix)),
              speeds)
        
        
        
        return pts, speeds
    
    # ---------------------------------------------------------------------------
    # Transform the solid into the observation frame
    # t is time in the observation frame (global time)
    # t can be shaped as the locations
    # locs are local locations
    
    def transform(self, t, locs):
        
        # ---------------------------------------------------------------------------
        # Let's first compute without rotation
        
        pts, taus = self.lorentz.sim_location(t, locs)
        
        # ---------------------------------------------------------------------------
        # No rotation : we have the results
        
        if self.omega is None:
            return pts, taus
        
        # ---------------------------------------------------------------------------
        # Rotation : need to compute the curvatures
        
        # ----- We have the bounds for taus
        
        tau_min = np.min(taus)
        tau_max = np.max(taus)
        
        del pts
        del taus
        
        # ----- Where is the center at time t
        
        _, tau = self.lorentz.sim_location(t, 0)
        
        # ----- Let's compute the proper time at each location
        # This proper time will change the rotation angle hencer
        # the location. The proper must be such as Lorentz transforms
        # at the global time t
        
        shape = arrays_shape(locs, t, (3,))
            
        # Let's prepare the rotation matrix used in the loop
            
        m = np.zeros(shape + (3, 3), float)
        m[:] = np.identity(3)
        
        # ---------------------------------------------------------------------------
        # The function to solve returns the universe time of each location
        # at their proper time v_tau. 
        # The dichotomy algorithm works only on time but we also need the locations
        # at the end. The supplementary argument events is an object collecting
        # the computed transformed event.
        
        def f(v_tau, events):
            
            # ---- Rotation
            
            ag = self.omega*v_tau
            
            ca = np.cos(ag)
            sa = np.sin(ag)
            
            m[..., 0, 0] =  ca
            m[..., 1, 1] =  ca
            m[..., 0, 1] =  sa
            m[..., 1, 0] = -sa
            
            # ----- Computation
            
            events.e = self.lorentz( # Inverse Lorentz transformation
              event(                 # Event made of rotated locations
                np.einsum(           # Einsum to rotate locations
                  '...ij,...i',
                  np.matmul(self.rot_matrix_, np.matmul(m, self.rot_matrix)),
                  locs),      
                v_tau),              # Time component of the events
              inv=True)              # Inverse transformation
            
            # ----- Return the new taus
            
            return events.e[..., 3]
                
            
        # ---------------------------------------------------------------------------
        # The proper times 
        
        class Events():
            pass
        
        events = Events()
        events.e = None
        
        taus = dichotomy(lambda x: f(x, events), target=t) #, start=tau, v_min=tau_min, v_max=tau_max)
        
        # Returns the universe locations at that times
        
        return events.e[..., :3], taus
    
    # ---------------------------------------------------------------------------
    # Transform the solid as it is perceived by the observer taking into account
    # the time necessary for the light to reachthe observer.
    # Observation point 
    
    def perception(self, t, locs, origin=0):
        
        # ---------------------------------------------------------------------------
        # The arguments into the same shape
        
        shape = arrays_shape(locs, t, (3,))
        
        ts = np.zeros(shape, float)
        ts[:] = t
        lcs = np.zeros(shape + (3,), float)
        lcs[:] = locs
        
        # ---------------------------------------------------------------------------
        # At a given 'global' time w, the locations is transformed at location l
        # The distance is d.
        # The signal will reach the observer at time w + d/c
        # Hence, w is computed such as
        # d(l(w))/c = t-w
        # 
        # The function is solved by dichotomy
        
        
        def f(w):
            pts, _ = self.transform(w, lcs)
            ds = np.linalg.norm(pts - origin, axis=-1)
            return w + ds
        
        ws = dichotomy(f, target=ts, start=ts, v_max=ts, debug="Perception")
        
        return self.transform(ws, lcs)
    
    # ---------------------------------------------------------------------------
    # Doppler effect
    
    def doppler(self, tau, locs, origin=0):

        # ----- Speeds at the given proper times
        
        pts, speeds = self.rotation(tau, locs)
        
        # ----- Transform the local points and time into the global frame
        
        pts = self.lorentz(event(pts, tau), inv=True)[..., :3]

        # ----- Combine the speeds with the speed of the solid

        vs = self.global_speed(speeds)
        
        #print("speeds", str_v(speeds[1]))
        #print("vs    ", str_v(vs[1]))
        #print()
        
        
        # ----- Emissions occur at locations locs width speed vs
        # We can compute the dopller factor with the formula
        # - f = sqrt((1+u)/(1-u))
        # where us is the speed along the direction between the observation point
        # and the location
        
        O = np.zeros(3, float)
        O[:] = origin
        
        pts -= O
        
        ns = np.linalg.norm(pts, axis=-1)
        ns[ns==0] = 1.
        
        pts = pts / np.expand_dims(ns, axis=-1)
        
        # ---- Speed along the direction
        
        ux = np.einsum('...i,...i', pts, vs)
        
        # ---- Doppler effect

        return self.lorentz.gamma*(1 - ux)
   
    

def build_simple_wheel(radius=1, count=5):
    
    return radius * np.transpose(np.stack((
            np.cos(np.linspace(0, 2*np.pi, count)),
            np.sin(np.linspace(0, 2*np.pi, count)),
            np.zeros(count, float)
            )))

def build_wheel(radius=1, diam_count=10, circ_count=4, count=128):
    
    total = diam_count + circ_count

    verts   = np.zeros((total, count, 3), float)
    
    # Diameters
    
    for i, ag in enumerate(np.linspace(0, np.pi, diam_count, False)):
        verts[i] = radius * np.transpose(np.stack((
            np.linspace(-np.cos(ag), np.cos(ag), count),
            np.linspace(-np.sin(ag), np.sin(ag), count),
            np.zeros(count, float)
            )))
        
    # Circles
    
    for i, r in enumerate(np.linspace(radius/(circ_count-1), radius, circ_count)):
        verts[diam_count + i] = r * np.transpose(np.stack((
            np.cos(np.linspace(0, 2*np.pi, count)),
            np.sin(np.linspace(0, 2*np.pi, count)),
            np.zeros(count, float)
            )))
        
    return verts

def test():
    
    beta = .8
    
    solid = Solid(location=0, speed=beta, omega=-beta, rot_axis=(0, 0, 1))
    
    wheel = build_wheel()
    #wheel = build_simple_wheel(count=20)
    #wheel = np.array([[1, 0, 0]])
    count=6
    ag = np.radians(-60)
    swheel = np.transpose(np.stack((
            np.linspace(0, np.cos(ag), count),
            np.linspace(0, np.sin(ag), count),
            np.zeros(count, float)
            )))
    
    #wheel = build_simple_wheel(count=20)
    
    import matplotlib.pyplot as plt
    import matplotlib.colors as colors
    
    def plot_at(obs_t=0.):
    
        pts, taus = solid.transform(obs_t, wheel)
        
        ps, ps_t = solid.perception(obs_t, wheel)
        
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        #ax.plot(0, 1, '.w')
        #ax.plot(-2, 1, '.w')
    
        def plot(vs, color):
            if len(np.shape(vs)) > 2:
                for v in vs:
                    plot(v, color)
                return
    
            ax.plot(vs[:, 0], vs[:, 1], color)
            
        #plot(wheel, 'lightgray')
        #plot(pts, 'gray')
        plot(ps, 'gray')
        
        dop = solid.doppler(ps_t, wheel)
        
        dmn = np.min(dop)
        dmx = np.max(dop)
        
        dop = (dop - dmn)/(dmx - dmn)*.7
    
        ps = np.reshape(ps, (np.size(ps)//3, 3))
        dop = np.reshape(dop, np.size(dop))
        
        for i, pt in enumerate(ps):
            ax.plot(ps[i, 0], ps[i, 1], '.', color=colors.hsv_to_rgb((dop[i], 1, 1)))
        
        
        plt.show()
        
    for obs_t in np.linspace(-3, 3, 20):
        plot_at(obs_t)
    
#test()


