import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Curve

class Curve(gn.Spline):
    """ Class Curve
    

    | Inherits from: gn.Spline 
    Index 
    

    Constructors
    ============
    - **ArcFromRadius**   : Arc curve (Curve) 
    - **BezierSegment**   : BezierSegment curve (Curve) 
    - **Circle**          : CurveCircle Sockets      [curve (Curve), center (Vector)] 
    - **Line**            : CurveLine curve (Curve) 
    - **QuadraticBezier** : QuadraticBezier curve (Curve) 
    - **Quadrilateral**   : Quadrilateral curve (Curve) 
    - **Spiral**          : Spiral curve (Curve) 
    - **Star**            : Star Sockets      [curve (Curve), outer_points (Boolean)] 
    

    Static methods
    ==============
    - **ArcFromPoints** : Arc Sockets      [curve (Curve), center (Vector), normal (Vector), radius (Float)]
    

    Methods
    =======
    - **length**    : CurveLength length (Float) 
    - **sample**    : SampleCurve Sockets      [position (Vector), tangent (Vector), normal (Vector)] 
    - **to_mesh**   : CurveToMesh mesh (Mesh) 
    - **to_points** : CurveToPoints Sockets      [points (Points), tangent (Vector), normal (Vector), rotation
      (Vector)] 
    

    Stacked methods
    ===============
    - **fill**                 : FillCurve Curve 
    - **fillet**               : FilletCurve Curve 
    - **resample**             : ResampleCurve Curve 
    - **reverse**              : ReverseCurve Curve 
    - **set_handle_positions** : SetHandlePositions Curve 
    - **set_handles**          : SetHandleType Curve 
    - **set_radius**           : SetCurveRadius Curve 
    - **set_spline_type**      : SetSplineType Curve 
    - **set_tilt**             : SetCurveTilt Curve 
    - **subdivide**            : SubdivideCurve Curve 
    - **trim**                 : TrimCurve Curve 
    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """ BezierSegment
        

        | Node: BezierSegment 
        Top Index 
        

            v = Curve.BezierSegment(resolution, start, start_handle, end_handle, end, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - resolution   : Integer 
            - start        : Vector 
            - start_handle : Vector 
            - end_handle   : Vector 
            - end          : Vector 
        

            Parameters arguments
            --------------------
            - mode : 'POSITION' in [POSITION, OFFSET] 
        

        Node creation
        =============
        

            node = nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle,
            end=end, mode=mode) 
        

        Returns
        =======
                Curve 
        """

        return cls(nodes.BezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode).curve)

    @classmethod
    def Circle(cls, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS'):
        """ Circle
        

        | Node: CurveCircle 
        Top Index 
        

            v = Curve.Circle(resolution, point_1, point_2, point_3, radius, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - resolution : Integer 
            - point_1    : Vector 
            - point_2    : Vector 
            - point_3    : Vector 
            - radius     : Float 
        

            Parameters arguments
            --------------------
            - mode : 'RADIUS' in [POINTS, RADIUS] 
        

        Node creation
        =============
        

            node = nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius,
            mode=mode) 
        

        Returns
        =======
                Sockets [curve (Curve), center (Vector)] 
        """

        return nodes.CurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode)

    @classmethod
    def Line(cls, start=None, end=None, direction=None, length=None, mode='POINTS'):
        """ Line
        

        | Node: CurveLine 
        Top Index 
        

            v = Curve.Line(start, end, direction, length, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - start     : Vector 
            - end       : Vector 
            - direction : Vector 
            - length    : Float 
        

            Parameters arguments
            --------------------
            - mode : 'POINTS' in [POINTS, DIRECTION] 
        

        Node creation
        =============
        

            node = nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode) 
        

        Returns
        =======
                Curve 
        """

        return cls(nodes.CurveLine(start=start, end=end, direction=direction, length=length, mode=mode).curve)

    @classmethod
    def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):
        """ Quadrilateral
        

        | Node: Quadrilateral 
        Top Index 
        

            v = Curve.Quadrilateral(width, height, bottom_width, top_width, offset, bottom_height, top_height, point_1,
            point_2, point_3, point_4, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - width         : Float 
            - height        : Float 
            - bottom_width  : Float 
            - top_width     : Float 
            - offset        : Float 
            - bottom_height : Float 
            - top_height    : Float 
            - point_1       : Vector 
            - point_2       : Vector 
            - point_3       : Vector 
            - point_4       : Vector 
        

            Parameters arguments
            --------------------
            - mode : 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS] 
        

        Node creation
        =============
        

            node = nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width,
            offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3,
            point_4=point_4, mode=mode) 
        

        Returns
        =======
                Curve 
        """

        return cls(nodes.Quadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode).curve)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """ QuadraticBezier
        

        | Node: QuadraticBezier 
        Top Index 
        

            v = Curve.QuadraticBezier(resolution, start, middle, end) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - resolution : Integer 
            - start      : Vector 
            - middle     : Vector 
            - end        : Vector 
        

        Node creation
        =============
        

            node = nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end) 
        

        Returns
        =======
                Curve 
        """

        return cls(nodes.QuadraticBezier(resolution=resolution, start=start, middle=middle, end=end).curve)

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """ Star
        

        | Node: Star 
        Top Index 
        

            v = Curve.Star(points, inner_radius, outer_radius, twist) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - points       : Integer 
            - inner_radius : Float 
            - outer_radius : Float 
            - twist        : Float 
        

        Node creation
        =============
        

            node = nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist) 
        

        Returns
        =======
                Sockets [curve (Curve), outer_points (Boolean)] 
        """

        return nodes.Star(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """ Spiral
        

        | Node: Spiral 
        Top Index 
        

            v = Curve.Spiral(resolution, rotations, start_radius, end_radius, height, reverse) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - resolution   : Integer 
            - rotations    : Float 
            - start_radius : Float 
            - end_radius   : Float 
            - height       : Float 
            - reverse      : Boolean 
        

        Node creation
        =============
        

            node = nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius,
            height=height, reverse=reverse) 
        

        Returns
        =======
                Curve 
        """

        return cls(nodes.Spiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse).curve)

    @classmethod
    def ArcFromRadius(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):
        """ ArcFromRadius
        

        | Node: Arc 
        Top Index 
        

            v = Curve.ArcFromRadius(resolution, radius, start_angle, sweep_angle, connect_center, invert_arc) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - resolution     : Integer 
            - radius         : Float 
            - start_angle    : Float 
            - sweep_angle    : Float 
            - connect_center : Boolean 
            - invert_arc     : Boolean 
        

            Fixed parameters
            ----------------
            - mode : 'RADIUS' 
        

        Node creation
        =============
        

            node = nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle,
            connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS') 
        

        Returns
        =======
                Curve 
        """

        return cls(nodes.Arc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS').curve)


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def ArcFromPoints(resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):
        """ ArcFromPoints
        

        | Node: Arc 
        Top Index 
        

            v = Curve.ArcFromPoints(resolution, start, middle, end, offset_angle, connect_center, invert_arc) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - resolution     : Integer 
            - start          : Vector 
            - middle         : Vector 
            - end            : Vector 
            - offset_angle   : Float 
            - connect_center : Boolean 
            - invert_arc     : Boolean 
        

            Fixed parameters
            ----------------
            - mode : 'POINTS' 
        

        Node creation
        =============
        

            node = nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle,
            connect_center=connect_center, invert_arc=invert_arc, mode='POINTS') 
        

        Returns
        =======
                Sockets [curve (Curve), center (Vector), normal (Vector), radius (Float)] 
        """

        return nodes.Arc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, profile_curve=None, fill_caps=None):
        """ to_mesh
        

        | Node: CurveToMesh 
        Top Index 
        

            v = curve.to_mesh(profile_curve, fill_caps) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve         : Curve (self) 
            - profile_curve : Geometry 
            - fill_caps     : Boolean 
        

        Node creation
        =============
        

            node = nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps) 
        

        Returns
        =======
                Mesh 
        """

        return nodes.CurveToMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps).mesh

    def to_points(self, count=None, length=None, mode='COUNT'):
        """ to_points
        

        | Node: CurveToPoints 
        Top Index 
        

            v = curve.to_points(count, length, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve  : Curve (self) 
            - count  : Integer 
            - length : Float 
        

            Parameters arguments
            --------------------
            - mode : 'COUNT' in [EVALUATED, COUNT, LENGTH] 
        

        Node creation
        =============
        

            node = nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode) 
        

        Returns
        =======
                Sockets [points (Points), tangent (Vector), normal (Vector), rotation (Vector)] 
        """

        return nodes.CurveToPoints(curve=self, count=count, length=length, mode=mode)

    def sample(self, factor=None, length=None, mode='LENGTH'):
        """ sample
        

        | Node: SampleCurve 
        Top Index 
        

            v = curve.sample(factor, length, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve  : Curve (self) 
            - factor : Float 
            - length : Float 
        

            Parameters arguments
            --------------------
            - mode : 'LENGTH' in [FACTOR, LENGTH] 
        

        Node creation
        =============
        

            node = nodes.SampleCurve(curve=self, factor=factor, length=length, mode=mode) 
        

        Returns
        =======
                Sockets [position (Vector), tangent (Vector), normal (Vector)] 
        """

        return nodes.SampleCurve(curve=self, factor=factor, length=length, mode=mode)

    def length(self):
        """ length
        

        | Node: CurveLength 
        Top Index 
        

            v = curve.length() 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve : Curve (self) 
        

        Node creation
        =============
        

            node = nodes.CurveLength(curve=self) 
        

        Returns
        =======
                Float 
        """

        return nodes.CurveLength(curve=self).length


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_handles(self, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """ set_handles
        

        | Node: SetHandleType 
        Top Index 
        

            curve.set_handles(selection, handle_type, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve     : Curve (self) 
            - selection : Boolean 
        

            Parameters arguments
            --------------------
            - handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN] 
            - mode        : {'RIGHT', 'LEFT'} 
        

        Node creation
        =============
        

            node = nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode))

    def set_spline_type(self, selection=None, spline_type='POLY'):
        """ set_spline_type
        

        | Node: SetSplineType 
        Top Index 
        

            curve.set_spline_type(selection, spline_type) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve     : Curve (self) 
            - selection : Boolean 
        

            Parameters arguments
            --------------------
            - spline_type : 'POLY' in [BEZIER, NURBS, POLY] 
        

        Node creation
        =============
        

            node = nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetSplineType(curve=self, selection=selection, spline_type=spline_type))

    def fill(self, mode='TRIANGLES'):
        """ fill
        

        | Node: FillCurve 
        Top Index 
        

            curve.fill(mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve : Curve (self) 
        

            Parameters arguments
            --------------------
            - mode : 'TRIANGLES' in [TRIANGLES, NGONS] 
        

        Node creation
        =============
        

            node = nodes.FillCurve(curve=self, mode=mode) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.FillCurve(curve=self, mode=mode))

    def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):
        """ fillet
        

        | Node: FilletCurve 
        Top Index 
        

            curve.fillet(count, radius, limit_radius, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve        : Curve (self) 
            - count        : Integer 
            - radius       : Float 
            - limit_radius : Boolean 
        

            Parameters arguments
            --------------------
            - mode : 'BEZIER' in [BEZIER, POLY] 
        

        Node creation
        =============
        

            node = nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode)
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.FilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode))

    def resample(self, selection=None, count=None, length=None, mode='COUNT'):
        """ resample
        

        | Node: ResampleCurve 
        Top Index 
        

            curve.resample(selection, count, length, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve     : Curve (self) 
            - selection : Boolean 
            - count     : Integer 
            - length    : Float 
        

            Parameters arguments
            --------------------
            - mode : 'COUNT' in [EVALUATED, COUNT, LENGTH] 
        

        Node creation
        =============
        

            node = nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.ResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode))

    def reverse(self, selection=None):
        """ reverse
        

        | Node: ReverseCurve 
        Top Index 
        

            curve.reverse(selection) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve     : Curve (self) 
            - selection : Boolean 
        

        Node creation
        =============
        

            node = nodes.ReverseCurve(curve=self, selection=selection) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.ReverseCurve(curve=self, selection=selection))

    def set_handle_positions(self, selection=None, position=None, offset=None, mode='LEFT'):
        """ set_handle_positions
        

        | Node: SetHandlePositions 
        Top Index 
        

            curve.set_handle_positions(selection, position, offset, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve     : Curve (self) 
            - selection : Boolean 
            - position  : Vector 
            - offset    : Vector 
        

            Parameters arguments
            --------------------
            - mode : 'LEFT' in [LEFT, RIGHT] 
        

        Node creation
        =============
        

            node = nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode)
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode))

    def set_radius(self, selection=None, radius=None):
        """ set_radius
        

        | Node: SetCurveRadius 
        Top Index 
        

            curve.set_radius(selection, radius) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve     : Curve (self) 
            - selection : Boolean 
            - radius    : Float 
        

        Node creation
        =============
        

            node = nodes.SetCurveRadius(curve=self, selection=selection, radius=radius) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetCurveRadius(curve=self, selection=selection, radius=radius))

    def set_tilt(self, selection=None, tilt=None):
        """ set_tilt
        

        | Node: SetCurveTilt 
        Top Index 
        

            curve.set_tilt(selection, tilt) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve     : Curve (self) 
            - selection : Boolean 
            - tilt      : Float 
        

        Node creation
        =============
        

            node = nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SetCurveTilt(curve=self, selection=selection, tilt=tilt))

    def subdivide(self, cuts=None):
        """ subdivide
        

        | Node: SubdivideCurve 
        Top Index 
        

            curve.subdivide(cuts) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve : Curve (self) 
            - cuts  : Integer 
        

        Node creation
        =============
        

            node = nodes.SubdivideCurve(curve=self, cuts=cuts) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.SubdivideCurve(curve=self, cuts=cuts))

    def trim(self, start0=None, end0=None, start1=None, end1=None, mode='FACTOR'):
        """ trim
        

        | Node: TrimCurve 
        Top Index 
        

            curve.trim(start0, end0, start1, end1, mode) 
        

        Arguments
        =========
        

            Sockets arguments
            -----------------
            - curve  : Curve (self) 
            - start0 : Float 
            - end0   : Float 
            - start1 : Float 
            - end1   : Float 
        

            Parameters arguments
            --------------------
            - mode : 'FACTOR' in [FACTOR, LENGTH] 
        

        Node creation
        =============
        

            node = nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode) 
        

        Returns
        =======
                self 
        """

        return self.stack(nodes.TrimCurve(curve=self, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode))


