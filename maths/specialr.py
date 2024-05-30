#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Nov 10 11:50:13 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Special relativity module.

Events are stored in 4-vectors in the order [x, y, z, t]
- events[:3] : vector
- events[3]  : time

A simple projection is proposed in this module using one parameter zt_angle:
- x and y are unchanged
- z and t are rotated perpendidulary to xy plane with an angle of zt_angle
"""

import numpy as np
from geonodes.maths import field

EVENT_X = 0
EVENT_Y = 1
EVENT_Z = 2
EVENT_T = 3

EVENT_V  = slice(EVENT_X, EVENT_Z + 1)
EVENT_XY = slice(EVENT_X, EVENT_Y + 1)
EVENT_YZ = slice(EVENT_Y, EVENT_Z + 1)

# ====================================================================================================
# Utility which convert vectors to events

# ----------------------------------------------------------------------------------------------------
# Events from spatial coordinates and additional time dimension

def events_at_time(points, t=0.):
    """ Build events from points at time t.

    Arguments
    ---------
    - points (array of vectors) : spatial coordinates
    - t (float or array of floats = 0) : time coordinate

    Returns
    -------
    - Array of events
    """

    if np.shape(points) == (3,):
        events = np.empty(4, float)
        events[EVENT_V] = points
        events[EVENT_T] = t
    else:
        events = np.empty((len(points), 4), float)
        events[:, EVENT_V] = points
        events[:, EVENT_T] = t

    return events

# ----------------------------------------------------------------------------------------------------
# Events where time is given by z coordinate

def events_at_z(points, z=0.):
    """ Build events using z coordinate as time

    Arguments
    ---------
    - points (array of vectors) : spatial coordinates
    - z (array of floats = 0.) : z coordinate

    Returns
    -------
    - Array of events
    """

    if np.shape(points) == (3,):
        events = np.empty(4, float)
        events[EVENT_XY] = points[:2]
        events[EVENT_Z]  = z
        events[EVENT_T]  = points[2]
    else:
        events = np.empty((len(points), 4), float)
        events[:, EVENT_XY] = points[:, :2]
        events[:, EVENT_Z]  = z
        events[:, EVENT_T]  = points[:, 2]

    return events





# ====================================================================================================
# Simple projection

def events_projection(events, zt_angle=0):
    """ Events projection into 3D.

    The simple projection doesn't change x and y coordinates while rotating z and t axis.

    Arguments
    ---------
    - events (array of events) : the events to project
    - zt_angle (float = 0) : rotation angle between z and t axis

    Returns
    -------
    - array of vectors
    """

    if zt_angle == 0:
        return events[:, EVENT_V]

    ca = np.cos(zt_angle)
    sa = np.sin(zt_angle)

    if np.shape(events) == (4,):
        return np.array([events[EVENT_X], events[EVENT_Y], events[EVENT_Z]*ca - events[EVENT_T]*sa])

    points = np.empty((len(events), 3), float)
    points[:, :2] = events[:, EVENT_XY]
    points[:, 2]  = ca*events[:, EVENT_T] - sa*events[:, EVENT_T]

    return points

# =============================================================================================================================
# Utility : computes beta and transformation matrix from speed

def get_beta_transformation(speed):
    """ Compute beta and spatial transformation matrix from a speed vector

    The argument 'speed' is a vector representing the speed. Its norm must be less than 1.
    The function computes a spatial transformation matrix which aligns x axis along the speed.
    It returns the beta value and the transformation matrix

    Arguments
    ---------
    - speed (vector) : speed vector with a norm less than 1.

    Returns
    -------
    - float, array(3, 3) : beta and the transformation matrix
    """

    # ----- If speed is a float, it is (beta, 0, 0)

    if np.shape(speed) == ():
        return np.clip(speed, -.99, .99), np.identity(3)

    # ----- Speed is a vector

    # Norm is beta
    speed = np.array(speed)
    beta  = np.linalg.norm(speed)

    # Norm is null,
    if beta < 1e-6:
        return 0., np.identity(3)

    # Unary vector along the speed
    e0 = speed/beta
    e1 = np.cross((0, 1, 0), e0)
    norm = np.linalg.norm(e1)
    if norm < 1e-6:
        transf = np.array([(0., 1., 0.), (0., 0., 1.), (1., 0., 0.)])
    else:
        e1 /= norm
        transf = np.array([e0, e1, np.cross(e0, e1)])

    return np.clip(beta, -.99, .99), transf

# =============================================================================================================================
# Lorentz Transformation

def lorentz_transformation(events, speed=0., event0=(0., 0., 0., 0.), event1=(0., 0., 0., 0.)):
    """ Lorentz transformation

    This function implements the Lorentz transformation with a speed having an arbitrary direction, not
    necessarily along the x axis.

    The origins of the two frames do not necessarily match. The event0 and event1 arguments refer to the same
    event, with event0 being the coordinates in R when event1 gives the coordinates in R'.

    TL(event0) = event1

    Without common event
    --------------------

    The base algorithm computes the transformation with event0 = event1 = (0, 0, 0, 0):

    - Step 1

      Spatial rotation : a spatial rotation is performed to express the spatial coordinates
      in a frame where the speed is along the x axis.

    - Step 2

      Lorentz transformation : the standard transformation is applied on the rotated coordinates :

      - t' = g(t - b.x)
      - x' = g(x - b.t)
      - y' = y
      - z' = z

    - Step 3

      Inverse spatial rotation : the inverse spatial rotation is performed to recover the inital axis.

    With common event
    -----------------

    To take event0 and event1 arguments into account the complementary operations are performed:

    - In R : before step 1, event0 is subtracted to events in order to work on a frame R the origin of which is event0.
    - In R' : after step 3, event0 is unchanged, its coordinates are (0, 0, 0, 0). We add event1 to get the proper coordinates.


    Arguments
    ---------
    - events : array of events (t, x, y, z)
    - speed (vector or float = 0.) : speed of the secondary frame
    - event0 (event = (0, 0, 0, 0) : the coordinates of an event E in the initial frame
    - event1 (event = (0, 0, 0, 0) : the coordinates of the event E in the secondary frame (lorentz_transormation(event0) = event1

    Returns
    -------
    - array of events
    """

    # -----------------------------------------------------------------------------------------------------------------------------
    # Preparation

    # ----- Events is a single event

    if np.shape(events) == (4,):
        return lorentz_transformation(np.reshape(events, (1, 4)), speed=speed, event0=event0, event1=event1)[0]

    if not isinstance(events, np.ndarray):
        events = np.array(events)

    # ----- Beta and transformation matrix

    beta, transf = get_beta_transformation(speed)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Transformation

    # ----- Step 1 : spatial rotation to express the event coordinates in a frame where the speed is along x axis

    rotated = np.einsum('ij, ...j', transf, (events - event0)[:, EVENT_V])
    x = rotated[:, 0]
    t = events[:, EVENT_T]

    # ----- Step 2 : Lorentz Transformation

    gamma = 1/np.sqrt(1 - beta*beta)

    t_ = gamma*(t - beta*x)
    x_ = gamma*(x - beta*t)

    events[:, EVENT_T]  = t_
    events[:, EVENT_X]  = x_
    events[:, EVENT_YZ] = rotated[:, 1:]

    # ----- Step 3 : inverse spatial rotation

    events[:, EVENT_V] = np.einsum('ij, ...j', np.linalg.inv(transf), events[:, EVENT_V])

    # ----- Returns the result with a shift in order that lorentz_transformation(event0) = event1

    return events + event1

# =============================================================================================================================
# Time snapshot

def snapshot(moving_points, time=0., speed=0., event0=(0, 0, 0, 0), event1=(0, 0, 0, 0)):
    """ Compute the points given in a frame R' in the frame R at time snapshot_time

    The function returns two arrays:
    - points : the point locations in frame R
    - t' : the proper time of each point in frame R'

    The arguments and results match the following egality:
    - lorentz_transformation( (t, points) ) = (t', moving_points)

    Once the spatial rotation has been performed, the equations to solve are:
    - t' = g(t - bx)
    - x' = g(x - bt)

    Where x' = moving_points and t = time are given and x and t' are the unknown.
    - x = x'/g + bt
    - t' = g(t - b(x'/g + bt)) = g(t - tb^2 - bx'/g) = t/g - bx'

    Arguments
    ---------
    - moving_points (array of vectors) : points coordinates in the frame R'
    - time (float = 0.) : snapshot time in frame R
    - speed (vector or float = 0.) : speed of the secondary frame
    - event0 (event = (0, 0, 0, 0) : the coordinates of an event E in the initial frame
    - event1 (event = (0, 0, 0, 0) : the coordinates of the event E in the secondary frame (lorentz_transormation(event0) = event1

    Returns
    -------
    - Array of vectors and array of floats : points coordinates and proper time
    """

    # -----------------------------------------------------------------------------------------------------------------------------
    # Preparation

    # ----- Points is a single point

    if np.shape(moving_points) == (3,):
        return snapshot(np.reshape(moving_points, (1, 3)), time=time, speed=speed, event0=event0, event1=event1)[0]

    # ----- Beta and transformation matrix

    beta, transf = get_beta_transformation(speed)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Transformation
    #
    # Since the moving_points are given in the frame R', the transformation is the inverse : we must change the sign of beta

    beta = -beta
    alpha = np.sqrt(1 - beta*beta)

    # ----- Step 1 : spatial rotation to express the event coordinates in a frame where the speed is along x axis

    rotated = np.einsum('ij, ...j', transf, moving_points - event1[1:])
    x_ = rotated[:, 0]

    # ----- Step 2 : We compute the snapshot points and the proper time in this rotated frame

    t = time - event0[EVENT_T]
    x = x_*alpha + beta*t
    t_ = t*alpha - beta*x_ + event1[EVENT_T]

    rotated[:, 0] = x

    # ----- Step 3 : inverse spatial rotation

    points = np.einsum('ij, ...j', np.linalg.inv(transf), rotated) + event0[EVENT_V]

    # ----- Returns the result with a shift in order that lorentz_transformation(event0) = event1

    return points, t_

# =============================================================================================================================
# Electromagnetic field transformation

def em_transformation(E, B, speed=0.):
    """ Lorentz transformation applied to an electromagnetic field.

    Arguments
    ---------
    - E (array of vectors) : the electric field
    - B (array of vectors) : the magnetic field
    - speed (vector or float = 0.) : speed of the secondary frame

    Returns
    -------
    - a couple of array of vectors : the transformed electric and magnetic fields
    """

    # -----------------------------------------------------------------------------------------------------------------------------
    # Preparation

    # ----- Beta and transformation matrix

    beta, transf = get_beta_transformation(speed)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Transformation
    #
    # Since the moving_points are given in the frame R', the transformation is the inverse : we must change the sign of beta

    gamma = 1/np.sqrt(1 - beta*beta)

    # ----- Step 1 : spatial rotation to express the event coordinates in a frame where the speed is along x axis

    RE = np.einsum('ij, ...j', transf, E)
    RB = np.einsum('ij, ...j', transf, B)

    # ----- Step 2 : Lorentz transformation

    RE_ = np.array(RE)
    RB_ = np.array(RB)

    RE_[:, 1] = gamma*(RE[:, 1] - beta*RB[:, 2])
    RE_[:, 2] = gamma*(RE[:, 2] + beta*RB[:, 1])

    RB_[:, 1] = gamma*(RB[:, 1] + beta*RE[:, 2])
    RB_[:, 2] = gamma*(RB[:, 2] - beta*RE[:, 1])

    # ----- Step 3 : inverse spatial rotation

    E_ = np.einsum('ij, ...j', np.linalg.inv(transf), RE_)
    B_ = np.einsum('ij, ...j', np.linalg.inv(transf), RB_)

    # ----- Returns the two fields

    return E_, B_

# =============================================================================================================================
# Electromagnetic field

def electromagnetic_field(points, locations=(0., 0., 0.), charges=1, speeds=(0., 0., 0.)):
    """ The electric and magnetic fields generated by charges

    Arguments
    ---------
    - points (array of vectors) : where to compute the fields
    - locations (array of vectors) : location of the charges
    - charges (array floats) : the electric charges generating the electromagnetic field
    - speeds (array of vectors) : the speeds of the charges

    Returns
    -------
    - Array (2, n) of vectors : electric (index=0) and and magnetic (index=1) fields
    """

    # ----- One single point

    if np.shape(points) == (3,):
        return electromagnetic_field(np.reshape(points, (1, 3)), charges=charges)[:, 0]

    # -----------------------------------------------------------------------------------------------------------------------------
    # Preparation

    source = np.empty(np.size(locations) // 3, dtype=[('locations', float, (3,)), ('charges', float), ('speeds', float, (3,))])
    source['locations'] = locations
    source['charges']   = charges
    source['speeds']    = speeds

    # -----------------------------------------------------------------------------------------------------------------------------
    # Loop on the charges in the loop

    total_field = np.zeros((2, len(points), 3), float)

    events = events_at_time(points)

    # Magnetic field is null
    B_ = np.zeros((len(events), 3), float)

    for loc, q, speed in source:

        # Charge event
        charge_event = events_at_time(loc)

        # points in the frame where the charge is at rest
        events_ = lorentz_transformation(events, speed=speed, event0=charge_event)

        # Electric field
        E_, _ = field.electric_field(events_[:, EVENT_V], locations=(0., 0., 0.), charges=q)

        # Transform these two fields in the main frame

        E, B = em_transformation(E_, B_, speed=-speed)

        total_field[0] += E
        total_field[1] += B

        # we have the result

    return total_field
