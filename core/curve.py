#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blender Python Geometry module

Created on Fri Nov 10 11:50:13 2023

@author: alain.bernard
@email: alain@ligloo.net

-----

Curve geometry.

"""

from contextlib import contextmanager

import numpy as np
import bpy
import mathutils

from geonodes import RotationSpline

from geonodes.core import blender
from geonodes.core import topology

from geonodes.maths.transformations import Transformations, tracker, rotate_xy_into_plane
from geonodes.maths.splinesmaths import Bezier
from geonodes.maths import field, distribs

from geonodes.core.geometry import Geometry
from geonodes.core.attributes import AttrVectors
from geonodes.core.domain import ControlPointDomain, SplineDomain


DATA_TEMP_NAME = "GEOPY_TEMP"

# =============================================================================================================================
# Curve, made of one or more splies

class Curve(Geometry):

    def __init__(self, types=None, splines=None, cyclic=None, resolution=None, material_index=None, materials=None, **attributes):
    #def __init__(self, materials=None, types=None, points=None, **attributes):
        """ Curve geometry.

        Arguments
        ---------
            - types (array of ints = None) : spline types in [BEZIER=0, POLY=1, NURBS=2]
            - splines (array of spline dictionnaries = None) : array of splines dictionnary
            - cyclic (array of bools = None) : splines are cyclic
            - resolution (array of ints = None) : splines resolution
            - material_index (arrays of ints = None) : material indices
            - materials (list of strs = None) : materials list
            - attributes : custom spline attributes
        """

        self.points  = ControlPointDomain.New()
        self.splines = SplineDomain.New(points=self.points)

        if materials is None:
            self.materials = []

        elif isinstance(materials, str):
            self.materials = [materials]

        else:
            self.materials = [mat for mat in materials]

        # ----------------------------------------------------------------------------------------------------
        # Create the splines

        if types is None:
            return

        if np.shape(types) == ():
            types = [types]

        nsplines = len(types)
        if nsplines == 0:
            return

        self.splines.add(nsplines, curve_type=types)

        # ----------------------------------------------------------------------------------------------------
        # Spline attributes

        if cyclic is not None:
            setattr(self.splines, 'cyclic', cyclic)

        if resolution is not None:
            setattr(self.splines, 'resolution', resolution)

        if material_index is not None:
            setattr(self.splines, 'material_index', material_index)

        for attr_name, attr_value in attributes.items():
            setattr(self.splines, attr_name, attr_value)

        # ----------------------------------------------------------------------------------------------------
        # Set the points

        if splines is None or len(splines) != nsplines:
            raise Exception(f"Curve init error: the Curve is initialized with {nsplines}. The 'splines' argument must be an array of {nsplines} dicts.")

        total = sum([len(spline_points['points']) for spline_points in splines])
        self.points.add(total)

        offset = 0
        for i_spline, (curve_type, spline_points) in enumerate(zip(types, splines)):

            count = len(spline_points['points'])
            self.splines.loop_start[i_spline] = offset
            self.splines.loop_total[i_spline] = count

            if curve_type == blender.BEZIER:
                self.points.attributes['position'][offset:offset+count] = spline_points['points']

            else:
                pts = spline_points['points']
                if np.shape(pts)[-1] == 3:
                    self.points.position[offset:offset+count] = pts
                else:
                    self.points[offset:offset+count].points4 = pts

            ok_left  = False
            ok_right = False

            for name in ['handle_left', 'handle_right', 'handle_type_left', 'handle_type_right', 'radius', 'tilt']:

                a = spline_points.get(name)
                if a is not None:

                    if name == 'handle_left':
                        ok_left = True
                    if name == 'handle_right':
                        ok_right = True

                    if not self.points.attributes.exists(name):
                        _ = getattr(self.points, name)
                    self.points.attributes[name][offset:offset+count] = a

            # ----- Bezier handles

            if curve_type == blender.BEZIER and (not ok_left or not ok_right):
                lefts, rights = Bezier.get_handles(spline_points['points'], cyclic=cyclic)
                if not ok_left:
                    if not self.points.attributes.exists('handle_left'):
                        _ = getattr(self.points, 'handle_left')
                    self.points.attributes['handle_left'][offset:offset+count] = lefts
                if not ok_right:
                    if not self.points.attributes.exists('handle_right'):
                        _ = getattr(self.points, 'handle_right')
                    self.points.attributes['handle_right'][offset:offset+count] = rights

            # ----- Next spline

            offset += count

    # -----------------------------------------------------------------------------------------------------------------------------

    def check(self, halt=True):
        return self.splines.check(halt=halt)

    def __str__(self):
        return f"<Curve: points {self.points.shape}, splines {self.splines.shape}>"

    def __repr__(self):
        s = "Curve:\n   " + "\n   ".join([str(self.points), str(self.splines)])
        return s

    # =============================================================================================================================
    # Clear the geometry

    def clear(self):
        """ Clear the geometry
        """

        self.points.attributes.clear()
        self.splines.attributes.clear()

    # -----------------------------------------------------------------------------------------------------------------------------
    # Capture another Mesh

    def capture(self, other):
        """ Capture the data of another Curve.

        Arguments
        ---------
            - other (Curve) : the curve to capture

        Returns
        -------
            - self
        """

        self.materials = other.materials

        self.points  = other.points
        self.splines = other.splines

        return self

    # =============================================================================================================================
    # =============================================================================================================================
    # Initialization methods
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Initialize from another Mesh

    @classmethod
    def FromCurve(cls, other):
        """ Create a Curve from another curve.

        Arguments
        ---------
            - other (Curve) : the curve to copy

        Returns
        -------
            - Curve
        """

        curve = cls(materials=other.materials)
        curve.points.attributes  = other.points.attributes.clone()
        curve.splines.attributes = other.splines.attributes.clone()

        return curve

    # -----------------------------------------------------------------------------------------------------------------------------
    # Initialize from an object

    @classmethod
    def FromObject(cls, obj, evaluated=False):
        """ Create a Curve from an existing curve.

        Arguments
        ---------
            - obj (str or Blender object) : the object to initialize from
            - evaluated (bool = False) : object modified by the modifiers if True, raw vertices otherwise

        Returns
        -------
            - Curve
        """

        if evaluated:
            depsgraph = bpy.context.evaluated_depsgraph_get()
            object_eval = blender.get_object(obj).evaluated_get(depsgraph)
            return cls.FromCurveData(object_eval.data)

        else:
            return cls.FromCurveData(blender.get_object(obj).data)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Initialize from curve data

    @classmethod
    def FromCurveData(cls, data):
        """ Initialize the geometry from a Blender Mesh

        Arguments
        ---------
            - mesh (Blender Mesh instance) : the mesh to load
        """

        return cls(**blender.get_splines(data), materials=[mat.name for mat in data.materials])


    # ====================================================================================================
    # From a dictionary

    @classmethod
    def FromComponents_OLD(cls, types, points, **spline_attrs):
        """ Create a new Curve from defintions.

        The number of splines is defined by the length of types list

        Arguments
        ---------
            - types (list of ints) : spline types in [BEZIER=0, POLY=1, NURBS=2]
            - point_counts (int or list of ints) : number of points per spline
            - points (dict=None) : points definition
            - spline_attrs : initial value for spline attributes

        Returns
        -------
            - Curve
        """

        # ----------------------------------------------------------------------------------------------------
        # Create the splines

        if np.shape(types) == ():
            types = [types]

        nsplines = len(types)
        if nsplines == 0:
            return cls()

        curve = cls()
        curve.splines.add(nsplines, curve_type=types)
        for name, value in spline_attrs.items():
            setattr(curve.splines, name, value)

        # ----------------------------------------------------------------------------------------------------
        # Set the points

        if 0 in types:
            curve.points.set_bezier()

        total = 0
        ok_radius = False
        ok_tilt   = False
        for spline_points in points:
            total += len(spline_points['points'])
            if spline_points.get('radius') is not None:
                ok_radius = True
            if spline_points.get('tilt') is not None:
                ok_tilt = True

        if ok_radius:
            _ = curve.points.radius
        if ok_tilt:
            _ = curve.points.tilt

        curve.points.add(total)

        offset = 0
        for i_spline, (curve_type, spline_points) in enumerate(zip(types, points)):

            count = len(spline_points['points'])
            curve.splines.loop_total[i_spline] = count

            if curve_type == blender.BEZIER:
                curve.points.attributes['position'][offset:offset+count] = spline_points['points']
            else:
                pts = spline_points['points']
                if np.shape(pts)[-1] == 3:
                    curve.points.position[offset:offset+count] = pts
                else:
                    curve.points.points4[offset:offset+count] = pts

            for name in ['handle_left', 'handle_right', 'handle_type_left', 'handle_type_right', 'radius', 'tilt']:
                a = spline_points.get(name)
                if a is not None:
                    curve.points.attributes[name][offset:offset+count] = a

            offset += count

        return curve


    # =============================================================================================================================
    # =============================================================================================================================
    # I/O wit Blender
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # To components

    def components(self):

        if len(self.splines) == 0:
            return {'types': [], 'splines': []}

        splines_dict = {'types': self.splines.curve_type, 'splines': [None]*len(self.splines), 'materials': [name for name in self.materials]}

        # ----------------------------------------------------------------------------------------------------
        # Splines attributes

        for name in self.splines.attributes.names:
            if name in ['curve_type', 'loop_total']:
                continue
            splines_dict[name] = getattr(self.splines, name)

        # ----------------------------------------------------------------------------------------------------
        # Points

        offset = 0
        for i_spline, (curve_type, count) in enumerate(zip(self.splines.curve_type, self.splines.loop_total)):

            spline_points = {}
            splines_dict['splines'][i_spline] = spline_points

            if curve_type == blender.BEZIER:
                spline_points['points'] = np.array(self.points.attributes['position'][offset:offset+count])
            else:
                spline_points['points'] = np.array(self.points.points4[offset:offset+count])

            for name in ['handle_left', 'handle_right', 'handle_type_left', 'handle_type_right', 'radius', 'tilt']:
                if self.points.attributes.exists(name):
                    spline_points[name] = np.array(self.points.attributes[name][offset:offset+count])

            offset += count

        return splines_dict

    # -----------------------------------------------------------------------------------------------------------------------------
    # Create / update an object

    def to_object(self, obj):
        """ Create or update a blender object.

        The method 'to_object' creates the whole geometry. It creates a new object if it doesn't already exist.
        If the object exists, it must be a curve, there is no object type conversion.

        Once the object is created, use the method 'update_object' to change the vertices.

        Arguments
        ---------
            - obj (str or Blender object) : the object the create

        Returns
        -------
            - Blender curve object
        """

        curve = blender.create_curve_object(obj)
        self.to_curve_data(curve.data)
        return curve

    # -----------------------------------------------------------------------------------------------------------------------------
    # To blender curve data

    def to_curve_data(self, data):
        """ Write the geometry into a Blender Curve

        Arguments
        ---------
            - mesh (Blender Mesh instance) : the mesh to write
        """

        blender.set_splines(data, self.components())

        # ----------------------------------------------------------------------------------------------------
        # Attributes : sadly, Curve has no attributes :-(

        #self.splines.attributes.to_object(data, update=False)
        #self.points.attributes.to_object(data, update=False)


    # =============================================================================================================================
    # Acces to blender data

    @contextmanager
    def blender_data(self, readonly=False):
        """ Acces to Blender Curve API.

        Transfer the geometry to a temporay Blender Curve.
        The example below use a blender Mesh to get the normals.

        ``` python
        curve = Curve.Spiral()

        with curve.blender_data() as bcurve:
            print("Number of points", len(bcurve.splines[0].points))

        # > Number of points 65
        ```

        Arguments
        ---------
            - readonly (bool=False) : don't read back the geometry if not modified

        Returns
        -------
            - Blender Mesh
        """

        data = bpy.data.curves.get(DATA_TEMP_NAME)
        if data is None:
            data = bpy.data.curves.new(DATA_TEMP_NAME, type='CURVE')

        self.to_curve_data(data)

        yield data

        # ----- Back

        if not readonly:
            self.capture(Curve.FromCurveData(data))

    # =============================================================================================================================
    # Material

    def get_material_index(self, mat_name):
        """ Return the index of a material name.

        If the material doesn't exist, it is created

        Arguments
        ---------
            - mat_name (str) : material name

        Returns
        -------
            - int : index of the material name in the materials list
        """

        if mat_name in self.materials:
            return self.materials.index(mat_name)
        else:
            self.materials.append(mat_name)
            return len(self.materials)-1

    def change_material(self, old, new):
        """ Change the material index from one value to another.

        Arguments
        ---------
            - old (int) : material index to replace
            - new (int) : new material index
        """

        self.faces.material_index[self.faces.material_index == old] = new

    def add_materials(self, materials):
        """ Add a materials list to the existing one.

        If a material already exist, it is not added another time.

        Arguments
        ---------
            - materials (list of strs) : the list of materials to append.
        """

        if isinstance(materials, str):
            self.materials.append(materials)
        else:
            self.materials.extend(materials)

    # =============================================================================================================================
    # Combining

    def join(self, *others, quick=False):
        """ Join another Curve.

        Arguments
        ---------
            - other (Curve) : the Curve to append
            - quick (bool=False) : don't check the attributes and the material indices
        """

        for other in others:

            # ----------------------------------------------------------------------------------------------------
            # Points

            v_ofs = self.points.size
            self.points.attributes.join(other.points.attributes)

            # ----------------------------------------------------------------------------------------------------
            # Splines

            s_ofs    = self.splines.size
            nsplines = len(self.splines)
            self.splines.attributes.join(other.splines.attributes)
            self.splines[nsplines:].loop_start += v_ofs

            # ----- Materials

            if not quick:
                remap = np.array([self.get_material_index(mat_name) for mat_name in other.materials])
                if len(remap)>0:
                    self.splines.material_index[f_ofs:] = remap[other.splines.material_index]

        return self

    # =============================================================================================================================
    # Add splines

    def add(self, points, curve_type='POLY',
            material_index=None, radius=None, tilt=None, cyclic=None, resolution=None,
            handle_left=None, handle_right=None, handle_type_left=None, handle_type_right=None):

        if len(np.shape(points)) < 2:
            raise RuntimeError(f"Curve.add error: the 'points' argument must be an array, or arrays, of vectors, not shape {np.shape(points)}.")

        if len(np.shape(points)) == 2:
            points = [points]

        nsplines = len(points)
        single = np.shape(curve_type) == ()
        if single:
            curve_type = [curve_type]*nsplines
            npoints = len(points[0])

            def check(attr_name, attr, item_shape):
                if attr is None:
                    return None
                #if item_shape == () and np.shape(attr) == ():
                #    return [attr] * npoints
                if item_shape == np.shape(attr):
                    return [attr] * npoints
                if np.shape(attr) != (npoints,) + item_shape:
                    raise RuntimeError(f"Curve.add error: 'points' argument is shaped {np.shape(points)[1:]} but the argument '{attr_name}' is shaped {np.shape(attr)}.")
                return [attr]

            handle_left       = check('handle_left',       handle_left,      (3,))
            handle_right      = check('handle_right',      handle_right,     (3,))
            handle_type_left  = check('handle_type_left',  handle_type_left, ())
            handle_type_right = check('handle_type_right', handle_type_right,())
            radius            = check('radius',            radius,           ())
            tilt              = check('tilt',              tilt,             ())

        if len(curve_type) != nsplines:
            raise RuntimeError(f"Curve.add error: the number of splines given by 'points' argument (nsplines) differs from the number given by 'curve_type' argument ({len(curve_type)})")

        # ----- Build the splines dict

        splines_dict = {'types': [blender.SPLINE_TYPES.index(ctype.upper()) for ctype in curve_type], 'splines': [None]*nsplines}

        def add_spline_attr(name, value):
            if value is None:
                return

            if np.shape(value) == ():
                splines_dict[name] = [value]*nsplines
            else:
                if len(value) != nsplines:
                    raise RuntimeError(f"Curve.add error: the argument '{name}' of length {len(value)} should have a length of {nsplines}.")
                splines_dict[name] = value

        add_spline_attr('material_index',  material_index)
        add_spline_attr('cyclic',          cyclic)
        add_spline_attr('resolution',      resolution)

        for i, pts in enumerate(points):
            splines_dict['splines'][i] = {'points': pts}
            if handle_left       is not None: splines_dict['splines'][i]['handle_left']       = handle_left[i]
            if handle_right      is not None: splines_dict['splines'][i]['handle_right']      = handle_right[i]
            if handle_type_left  is not None: splines_dict['splines'][i]['handle_type_left']  = handle_type_left[i]
            if handle_type_right is not None: splines_dict['splines'][i]['handle_type_right'] = handle_type_right[i]
            if radius is not None:            splines_dict['splines'][i]['radius']            = radius[i]
            if tilt is not None:              splines_dict['splines'][i]['tilt']              = tilt[i]

        self.join(Curve(**splines_dict))

        return self


    # =============================================================================================================================
    # Multiply

    def __mul__(self, count):
        if not isinstance(count, (int, np.int32, np.int64)):
            print("count:", type(count))
            raise Exception(f"A Curve can be multiplied only by an int, not '{count}'")

        return self.multiply(count)

    def __imul__(self, count):
        if not isinstance(count, (int, np.int32, np.int64)):
            raise Exception(f"A Mesh can be multiplied only by an int, not '{count}'")

        if count <= 1:
            return

        # ----------------------------------------------------------------------------------------------------
        # Vertices

        v_ofs = self.points.size
        self.points.attributes.multiply(count)

        # ----------------------------------------------------------------------------------------------------
        # Splines

        s_ofs = self.splines.size
        ofs = (np.arange(count)*v_ofs)[:, None] + np.zeros((1, s_ofs), int)
        self.splines.attributes.multiply(count)

        return self


    def multiply(self, count=10, offset=None, **attributes):
        """ Duplicate the geometry.

        Multiplying is a way to efficiently duplicate the geometry a great number of times.

        ``` python
        count = 16

        mb = MeshBuilder.Cube() * count
        ags = np.linspace(0, 2*np.pi, count, endpoint=False)
        r = 6

        np.reshape(mb.verts, (count, 8, 3))[..., 0] += (r*np.cos(ags))[:, None]
        np.reshape(mb.verts, (count, 8, 3))[..., 1] += (r*np.sin(ags))[:, None]

        mb.to_object("Cubes")
        ```

        See also 'instances' method for a better control of the instances

        Arguments
        ---------
            - count (int=10) : number of instances
            - offset (array of vectors = None) : offset to apply to the instances
            - attributes (name=value) : value for named attributes

        Returns
        -------
            - Curve
        """

        curve = Curve()
        curve.join(self)

        curve *= count
        return curve

    # =============================================================================================================================
    # =============================================================================================================================
    # Constructors
    # =============================================================================================================================

    # -----------------------------------------------------------------------------------------------------------------------------
    # Test the constructors

    @staticmethod
    def all_primitives():

        curve = Curve()

        loc = np.array((0, 0, 0))

        # ----- Bezier Circle

        c = Curve.BezierCircle()
        c.points.translate(loc)
        loc[0] += 5
        curve.join(c)

        # ----- Poly Circle

        c = Curve.Circle()
        c.points.position += loc
        loc[0] += 5
        curve.join(c)

        # ----- Arc

        c = Curve.Arc()
        c.points.position += loc
        loc[0] += 5
        curve.join(c)

        # ----- BezierSegment

        c = Curve.BezierSegment()
        c.points.translate(loc)
        loc[0] += 5
        curve.join(c)

        # ----- Line

        c = Curve.Line()
        c.points.position += loc
        loc[0] += 5
        curve.join(c)

        # ----- Spiral

        c = Curve.Spiral()
        c.points.position += loc
        loc[0] += 5
        curve.join(c)

        # ----- Quadratic Bezier

        if False:
            c = Curve.QuadraticBezier()
            c.points.translate(loc)
            loc[0] += 5
            curve.join(c)

        # ----- Quadrilateral

        c = Curve.Quadrilateral()
        c.points.position += loc
        loc[0] += 5
        curve.join(c)

        curve.to_object("Curve primitives")

    @classmethod
    def BezierCircle(cls):
        return cls().add(points=[[-1.,  0.,  0.], [ 0.,  1.,  0.], [ 1.,  0.,  0.], [ 0., -1.,  0.]],
                         curve_type='BEZIER', cyclic=True,
                         handle_left = [[-1., -0.55212522,  0.], [-0.55212522,  1.,  0.], [ 1.,  0.55212522,  0.], [ 0.55212522, -1.,  0.]],
                         handle_right = [[-1.,  0.55212522,  0.], [ 0.55212522,  1.,  0. ],[ 1., -0.55212522,  0.], [-0.55212522, -1.,  0.]]
                         )

    @classmethod
    def Circle(cls, resolution=32, radius=1.):
        ags = np.linspace(0, 2*np.pi, resolution, endpoint=False)
        return cls().add(points=np.stack((radius*np.cos(ags), radius*np.sin(ags), np.zeros(resolution, float)), axis=-1),
                         curve_type='POLY', cyclic=True)

    @classmethod
    def Arc(cls, resolution=16, radius=1., start_angle=0., sweep_angle=7*np.pi/4, connect_center=False, invert_arc=False):
        ag0, ag1 = (start_angle + sweep_angle - 2*np.pi, start_angle) if invert_arc else (start_angle, start_angle + sweep_angle)
        ags = np.linspace(ag0, ag1, resolution)
        points = np.stack((radius*np.cos(ags), radius*np.sin(ags), np.zeros(resolution, float)), axis=-1)
        if connect_center:
            points = np.append(points, [(0, 0, 0)], axis=0)

        return cls().add(points=points, curve_type='POLY', cyclic=connect_center)

    @classmethod
    def BezierSegment(cls, resolution=16, start=(-1, 0, 0), start_handle=(-.5, .5, 0), end_handle=(0, 0, 0), end=(1, 0, 0)):
        points = np.array([start, end])
        return cls().add(points=points, curve_type='BEZIER',
                         handle_left  = [2*points[0] - start_handle, end_handle],
                         handle_right = [start_handle, 2*points[1] - end_handle]
                         )

    @classmethod
    def Line(cls, start=(0, 0, 0), end=(0, 0, 1), resolution=2):
        resolution = max(2, resolution)
        return cls().add(points=np.linspace(start, end, resolution), curve_type='POLY')

    @classmethod
    def Spiral(cls, resolution=32, rotations=2., start_radius=1., end_radius=2., height=2., reverse=False):
        count = 1 + int(rotations*resolution)
        # Reverse is strangely trigonometric!
        ags = np.linspace(0, 2*np.pi*rotations, count) * (1 if reverse else -1)
        rs  = np.linspace(start_radius, end_radius, count)
        return cls().add(points = np.stack((rs*np.cos(ags), rs*np.sin(ags), np.linspace(0, height, count)), axis=-1),
                         curve_type='POLY')

    @classmethod
    def QuadraticBezier(cls, resolution=16, start=(-1, 0, 0), middle=(0, 2, 0), end=(1, 0, 0)):
        raise Exception(f"Not implemented yet")

    @classmethod
    def Quadrilateral(cls, width=2., height=2.):
        return cls().add(points=[(-width/2, -height/2, 0), (width/2, -height/2, 0), (width/2, height/2, 0), (-width/2, height/2, 0)],
                                 curve_type='POLY', cyclic=True)

    @classmethod
    def Star(cls, points=8, inner_radius=1, outer_radius=2, twist=0.):

        points = max(3, points)
        ag = np.linspace(0, 2*np.pi, points, endpoint=False)

        vs = np.zeros((points, 2, 3), float)
        vs[:, 0, 0] = np.cos(ag)
        vs[:, 0, 1] = np.sin(ag)
        vs[:, 1, :2] = inner_radius * vs[:, 0, :2]
        vs[:, 0, :2] *= outer_radius

        rot = np.pi/points + twist
        M = np.zeros((2, 2), float)
        M[0, 0] = np.cos(rot)
        M[1, 1] = M[0, 0]
        M[1, 0] = np.sin(rot)
        M[0, 1] = -M[1, 0]

        vs[:, 1, :2] = np.einsum('...ij, ...j', M[None], vs[:, 1, :2])

        return cls().add(points=np.reshape(vs, (2*points, 3)), curve_type='POLY', cyclic=True)

    # =============================================================================================================================
    # Vector Field

    @classmethod
    def FieldLine(cls, field_func, start_point, max_len=10., prec=.01, sub_steps=10):

        pts = [start_point]
        rs  = [np.linalg.norm(field_func(start_point))]
        p   = np.array(start_point)
        l   = 0.
        for _ in range(10000):
            for _ in range(sub_steps):

                # ----- Vector at current location
                v0 = field_func(p)

                # ----- Precision along this vector
                norm  = np.sqrt(np.dot(v0, v0))
                factor = prec/norm
                v0 *= factor

                # ----- Average with target vector for more accurracy
                v1 = field_func(p + v0)*factor
                v = (v0 + v1)/2

                # ----- Next point
                p += v

            # ----- Segment length

            v = p - pts[-1]
            l += np.sqrt(np.dot(v, v))

            # ----- Add a new point

            pts.append(np.array(p))
            rs.append(norm)

            # ----- Done if loop or max_len is reached

            v = p - start_point
            cyclic = np.sqrt(np.dot(v, v)) < prec*(sub_steps-1)
            if cyclic or l >= max_len:
                pts.append(np.array(start_point))
                break

        if cyclic:
            pts.pop()

        line = cls().add(pts, curve_type='POLY', cyclic=cyclic)
        line.points.radius = rs

        return line

    # =============================================================================================================================
    # =============================================================================================================================
    # Lines of field

    # -----------------------------------------------------------------------------------------------------------------------------
    # Lines of field

    @classmethod
    def FieldLines(cls, field_func, start_points,
        backwards=False, max_length=None, length_scale=None, end_points=None, zero=1e-6, max_points=1000,
        precision=.1, sub_steps=10, seed=0, **kwargs):

        """ Build splines showing lines of field

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
        """

        splines = field.field_lines(field_func, start_points,
            backwards       = backwards,
            max_length      = max_length,
            length_scale    = length_scale,
            end_points      = end_points,
            zero            = zero,
            max_points      = max_points,
            precision       = precision,
            sub_steps       = sub_steps,
            seed            = seed,
            **kwargs)

        return cls(**splines)

        curves = cls()
        for avects, cyclic in lines:
            if len(avects) <= 1:
                continue
            curves.add(avects.co, curve_type='POLY', cyclic=cyclic, radius=avects.radius, tilt=avects.color)

        return curves

    # =============================================================================================================================
    # Lines of electric field

    @classmethod
    def ElectricFieldLines(cls, charge_locations, charges=1., field_color=True,
                           count=100, start_points=None, plane=None, plane_center=(0, 0, 0),
                           frag_length=None, frag_scale=None, max_points=1000,
                           precision=.1, sub_steps=10, seed=None):

        """ Create lines of field for a vector field generated by charges, typically an electric field.

        Arguments:
        ----------
            - charge_locations (array (n, 3) of vectors) : where the charges are located
            - charges (float or array (n) of floats = 1) : the charges
            - field_color (bool = True) : manage the field_color attribute
            - count (int = 100) : number of lines to create. Overriden by len(start_points) if not None
            - start_points (array (s, 3) of vectors = None) : the starting points to compute the lines from
            - plane (vector = None) = restrict start points to a plane defined by its perpendicular
            - plane_center (vector = (0, 0, 0)) : center of the plane
            - frag_length (float=None) : length of fragments, None for full lines
            - frag_scale (float=None) : length distribution scale
            - precision (float = .1) : step precision
            - sub_steps (int=10) : number of steps between two sucessive points of the lines
        """

        # ----------------------------------------------------------------------------------------------------
        # Field function

        poles = AttrVectors(charge_locations, charge=charges)
        field_func = lambda points: field.electric_field(points,
                            locations=poles.co, charges=poles.charge)

        # ----------------------------------------------------------------------------------------------------
        # Starting points

        rng = np.random.default_rng(seed=seed)
        n_charges = len(poles)

        backwards = rng.choice([True, False], count)
        if start_points is None:
            if frag_length is None:
                if plane is None:
                    start_points, _ = distribs.sphere_dist(radius=precision, count=count, seed=rng.integers(1<<63))
                else:
                    start_points, _ = distribs.circle_dist(radius=precision, count=count, seed=rng.integers(1<<63))
                    start_points = rotate_xy_into_plane(start_points, plane=plane, origin=plane_center)

                inds = rng.integers(0, n_charges, count)
                start_points += poles.co[inds]
                backwards[:] = poles.charge[inds] < 0

            else:
                center = np.average(poles.co, axis=0)
                bbox0, bbox1 = np.min(poles.co, axis=0), np.max(poles.co, axis=0)
                radius = 1.3*max(np.linalg.norm(bbox1 - center), np.linalg.norm(bbox0 - center))

                if plane is None:
                    start_points, _ = distribs.ball_dist(radius=radius, count=count, seed=rng.integers(1<<63))
                    start_points += center
                else:
                    start_points, _ = distribs.disk_dist(radius=radius, count=count, seed=rng.integers(1<<63))
                    start_points = rotate_xy_into_plane(start_points, plane=plane, origin=plane_center)

        else:
            if len(np.shape(start_points)) == 1:
                count = 1
            else:
                count = len(start_points)

        # ----------------------------------------------------------------------------------------------------
        # Field lines

        lines = field.field_lines(field_func,
            start_points    = start_points,
            backwards       = backwards,
            max_length      = frag_length,
            length_scale    = frag_scale,
            end_points      = charge_locations,
            max_points      = max_points,
            precision       = precision,
            sub_steps       = sub_steps,
            seed            = rng.integers(1 << 63),
            )

        return cls(**lines)

    # =============================================================================================================================
    # Lines of magnetic field

    @classmethod
    def MagneticFieldLines(cls, magnet_locations, moments=(1, 0, 0), field_color=True,
                           count=100, start_points=None, min_width=.3, plane=None, plane_center=(0, 0, 0),
                           frag_length=None, frag_scale=None, max_points=1000,
                           precision=.1, sub_steps=10, seed=None):

        """ Create lines of field for a vector field generated by bipoles, typically an magnetic field.

        Arguments:
        ----------
            - magnet_locations (array (n, 3) of vectors) : where the bipoles are located
            - moments (vector or array (n) of vectors = (1, 0, 0)) : the moments of the magnets
            - field_color (bool = True) : manage the field_color attribute
            - count (int = 100) : number of lines to create. Overriden by len(start_points) if not None
            - start_points (array (s, 3) of vectors = None) : the starting points to compute the lines from
            - min_width (float = .3) : min width for volume generation when magnet locations are in a plane
            - plane (vector = None) = restrict start points to a plane defined by its perpendicular
            - plane_center (vector = (0, 0, 0)) : center of the plane
            - frag_length (float=None) : length of fragments, None for full lines
            - frag_scale (float=None) : length distribution scale
            - precision (float = .1) : step precision
            - sub_steps (int=10) : number of steps between two sucessive points of the lines
        """

        # ----------------------------------------------------------------------------------------------------
        # Field function

        magnets = AttrVectors(magnet_locations, moment=moments)
        field_func = lambda points: field.magnetic_field(points,
                            locations=magnets.co, moments=magnets.moment)

        # ----------------------------------------------------------------------------------------------------
        # Starting points

        rng = np.random.default_rng(seed=seed)
        n_magnets = len(magnets)

        backwards = rng.choice([True, False], count)
        if start_points is None:
            if frag_length is None:
                if plane is None:
                    start_points, _ = distribs.sphere_dist(radius=precision*10, count=count, seed=rng.integers(1<<63))
                else:
                    start_points, _ = distribs.circle_dist(radius=precision*10, count=count, seed=rng.integers(1<<63))
                    start_points = rotate_xy_into_plane(start_points, plane=plane, origin=plane_center)

                inds = rng.integers(0, n_magnets, count)
                mag_locs = magnets.co[inds]
                backwards[:] = np.einsum('...i, ...i', start_points, magnets.moment[inds]) < 0
                start_points += mag_locs

            else:
                center = np.average(magnets.co, axis=0)
                bbox0, bbox1 = np.min(magnets.co, axis=0), np.max(magnets.co, axis=0)
                radius = 1.3*max(1., max(np.linalg.norm(bbox1 - center), np.linalg.norm(bbox0 - center)))

                if plane is None:
                    dims = np.maximum(bbox1 - bbox0, (min_width, min_width, min_width))
                    center = (bbox0 + bbox1)/2
                    bbox0, bbox1 = center - 1.3*dims, center + 1.3*dims

                    start_points, _ = distribs.cube_dist(corner0=bbox0, corner1=bbox1, count=count, seed=rng.integers(1<<63))
                else:
                    start_points, _ = distribs.disk_dist(radius=radius, count=count, seed=rng.integers(1<<63))
                    start_points = rotate_xy_into_plane(start_points, plane=plane, origin=plane_center)

        else:
            if len(np.shape(start_points)) == 1:
                count = 1
            else:
                count = len(start_points)

        # ----------------------------------------------------------------------------------------------------
        # Field lines

        lines = field.field_lines(field_func,
            start_points    = start_points,
            backwards       = backwards,
            max_length      = frag_length,
            length_scale    = frag_scale,
            end_points      = magnet_locations,
            max_points      = max_points,
            precision       = precision,
            sub_steps       = sub_steps,
            seed            = rng.integers(1 << 63),
            )

        return cls(**lines)

    # =============================================================================================================================
    # =============================================================================================================================
    # Operations

    def to_mesh(self, profile=None, caps=True, t0=None, t1=1.):

        from geonodes.core.mesh import Mesh

        # ---------------------------------------------------------------------------
        # Which profile for the section ?

        # tuple : (segments, radius)

        if profile is None:
            profile = (8, .1)

        elif isinstance(profile, (int, np.int64, np.int32)):
            profile = (profile, .1)

        if isinstance(profile, tuple):
            verts = Curve.Circle(resolution=profile[0], radius=profile[1]).splines[0].get_verts()

        # Str or object: must be a curve
        elif isinstance(profile, (str, bpy.types.Object)):
            verts = Curve.FromObject(profile).splines[0].get_verts()

        # A Curve  let's take the first spline
        elif isinstance(profile, Curve):
            verts = profile.splines[0].get_verts()

        elif hasattr(profile, '__call__'):
            verts = profile(0, 1)

        elif isinstance(profile, np.ndarray):
            verts = profile

        elif isinstance(profile, list):
            verts = np.array(profile)

        else:
            raise RuntimeError(f"Curve.to_mesh : impossible to use profile: {profile}")

        # ---------------------------------------------------------------------------
        # Loop on the splines

        mesh = Mesh(materials=self.materials)
        for i_spline, func in enumerate(self.splines.functions):

            cyclic = self.splines.cyclic[i_spline]

            # Curve back bone points

            bbone = func.sample_points
            if cyclic:
                bbone = bbone[:-1]

            # Locate, scale and rotate the rings

            radius = func.sample_value(self.splines[i_spline].get_points().radius)(np.linspace(0, 1, len(bbone)))

            transfos = tracker(func.tangent(np.linspace(0, 1, len(bbone), endpoint=not cyclic)), 'Z', 'X')
            transfos.position = bbone
            transfos.scale    = np.ones((len(bbone), 3))*radius[:, None]

            #if cyclic:
            #    transfos.rotation[-1] = transfos.rotation[0].inv()

            cyl_verts = transfos[:, None] @ np.resize(verts, (len(bbone),) + np.shape(verts))

            # Cylinder / torus topology
            if cyclic:
                cyl = topology.torus(x_count=len(verts), y_count=len(bbone), verts=cyl_verts)
            else:
                cyl = topology.cylinder(x_count=len(verts), y_count=1, z_count=len(bbone), caps='NGON' if caps else 'NONE', verts=cyl_verts)

            # Create the mesh

            meshed = Mesh(materials=self.materials, **cyl)

            # Transfer the attributes

            for name in self.splines.attributes.names:
                if name in ['loop_start', 'loop_total', 'curve_type', 'cyclic', 'resolution']:
                    continue

                meshed.points.attributes.copy_attribute(self.splines.attributes, name)
                setattr(meshed.points, name, getattr(self.splines, name))

            for name in self.points.attributes.names:
                if name in ['position', 'w', 'radius']:
                    continue

                vals = func.sample_value(getattr(self.splines[i_spline].get_points(), name))(np.linspace(0, 1, len(bbone)))

                meshed.points.attributes.copy_attribute(self.points.attributes, name)
                setattr(meshed.points, name, vals)

            # Join the new meshed spline
            mesh.join(meshed)

        return mesh
