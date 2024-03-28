#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:29:17 2022

@author: alain
"""

# ---------------------------------------------------------------------------
# Blender shape keys are organized
#
# object
#      shape_keys (Key)
#           key_blocks (Prop Collection of ShapeKey)
#                data (Prop Collection of
#                     ShapeKeyPoint
#                     ShapeKeyBezierPoint
#                     ShapeKeyCurvePoint
#       
# cube.data.shape_keys.key_blocks[].data[].co
#
# A key is either a string (name of the shape) or an int (index in the array)
# Series are managed through a key name and a number of steps

import numpy as np
from geonodes import CubicSpline, BSpline


if __name__ != '__main__':
    
    import bpy

    from geonodes.core import blender
    from geonodes.core.cloud import Cloud
    from geonodes.core.instances import Instances
    from geonodes.core.mesh import Mesh
    from geonodes.core.curve import Curve


#from geonodes.core.meshbuilder import MeshBuilder
#from geonodes.core.curvebuilder import CurveBuilder, BezierBuilder, PolyBuilder, NurbsBuilder
#from geonodes.core.maprange import maprange
#from geonodes.core.transformations import TMatrices

# ====================================================================================================
# Float attributes shape keys

class ShapeKeys:
    def __init__(self, attributes, count=1):
        self.attributes = attributes
        self.values = np.resize(self.attributes.float_array, (count,) + np.shape(self.attributes.float_array))
        
    def __str__(self):
        return f"<Shapekeys: {len(self)} shapes of {self.points_count} points, attributes: {self.names}>"

    # =============================================================================================================================
    # As an array of arrays
        
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, index):
        return self.values[index]

    def __setitem__(self, index, value):
        self.values[index] = value
        
    @property
    def points_count(self):
        return self.values.shape[1]
    
    def new(self):
        self.values = np.resize(self.values, (len(self)+1,) + np.shape(self.values)[1:])
    
    # =============================================================================================================================
    # Shaped named attributes
    
    @property
    def names(self):
        return [name for name in self.attributes.names if self.attributes.attribute_dtype(name) == float]
    
    def get_value(self, index, name):
        return self.values[index, :, self.attributes.get_attr_slice(name)]
    
    def set_value(self, index, name, value):
        self.values[index, :, self.attributes.get_attr_slice(name)] = value
        
    def get_interpolated_value(self, int_values, name):
        
        count = np.prod(np.shape(int_values)[:-1], dtype=int)
        shape = (count,) + self.attributes.attribute_shape(name)
        return np.reshape(int_values[..., self.attributes.get_attr_slice(name)], shape)
    
    # =============================================================================================================================
    # From Geometry
    
    @classmethod
    def FromGeometry(cls, geometry, count):
        if isinstance(geometry, Curve):
            _ = geometry.points.radius
            _ = geometry.points.tilt

        return cls(geometry.points._attributes, count=count)
    
    # =============================================================================================================================
    # From / to Blender Object
    
    @classmethod
    def FromObject(cls, spec):
        
        obj = blender.get_object(spec)
        if obj is None:
            return None

        elif isinstance(obj.data, bpy.types.Mesh):
            return cls.FromMeshObject(obj)

        elif isinstance(obj.data, bpy.types.Curve):
            return cls.FromCurveObject(obj)
        
        else:
            raise RuntimeError(f"Impossible to read shape keys from object of type '{type(obj.data).__name__}'")
            
    def to_object(self, spec, name="Key", clear_shape_keys=True):
        
        obj = blender.get_object(spec)
        if obj is None:
            return None

        elif isinstance(obj.data, bpy.types.Mesh):
            return self.to_mesh_object(obj, name=name, clear_shape_keys=clear_shape_keys)

        elif isinstance(obj.data, bpy.types.Curve):
            return self.to_curve_object(obj, name=name, clear_shape_keys=clear_shape_keys)
        
        else:
            raise RuntimeError(f"Impossible to write shape keys to object of type '{type(obj.data).__name__}'")
    
    # =============================================================================================================================
    # Mesh
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Read the shapes defined in an object
    
    @classmethod
    def FromMeshObject(cls, spec):
        
        obj   = blender.get_object(spec)
        mesh  = Mesh.FromObject(obj)
        sks   = cls(mesh.points._attributes)
        count = blender.shape_keys_count(obj)
        
        if count == 0:
            return sks
        
        a = np.empty(len(mesh.points)*3, float)
        for index in range(count):
            kb = blender.get_key_block(obj, index)
            kb.data.foreach_get('co', a)
            
            if index > 0:
                sks.new()
                
            sks.set_value(-1, 'position', np.reshape(a, (sks.points_count, 3)))
            
        return sks
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Write the shapes in an existing mesh object
    
    def to_mesh_object(self, spec, name="Key", clear_shape_keys=True):

        obj = blender.get_object(spec)
        assert(len(obj.data.vertices) == self.points_count)
        
        if clear_shape_keys:
            blender.shape_keys_clear(obj)
            
        count = blender.shape_keys_count(obj)
        
        a = np.empty(self.points_count*3, float)
        
        for index in range(0, len(self)):
            kb = blender.get_key_block(obj, count + index, create=True, name=f"{name}.{index:03d}")
            a[:] = np.reshape(self.get_value(index, 'position'), a.shape)
            kb.data.foreach_set('co', a)
                
        return obj
    
    # =============================================================================================================================
    # Curve
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Read the shapes defined in a curve object
    
    @classmethod
    def FromCurveObject(cls, spec):
        
        obj = blender.get_object(spec)
        curve = Curve.FromObject(obj)
        _ = curve.points.radius
        _ = curve.points.tilt
        
        count = blender.shape_keys_count(obj)
        sks = cls(curve.points._attributes, count)
        
        # ----------------------------------------------------------------------------------------------------
        # No shape key
        
        if count == 0:
            return sks
        
        # ----------------------------------------------------------------------------------------------------
        # Loop on the shape keys
        
        nverts = len(curve.points)
        
        for index in range(count):
            
            key_data = blender.get_key_block(obj, index).data
            
            # ----------------------------------------------------------------------------------------------------
            # Loop on the splines
            
            for curve_type, loop_start, loop_total in zip(curve.splines.curve_type, curve.splines.loop_start, curve.splines.loop_total):
                
                # ----- Bezier
                
                if curve_type == blender.BEZIER:
                    
                    for i in range(loop_total):
                        sks.values[index, loop_start + i, sks.attributes.get_attr_slice('position')] = key_data[loop_start + i].co
                        sks.values[index, loop_start + i, sks.attributes.get_attr_slice('handle_left')] = key_data[loop_start + i].handle_left
                        sks.values[index, loop_start + i, sks.attributes.get_attr_slice('handle_right')] = key_data[loop_start + i].handle_right
    
                        sks.values[index, loop_start + i, sks.attributes.get_attr_slice('radius')] = key_data[loop_start + i].radius
                        sks.values[index, loop_start + i, sks.attributes.get_attr_slice('tilt')]   = key_data[loop_start + i].tilt
                    
                # ----- Non Bezier
                
                else:

                    for i in range(loop_total):
                        sks.values[index, loop_start + i, self.attributes.get_attr_slice('position')] = key_data[loop_start + i].co
                        try:
                            radius, tilt = key_data[loop_start + i].radius, key_data[loop_start + i].tilt
                        except:
                            radius, tilt = 1., 0.
        
                        sks.values[index, loop_start + i, self.attributes.get_attr_slice('radius')] = radius
                        sks.values[index, loop_start + i, self.attributes.get_attr_slice('tilt')]   = tilt

        return sks    
    
    # -----------------------------------------------------------------------------------------------------------------------------
    # Write the shapes in an existing curve object
    
    def to_curve_object(self, spec, name="Key", clear_shape_keys=True):

        obj = blender.get_object(spec)
        curve = Curve.FromObject(obj)
        
        if clear_shape_keys:
            blender.shape_keys_clear(obj)
            
        count = blender.shape_keys_count(obj)
        for index in range(len(self)):
            
            key_data = blender.get_key_block(obj, count + index, create=True, name=f"{name}.{index:03d}").data
            
            # ----------------------------------------------------------------------------------------------------
            # Loop on the splines
            
            for curve_type, loop_start, loop_total in zip(curve.splines.curve_type, curve.splines.loop_start, curve.splines.loop_total):
                
                # ----- Bezier
                
                if curve_type == blender.BEZIER:
                    
                    for i in range(loop_total):
                        key_data[loop_start + i].co = self.values[index, loop_start + i, self.attributes.get_attr_slice('position')]
                        key_data[loop_start + i].handle_left = self.values[index, loop_start + i, self.attributes.get_attr_slice('handle_left')]
                        key_data[loop_start + i].handle_right = self.values[index, loop_start + i, self.attributes.get_attr_slice('handle_right')]
    
                        key_data[loop_start + i].radius = self.values[index, loop_start + i, self.attributes.get_attr_slice('radius')]
                        key_data[loop_start + i].tilt   = self.values[index, loop_start + i, self.attributes.get_attr_slice('tilt')]
                    
                # ----- Non Bezier
                
                else:

                    for i in range(loop_total):
                        key_data[loop_start + i].co = self.values[index, loop_start + i, self.attributes.get_attr_slice('position')]
                        if hasattr(key_data[loop_start + i], 'radius'):
                            key_data[loop_start + i].radius = self.values[index, loop_start + i, self.attributes.get_attr_slice('radius')]
                            key_data[loop_start + i].tilt = self.values[index, loop_start + i, self.attributes.get_attr_slice('tilt')]
                
        return obj
    
    # ====================================================================================================
    # Interpolation (default is absolute)
    
    def interpolate(self, t, relative=False, extrapolation='CLIP', smooth=1):
        """ Interpolation.
        
        Use rel_interpolate for relative interpolation.
        
        Smooth define the interpolation on each interval:
            - integer : Degree of BSpline interpolation
            - str     : Name of an interpolation function
            - function : function to use
        
        Arguments
        ---------
            - t (float or array of floats) : interpolation factor in [0, 1]
            - extrapolation (str in 'CLIP', 'CYCLIC', 'BACK' = 'CLIP') : extrapolation mode
            - smooth (function = None) : smooth function
            
        Returns
        -------
            - array of floats
        """

        # ---------------------------------------------------------------------------
        # Only one shape
        
        if len(self) == 1:
            return np.resize(self.values, np.shape(t) + np.shape(self.values)[1:])
        
        # ---------------------------------------------------------------------------
        # Compute factors between 0 and 1 depending upon the mode
            
        t_shape = np.shape(t)
        single = t_shape == ()
        if single:
            t = np.reshape(t, (1,))
        
        if extrapolation == 'CLIP':
            factors = np.clip(t, 0, 1).astype(float)
            
        elif extrapolation == 'CYCLIC':
            factors = np.array(t) % 1.
            
        elif extrapolation == 'BACK':
            factors = (2*np.array(t)) % 2.
            i_back = factors > 1
            factors[i_back] = 2 - factors[i_back]
        
        else:
            raise AttributeError(f"ShapeKeys.interpolate error: invalid extrapolation '{extrapolation}'.")
            
        # ---------------------------------------------------------------------------
        # Smooth
        
        degree = None
        use_cubic = False
        if smooth is None:
            degree = 1
            
        elif isinstance(smooth, (int, np.int64, np.int32)):
            degree = smooth
        
        elif hasattr(smooth, '__call__'):
            factors = smooth(factors)
            
        elif isinstance(smooth, str):
            if smooth == 'CUBIC':
                use_cubic = True
            else:
                factors = maprange(factors, easing=smooth)
            
        else:
            raise AttributeError(f"ShapeKeys.interpolate error: smooth parameter must be a function or a string, not {type(smooth).__name__}.")
            
        # ---------------------------------------------------------------------------
        # Interpolation
        
        if degree is None:
            
            fs = factors*(len(self) - 1)
            inds = np.floor(fs).astype(int)
            inds[inds == len(self) - 1] = len(self) - 2
            p = np.reshape(fs - inds, np.shape(fs) + (1, 1))
            
            verts = self.values[inds]*(1 - p) + self.values[inds + 1]*p
            
        elif use_cubic:
            verts = CubicSpline(np.linspace(0, 1, self.points_count), self.values, extrapolate=False)(factors)
            
        else:
            
            n = len(self)
            k = smooth
            
            dx = 1/(n - 1)
            t = np.linspace(-k*dx, 1 + k*dx, n + k + 1)
            
            verts = BSpline(t, self.values, k=k, extrapolate=False)(factors)
            
        # ---------------------------------------------------------------------------
        # Done

        if single:
            return verts[0]
        else:
            return verts    
        
    # ====================================================================================================
    # Relative interpolation
    
    def rel_interpolate(self, weights, smooth=1):
        """ Relative interpolation.
        
        Use interpolate for absolute interpolation.
        
        The number of weights must be equal to the number of shapes minus 1.
        The interpolation mixes the differences of each shape with the first one.
        
        Smooth define the interpolation on each interval:
            - integer : Degree of BSpline interpolation
            - str     : Name of an interpolation function
            - function : function to use
        
        Arguments
        ---------
            - weights (array of floats or array of arrays of flaotsd) : interpolation factor in [0, 1]
            - extrapolation (str in 'CLIP', 'CYCLIC', 'BACK' = 'CLIP') : extrapolation mode
            - smooth (function = None) : smooth function
            
        Returns
        -------
            - array of floats
        """
        
        # ---------------------------------------------------------------------------
        # Check the validity of the array of weights
        
        ok     = True
        single = False
        if np.shape(weights) == ():
            if len(self) != 2:
                ok = False
            single = True
            weights = np.reshape(weight, (1, 1))
        else:
            if np.shape(weights)[-1] != len(self) - 1:
                ok = False
                
        if not ok:
            raise RuntimeError(f"ShapeKeys.rel_interpolate error: the shape of the array of weights is not valid {np.shape(weights)}, expected (n, {len(self)-1})")
            
            
        weights = np.clip(weights, 0, 1)
            
        # ---------------------------------------------------------------------------
        # Smooth
        
        degree = None
        use_cubic = False
        if smooth is None:
            degree = 1
            
        elif isinstance(smooth, (int, np.int64, np.int32)):
            degree = smooth
        
        elif hasattr(smooth, '__call__'):
            weights = smooth(weights)
            
        elif isinstance(smooth, str):
            if smooth == 'CUBIC':
                use_cubic = True
            else:
                weights = maprange(weights, easing=smooth)
            
        else:
            raise AttributeError(f"ShapeKeys.rel_interpolate error: smooth parameter must be a function or a string, not {type(smooth).__name__}.")

        # ---------------------------------------------------------------------------
        # Relative interpolation:
        # basis shape + weights * differences
            
        verts = self.values[0] + np.sum(
                    (self.values[1:] - self.values[0])*np.reshape(weights, np.shape(weights) + (1, 1)),
                    axis = - 3)
            
        # ---------------------------------------------------------------------------
        # Done

        if single:
            return verts[0]
        else:
            return verts     
        
    # ====================================================================================================
    # Instantiate with absolute interpolation weights
    
    def instantiate(self, geometry, t, extrapolation='CLIP', smooth=1):
        
        verts = self.interpolate(t, extrapolation=extrapolation, smooth=smooth)
        
        count = 1 if len(np.shape(verts)) == 2 else len(verts)
        n = self.points_count
        
        geos = geometry*count
        for name in self.attributes.names:
            setattr(geos.points, name, self.get_interpolated_value(verts, name))
        
        return geos
        
    # ====================================================================================================
    # Instantiate with relative interpolation weights
    
    def rel_instantiate(self, geometry, weights, smooth=1):
        
        verts = self.rel_interpolate(weights, smooth=smooth)
        
        count = 1 if len(np.shape(verts)) == 2 else len(verts)
        n = self.points_count
        
        geos = geometry*count
        for name in self.attributes.names:
            setattr(geos.points, name, self.get_interpolated_value(verts, name))
        
        return geos
    
# ====================================================================================================
# Demo shape keys
    
def demo(seed=0):
    
    rng = np.random.default_rng(seed)
    
    # ====================================================================================================
    # Instantiate
    
    def instantiate(geo, sks, plural_name, location=(0, 0, 0)):
    
        # ----- Instantiate with absolute interpolation
        
        count = 10
        t = rng.uniform(0, 1, count)
        locs = rng.uniform(-10, 10, (count, 3))
        
        geos = sks.instantiate(geo, t, smooth=1)
        geos.points.translate(locs)
        obj = geos.to_object(plural_name)
        obj.location = location
        
        # ----- Instantiate with relative interpolation
        
        count = 10
        w = rng.uniform(0, 1, (count, len(sks)-1))
        locs = rng.uniform(-10, 10, (count, 3))
        
        geos = sks.rel_instantiate(geo, w, smooth=1)
        geos.points.translate(locs)
        obj = geos.to_object(f"{plural_name} Rel")
        obj.location = location
        obj.location.x += 30
    
    # ====================================================================================================
    # Mesh
    
    cube = Mesh.Cube()
    sks = ShapeKeys.FromGeometry(cube, 4)
    
    a = sks.get_value(1, 'position')
    a[a[:, 2] > .5] *= (.1, .1, 1)
    
    a = sks.get_value(2, 'position')
    a[a[:, 1] < -.5] *= (2, 2, 1)
    
    a = sks.get_value(3, 'position')
    a[a[:, 0] > .5] += (2, 0, 0)
    
    obj = cube.to_object("SKS Cube", shade_smooth=False)
    sks.to_object(obj)
    
    instantiate(cube, sks, "SKS Cubes", location=(0, 0, 0))
    
    # ====================================================================================================
    # Curve
    
    curve = Curve.BezierSegment()
    curve.points.position[:, 2] -= 1
    
    curve.join(Curve.Spiral())

    sks = ShapeKeys.FromGeometry(curve, 4)
    
    a = sks.get_value(1, 'position')
    a[a[:, 2] > .5] *= (.1, .1, 1)
    
    a = sks.get_value(2, 'position')
    a[a[:, 1] < -.5] *= (2, 2, 1)
    
    a = sks.get_value(3, 'position')
    a[a[:, 0] > .5] += (2, 0, 0)
    
    obj = curve.to_object("SKS Curve")
    sks.to_object(obj)
    
    instantiate(curve, sks, "SKS Curves", location=(0, 30, 0))

    
# =============================================================================================================================
# Interpolation 

if __name__ == '__main__':

    import numpy as np
    from scipy.interpolate import CubicSpline
    from scipy.interpolate import BSpline
    import matplotlib.pyplot as plt

    rng = np.random.default_rng(0)
    count = 10
    
    x = np.linspace(0, 1, count)
    y = rng.uniform(0, 1, count)
    
    t = np.linspace(-.5, 1.5, 100)
    
    # BSpline
    
    for k in range(4):
        
        if True:
            dx = 1/(count-1)
            x1 = np.linspace(-dx*k, 1+k*dx, count + k + 1)
            
            y1 = y
        
        else:
            dx = 1/(count-1)
            x1 = np.linspace(-dx*k, 1+dx*k, count+2*k)
            
            y1 = np.resize(y, count+k)
            y1[0] = y[0]
            y1[-1] = y[-1]
            if k == 1:
                y1[:-k] = y
            elif k == 2:
                y1[1:-1] = y
            elif k == 3:
                y1[1:-2] = y
            else:
                y1[:len(y)] = y
            
        
        bs = BSpline(x1, y1, k=k, extrapolate=False)
        
        fig, ax = plt.subplots()
        
        ax.plot(t, bs(t))
        ax.plot(x, y, 'xr')
        
        plt.title(f"Degree {k}")
        
        plt.show()
        
    # CubicSpline
    
    cs = CubicSpline(x, y, extrapolate=False)

    fig, ax = plt.subplots()
    
    ax.plot(t, cs(t))
    ax.plot(x, y, 'xr')
    
    plt.title(f"CubicSpline")
    
    plt.show()
    
    
    

        


    
    
    
    
    
        
        
        
                            
                            
                            

