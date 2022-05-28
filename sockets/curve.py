import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes

import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Curve

class Curve(gn.Spline):
    """ Data socket Curve

    Constructors
    ------------
        ArcFromRadius             : curve        (Geometry)
        BezierSegment             : curve        (Geometry)
        Circle                    : Sockets      [curve (Geometry), center (Vector)]
        Line                      : curve        (Geometry)
        QuadraticBezier           : curve        (Geometry)
        Quadrilateral             : curve        (Geometry)
        Spiral                    : curve        (Geometry)
        Star                      : Sockets      [curve (Geometry), outer_points (Boolean)]

    Static methods
    --------------
        ArcFromPoints             : Sockets      [curve (Geometry), center (Vector), normal (Vector), radius (Float)]

    Attribute captures
    ------------------
        capture_endpoint_selection : selection    (Boolean)
        capture_handle_positions  : Sockets      [left (Vector), right (Vector)]
        capture_handle_type_selection : selection    (Boolean)
        capture_radius            : radius       (Float)
        capture_tilt              : tilt         (Float)

    Attributes
    ----------
        endpoint_selection        : Boolean   = capture_endpoint_selection(domain='CURVE')
        handle_type_selection     : Boolean   = capture_handle_type_selection(domain='CURVE')
        left_handle_position      : Vector    = capture_handle_positions(domain='CURVE').left
        radius                    : Float     = capture_radius(domain='CURVE')
        right_handle_position     : Vector    = capture_handle_positions(domain='CURVE').right
        spline_ID                 : Integer   = capture_ID(domain='SPLINE')
        spline_index              : Integer   = capture_index(domain='SPLINE')
        tilt                      : Float     = capture_tilt(domain='CURVE')

    Methods
    -------
        length                    : length       (Float)
        sample                    : Sockets      [position (Vector), tangent (Vector), normal (Vector)]
        to_mesh                   : mesh         (Geometry)
        to_points                 : Sockets      [points (Geometry), tangent (Vector), normal (Vector), rotation (Vector)]

    Stacked methods
    ---------------
        fill                      : Curve
        fillet                    : Curve
        resample                  : Curve
        reverse                   : Curve
        set_handle_positions      : Curve
        set_handles               : Curve
        set_radius                : Curve
        set_spline_type           : Curve
        set_tilt                  : Curve
        subdivide                 : Curve
        trim                      : Curve
    """

    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """Call node NodeBezierSegment (GeometryNodeCurvePrimitiveBezierSegment)

        Sockets arguments
        -----------------
            resolution     : Integer
            start          : Vector
            start_handle   : Vector
            end_handle     : Vector
            end            : Vector

        Parameters arguments
        --------------------
            mode           : 'POSITION' in [POSITION, OFFSET]

        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeBezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode).curve)

    @classmethod
    def Circle(cls, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS'):
        """Call node NodeCurveCircle (GeometryNodeCurvePrimitiveCircle)

        Sockets arguments
        -----------------
            resolution     : Integer
            point_1        : Vector
            point_2        : Vector
            point_3        : Vector
            radius         : Float

        Parameters arguments
        --------------------
            mode           : 'RADIUS' in [POINTS, RADIUS]

        Returns
        -------
            Sockets [curve (Geometry), center (Vector)]
        """

        return nodes.NodeCurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode)

    @classmethod
    def Line(cls, start=None, end=None, direction=None, length=None, mode='POINTS'):
        """Call node NodeCurveLine (GeometryNodeCurvePrimitiveLine)

        Sockets arguments
        -----------------
            start          : Vector
            end            : Vector
            direction      : Vector
            length         : Float

        Parameters arguments
        --------------------
            mode           : 'POINTS' in [POINTS, DIRECTION]

        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeCurveLine(start=start, end=end, direction=direction, length=length, mode=mode).curve)

    @classmethod
    def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):
        """Call node NodeQuadrilateral (GeometryNodeCurvePrimitiveQuadrilateral)

        Sockets arguments
        -----------------
            width          : Float
            height         : Float
            bottom_width   : Float
            top_width      : Float
            offset         : Float
            bottom_height  : Float
            top_height     : Float
            point_1        : Vector
            point_2        : Vector
            point_3        : Vector
            point_4        : Vector

        Parameters arguments
        --------------------
            mode           : 'RECTANGLE' in [RECTANGLE, PARALLELOGRAM, TRAPEZOID, KITE, POINTS]

        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeQuadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode).curve)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """Call node NodeQuadraticBezier (GeometryNodeCurveQuadraticBezier)

        Sockets arguments
        -----------------
            resolution     : Integer
            start          : Vector
            middle         : Vector
            end            : Vector

        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeQuadraticBezier(resolution=resolution, start=start, middle=middle, end=end).curve)

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """Call node NodeStar (GeometryNodeCurveStar)

        Sockets arguments
        -----------------
            points         : Integer
            inner_radius   : Float
            outer_radius   : Float
            twist          : Float

        Returns
        -------
            Sockets [curve (Geometry), outer_points (Boolean)]
        """

        return nodes.NodeStar(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist)

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """Call node NodeSpiral (GeometryNodeCurveSpiral)

        Sockets arguments
        -----------------
            resolution     : Integer
            rotations      : Float
            start_radius   : Float
            end_radius     : Float
            height         : Float
            reverse        : Boolean

        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeSpiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse).curve)

    @classmethod
    def ArcFromRadius(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):
        """Call node NodeArc (GeometryNodeCurveArc)

        Sockets arguments
        -----------------
            resolution     : Integer
            radius         : Float
            start_angle    : Float
            sweep_angle    : Float
            connect_center : Boolean
            invert_arc     : Boolean

        Fixed parameters
        ----------------
            mode           : 'RADIUS'

        Returns
        -------
            Geometry
        """

        return cls(nodes.NodeArc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS').curve)


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def ArcFromPoints(resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):
        """Call node NodeArc (GeometryNodeCurveArc)

        Sockets arguments
        -----------------
            resolution     : Integer
            start          : Vector
            middle         : Vector
            end            : Vector
            offset_angle   : Float
            connect_center : Boolean
            invert_arc     : Boolean

        Fixed parameters
        ----------------
            mode           : 'POINTS'

        Returns
        -------
            Sockets [curve (Geometry), center (Vector), normal (Vector), radius (Float)]
        """

        return nodes.NodeArc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS')


    # ----------------------------------------------------------------------------------------------------
    # Attribute captures

    def capture_endpoint_selection(self, start_size=None, end_size=None, domain='CURVE'):
        """Call node NodeEndpointSelection (GeometryNodeCurveEndpointSelection)

        Sockets arguments
        -----------------
            start_size     : Integer
            end_size       : Integer

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_endpoint_selection_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeEndpointSelection(start_size=start_size, end_size=end_size)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).selection

    def capture_handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, domain='CURVE'):
        """Call node NodeHandleTypeSelection (GeometryNodeCurveHandleTypeSelection)

        Parameters arguments
        --------------------
            handle_type    : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode           : {'RIGHT', 'LEFT'}

        Returns
        -------
            Boolean
        """

        attr_name = 'capture_handle_type_selection_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeHandleTypeSelection(handle_type=handle_type, mode=mode)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).selection

    def capture_tilt(self, domain='CURVE'):
        """Call node NodeCurveTilt (GeometryNodeInputCurveTilt)

        Returns
        -------
            Float
        """

        attr_name = 'capture_tilt_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeCurveTilt()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).tilt

    def capture_radius(self, domain='CURVE'):
        """Call node NodeRadius (GeometryNodeInputRadius)

        Returns
        -------
            Float
        """

        attr_name = 'capture_radius_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeRadius()
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name).radius

    def capture_handle_positions(self, relative=None, domain='CURVE'):
        """Call node NodeCurveHandlePositions (GeometryNodeInputCurveHandlePositions)

        Sockets arguments
        -----------------
            relative       : Boolean

        Returns
        -------
            Sockets [left (Vector), right (Vector)]
        """

        attr_name = 'capture_handle_positions_' + domain
        if not hasattr(self, attr_name):
            node = nodes.NodeCurveHandlePositions(relative=relative)
            node.as_attribute(owning_socket=self, domain=domain)
            setattr(self, attr_name, node)
        return getattr(self, attr_name)


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def spline_ID(self):
        """Call node NodeID (GeometryNodeInputID)

        Returns
        -------
            Integer
        """

        return self.capture_ID(domain='SPLINE')

    @property
    def spline_index(self):
        """Call node NodeIndex (GeometryNodeInputIndex)

        Returns
        -------
            Integer
        """

        return self.capture_index(domain='SPLINE')

    @property
    def endpoint_selection(self, start_size=None, end_size=None):
        """Call node NodeEndpointSelection (GeometryNodeCurveEndpointSelection)

        Sockets arguments
        -----------------
            start_size     : Integer
            end_size       : Integer

        Returns
        -------
            Boolean
        """

        return self.capture_endpoint_selection(domain='CURVE')

    @property
    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """Call node NodeHandleTypeSelection (GeometryNodeCurveHandleTypeSelection)

        Parameters arguments
        --------------------
            handle_type    : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode           : {'RIGHT', 'LEFT'}

        Returns
        -------
            Boolean
        """

        return self.capture_handle_type_selection(domain='CURVE')

    @property
    def tilt(self):
        """Call node NodeCurveTilt (GeometryNodeInputCurveTilt)

        Returns
        -------
            Float
        """

        return self.capture_tilt(domain='CURVE')

    @property
    def radius(self):
        """Call node NodeRadius (GeometryNodeInputRadius)

        Returns
        -------
            Float
        """

        return self.capture_radius(domain='CURVE')

    @property
    def left_handle_position(self, relative=None):
        """Call node NodeCurveHandlePositions (GeometryNodeInputCurveHandlePositions)

        Sockets arguments
        -----------------
            relative       : Boolean

        Returns
        -------
            Vector
        """

        return self.capture_handle_positions(domain='CURVE').output_sockets[0]

    @property
    def right_handle_position(self, relative=None):
        """Call node NodeCurveHandlePositions (GeometryNodeInputCurveHandlePositions)

        Sockets arguments
        -----------------
            relative       : Boolean

        Returns
        -------
            Vector
        """

        return self.capture_handle_positions(domain='CURVE').output_sockets[1]


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(curve=None, profile_curve=None, fill_caps=None):
        """Call node NodeCurveToMesh (GeometryNodeCurveToMesh)

        Sockets arguments
        -----------------
            curve          : Geometry
            profile_curve  : Geometry
            fill_caps      : Boolean

        Returns
        -------
            Geometry
        """

        return nodes.NodeCurveToMesh(curve=curve, profile_curve=profile_curve, fill_caps=fill_caps).mesh

    def to_points(curve=None, count=None, length=None, mode='COUNT'):
        """Call node NodeCurveToPoints (GeometryNodeCurveToPoints)

        Sockets arguments
        -----------------
            curve          : Geometry
            count          : Integer
            length         : Float

        Parameters arguments
        --------------------
            mode           : 'COUNT' in [EVALUATED, COUNT, LENGTH]

        Returns
        -------
            Sockets [points (Geometry), tangent (Vector), normal (Vector), rotation (Vector)]
        """

        return nodes.NodeCurveToPoints(curve=curve, count=count, length=length, mode=mode)

    def sample(curve=None, factor=None, length=None, mode='LENGTH'):
        """Call node NodeSampleCurve (GeometryNodeSampleCurve)

        Sockets arguments
        -----------------
            curve          : Geometry
            factor         : Float
            length         : Float

        Parameters arguments
        --------------------
            mode           : 'LENGTH' in [FACTOR, LENGTH]

        Returns
        -------
            Sockets [position (Vector), tangent (Vector), normal (Vector)]
        """

        return nodes.NodeSampleCurve(curve=curve, factor=factor, length=length, mode=mode)

    def length(curve=None):
        """Call node NodeCurveLength (GeometryNodeCurveLength)

        Sockets arguments
        -----------------
            curve          : Geometry

        Returns
        -------
            Float
        """

        return nodes.NodeCurveLength(curve=curve).length


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_handles(curve=None, selection=None, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """Call node NodeSetHandleType (GeometryNodeCurveSetHandles)

        Sockets arguments
        -----------------
            curve          : Geometry
            selection      : Boolean

        Parameters arguments
        --------------------
            handle_type    : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            mode           : {'RIGHT', 'LEFT'}

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetHandleType(curve=curve, selection=selection, handle_type=handle_type, mode=mode))

    def set_spline_type(curve=None, selection=None, spline_type='POLY'):
        """Call node NodeSetSplineType (GeometryNodeCurveSplineType)

        Sockets arguments
        -----------------
            curve          : Geometry
            selection      : Boolean

        Parameters arguments
        --------------------
            spline_type    : 'POLY' in [BEZIER, NURBS, POLY]

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetSplineType(curve=curve, selection=selection, spline_type=spline_type))

    def fill(curve=None, mode='TRIANGLES'):
        """Call node NodeFillCurve (GeometryNodeFillCurve)

        Sockets arguments
        -----------------
            curve          : Geometry

        Parameters arguments
        --------------------
            mode           : 'TRIANGLES' in [TRIANGLES, NGONS]

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeFillCurve(curve=curve, mode=mode))

    def fillet(curve=None, count=None, radius=None, limit_radius=None, mode='BEZIER'):
        """Call node NodeFilletCurve (GeometryNodeFilletCurve)

        Sockets arguments
        -----------------
            curve          : Geometry
            count          : Integer
            radius         : Float
            limit_radius   : Boolean

        Parameters arguments
        --------------------
            mode           : 'BEZIER' in [BEZIER, POLY]

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeFilletCurve(curve=curve, count=count, radius=radius, limit_radius=limit_radius, mode=mode))

    def resample(curve=None, selection=None, count=None, length=None, mode='COUNT'):
        """Call node NodeResampleCurve (GeometryNodeResampleCurve)

        Sockets arguments
        -----------------
            curve          : Geometry
            selection      : Boolean
            count          : Integer
            length         : Float

        Parameters arguments
        --------------------
            mode           : 'COUNT' in [EVALUATED, COUNT, LENGTH]

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeResampleCurve(curve=curve, selection=selection, count=count, length=length, mode=mode))

    def reverse(curve=None, selection=None):
        """Call node NodeReverseCurve (GeometryNodeReverseCurve)

        Sockets arguments
        -----------------
            curve          : Geometry
            selection      : Boolean

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeReverseCurve(curve=curve, selection=selection))

    def set_handle_positions(curve=None, selection=None, position=None, offset=None, mode='LEFT'):
        """Call node NodeSetHandlePositions (GeometryNodeSetCurveHandlePositions)

        Sockets arguments
        -----------------
            curve          : Geometry
            selection      : Boolean
            position       : Vector
            offset         : Vector

        Parameters arguments
        --------------------
            mode           : 'LEFT' in [LEFT, RIGHT]

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetHandlePositions(curve=curve, selection=selection, position=position, offset=offset, mode=mode))

    def set_radius(curve=None, selection=None, radius=None):
        """Call node NodeSetCurveRadius (GeometryNodeSetCurveRadius)

        Sockets arguments
        -----------------
            curve          : Geometry
            selection      : Boolean
            radius         : Float

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetCurveRadius(curve=curve, selection=selection, radius=radius))

    def set_tilt(curve=None, selection=None, tilt=None):
        """Call node NodeSetCurveTilt (GeometryNodeSetCurveTilt)

        Sockets arguments
        -----------------
            curve          : Geometry
            selection      : Boolean
            tilt           : Float

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSetCurveTilt(curve=curve, selection=selection, tilt=tilt))

    def subdivide(curve=None, cuts=None):
        """Call node NodeSubdivideCurve (GeometryNodeSubdivideCurve)

        Sockets arguments
        -----------------
            curve          : Geometry
            cuts           : Integer

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeSubdivideCurve(curve=curve, cuts=cuts))

    def trim(curve=None, start0=None, end0=None, start1=None, end1=None, mode='FACTOR'):
        """Call node NodeTrimCurve (GeometryNodeTrimCurve)

        Sockets arguments
        -----------------
            curve          : Geometry
            start0         : Float
            end0           : Float
            start1         : Float
            end1           : Float

        Parameters arguments
        --------------------
            mode           : 'FACTOR' in [FACTOR, LENGTH]

        Returns
        -------
            self

        """

        return self.stack(nodes.NodeTrimCurve(curve=curve, start0=start0, end0=end0, start1=start1, end1=end1, mode=mode))


