#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-08-21
@author: Generated from generator module
Blender version: 3.2.2
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import geonodes.core.domains as domains

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Curve

class Curve(gn.Geometry):
    """ Data class Curve
    """

    def copy(self):

        return Curve(self)

    def init_domains(self):
        self.points  = domains.ControlPoint(self)
        self.splines = domains.Spline(self)

    @property
    def point(self):
        return self.points
    @property
    def spline(self):
        return self.splines


    def reset_properties(self):

        super().reset_properties()

        self.domain_size_ = None

        self.point_count_ = None

        self.spline_count_ = None

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION', node_label = None, node_color = None):
        """ Geometry node [*Bezier Segment*].
        
        
            Args:
                resolution: Integer
                start: Vector
                start_handle: Vector
                end_handle: Vector
                end: Vector
                mode (str): 'POSITION' in [POSITION, OFFSET]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.BezierSegment`
            
            
            .. blid:: GeometryNodeCurvePrimitiveBezierSegment
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode, label=node_label, node_color=node_color).curve)

    @classmethod
    def Circle(cls, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS', node_label = None, node_color = None):
        """ Geometry node [*Curve Circle*].
        
        
            Args:
                resolution: Integer
                point_1: Vector
                point_2: Vector
                point_3: Vector
                radius: Float
                mode (str): 'RADIUS' in [POINTS, RADIUS]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [curve (Curve), center (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CurveCircle`
            
            
            .. blid:: GeometryNodeCurvePrimitiveCircle
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode, label=node_label, node_color=node_color)
                
        """

        return nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode, label=node_label, node_color=node_color)

    @classmethod
    def Line(cls, start=None, end=None, direction=None, length=None, mode='POINTS', node_label = None, node_color = None):
        """ Geometry node [*Curve Line*].
        
        
            Args:
                start: Vector
                end: Vector
                direction: Vector
                length: Float
                mode (str): 'POINTS' in [POINTS, DIRECTION]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CurveLine`
            
            
            .. blid:: GeometryNodeCurvePrimitiveLine
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode, label=node_label, node_color=node_color).curve)

    @classmethod
    def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE', node_label = None, node_color = None):
        """ Geometry node [*Quadrilateral*].
        
        
            Args:
                width: Float
                height: Float
                bottom_width: Float
                top_width: Float
                offset: Float
                bottom_height: Float
                top_height: Float
                point_1: Vector
                point_2: Vector
                point_3: Vector
                point_4: Vector
                mode (str): 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Quadrilateral`
            
            
            .. blid:: GeometryNodeCurvePrimitiveQuadrilateral
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode, label=node_label, node_color=node_color).curve)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None, node_label = None, node_color = None):
        """ Geometry node [*Quadratic Bezier*].
        
        
            Args:
                resolution: Integer
                start: Vector
                middle: Vector
                end: Vector
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.QuadraticBezier`
            
            
            .. blid:: GeometryNodeCurveQuadraticBezier
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end, label=node_label, node_color=node_color).curve)

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None, node_label = None, node_color = None):
        """ Geometry node [*Star*].
        
        
            Args:
                points: Integer
                inner_radius: Float
                outer_radius: Float
                twist: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [curve (Curve), outer_points (Boolean)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Star`
            
            
            .. blid:: GeometryNodeCurveStar
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist, label=node_label, node_color=node_color)
                
        """

        return nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist, label=node_label, node_color=node_color)

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None, node_label = None, node_color = None):
        """ Geometry node [*Spiral*].
        
        
            Args:
                resolution: Integer
                rotations: Float
                start_radius: Float
                end_radius: Float
                height: Float
                reverse: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Spiral`
            
            
            .. blid:: GeometryNodeCurveSpiral
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse, label=node_label, node_color=node_color)
                
        """

        return cls(nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse, label=node_label, node_color=node_color).curve)

    @classmethod
    def ArcFromRadius(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None, node_label = None, node_color = None):
        """ Geometry node [*Arc*].
        
        
            Args:
                resolution: Integer
                radius: Float
                start_angle: Float
                sweep_angle: Float
                connect_center: Boolean
                invert_arc: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Arc`
            
                - mode = 'RADIUS'
                  
            .. blid:: GeometryNodeCurveArc
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS', label=node_label, node_color=node_color)
                
        """

        return cls(nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS', label=node_label, node_color=node_color).curve)


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def ArcFromPoints(resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None, node_label = None, node_color = None):
        """ Geometry node [*Arc*].
        
        
            Args:
                resolution: Integer
                start: Vector
                middle: Vector
                end: Vector
                offset_angle: Float
                connect_center: Boolean
                invert_arc: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [curve (Curve), center (Vector), normal (Vector), radius (Float)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.Arc`
            
                - mode = 'POINTS'
                  
            .. blid:: GeometryNodeCurveArc
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS', label=node_label, node_color=node_color)
                
        """

        return nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS', label=node_label, node_color=node_color)


    # ----------------------------------------------------------------------------------------------------
    # Properties

    @property
    def domain_size(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Sockets [point_count (Integer), spline_count (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'CURVE'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='CURVE', label=f"{self.node_chain_label}.domain_size")
                
        """

        if self.domain_size_ is None:
            self.domain_size_ = nodes.DomainSize(geometry=self, component='CURVE', label=f"{self.node_chain_label}.domain_size")
        return self.domain_size_

    @property
    def point_count(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Sockets [point_count (Integer), spline_count (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'CURVE'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='CURVE', label=f"{self.node_chain_label}.point_count")
                
        """

        return self.domain_size.point_count

    @property
    def spline_count(self):
        """ Geometry node [*Domain Size*].
        
        
        
            Returns:
                Sockets [point_count (Integer), spline_count (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DomainSize`
            
                - component = 'CURVE'
                  
            .. blid:: GeometryNodeAttributeDomainSize
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DomainSize(geometry=self, component='CURVE', label=f"{self.node_chain_label}.spline_count")
                
        """

        return self.domain_size.spline_count


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def set_cyclic(self, selection=None, cyclic=None, node_label = None, node_color = None):
        """ Geometry node [*Set Spline Cyclic*].
        
        
            Args:
                selection: Boolean
                cyclic: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetSplineCyclic`
            
            
            .. blid:: GeometryNodeSetSplineCyclic
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic, label=node_label, node_color=node_color))

    def set_resolution(self, selection=None, resolution=None, node_label = None, node_color = None):
        """ Geometry node [*Set Spline Resolution*].
        
        
            Args:
                selection: Boolean
                resolution: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Geometry
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetSplineResolution`
            
            
            .. blid:: GeometryNodeSetSplineResolution
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetSplineResolution(geometry=self, selection=selection, resolution=resolution, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetSplineResolution(geometry=self, selection=selection, resolution=resolution, label=node_label, node_color=node_color))

    def set_handles(self, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, node_label = None, node_color = None):
        """ Geometry node [*Set Handle Type*].
        
        
            Args:
                selection: Boolean
                handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
                mode (set): {'RIGHT', 'LEFT'}
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetHandleType`
            
            
            .. blid:: GeometryNodeCurveSetHandles
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode, label=node_label, node_color=node_color))

    def set_spline_type(self, selection=None, spline_type='POLY', node_label = None, node_color = None):
        """ Geometry node [*Set Spline Type*].
        
        
            Args:
                selection: Boolean
                spline_type (str): 'POLY' in [BEZIER, NURBS, POLY]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetSplineType`
            
            
            .. blid:: GeometryNodeCurveSplineType
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type, label=node_label, node_color=node_color))

    def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER', node_label = None, node_color = None):
        """ Geometry node [*Fillet Curve*].
        
        
            Args:
                count: Integer
                radius: Float
                limit_radius: Boolean
                mode (str): 'BEZIER' in [BEZIER, POLY]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.FilletCurve`
            
            
            .. blid:: GeometryNodeFilletCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode, label=node_label, node_color=node_color))

    def resample(self, selection=None, count=None, length=None, mode='COUNT', node_label = None, node_color = None):
        """ Geometry node [*Resample Curve*].
        
        
            Args:
                selection: Boolean
                count: Integer
                length: Float
                mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ResampleCurve`
            
            
            .. blid:: GeometryNodeResampleCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode, label=node_label, node_color=node_color))

    def reverse(self, selection=None, node_label = None, node_color = None):
        """ Geometry node [*Reverse Curve*].
        
        
            Args:
                selection: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.ReverseCurve`
            
            
            .. blid:: GeometryNodeReverseCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.ReverseCurve(curve=self, selection=selection, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.ReverseCurve(curve=self, selection=selection, label=node_label, node_color=node_color))

    def set_handle_positions(self, selection=None, position=None, offset=None, mode='LEFT', node_label = None, node_color = None):
        """ Geometry node [*Set Handle Positions*].
        
        
            Args:
                selection: Boolean
                position: Vector
                offset: Vector
                mode (str): 'LEFT' in [LEFT, RIGHT]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetHandlePositions`
            
            
            .. blid:: GeometryNodeSetCurveHandlePositions
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode, label=node_label, node_color=node_color))

    def set_radius(self, selection=None, radius=None, node_label = None, node_color = None):
        """ Geometry node [*Set Curve Radius*].
        
        
            Args:
                selection: Boolean
                radius: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetCurveRadius`
            
            
            .. blid:: GeometryNodeSetCurveRadius
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetCurveRadius(curve=self, selection=selection, radius=radius, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetCurveRadius(curve=self, selection=selection, radius=radius, label=node_label, node_color=node_color))

    def set_tilt(self, selection=None, tilt=None, node_label = None, node_color = None):
        """ Geometry node [*Set Curve Tilt*].
        
        
            Args:
                selection: Boolean
                tilt: Float
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SetCurveTilt`
            
            
            .. blid:: GeometryNodeSetCurveTilt
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt, label=node_label, node_color=node_color))

    def subdivide(self, cuts=None, node_label = None, node_color = None):
        """ Geometry node [*Subdivide Curve*].
        
        
            Args:
                cuts: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SubdivideCurve`
            
            
            .. blid:: GeometryNodeSubdivideCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SubdivideCurve(curve=self, cuts=cuts, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.SubdivideCurve(curve=self, cuts=cuts, label=node_label, node_color=node_color))

    def trim(self, start0=None, end0=None, start1=None, end1=None, mode='FACTOR', node_label = None, node_color = None):
        """ Geometry node [*Trim Curve*].
        
        
            Args:
                start0: Float
                end0: Float
                start1: Float
                end1: Float
                mode (str): 'FACTOR' in [FACTOR, LENGTH]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Curve
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.TrimCurve`
            
            
            .. blid:: GeometryNodeTrimCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode, label=node_label, node_color=node_color)
                
        """

        return self.stack(nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode, label=node_label, node_color=node_color))

    def duplicate_splines(self, selection=None, amount=None, node_label = None, node_color = None):
        """ Geometry node [*Duplicate Elements*].
        
        
            Args:
                selection: Boolean
                amount: Integer
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [geometry (Geometry), duplicate_index (Integer)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.DuplicateElements`
            
                - domain = 'SPLINE'
                  
            .. blid:: GeometryNodeDuplicateElements
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='SPLINE', label=node_label, node_color=node_color)
                
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='SPLINE', label=node_label, node_color=node_color)

    def fill(self, mode='TRIANGLES', node_label = None, node_color = None):
        """ Geometry node [*Fill Curve*].
        
        
            Args:
                mode (str): 'TRIANGLES' in [TRIANGLES, NGONS]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.FillCurve`
            
            
            .. blid:: GeometryNodeFillCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.FillCurve(curve=self, mode=mode, label=node_label, node_color=node_color)
                
        """

        return nodes.FillCurve(curve=self, mode=mode, label=node_label, node_color=node_color).mesh

    def to_mesh(self, profile_curve=None, fill_caps=None, node_label = None, node_color = None):
        """ Geometry node [*Curve to Mesh*].
        
        
            Args:
                profile_curve: Geometry
                fill_caps: Boolean
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Mesh
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CurveToMesh`
            
            
            .. blid:: GeometryNodeCurveToMesh
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps, label=node_label, node_color=node_color)
                
        """

        return nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps, label=node_label, node_color=node_color).mesh

    def to_points(self, count=None, length=None, mode='COUNT', node_label = None, node_color = None):
        """ Geometry node [*Curve to Points*].
        
        
            Args:
                count: Integer
                length: Float
                mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CurveToPoints`
            
            
            .. blid:: GeometryNodeCurveToPoints
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode, label=node_label, node_color=node_color)
                
        """

        return nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode, label=node_label, node_color=node_color)

    def sample(self, factor=None, length=None, mode='LENGTH', node_label = None, node_color = None):
        """ Geometry node [*Sample Curve*].
        
        
            Args:
                factor: Float
                length: Float
                mode (str): 'LENGTH' in [FACTOR, LENGTH]
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Sockets [position (Vector), tangent (Vector), normal (Vector)]
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.SampleCurve`
            
            
            .. blid:: GeometryNodeSampleCurve
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.SampleCurve(curve=self, factor=factor, length=length, mode=mode, label=node_label, node_color=node_color)
                
        """

        return nodes.SampleCurve(curve=self, factor=factor, length=length, mode=mode, label=node_label, node_color=node_color)

    def length(self, node_label = None, node_color = None):
        """ Geometry node [*Curve Length*].
        
        
            Args:
                node_label (str): Node label
                node_color (color): Node background color
                
            Returns:
                Float
                
            **Node creation**
            
            Node :class:`~geonodes.nodes.nodes.CurveLength`
            
            
            .. blid:: GeometryNodeCurveLength
            
            .. code-block:: python
            
                from geonodes import nodes
                nodes.CurveLength(curve=self, label=node_label, node_color=node_color)
                
        """

        return nodes.CurveLength(curve=self, label=node_label, node_color=node_color).length


