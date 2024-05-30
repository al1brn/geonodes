#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 07:37:07 2023

Blender Python Geometry module

Created on Wed Jun 29 17:03:43 2022

@author: alain.bernard
@email: alain@ligloo.net

-----

The maths for spline curve.

Implement the maths necessary to compute thje curve splines using scipy module.
"""

import numpy as np

if True:
    from geonodes import CubicSpline, BSpline, make_interp_spline, splder
else:
    from scipy.interpolate import BSpline, make_interp_spline, CubicSpline, splder


PI  = np.pi
TAU = 2*np.pi

def derivative(f, t, dt):
    return (f(t + dt) - f(t - dt))/(2*dt)

# =============================================================================================================================
# Nurbs function

class NurbsFunction:

    def __init__(self, bspline, den_bspline=None, w=None):
        self.bspline     = bspline
        self.den_bspline = den_bspline
        self.w           = w

    @classmethod
    def FromKnots(cls, knots, value, w, order):

        if w is None:
            bspline    = BSpline(knots, value, order - 1, extrapolate=False)
            den_spline = None
        else:
            wvalue = value*w[:, None] if len(np.shape(value)) == 2 else value*w

            bspline     = BSpline(knots, wvalue, order - 1, extrapolate=False)
            den_bspline = BSpline(knots, w,      order - 1, extrapolate=False)

        return NurbsFunction(bspline, den_bspline=den_bspline, w=w)

    def __call__(self, t):

        if self.den_bspline is None:
            return self.bspline(t)
        else:
            return self.bspline(t)/self.den_bspline(t)[:, None]


# =============================================================================================================================
# Root class for spline maths

class Spline:

    def __init__(self, points_count, cyclic=False, resolution=12, order=4, endpoint=False, bezier=False):
        """ Root class for math functions linked to spline types.

        Arguments
        ---------
            - points (array of vectors) : the points of the spline
            - cyclic (bool=False) : spline is cyclic
            - resolution (int=12) : Nubs and Bezier resolution
        """

        self.points_count = points_count
        self.cyclic       = cyclic
        self.resolution   = resolution

        # ----- Nurbs specific

        self.order    = order
        self.endpoint = endpoint
        self.bezier   = bezier

    # ====================================================================================================
    # Parameter

    @property
    def length(self):
        pts = self.sample_points
        return np.sum(np.linalg.norm(pts[1:] - pts[:-1], axis=-1))

    def length_func(self):
        pts = self.sample_points
        l = np.append([0], np.cumsum(np.linalg.norm(pts[1:] - pts[:-1], axis=-1)))
        return CubicSpline(np.linspace(0, 1, len(l)), l)

    # ====================================================================================================
    # Sample a value along the curve

    def sample_value(self, value):

        count = len(value)
        if count != self.points_count:
            raise RuntimeError(f"Spline sample_value needs one value per point. Expected: {self.points_count}, len('value'): {len(value)}")

        if self.cyclic:
            count += 1
            value = np.resize(value, (count,) + np.shape(value)[1:])

        return make_interp_spline(np.linspace(0, 1, count), value, k = min(count-1, 3))


# =============================================================================================================================
# Poly lines

class Poly(Spline):

    def __init__(self, points, cyclic=False):

        super().__init__(len(points), cyclic=cyclic)


        # ----- Add the first point at the end if cyclic

        count = len(points)

        if self.cyclic:
            count += 1
            points = np.resize(points, (count, 3))

        elif not isinstance(points, np.ndarray):
            points = np.array(points)

        assert(points.shape == (count, 3))

        # ----- BSpline parameters

        knots = np.arange(-1, count+1)/count
        self.bspline = BSpline(knots, points, 1, extrapolate=True)


        # ----------------------------------------------------------------------------------------------------
        # Derivative to managed angular points

        segms = points[1:] - points[:-1]

        nrms = np.linalg.norm(segms, axis=-1)
        nrms[nrms < .0001] = 1
        segms /= nrms[:, None]

        ders = np.empty_like(points)
        ders[0]    = segms[0]
        ders[-1]   = segms[-1]
        ders[1:-1] = (segms[:-1] + segms[1:])/2

        nrms = np.linalg.norm(ders, axis=-1)
        nrms[nrms < .0001] = 1
        ders /= nrms[:, None]

        self.tangent_func = make_interp_spline(np.linspace(0, 1, count), ders, k = min(count-1, 3))


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def FromFunction(cls, f, t0=0, t1=1, count=6, cyclic=False):
        return cls(f(np.linspace(t0, t1, count, endpoint=not cyclic)), cyclic=cyclic)

    # ====================================================================================================
    # Call

    def __call__(self, t):
        if self.cyclic:
            t = t % 1
        else:
            t = np.clip(t, 0, 1)

        return self.bspline(t)

    @property
    def tangent(self):

        return self.tangent_func


        return self.bspline.derivative(1)

    # ----------------------------------------------------------------------------------------------------
    # Points used in the representation

    @property
    def sample_points(self):
        return self.bspline.c

# =============================================================================================================================
# Bezier

class Bezier(Spline):

    def __init__(self, points, lefts=None, rights=None, cyclic=False, resolution=12):

        super().__init__(len(points), cyclic=cyclic, resolution=resolution)

        self.bspline = self.build_bspline(points, lefts=lefts, rights=rights)


    # ====================================================================================================
    # Compute Bezier left and right handles

    @staticmethod
    def get_handles(points, cyclic=False):

        # ----- Add the first point at the end if cyclic

        count = len(points)

        if cyclic:
            count += 1
            points = np.resize(points, (count, 3)).astype(float)

        # ----- Compute the control points

        der = np.empty((count, 3), float)
        der[1:-1] = points[2:]  - points[:-2]
        der[ 0]   = (points[ 1] - points[0])/2
        der[-1]   = (points[-1] - points[-2])/2

        nrm = np.linalg.norm(der, axis=-1)
        nrm[abs(nrm) < 0.001] = 1.
        der /= nrm[:, None]

        dists = np.linalg.norm(points[1:] - points[:-1], axis=-1)[:, None]

        # Left handles
        lefts = np.array(points)
        lefts[1:] -= der[1:]*dists/3
        lefts[0]  -= der[0]*dists[0]/3

        # Right handles
        rights = np.array(points)
        rights[:-1] += der[:-1]*dists/3
        rights[-1]  += der[-1]*dists[-1]/3

        # ----- Returns the result

        if cyclic:
            return np.array(lefts[:-1]), np.array(rights[:-1])
        else:
            return lefts, rights

    # ====================================================================================================
    # Build the BSpline

    def build_bspline(self, value, lefts=None, rights=None):

        # ----- Add the first point at the end if cyclic

        count = len(value)

        if self.cyclic:
            count += 1

            value = np.resize(value, (count,) + np.shape(value)[1:])

            if lefts is not None:
                lefts = np.resize(lefts, np.shape(value))

            if rights is not None:
                rights = np.resize(rights, np.shape(value))

        elif not isinstance(value, np.ndarray) or not value.dtype in [np.float64, float]:

            value = np.array(value).astype(float)

        assert(len(value) == count)

        is_vec = len(np.shape(value)) == 2
        if is_vec:
            vdim = np.shape(value)[-1]
        else:
            vdim = 1

        # ----- Compute the control points if not provided

        if lefts is None or rights is None:

            der = np.empty(np.shape(value), float)
            der[1:-1] = value[2:]  - value[:-2]
            der[ 0]   = (value[ 1] - value[0])/2
            der[-1]   = (value[-1] - value[-2])/2

            if is_vec:
                nrm       = np.linalg.norm(der, axis=-1)
                nrm[abs(nrm) < 0.001] = 1.
                der /= nrm[:, None]
            else:
                nrm       = np.abs(der)
                nrm[nrm < 0.001] = 1.
                der /= nrm

            if is_vec:
                dists = np.linalg.norm(value[1:] - value[:-1], axis=-1)[:, None]
            else:
                dists = np.abs(value[1:] - value[:-1])

            # Left handles

            if lefts is None:
                lefts = np.array(value)
                lefts[1:] -= der[1:]*dists/3
                lefts[0]  -= der[0]*dists[0]/3

            # Right handles

            if rights is None:
                rights = np.array(value)
                rights[:-1] += der[:-1]*dists/3
                rights[-1]  += der[-1]*dists[-1]/3

        # ----- BSpline parameters

        # Knots : 0 0 0 0  1 1 1 2 2 2 ... n-1 n-1 n-1 n n n n

        kernel = np.empty((count, 3), int)
        kernel[:] = np.arange(count)[:, None]
        knots = np.zeros(2 + count*3, int)
        knots[1:-1] = kernel.flatten()
        knots[-1] = count - 1
        knots = knots/(count-1)

        # Control points

        C = np.empty((count-1, 3) + np.shape(value)[1:], float)
        C[:, 0] = value[:-1]
        C[:, 1] = rights[:-1]
        C[:, 2] = lefts[1:]

        if is_vec:
            C = np.reshape(C, (np.size(C)//3, 3))
        else:
            C = C.flatten()

        C = np.append(C, [value[-1]], axis=0)

        # B-Spline

        return BSpline(knots, C, 3, extrapolate=False)


    # ====================================================================================================
    # Constructors

    @classmethod
    def FromFunction(cls, f, t0=0, t1=1, count=6, cyclic=False, resolution=12):

        if cyclic:
            count += 1

        dt = (t1 - t0)/(count*resolution + 1)
        t = np.linspace(t0, t1, count)

        # ----- Points

        points = f(t)

        # ----- Derivatives / 3

        ders = derivative(f, t, dt) / (3*(count-1))

        # ----- Result

        if cyclic:
            return cls(points[:-1], lefts=points[:-1] - ders[:-1], rights=points[:-1] + ders[:-1], cyclic=True, resolution=resolution)
        else:
            return cls(points, lefts=points - ders, rights=points + ders, cyclic=False, resolution=resolution)

    # ====================================================================================================
    # Call

    def __call__(self, t):
        if self.cyclic:
            t = t % 1
        else:
            t = np.clip(t, 0, 1)

        return self.bspline(t)

    @property
    def tangent(self):
        return self.bspline.derivative(1)

    # ----------------------------------------------------------------------------------------------------
    # Points used in the representation

    @property
    def sample_points(self):
        npoints = len(self.bspline.c)
        count = npoints*self.resolution if self.cyclic else (npoints - 1)*self.resolution + 1
        return self(np.linspace(0, 1, count))

    # ----------------------------------------------------------------------------------------------------
    # Sample values along the curve

    def sample_value_NO(self, value):
        return self.build_bspline(value)



# =============================================================================================================================
# Nurbs
#
# Knot vector : a list of m+1 values (0 to m) Ki where:
# - values are increasing
# - the same value can't be repeated more thant k times where k is the order of the Nurbs
#
# Control points : a list of n+1 vectors / values (0 to n) Di
#
# m = n + k
#
# Knot vectors can be classified as:
# - periodic / uniform : interval between to successive values in the knots is constant
#   ex : n=3, k=3 : knot = [0, 1, 2, 3, 4, 5, 6]
# - non periodic : k repeated values at the begining and at the end
#   ex : n=3, k=3 : knot = [0, 0, 0, 1, 2, 2, 2]
# - non uniform -> NURBS
#
# Bezier representation : simple case when
# - number of control points = order
# - a non periodic knot is considered

class Nurbs(Spline):

    def __init__(self, points, w=1, cyclic=False, resolution=12, order=4, endpoint=False, bezier=False):

        super().__init__(0 if points is None else len(points), cyclic=cyclic, resolution=resolution, order=order, endpoint=endpoint, bezier=bezier)

        self.nurbs_func = self.build_nurbs_func(points, w=w)
        return

        if False:
            self.den_bspline = None

        if points is None:
            return

        # ----- Points and weights

        if isinstance(points, np.ndarray):
            self.points = points
        else:
            self.points = np.array(points)

        self.w    = np.empty(len(points), float)
        self.w[:] = w

        # ----- B-Spline parameters

        n = len(points)
        k = self.order

        pts = self.points
        w   = self.w

        if self.cyclic:

            nadd = self.order
            npts = len(points) + 2*nadd

            pts = np.zeros((npts, 3), float)
            w   = np.zeros(npts, float)

            pts[:nadd]      = self.points[-nadd:]
            pts[nadd:-nadd] = self.points
            pts[-nadd:]     = self.points[:nadd]

            w[:nadd]        = self.w[-nadd:]
            w[nadd:-nadd]   = self.w
            w[-nadd:]       = self.w[:nadd]

            knots = np.arange(-nadd, len(self.points) + nadd)/len(self.points)

            if self.endpoint:
                pass

            if self.bezier:
                pass

        elif self.endpoint:

            knots = np.zeros(n + k)
            knots[-self.order:] = 1
            r = n - k + 1
            knots[k-1:k+r] = np.linspace(0, 1, r+1)

        else:
            knots = np.linspace(0, 1, n + k)

        # ----- b splines

        if True:
            self.nurbs_func = NurbsFunction.FromKnots(knots, pts, w, self.order)
        else:
            self.nurbs_func = NurbsFunction(
                bspline = BSpline(knots, pts*w[:, None], self.order - 1, extrapolate=False),
                den_bspline = BSpline(knots, w, self.order - 1, extrapolate=False),
                )

        if False:
            self.bspline = BSpline(knots, pts*w[:, None], self.order - 1, extrapolate=False)
            self.den_bspline = BSpline(knots, w, self.order - 1, extrapolate=False)

    # ====================================================================================================
    # Build the Nurbs function

    def build_nurbs_func(self, value, w):

        if value is None:
            return None

        # ----- Points and weights

        if not isinstance(value, np.ndarray) or value.dtype not in [np.float64, float]:
            value = np.array(value).astype(float)

        if w is None:
            w = 1.

        w = np.resize(w, len(value)).astype(float)

        is_vec = len(np.shape(value)) == 2

        # ----- B-Spline parameters

        n = len(value)
        k = self.order

        pts = value
        ws  = w

        if self.cyclic:

            nadd = self.order
            npts = len(value) + 2*nadd

            pts = np.zeros((npts,) + np.shape(value)[1:], float)
            pts[:nadd]      = value[-nadd:]
            pts[nadd:-nadd] = value
            pts[-nadd:]     = value[:nadd]

            ws  = np.zeros(npts, float)
            ws[:nadd]        = w[-nadd:]
            ws[nadd:-nadd]   = w
            ws[-nadd:]       = w[:nadd]

            knots = np.arange(-nadd, len(value) + nadd)/len(value)

            if self.endpoint:
                pass

            if self.bezier:
                pass

        elif self.endpoint:

            knots = np.zeros(n + k)
            knots[-self.order:] = 1
            r = n - k + 1
            knots[k-1:k+r] = np.linspace(0, 1, r+1)

        else:
            knots = np.linspace(0, 1, n + k)

        # ----- b splines

        return NurbsFunction.FromKnots(knots, pts, ws, self.order)


    # ====================================================================================================
    # Constructor

    @classmethod
    def Circle(cls, radius=1):
        pts = [(1, -1, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (-1, 1, 0), (-1, 0, 0), (-1, -1, 0), (0, -1, 0)]
        w   = [1/np.sqrt(2), 1] * 4

        #pts = [(0, -1, 0), (1, -1, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (-1, 1, 0), (-1, 0, 0), (-1, -1, 0)]
        #w   = [1, 1/np.sqrt(2)] * 4
        return cls(pts, w, order=3, cyclic=True, endpoint=True, bezier=True)

    @classmethod
    def FromFunction(cls, f, t0=0, t1=1, order=3, count=6, cyclic=False, resolution=12):

        nurbs = cls(None, cyclic=cyclic, resolution=resolution, order=order, endpoint=True, bezier=False)

        x = np.linspace(t0, t1, count, endpoint=not cyclic)
        p = f(x)

        if True:
            nurbs.nurbs_func = NurbsFunction(
                bspline     = make_interp_spline(x/np.max(x), p),
                den_bspline = None,
                )
            nurbs.points_count = count

        else:
            nurbs.bspline = make_interp_spline(x/np.max(x), p)

        return nurbs

    # ====================================================================================================
    # Point from parameter

    def __call__(self, t):

        if self.cyclic:
            t = t % 1
        else:
            t = np.clip(t, 0, 1)

        if self.nurbs_func is None:
            return None

        return self.nurbs_func(t)

        if self.den_bspline is None:
            return self.bspline(t)
        else:
            return self.bspline(t)/self.den_bspline(t)[:, None]

    def tangent_NEW(self, t):
        # (u/v)' = (u'v - uv')/v2

        if self.cyclic:
            t = t % 1
        else:
            t = np.clip(t, 0, 1)

        u  = self.bspline(t)
        u_ = self.bspline.derivative(t)
        v  = self.den_bspline(t)
        v_ = self.den_bspline.derivative(t)

        return (u_*v[:, None] - v*v_[:, None])/((v**2)[:, None])

    # ----------------------------------------------------------------------------------------------------
    # Sample values along the curve

    def sample_value_NO(self, value):
        return self.build_nurbs_func(value, self.nurbs_func.w)




# =============================================================================================================================
# List of splines

class BSplines(list):
    def __init__(self):
        super().__init__()

        self._length  = None
        self._tangent = None

    def __call__(self, t):
        res = np.zeros( (len(self),) + np.shape(t) + (3,), float)
        for i, spline in enumerate(self):
            res[i] = spline(t)
        return res

    @property
    def length(self):
        if self._length is None:
            self._length = np.array([spline.length for spline in self])
        return self._length

    def tangent(self, t):
        if self._tangent is None:
            self._tangent = [spline.tangent for spline in self]

        res = np.zeros( (len(self),) + np.shape(t) + (3,), float)
        for i, tg in enumerate(self._tangent):
            res[i] = tg(t)
        return res


# =============================================================================================================================
# Test

if __name__ == '__main__':

    import matplotlib.pyplot as plt

    np.set_printoptions(formatter={'float': lambda x: f"{x:.3f}"})

    # ----------------------------------------------------------------------------------------------------
    # Plot a spline

    def plot(spline, title, tangents=None, t0=0, t1=1):

        fig, ax = plt.subplots()
        plt.title(f"{title}") #" - {spline.points_count}")


        P = spline(np.linspace(t0, t1, 100))
        ax.plot(P[:, 0], P[:, 1])
        ax.set_aspect('equal')

        if tangents is None and isinstance(spline, Poly):
            ax.plot(spline.points[:, 0], spline.points[:, 1], 'xk')
            pass

        if tangents is not None:
            ntg = tangents
            for i, t in enumerate(np.linspace(0, 1, ntg)):
                P = spline(t)
                T = spline.tangent(t)
                v = T - P
                v = v/np.linalg.norm(v)
                T = P + v
                ax.plot([P[0], T[0]], [P[1], T[1]], '-b')

        plt.show()

    # ----------------------------------------------------------------------------------------------------
    # Tests

    def circle(t):
        if np.shape(t) == ():
            return f([t])[0]

        return np.stack((np.cos(t*TAU), np.sin(t*TAU), np.zeros_like(t)), axis=-1)

    def sine(t):
        return np.stack((t, np.sin(3*TAU*t), np.zeros_like(t)), axis=-1)

    if False:
        ply = Poly.FromFunction(sine, count=20, cyclic=False)
        plot(ply, "Poly Sine", tangents=6)

        ply = Poly.FromFunction(circle, count=20, cyclic=True)
        plot(ply, "Poly Circle", tangents=6)

    if False:
        bez = Bezier.FromFunction(sine, count=20, cyclic=False, resolution=12)
        plot(bez, "Bezier Sine")

        b = bez.sample_value(np.arange(20*3).reshape(20, 3))
        print(b(np.linspace(0, 1, 100)))

        bez = Bezier.FromFunction(circle, count=4, cyclic=True, resolution=12)
        plot(bez, "Bezier Circle")

    if True:
        nb = Nurbs.FromFunction(sine, count=20, cyclic=False)
        plot(nb, "Nurbs Sine", tangents=None)

        nb = Nurbs.Circle()
        plot(nb, "Nurbs Circle CLS")

        nb = Nurbs.FromFunction(circle, count=20, cyclic=True)
        #plot(nb, "Nurbs Circle FUNC")
