#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Wed Mar  9 13:33:50 2022

@author: alain.bernard
@email: alain@ligloo.net

-----

Spatial transformations and geometry utilities

"""

import numpy as np
from numpy import pi

from geonodes import Rotation

# Zero
ZERO = 1e-6
PI   = np.pi
TAU  = 2*np.pi

# =============================================================================================================================
# Spatial operations

# -----------------------------------------------------------------------------------------------------------------------------
# Normalize vectors

def normalize(v, null=(0, 0, 1)):
    """ Return the normalized vector and the norm of a vector or an array of vectors.

    The vector can be specified as a string naming an axis : 'x', '-z', ...

    Arguments
    ---------
        - v (vector or array of vectors or str) : the vector to normalize
        - null (vector=(0, 0, 1)) : value to set to null vectors

    Returns
    -------
        - normalized vector(s), vector norm(s)
    """

    # ----- An axis string specification

    if isinstance(v, str):

        upper = v.upper()

        if upper in ['X', '+X', 'POS_X', 'I', '+I']:
            return np.array((1., 0., 0.)), 1
        elif upper in ['Y', '+Y', 'POS_Y', 'J', '+J']:
            return np.array((0., 1., 0.)), 1
        elif upper in ['Z', '+Z', 'POS_Z', 'K', '+K']:
            return np.array((0., 0., 1.)), 1

        elif upper in ['-X', 'NEG_X', '-I']:
            return np.array((-1., 0., 0.)), 1
        elif upper in ['-Y', 'NEG_Y', '-J']:
            return np.array((0., -1., 0.)), 1
        elif upper in ['-Z', 'NEG_Z', '-K']:
            return np.array((0., 0., -1.)), 1
        else:
            raise RuntimeError(f"Unknwon axis spec: '{vectors}'")

    # ----- Make sure it is an array

    if not isinstance(v, np.ndarray):
        v = np.array(v, float)

    # ----- Single vector

    if len(np.shape(v)) == 1:
        n = np.linalg.norm(v)
        if n < ZERO:
            return np.array(null, float), 0.
        else:
            return v/n, n

    # ----- Array of vectors

    n = np.linalg.norm(v, axis=-1)

    # All good

    ok = n > ZERO
    if np.sum(ok) == np.size(v)//3:
        return v/n[:, None], n

    # Some null vectors

    u = np.resize((0., 0., 1.), np.shape(v))
    u[ok] = v[ok]/n[ok, None]

    return u, n

# -----------------------------------------------------------------------------------------------------------------------------
# Axis vector : initial norm not needed

def axis_vector(v, null=(0, 0, 1)):
    """ Return the normalization of a vector or an array of vector.

    The vector can be specified as a string naming an axis : 'x', '-z', ...

    Arguments
    ---------
        - v (vector or array of vectors or str) : the vector to normalize
        - null (vector=(0, 0, 1)) : value to set to null vectors

    Returns
    -------
        - normalized vector(s)
    """

    return normalize(v, null=null)[0]

# -----------------------------------------------------------------------------------------------------------------------------
# Perpendicular plane

def get_plane(v):
    """ Get the two vectors, or array of vectors, forming the plane perpendicular to the argument.

    Arguments
    ---------
        - v (vector or array of vectors) : the vectors perpendicular to the planes

    Returns
    -------
        - couple of vectors or couple of arrays of vectors
    """

    u, n = normalize(v, null=(0, 0, 1))

    # Single vector

    if np.shape(v) == (3,):

        if n < ZERO:
            return np.array((1., 0., 0.), (0., 1., 0.))

        i, i_n = normalize(np.cross((0, 1, 0), u))
        if i_n < ZERO:
            return np.array((0., 0., 1.)), np.cross(u, (0, 0, 1))

        return i, np.cross(u, i)

    # Multiple vectors

    i, i_n = normalize(np.cross((0, 1, 0), u))
    i[i_n < ZERO] = (1, 0, 0)

    return i, np.cross(u, i)

# -----------------------------------------------------------------------------------------------------------------------------
# One perpendicular vector

def one_perp_vector(u):
    """ Returns one vector perpendicular to the argument.

    Arguments
    ---------
        - u (vector or arraay of vectors) : the vectors

    Returns
    -------
        - vector or array of vectors : vectors perpendicular to the argument
    """

    return get_plane(u)[0]

# -----------------------------------------------------------------------------------------------------------------------------
# Rotation from vectors to other ones

def rotation_to(v0, v1, perp_axis=None):
    """ Get the rotation turning one vector to another one.

    Arguments
    ---------
        - v0 (vector or array of vectors) : first vector
        - v1 (vector or array of vectors) : second vectors
        - perp_axis (vector or array of vectors = None) : an axis to use in case the two vectors are aligned

    Returns
    -------
        - Transformations : transformations rotating v0 to v1
    """

    u0, _ = normalize(v0)
    u1, _ = normalize(v1)

    perp, sn = normalize(np.cross(u0, u1))

    # ----- Single vector

    if np.shape(sn) == ():
        cs = np.dot(u0, u1)
        if abs(sn) < ZERO:
            if cs > 0 or abs(cs) < ZERO:
                return Rotation.identity()
            else:
                if perp_axis is None:
                    perp_axis = one_perp_vector(u0)
                return Rotation.from_rotvec(perp_axis * np.pi)

        ag = np.arctan2(sn, cs)
        return Rotation.from_rotvec(perp*ag)

    # ----- Multiple vectors

    sn_0 = np.abs(sn) < ZERO
    if np.sum(sn_0):
        u = u0 if np.size(u0) > np.size(u1) else u1
        if perp_axis is None:
            perp[sn_0] = one_perp_vector(u[sn_0])
        elif np.shape(perp_axis) == (3,):
            perp[sn_0] = perp_axis
        else:
            perp[sn_0] = perp_axis[sn_0]

    cs = np.einsum('...i, ...i', u0, u1)
    ag = np.arctan2(sn, cs)

    return Rotation.from_rotvec(perp*ag[:, None])

# -----------------------------------------------------------------------------------------------------------------------------
# A tracker orients axis towards a target direction.
# Another contraint is to have the up axis oriented towards the sky
# The sky direction is the normally the Z
#
# - direction  : The target direction for the axis
# - track_axis : The axis to rotate into the given direction
# - up_axis    : The up direction wich must remain oriented vertically
# - vertical   : The up axis must be rotated into the plane (target, vertical)

def tracker(direction, track_axis='+Y', up_axis=None, vertical='Z'):
    """Compute a rotation which rotates a track axis into a direction.

    The rotation is computed using a complementary axis named 'up' which
    must be oriented vertically.
    The vertical direction is Z by default and can be overriden by the argument 'vertical'.

    After rotation:
        - 'track axis' is oriented in the 'direction'.
        - 'up axis' is in the plane (direction, vertical)

    Arguments
    ---------
        - direction (vector) : the target direction for the track axis.
        - track_axis (vector='+Y') : the axis to orient along direction
        - up_axis (vector=None) : up axis to keep in the plane (direction, vertical)
        - vertical (vector='Z') : the vertical direction

    Returns
    -------
        - Transformations
    """

    # ----- Rotate track axis toward direction

    u_track = axis_vector(track_axis)
    u_dir   = axis_vector(direction)
    rot     = rotation_to(u_track, u_dir)

    # ----- No constraint on up, it is all what we need

    if up_axis is None:
        return Transformations(rotation=rot)

    # ----- We must rotate the up axis around direction in the plane containing vertical and direction

    rotated_up = rot.apply(axis_vector(up_axis))

    # ----- Vertical vector

    Z = axis_vector(vertical)

    # ----- Perpendicular to the target plane

    perp = np.cross(Z, u_dir)

    # ----- Back to the plane

    target, t_n = normalize(np.cross(u_dir, perp))

    # ----- Single vector

    if np.shape(target) == (3,):
        if t_n < ZERO:#
            return Transformations(rotation=rot)
        else:
            return Transformations(rotation=rotation_to(rotated_up, target, perp_axis=u_dir) * rot)

    # ----- Multiple vector

    if np.shape(rotated_up) == (3,):
        target[t_n < ZERO] = rotated_up
    else:
        target[t_n < ZERO] = rotated_up[t_n < ZERO]

    return Transformations(rotation=rotation_to(rotated_up, target, perp_axis=u_dir) * rot)

# -----------------------------------------------------------------------------------------------------------------------------
# Rotate points located in XY plane to a plane perpendicular to the given vector

def rotate_xy_into_plane(points, plane=None, origin=(0, 0, 0)):
    if plane is None:
        return points

    i, j = get_plane(plane)
    if np.shape(points) == (3,):
        return i*points[0] + j*points[1] + origin
    else:
        return i*points[..., 0, None] + j*points[..., 1, None] + origin

# -----------------------------------------------------------------------------------------------------------------------------
# Index of an axis

def axis_index(vector, signed=False):
    """ Return the axis index of a vector.

    If the argument 'signed' is False, the returned index is in [0, 1, 2], otherwise it is in [-3, -2, -1, 1, 2, 3].

    Arguments
    ---------
        - vector (vector or str) : an axis vector
        - signed (bool=False) : take the orientation into account

    Returns
    -------
        - Axis index
    """

    if isinstance(vector, str):

        upper = vector.upper()

        if upper in ['X', '+X', 'POS_X', 'I', '+I']:
            index = 1
        elif upper in ['Y', '+Y', 'POS_Y', 'J', '+J']:
            index = 2
        elif upper in ['Z', '+Z', 'POS_Z', 'K', '+K']:
            index = 3

        elif upper in ['-X', 'NEG_X', '-I']:
            index = -1
        elif upper in ['-Y', 'NEG_Y', '-J']:
            index = -2
        elif upper in ['-Z', 'NEG_Z', '-K']:
            index = -3
        else:
            raise RuntimeError(f"Unknwon axis spec: '{vectors}'")

    else:
        vector = np.reshape(vector, (3,))
        v = axis_vector(vector)

        index = np.argmax(v)
        if v[index] < 0:
            index = - (index + 1)
        else:
            index += 1

    if signed:
        return index
    else:
        return abs(index) - 1

# ---------------------------------------------------------------------------
# Angle with another vector

def angle_with(v0, v1):
    """ Angle between to vectors.

    Arguments
    ---------
        - v0 (vector or array of vectors) : first vector
        - v1 (vector or array of vectors) : second vector

    Returns
    -------
        - angle : the angle (mod pi) between the two vectors
    """

    return np.arccos(np.clip(np.einsum('...i, ...i', axis_vector(v0), axis_vector(v1)), -1, 1))

# =============================================================================================================================
# Transformation

class Transformations:
    def __init__(self, position=None, scale=None, rotation=None, order='xyz'):
        """ Transformations manages the 3 transformation : position, scale and rotation.

        The rotation can be either an array of eulers angles or a, instance of scipy Rotation

        Arguments
        ---------
            - position (vector or array of vectors = None) : the translation part
            - scale (vector or array of vectors = None) : the scale part
            - rotation (vector or array of vectors or Rotation = None) = the rotation part
        """

        # scale can be a float

        if scale is not None and np.shape(scale) == ():
            scale = (scale, scale, scale)

        # rotation can be array of eulers or Rotation

        if rotation is None:
            rot_shape = ()
        else:
            if isinstance(rotation, Rotation):
                if rotation.single:
                    rot_shape = (3,)
                else:
                    rot_shape = (len(rotation), 3)

            else:
                rot_shape = np.shape(rotation)
                rotation = Rotation.from_euler(order.lower(), np.reshape(rotation, (np.size(rotation)//3, 3)))

        # Global shape

        self._shape = np.broadcast_shapes(np.shape(position), np.shape(scale), rot_shape)
        self._size  = np.prod(self._shape, dtype=int)

        # We are still alove, let's init

        self.position = None if position is None else np.reshape(position, (np.size(position)//3, 3))
        self.scale    = None if scale    is None else np.reshape(scale,    (np.size(scale)   //3, 3))
        self.rotation = rotation

    def __str__(self):
        return f"<Transformations {self.shape}: position: {np.shape(self.position)[:-1]}, scale: {np.shape(self.scale)[:-1]}, rotation: ({'' if self.rotation is None else len(self.rotation)},)>"

    # =============================================================================================================================
    # Shape

    @property
    def shape(self):
        """ The shape of the Transformations.

        Returns
        -------
            - tuple : shape
        """

        return self._shape[:-1]

    @property
    def size(self):
        """ The size of the Transformations.

        Returns
        -------
            - int : Transformations size
        """

        return self._size // 3

    @property
    def single(self):
        """ A single transformation (no shape, no len).

        Returns
        -------
            - bool : True if single, False otherwise
        """

        return self._shape == (3,)

    def reshape(self, *new_shape):
        """ Change the shape of the Transformations.

        Both the following syntaxes are accepted:
            - ``` transfos.reshape(2, 3, 4) ````
            - ``` transfos.reshape((2, 3, 4)) ```

        Raises an error if the size of the shape doesn't correspond to the current size.

        Arguments
        ---------
            - ints or tuple of ints : the new shape
        """

        if len(new_shape) == 1:
            target = new_shape[0]
        else:
            target = new_shape

        if isinstance(target, list):
            target = tuple(target)
        elif not isinstance(target, tuple):
            target = (target,)

        if np.prod(target, dtype=int) != self.size:
            raise RuntimeError(f"Impossible to resize Transformations of shape {self.shape} to shape {target}")

        self._shape = target + (3,)

    # =============================================================================================================================
    # As a list of transformation

    def __len__(self):
        if self.single:
            raise TypeError(f"Single Transformations has no len()")
        else:
            return self._shape[0]

    def __getitem__(self, index):

        if self.single:
            raise TypeError(f"Single Transformations is not subscriptable")

        indices      = np.reshape(range(self.size), self.shape)[index]
        target_shape = np.shape(indices)
        indices      = indices.flatten()

        count = len(indices)
        if count == 0:
            return None

        if self.position is None:
            position = None
        elif np.size(self.position) == 3:
            position = np.reshape(self.position, (3,))
        else:
            position = self.position[indices]

        if self.scale is None:
            scale = None
        elif np.size(self.scale) == 3:
            scale = np.reshape(self.scale, (3,))
        else:
            scale = self.scale[indices]

        if self.rotation is None:
            rotation = None
        elif self.rotation.single:
            rotation = self.rotation
        else:
            rotation = self.rotation[indices]

        transfos = Transformations(position=position, scale=scale, rotation=rotation)
        transfos.reshape(target_shape)

        return transfos

    # =============================================================================================================================
    # Transformation matrices

    @property
    def scaled_matrices(self):
        size = 1 if self.shape == () else self.size

        if self.rotation is None:
            mats = Rotation.identity(size).as_matrix()

        else:
            mats = np.resize(self.rotation.as_matrix(), (self.size, 3, 3))

        if self.scale is not None:
            mats[:, :3, 0] *= self.scale[:, 0, None]
            mats[:, :3, 1] *= self.scale[:, 1, None]
            mats[:, :3, 2] *= self.scale[:, 2, None]

        return np.reshape(mats, self.shape + (3, 3))

    @scaled_matrices.setter
    def scaled_matrices(self, mats):

        size = 1 if self.shape == () else self.size
        mats = np.reshape(mats, (size, 3, 3))

        scale = np.linalg.norm(mats, axis=-1)
        self.scale = np.array(scale)

        scale[scales < ZERO] = 1
        self.rotation = Rotation.from_matrix(mats / scale[..., None])


    @property
    def tmatrices(self):

        size = 1 if self.shape == () else self.size

        tmats = np.ones((size, 4, 4), float)
        tmats[:,  3, 3]  = 0
        if self.position is None:
            tmats[:, :3, 3]  = 0
        else:
            tmats[:, :3, 3]  = self.position
        tmats[:, :3, :3] = np.reshape(self.scaled_matrices, (size, 3, 3))

        return np.reshape(tmats, self.shape + (4, 4))

    @tmatrices.setter
    def tmatrices(self, tmats):

        size = 1 if self.shape == () else self.size
        mats = np.reshape(tmats, (size, 4, 4))

        self.position        = tmats[..., :3, 3]
        self.scaled_matrices = tmats[..., :3, :3]

    # =============================================================================================================================
    # Transformation

    def __matmul__(self, other):
        return self.transform(other)

    def transform(self, v):
        """ Transform an array of vectors.

        The shape of the argument 'v' must be broadcastable with the shape of the transformations.

        Arguments
        ----------
            - v (vector or array of vectors) : the vectors to transform

        Returns
        -------
            - array of vectors :  the transformed vectors
        """

        # ----- Simple : both are linear

        if len(np.shape(v)) <= 2 and len(self._shape) <= 2:
            if self.scale is not None:
                v = v * self.scale

            if self.rotation is not None:
                v = self.rotation.apply(v)

            if self.position is not None:
                v = v + self.position

            return v

        # ----- Things are shapped, we must use a shapped transformation matrix

        v = np.append(v, np.ones(np.shape(v)[:-1] + (1,), float), axis=-1)

        v = np.einsum('...ij,...j', self.tmatrices, v)

        return np.delete(v, 3, axis=-1)
