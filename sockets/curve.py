import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Curve

class Curve(gn.Spline):
    """ 

    Data socket Curve
    -----------------
        > Inherits from gn.Spline
          
        <sub>go to index</sub>
        
        
    

        Constructors
        ------------
            - ArcFromRadius : curve (Curve)
            - BezierSegment : curve (Curve)
            - Circle : Sockets      [curve (Curve), center (Vector)]
            - Line : curve (Curve)
            - QuadraticBezier : curve (Curve)
            - Quadrilateral : curve (Curve)
            - Spiral : curve (Curve)
            - Star : Sockets      [curve (Curve), outer_points (Boolean)]
    

        Static methods
        --------------
            - ArcFromPoints : Sockets      [curve (Curve), center (Vector), normal (Vector), radius (Float)]
    

        Methods
        -------
            - fill : mesh (Mesh)
            - fillet : curve (Curve)
            - length : length (Float)
            - resample : curve (Curve)
            - reverse : curve (Curve)
            - sample : Sockets      [position (Vector), tangent (Vector), normal (Vector)]
            - set_handle_positions : curve (Curve)
            - set_handles : curve (Curve)
            - set_radius : curve (Curve)
            - set_spline_type : curve (Curve)
            - set_tilt : curve (Curve)
            - subdivide : curve (Curve)
            - to_mesh : mesh (Mesh)
            - to_points : Sockets      [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]
            - trim : curve (Curve)
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """ > Node: BezierSegment
          
        <sub>go to: top index
        blender ref GeometryNodeCurvePrimitiveBezierSegment
        node ref Bezier Segment </sub>
        
        ```python
        v = Curve.BezierSegment(resolution, start, start_handle, end_handle, end, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - resolution : Integer
            - start : Vector
            - start_handle : Vector
            - end_handle : Vector
            - end : Vector## Parameters
            - mode : 'POSITION' in [POSITION, OFFSET]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode)
            ```
    

        Returns
        -------
            Curve
            
        """

        return cls(nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode).curve)

    @classmethod
    def Circle(cls, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS'):
        """ > Node: CurveCircle
          
        <sub>go to: top index
        blender ref GeometryNodeCurvePrimitiveCircle
        node ref Curve Circle </sub>
        
        ```python
        v = Curve.Circle(resolution, point_1, point_2, point_3, radius, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - resolution : Integer
            - point_1 : Vector
            - point_2 : Vector
            - point_3 : Vector
            - radius : Float## Parameters
            - mode : 'RADIUS' in [POINTS, RADIUS]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode)
            ```
    

        Returns
        -------
            Sockets [curve (Curve), center (Vector)]
            
        """

        return nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode)

    @classmethod
    def Line(cls, start=None, end=None, direction=None, length=None, mode='POINTS'):
        """ > Node: CurveLine
          
        <sub>go to: top index
        blender ref GeometryNodeCurvePrimitiveLine
        node ref Curve Line </sub>
        
        ```python
        v = Curve.Line(start, end, direction, length, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - start : Vector
            - end : Vector
            - direction : Vector
            - length : Float## Parameters
            - mode : 'POINTS' in [POINTS, DIRECTION]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode)
            ```
    

        Returns
        -------
            Curve
            
        """

        return cls(nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode).curve)

    @classmethod
    def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):
        """ > Node: Quadrilateral
          
        <sub>go to: top index
        blender ref GeometryNodeCurvePrimitiveQuadrilateral
        node ref Quadrilateral </sub>
        
        ```python
        v = Curve.Quadrilateral(width, height, bottom_width, top_width, offset, bottom_height, top_height, point_1, point_2, point_3, point_4, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - width : Float
            - height : Float
            - bottom_width : Float
            - top_width : Float
            - offset : Float
            - bottom_height : Float
            - top_height : Float
            - point_1 : Vector
            - point_2 : Vector
            - point_3 : Vector
            - point_4 : Vector## Parameters
            - mode : 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode)
            ```
    

        Returns
        -------
            Curve
            
        """

        return cls(nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode).curve)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """ > Node: QuadraticBezier
          
        <sub>go to: top index
        blender ref GeometryNodeCurveQuadraticBezier
        node ref Quadratic Bezier </sub>
        
        ```python
        v = Curve.QuadraticBezier(resolution, start, middle, end)
        ```
    

        Arguments
        ---------
            ## Sockets
            - resolution : Integer
            - start : Vector
            - middle : Vector
            - end : Vector
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end)
            ```
    

        Returns
        -------
            Curve
            
        """

        return cls(nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end).curve)

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """ > Node: Star
          
        <sub>go to: top index
        blender ref GeometryNodeCurveStar
        node ref Star </sub>
        
        ```python
        v = Curve.Star(points, inner_radius, outer_radius, twist)
        ```
    

        Arguments
        ---------
            ## Sockets
            - points : Integer
            - inner_radius : Float
            - outer_radius : Float
            - twist : Float
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)
            ```
    

        Returns
        -------
            Sockets [curve (Curve), outer_points (Boolean)]
            
        """

        return nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """ > Node: Spiral
          
        <sub>go to: top index
        blender ref GeometryNodeCurveSpiral
        node ref Spiral </sub>
        
        ```python
        v = Curve.Spiral(resolution, rotations, start_radius, end_radius, height, reverse)
        ```
    

        Arguments
        ---------
            ## Sockets
            - resolution : Integer
            - rotations : Float
            - start_radius : Float
            - end_radius : Float
            - height : Float
            - reverse : Boolean
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse)
            ```
    

        Returns
        -------
            Curve
            
        """

        return cls(nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse).curve)

    @classmethod
    def ArcFromRadius(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):
        """ > Node: Arc
          
        <sub>go to: top index
        blender ref GeometryNodeCurveArc
        node ref Arc </sub>
        
        ```python
        v = Curve.ArcFromRadius(resolution, radius, start_angle, sweep_angle, connect_center, invert_arc)
        ```
    

        Arguments
        ---------
            ## Sockets
            - resolution : Integer
            - radius : Float
            - start_angle : Float
            - sweep_angle : Float
            - connect_center : Boolean
            - invert_arc : Boolean## Fixed parameters
            - mode : 'RADIUS'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS')
            ```
    

        Returns
        -------
            Curve
            
        """

        return cls(nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS').curve)


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def ArcFromPoints(resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):
        """ > Node: Arc
          
        <sub>go to: top index
        blender ref GeometryNodeCurveArc
        node ref Arc </sub>
        
        ```python
        v = Curve.ArcFromPoints(resolution, start, middle, end, offset_angle, connect_center, invert_arc)
        ```
    

        Arguments
        ---------
            ## Sockets
            - resolution : Integer
            - start : Vector
            - middle : Vector
            - end : Vector
            - offset_angle : Float
            - connect_center : Boolean
            - invert_arc : Boolean## Fixed parameters
            - mode : 'POINTS'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS')
            ```
    

        Returns
        -------
            Sockets [curve (Curve), center (Vector), normal (Vector), radius (Float)]
            
        """

        return nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def set_handles(self, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ > Node: SetHandleType
          
        <sub>go to: top index
        blender ref GeometryNodeCurveSetHandles
        node ref Set Handle Type </sub>
        
        ```python
        v = curve.set_handles(selection, handle_type, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - selection : Boolean## Parameters
            - handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            - mode : {'LEFT', 'RIGHT'}
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode))

    def set_spline_type(self, selection=None, spline_type='POLY'):
        """ > Node: SetSplineType
          
        <sub>go to: top index
        blender ref GeometryNodeCurveSplineType
        node ref Set Spline Type </sub>
        
        ```python
        v = curve.set_spline_type(selection, spline_type)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - selection : Boolean## Parameters
            - spline_type : 'POLY' in [BEZIER, NURBS, POLY]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type))

    def fill(self, mode='TRIANGLES'):
        """ > Node: FillCurve
          
        <sub>go to: top index
        blender ref GeometryNodeFillCurve
        node ref Fill Curve </sub>
        
        ```python
        v = curve.fill(mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)## Parameters
            - mode : 'TRIANGLES' in [TRIANGLES, NGONS]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FillCurve(curve=self, mode=mode)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return self.stack(nodes.FillCurve(curve=self, mode=mode))

    def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):
        """ > Node: FilletCurve
          
        <sub>go to: top index
        blender ref GeometryNodeFilletCurve
        node ref Fillet Curve </sub>
        
        ```python
        v = curve.fillet(count, radius, limit_radius, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - count : Integer
            - radius : Float
            - limit_radius : Boolean## Parameters
            - mode : 'BEZIER' in [BEZIER, POLY]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode))

    def resample(self, selection=None, count=None, length=None, mode='COUNT'):
        """ > Node: ResampleCurve
          
        <sub>go to: top index
        blender ref GeometryNodeResampleCurve
        node ref Resample Curve </sub>
        
        ```python
        v = curve.resample(selection, count, length, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - selection : Boolean
            - count : Integer
            - length : Float## Parameters
            - mode : 'COUNT' in [EVALUATED, COUNT, LENGTH]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode))

    def reverse(self, selection=None):
        """ > Node: ReverseCurve
          
        <sub>go to: top index
        blender ref GeometryNodeReverseCurve
        node ref Reverse Curve </sub>
        
        ```python
        v = curve.reverse(selection)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - selection : Boolean
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ReverseCurve(curve=self, selection=selection)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.ReverseCurve(curve=self, selection=selection))

    def set_handle_positions(self, selection=None, position=None, offset=None, mode='LEFT'):
        """ > Node: SetHandlePositions
          
        <sub>go to: top index
        blender ref GeometryNodeSetCurveHandlePositions
        node ref Set Handle Positions </sub>
        
        ```python
        v = curve.set_handle_positions(selection, position, offset, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - selection : Boolean
            - position : Vector
            - offset : Vector## Parameters
            - mode : 'LEFT' in [LEFT, RIGHT]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode))

    def set_radius(self, selection=None, radius=None):
        """ > Node: SetCurveRadius
          
        <sub>go to: top index
        blender ref GeometryNodeSetCurveRadius
        node ref Set Curve Radius </sub>
        
        ```python
        v = curve.set_radius(selection, radius)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - selection : Boolean
            - radius : Float
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetCurveRadius(curve=self, selection=selection, radius=radius)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.SetCurveRadius(curve=self, selection=selection, radius=radius))

    def set_tilt(self, selection=None, tilt=None):
        """ > Node: SetCurveTilt
          
        <sub>go to: top index
        blender ref GeometryNodeSetCurveTilt
        node ref Set Curve Tilt </sub>
        
        ```python
        v = curve.set_tilt(selection, tilt)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - selection : Boolean
            - tilt : Float
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt))

    def subdivide(self, cuts=None):
        """ > Node: SubdivideCurve
          
        <sub>go to: top index
        blender ref GeometryNodeSubdivideCurve
        node ref Subdivide Curve </sub>
        
        ```python
        v = curve.subdivide(cuts)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - cuts : Integer
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SubdivideCurve(curve=self, cuts=cuts)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.SubdivideCurve(curve=self, cuts=cuts))

    def trim(self, start0=None, end0=None, start1=None, end1=None, mode='FACTOR'):
        """ > Node: TrimCurve
          
        <sub>go to: top index
        blender ref GeometryNodeTrimCurve
        node ref Trim Curve </sub>
        
        ```python
        v = curve.trim(start0, end0, start1, end1, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - start0 : Float
            - end0 : Float
            - start1 : Float
            - end1 : Float## Parameters
            - mode : 'FACTOR' in [FACTOR, LENGTH]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode)
            ```
    

        Returns
        -------
            Curve
            
        """

        return self.stack(nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode))

    def to_mesh(self, profile_curve=None, fill_caps=None):
        """ > Node: CurveToMesh
          
        <sub>go to: top index
        blender ref GeometryNodeCurveToMesh
        node ref Curve to Mesh </sub>
        
        ```python
        v = curve.to_mesh(profile_curve, fill_caps)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - profile_curve : Geometry
            - fill_caps : Boolean
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps)
            ```
    

        Returns
        -------
            Mesh
            
        """

        return nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps).mesh

    def to_points(self, count=None, length=None, mode='COUNT'):
        """ > Node: CurveToPoints
          
        <sub>go to: top index
        blender ref GeometryNodeCurveToPoints
        node ref Curve to Points </sub>
        
        ```python
        v = curve.to_points(count, length, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - count : Integer
            - length : Float## Parameters
            - mode : 'COUNT' in [EVALUATED, COUNT, LENGTH]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode)
            ```
    

        Returns
        -------
            Sockets [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]
            
        """

        return nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode)

    def sample(self, factor=None, length=None, mode='LENGTH'):
        """ > Node: SampleCurve
          
        <sub>go to: top index
        blender ref GeometryNodeSampleCurve
        node ref Sample Curve </sub>
        
        ```python
        v = curve.sample(factor, length, mode)
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
            - factor : Float
            - length : Float## Parameters
            - mode : 'LENGTH' in [FACTOR, LENGTH]
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SampleCurve(curve=self, factor=factor, length=length, mode=mode)
            ```
    

        Returns
        -------
            Sockets [position (Vector), tangent (Vector), normal (Vector)]
            
        """

        return nodes.SampleCurve(curve=self, factor=factor, length=length, mode=mode)

    def length(self):
        """ > Node: CurveLength
          
        <sub>go to: top index
        blender ref GeometryNodeCurveLength
        node ref Curve Length </sub>
        
        ```python
        v = curve.length()
        ```
    

        Arguments
        ---------
            ## Sockets
            - curve : Curve (self)
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveLength(curve=self)
            ```
    

        Returns
        -------
            Float
            
        """

        return nodes.CurveLength(curve=self).length


