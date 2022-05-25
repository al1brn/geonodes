import geonodes as gn
from geonodes.core import socket as bcls
from geonodes.nodes import nodes
import logging
logger = logging.Logger('geonodes')

# ----------------------------------------------------------------------------------------------------
# Argument is a vector

def is_vector(arg):
    return isinstance(arg, Vector) or (isinstance(arg, (tuple, list)) and len(arg) == 3)

# ----------------------------------------------------------------------------------------------------
# Sockets outputs

class Sockets(bcls.Sockets):
    pass


# ==============================================================================================================
# Data class Curve

class Curve(gn.Spline):
    """ Socket data class Curve

    Constructors
    ------------
        ArcFromRadius        : Curve
        BezierSegment        : Curve
        Circle               : Curve
        Line                 : Curve
        QuadraticBezier      : Curve
        Quadrilateral        : Curve
        Spiral               : Curve
        Star                 : Sockets [curve (Curve), outer_points (Boolean)]

    Static methods
    --------------
        ArcFromPoints        : Sockets [curve (Curve), center (Vector), normal (Vector), radius (Float)]

    Attributes
    ----------
        capture_endpoint_selection : Boolean
        capture_handle_positions_left : Sockets [left (Vector), right (Vector)]
        capture_handle_positions_right : Sockets [left (Vector), right (Vector)]
        capture_handle_type_selection : Boolean
        capture_radius       : Float
        capture_tilt         : Float
        endpoint_selection   : Boolean
        handle_positions_left : Sockets [left (Vector), right (Vector)]
        handle_positions_right : Sockets [left (Vector), right (Vector)]
        handle_type_selection : Boolean
        radius               : Float
        spline_ID            : Integer
        spline_index         : Integer
        tilt                 : Float

    Methods
    -------
        length               : Float
        sample               : Sockets [position (Vector), tangent (Vector), normal (Vector)]
        to_mesh              : Mesh
        to_points            : Sockets [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]

    Stacked methods
    ---------------
        fill                 : Curve
        fillet               : Curve
        resample             : Curve
        reverse              : Curve
        set_handle_positions : Curve
        set_handles          : Curve
        set_radius           : Curve
        set_spline_type      : Curve
        set_tilt             : Curve
        subdivide            : Curve
        trim                 : Curve

    """


    # ----------------------------------------------------------------------------------------------------
    # Constructors

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """ Constructor BezierSegment using node NodeBezierSegment

        Arguments
        ---------
            resolution      : Integer
            start           : Vector
            start_handle    : Vector
            end_handle      : Vector
            end             : Vector

            mode            : str

        Returns
        -------
            Curve
        """

        return nodes.NodeBezierSegment(resolution=resolution, start=start, start_handle=start_handle, end_handle=end_handle, end=end, mode=mode).output

    @classmethod
    def Circle(cls, resolution=None, point_1=None, point_2=None, point_3=None, radius=None, mode='RADIUS'):
        """ Constructor Circle using node NodeCurveCircle

        Arguments
        ---------
            resolution      : Integer
            point_1         : Vector
            point_2         : Vector
            point_3         : Vector
            radius          : Float

            mode            : str

        Returns
        -------
            Curve
        """

        return nodes.NodeCurveCircle(resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3, radius=radius, mode=mode).output

    @classmethod
    def Line(cls, start=None, end=None, direction=None, length=None, mode='POINTS'):
        """ Constructor Line using node NodeCurveLine

        Arguments
        ---------
            start           : Vector
            end             : Vector
            direction       : Vector
            length          : Float

            mode            : str

        Returns
        -------
            Curve
        """

        return nodes.NodeCurveLine(start=start, end=end, direction=direction, length=length, mode=mode).output

    @classmethod
    def Quadrilateral(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None, bottom_height=None, top_height=None, point_1=None, point_2=None, point_3=None, point_4=None, mode='RECTANGLE'):
        """ Constructor Quadrilateral using node NodeQuadrilateral

        Arguments
        ---------
            width           : Float
            height          : Float
            bottom_width    : Float
            top_width       : Float
            offset          : Float
            bottom_height   : Float
            top_height      : Float
            point_1         : Vector
            point_2         : Vector
            point_3         : Vector
            point_4         : Vector

            mode            : str

        Returns
        -------
            Curve
        """

        return nodes.NodeQuadrilateral(width=width, height=height, bottom_width=bottom_width, top_width=top_width, offset=offset, bottom_height=bottom_height, top_height=top_height, point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4, mode=mode).output

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """ Constructor QuadraticBezier using node NodeQuadraticBezier

        Arguments
        ---------
            resolution      : Integer
            start           : Vector
            middle          : Vector
            end             : Vector

        Returns
        -------
            Curve
        """

        return nodes.NodeQuadraticBezier(resolution=resolution, start=start, middle=middle, end=end).output

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """ Constructor Star using node NodeStar

        Arguments
        ---------
            points          : Points
            inner_radius    : Float
            outer_radius    : Float
            twist           : Float

        Returns
        -------
            Sockets [curve (Curve), outer_points (Boolean)]
        """

        return nodes.NodeStar(points=points, inner_radius=inner_radius, outer_radius=outer_radius, twist=twist).output

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """ Constructor Spiral using node NodeSpiral

        Arguments
        ---------
            resolution      : Integer
            rotations       : Float
            start_radius    : Float
            end_radius      : Float
            height          : Float
            reverse         : Boolean

        Returns
        -------
            Curve
        """

        return nodes.NodeSpiral(resolution=resolution, rotations=rotations, start_radius=start_radius, end_radius=end_radius, height=height, reverse=reverse).output

    @classmethod
    def ArcFromRadius(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):
        """ Constructor ArcFromRadius using node NodeArc

        Arguments
        ---------
            resolution      : Integer
            radius          : Float
            start_angle     : Float
            sweep_angle     : Float
            connect_center  : Boolean
            invert_arc      : Boolean

        Node parameters settings
        ------------------------
            mode            : node parameter set to 'RADIUS'

        Returns
        -------
            Curve
        """

        return nodes.NodeArc(resolution=resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc, mode='RADIUS').output


    # ----------------------------------------------------------------------------------------------------
    # Static methods

    @staticmethod
    def ArcFromPoints(resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):
        """ Static method ArcFromPoints using node NodeArc

        Arguments
        ---------
            resolution      : Integer
            start           : Vector
            middle          : Vector
            end             : Vector
            offset_angle    : Float
            connect_center  : Boolean
            invert_arc      : Boolean

        Node parameters settings
        ------------------------
            mode            : node parameter set to 'POINTS'

        Returns
        -------
            Sockets [curve (Curve), center (Vector), normal (Vector), radius (Float)]
        """

        return nodes.NodeArc(resolution=resolution, start=start, middle=middle, end=end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc, mode='POINTS').output


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def spline_ID(self):
        """ Attribute spline_ID using node NodeID

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    @property
    def spline_index(self):
        """ Attribute spline_index using node NodeIndex

        Arguments
        ---------

        Returns
        -------
            Integer
        """

        return nodes.Attribute().output

    def capture_endpoint_selection(selfself, end_size=None, domain='CURVE'):
        """ Attribute capture_endpoint_selection using node NodeEndpointSelection

        Arguments
        ---------
            start_size      : Integer: self socket
            end_size        : Integer

        Returns
        -------
            Boolean
        """

        return nodes.Attribute(start_size=self, end_size=end_size).output

    @property
    def endpoint_selection(selfself, end_size=None):
        """ Attribute endpoint_selection using node NodeEndpointSelection

        Arguments
        ---------
            start_size      : Integer: self socket
            end_size        : Integer

        Returns
        -------
            Boolean
        """

        return nodes.Attribute(start_size=self, end_size=end_size).output

    def capture_handle_type_selection(selfhandle_type='AUTO', mode={'LEFT', 'RIGHT'}, domain='CURVE'):
        """ Attribute capture_handle_type_selection using node NodeHandleTypeSelection

        Arguments
        ---------

            handle_type     : str
            mode            : set

        Returns
        -------
            Boolean
        """

        return nodes.Attribute(handle_type=handle_type, mode=mode).output

    @property
    def handle_type_selection(selfhandle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ Attribute handle_type_selection using node NodeHandleTypeSelection

        Arguments
        ---------

            handle_type     : str
            mode            : set

        Returns
        -------
            Boolean
        """

        return nodes.Attribute(handle_type=handle_type, mode=mode).output

    def capture_tilt(self, domain='CURVE'):
        """ Attribute capture_tilt using node NodeCurveTilt

        Arguments
        ---------

        Returns
        -------
            Float
        """

        return nodes.Attribute().output

    @property
    def tilt(self):
        """ Attribute tilt using node NodeCurveTilt

        Arguments
        ---------

        Returns
        -------
            Float
        """

        return nodes.Attribute().output

    def capture_radius(self, domain='CURVE'):
        """ Attribute capture_radius using node NodeRadius

        Arguments
        ---------

        Returns
        -------
            Float
        """

        return nodes.Attribute().output

    @property
    def radius(self):
        """ Attribute radius using node NodeRadius

        Arguments
        ---------

        Returns
        -------
            Float
        """

        return nodes.Attribute().output

    def capture_handle_positions_left(selfself, domain='CURVE'):
        """ Attribute capture_handle_positions_left using node NodeCurveHandlePositions

        Arguments
        ---------
            relative        : Boolean: self socket

        Returns
        -------
            Sockets [left (Vector), right (Vector)]
        """

        return nodes.Attribute(relative=self).output

    def handle_positions_left(selfself):
        """ Attribute handle_positions_left using node NodeCurveHandlePositions

        Arguments
        ---------
            relative        : Boolean: self socket

        Returns
        -------
            Sockets [left (Vector), right (Vector)]
        """

        return nodes.Attribute(relative=self).output

    def capture_handle_positions_right(selfself, domain='CURVE'):
        """ Attribute capture_handle_positions_right using node NodeCurveHandlePositions

        Arguments
        ---------
            relative        : Boolean: self socket

        Returns
        -------
            Sockets [left (Vector), right (Vector)]
        """

        return nodes.Attribute(relative=self).output

    def handle_positions_right(selfself):
        """ Attribute handle_positions_right using node NodeCurveHandlePositions

        Arguments
        ---------
            relative        : Boolean: self socket

        Returns
        -------
            Sockets [left (Vector), right (Vector)]
        """

        return nodes.Attribute(relative=self).output


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def to_mesh(self, profile_curve=None, fill_caps=None):
        """ Method to_mesh using node NodeCurvetoMesh

        Arguments
        ---------
            curve           : Curve: self socket
            profile_curve   : Geometry
            fill_caps       : Boolean

        Returns
        -------
            Mesh
        """

        return nodes.NodeCurvetoMesh(curve=self, profile_curve=profile_curve, fill_caps=fill_caps).output

    def to_points(self, count=None, length=None, mode='COUNT'):
        """ Method to_points using node NodeCurvetoPoints

        Arguments
        ---------
            curve           : Curve: self socket
            count           : Integer
            length          : Float

            mode            : str

        Returns
        -------
            Sockets [points (Points), tangent (Vector), normal (Vector), rotation (Vector)]
        """

        return nodes.NodeCurvetoPoints(curve=self, count=count, length=length, mode=mode).output

    def sample(self, factor=None, length=None, mode='LENGTH'):
        """ Method sample using node NodeSampleCurve

        Arguments
        ---------
            curve           : Curve: self socket
            factor          : Float
            length          : Float

            mode            : str

        Returns
        -------
            Sockets [position (Vector), tangent (Vector), normal (Vector)]
        """

        return nodes.NodeSampleCurve(curve=self, factor=factor, length=length, mode=mode).output

    def length(self):
        """ Method length using node NodeCurveLength

        Arguments
        ---------
            curve           : Curve: self socket

        Returns
        -------
            Float
        """

        return nodes.NodeCurveLength(curve=self).output


    # ----------------------------------------------------------------------------------------------------
    # Stacked methods

    def set_handles(self, selection=None, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ Stacked method set_handles using node NodeSetHandleType

        Arguments
        ---------
            curve           : Curve: self socket
            selection       : Boolean

            handle_type     : str
            mode            : set

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeSetHandleType(curve=self, selection=selection, handle_type=handle_type, mode=mode))

    def set_spline_type(self, selection=None, spline_type='POLY'):
        """ Stacked method set_spline_type using node NodeSetSplineType

        Arguments
        ---------
            curve           : Curve: self socket
            selection       : Boolean

            spline_type     : str

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeSetSplineType(curve=self, selection=selection, spline_type=spline_type))

    def fill(self, mode='TRIANGLES'):
        """ Stacked method fill using node NodeFillCurve

        Arguments
        ---------
            curve           : Curve: self socket

            mode            : str

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeFillCurve(curve=self, mode=mode))

    def fillet(self, count=None, radius=None, limit_radius=None, mode='BEZIER'):
        """ Stacked method fillet using node NodeFilletCurve

        Arguments
        ---------
            curve           : Curve: self socket
            count           : Integer
            radius          : Float
            limit_radius    : Boolean

            mode            : str

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeFilletCurve(curve=self, count=count, radius=radius, limit_radius=limit_radius, mode=mode))

    def resample(self, selection=None, count=None, length=None, mode='COUNT'):
        """ Stacked method resample using node NodeResampleCurve

        Arguments
        ---------
            curve           : Curve: self socket
            selection       : Boolean
            count           : Integer
            length          : Float

            mode            : str

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeResampleCurve(curve=self, selection=selection, count=count, length=length, mode=mode))

    def reverse(self, selection=None):
        """ Stacked method reverse using node NodeReverseCurve

        Arguments
        ---------
            curve           : Curve: self socket
            selection       : Boolean

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeReverseCurve(curve=self, selection=selection))

    def set_handle_positions(self, selection=None, position=None, offset=None, mode='LEFT'):
        """ Stacked method set_handle_positions using node NodeSetHandlePositions

        Arguments
        ---------
            curve           : Curve: self socket
            selection       : Boolean
            position        : Vector
            offset          : Vector

            mode            : str

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeSetHandlePositions(curve=self, selection=selection, position=position, offset=offset, mode=mode))

    def set_radius(self, selection=None, radius=None):
        """ Stacked method set_radius using node NodeSetCurveRadius

        Arguments
        ---------
            curve           : Curve: self socket
            selection       : Boolean
            radius          : Float

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeSetCurveRadius(curve=self, selection=selection, radius=radius))

    def set_tilt(self, selection=None, tilt=None):
        """ Stacked method set_tilt using node NodeSetCurveTilt

        Arguments
        ---------
            curve           : Curve: self socket
            selection       : Boolean
            tilt            : Float

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeSetCurveTilt(curve=self, selection=selection, tilt=tilt))

    def subdivide(self, cuts=None):
        """ Stacked method subdivide using node NodeSubdivideCurve

        Arguments
        ---------
            curve           : Curve: self socket
            cuts            : Integer

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeSubdivideCurve(curve=self, cuts=cuts))

    def trim(self, start=None, end=None, mode='FACTOR'):
        """ Stacked method trim using node NodeTrimCurve

        Arguments
        ---------
            curve           : Curve: self socket
            start           : Float
            end             : Float

            mode            : str

        Returns
        -------
            Curve
        """

        return self.stack(nodes.NodeTrimCurve(curve=self, start=start, end=end, mode=mode))



