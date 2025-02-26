from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Curve(Socket):
    """"
    $DOC SET hidden
    """
    def domain_size(self):
        """ > Node <&Node Domain Size>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'component' : 'CURVE'

        Returns
        -------
        - node [point_count (Integer), spline_count (Integer)]
        """
        node = self._cache('Domain Size', sockets={'Geometry': self}, component='CURVE')
        return node

    @classmethod
    def ArcPoints(cls, resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):
        """ > Node <&Node Arc>

        Information
        -----------
        - Parameter 'mode' : 'POINTS'

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - start (Vector) : socket 'Start' (id: Start)
        - middle (Vector) : socket 'Middle' (id: Middle)
        - end (Vector) : socket 'End' (id: End)
        - offset_angle (Float) : socket 'Offset Angle' (id: Offset Angle)
        - connect_center (Boolean) : socket 'Connect Center' (id: Connect Center)
        - invert_arc (Boolean) : socket 'Invert Arc' (id: Invert Arc)

        Returns
        -------
        - Curve
        """
        node = Node('Arc', sockets={'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end, 'Offset Angle': offset_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode='POINTS')
        return cls(node._out)

    @classmethod
    def ArcRadius(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):
        """ > Node <&Node Arc>

        Information
        -----------
        - Parameter 'mode' : 'RADIUS'

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - radius (Float) : socket 'Radius' (id: Radius)
        - start_angle (Float) : socket 'Start Angle' (id: Start Angle)
        - sweep_angle (Float) : socket 'Sweep Angle' (id: Sweep Angle)
        - connect_center (Boolean) : socket 'Connect Center' (id: Connect Center)
        - invert_arc (Boolean) : socket 'Invert Arc' (id: Invert Arc)

        Returns
        -------
        - Curve
        """
        node = Node('Arc', sockets={'Resolution': resolution, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode='RADIUS')
        return cls(node._out)

    @classmethod
    def Arc(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None, mode='RADIUS'):
        """ > Node <&Node Arc>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - radius (Float) : socket 'Radius' (id: Radius)
        - start_angle (Float) : socket 'Start Angle' (id: Start Angle)
        - sweep_angle (Float) : socket 'Sweep Angle' (id: Sweep Angle)
        - connect_center (Boolean) : socket 'Connect Center' (id: Connect Center)
        - invert_arc (Boolean) : socket 'Invert Arc' (id: Invert Arc)
        - mode (str): parameter 'mode' in ['POINTS', 'RADIUS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Arc', 'mode', mode, 'Arc', ('POINTS', 'RADIUS'))
        node = Node('Arc', sockets={'Resolution': resolution, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode=mode)
        return cls(node._out)

    @classmethod
    def endpoint_selection(cls, start_size=None, end_size=None):
        """ > Node <&Node Endpoint Selection>

        Arguments
        ---------
        - start_size (Integer) : socket 'Start Size' (id: Start Size)
        - end_size (Integer) : socket 'End Size' (id: End Size)

        Returns
        -------
        - Boolean
        """
        node = Node('Endpoint Selection', sockets={'Start Size': start_size, 'End Size': end_size})
        return node._out

    @classmethod
    def handle_type_selection(cls, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ > Node <&Node Handle Type Selection>

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']
        - mode (set): parameter 'mode'

        Returns
        -------
        - Boolean
        """
        utils.check_enum_arg('Handle Type Selection', 'handle_type', handle_type, 'handle_type_selection', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Handle Type Selection', sockets={}, handle_type=handle_type, mode=mode)
        return node._out

    def length(self):
        """ > Node <&Node Curve Length>

        Information
        -----------
        - Socket 'Curve' : self

        Returns
        -------
        - Float
        """
        node = Node('Curve Length', sockets={'Curve': self})
        return node._out

    @classmethod
    def curve_of_point(cls, point_index=None):
        """ > Node <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)

        Returns
        -------
        - Integer [index_in_curve_ (Integer)]
        """
        node = Node('Curve of Point', sockets={'Point Index': point_index})
        return node._out

    @classmethod
    def BeziersegmentPosition(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None):
        """ > Node <&Node Bézier Segment>

        Information
        -----------
        - Parameter 'mode' : 'POSITION'

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - start (Vector) : socket 'Start' (id: Start)
        - start_handle (Vector) : socket 'Start Handle' (id: Start Handle)
        - end_handle (Vector) : socket 'End Handle' (id: End Handle)
        - end (Vector) : socket 'End' (id: End)

        Returns
        -------
        - Curve
        """
        node = Node('Bézier Segment', sockets={'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode='POSITION')
        return cls(node._out)

    @classmethod
    def BeziersegmentOffset(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None):
        """ > Node <&Node Bézier Segment>

        Information
        -----------
        - Parameter 'mode' : 'OFFSET'

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - start (Vector) : socket 'Start' (id: Start)
        - start_handle (Vector) : socket 'Start Handle' (id: Start Handle)
        - end_handle (Vector) : socket 'End Handle' (id: End Handle)
        - end (Vector) : socket 'End' (id: End)

        Returns
        -------
        - Curve
        """
        node = Node('Bézier Segment', sockets={'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode='OFFSET')
        return cls(node._out)

    @classmethod
    def BezierSegment(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None, mode='POSITION'):
        """ > Node <&Node Bézier Segment>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - start (Vector) : socket 'Start' (id: Start)
        - start_handle (Vector) : socket 'Start Handle' (id: Start Handle)
        - end_handle (Vector) : socket 'End Handle' (id: End Handle)
        - end (Vector) : socket 'End' (id: End)
        - mode (str): parameter 'mode' in ['POSITION', 'OFFSET']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Bézier Segment', 'mode', mode, 'BezierSegment', ('POSITION', 'OFFSET'))
        node = Node('Bézier Segment', sockets={'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode=mode)
        return cls(node._out)

    @classmethod
    def CirclePoints(cls, resolution=None, point_1=None, point_2=None, point_3=None):
        """ > Node <&Node Curve Circle>

        Information
        -----------
        - Parameter 'mode' : 'POINTS'

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - point_1 (Vector) : socket 'Point 1' (id: Point 1)
        - point_2 (Vector) : socket 'Point 2' (id: Point 2)
        - point_3 (Vector) : socket 'Point 3' (id: Point 3)

        Returns
        -------
        - Curve
        """
        node = Node('Curve Circle', sockets={'Resolution': resolution, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3}, mode='POINTS')
        return cls(node._out)

    @classmethod
    def CircleRadius(cls, resolution=None, radius=None):
        """ > Node <&Node Curve Circle>

        Information
        -----------
        - Parameter 'mode' : 'RADIUS'

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Curve
        """
        node = Node('Curve Circle', sockets={'Resolution': resolution, 'Radius': radius}, mode='RADIUS')
        return cls(node._out)

    @classmethod
    def Circle(cls, resolution=None, radius=None, mode='RADIUS'):
        """ > Node <&Node Curve Circle>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - radius (Float) : socket 'Radius' (id: Radius)
        - mode (str): parameter 'mode' in ['POINTS', 'RADIUS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Curve Circle', 'mode', mode, 'Circle', ('POINTS', 'RADIUS'))
        node = Node('Curve Circle', sockets={'Resolution': resolution, 'Radius': radius}, mode=mode)
        return cls(node._out)

    @classmethod
    def LinePoints(cls, start=None, end=None):
        """ > Node <&Node Curve Line>

        Information
        -----------
        - Parameter 'mode' : 'POINTS'

        Arguments
        ---------
        - start (Vector) : socket 'Start' (id: Start)
        - end (Vector) : socket 'End' (id: End)

        Returns
        -------
        - Curve
        """
        node = Node('Curve Line', sockets={'Start': start, 'End': end}, mode='POINTS')
        return cls(node._out)

    @classmethod
    def LineDirection(cls, start=None, direction=None, length=None):
        """ > Node <&Node Curve Line>

        Information
        -----------
        - Parameter 'mode' : 'DIRECTION'

        Arguments
        ---------
        - start (Vector) : socket 'Start' (id: Start)
        - direction (Vector) : socket 'Direction' (id: Direction)
        - length (Float) : socket 'Length' (id: Length)

        Returns
        -------
        - Curve
        """
        node = Node('Curve Line', sockets={'Start': start, 'Direction': direction, 'Length': length}, mode='DIRECTION')
        return cls(node._out)

    @classmethod
    def Line(cls, start=None, end=None, mode='POINTS'):
        """ > Node <&Node Curve Line>

        Arguments
        ---------
        - start (Vector) : socket 'Start' (id: Start)
        - end (Vector) : socket 'End' (id: End)
        - mode (str): parameter 'mode' in ['POINTS', 'DIRECTION']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Curve Line', 'mode', mode, 'Line', ('POINTS', 'DIRECTION'))
        node = Node('Curve Line', sockets={'Start': start, 'End': end}, mode=mode)
        return cls(node._out)

    @classmethod
    def QuadrilateralRectangle(cls, width=None, height=None):
        """ > Node <&Node Quadrilateral>

        Information
        -----------
        - Parameter 'mode' : 'RECTANGLE'

        Arguments
        ---------
        - width (Float) : socket 'Width' (id: Width)
        - height (Float) : socket 'Height' (id: Height)

        Returns
        -------
        - Curve
        """
        node = Node('Quadrilateral', sockets={'Width': width, 'Height': height}, mode='RECTANGLE')
        return cls(node._out)

    @classmethod
    def QuadrilateralParallelogram(cls, width=None, height=None, offset=None):
        """ > Node <&Node Quadrilateral>

        Information
        -----------
        - Parameter 'mode' : 'PARALLELOGRAM'

        Arguments
        ---------
        - width (Float) : socket 'Width' (id: Width)
        - height (Float) : socket 'Height' (id: Height)
        - offset (Float) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Curve
        """
        node = Node('Quadrilateral', sockets={'Width': width, 'Height': height, 'Offset': offset}, mode='PARALLELOGRAM')
        return cls(node._out)

    @classmethod
    def QuadrilateralTrapezoid(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None):
        """ > Node <&Node Quadrilateral>

        Information
        -----------
        - Parameter 'mode' : 'TRAPEZOID'

        Arguments
        ---------
        - width (Float) : socket 'Width' (id: Width)
        - height (Float) : socket 'Height' (id: Height)
        - bottom_width (Float) : socket 'Bottom Width' (id: Bottom Width)
        - top_width (Float) : socket 'Top Width' (id: Top Width)
        - offset (Float) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Curve
        """
        node = Node('Quadrilateral', sockets={'Width': width, 'Height': height, 'Bottom Width': bottom_width, 'Top Width': top_width, 'Offset': offset}, mode='TRAPEZOID')
        return cls(node._out)

    @classmethod
    def QuadrilateralKite(cls, width=None, bottom_height=None, top_height=None):
        """ > Node <&Node Quadrilateral>

        Information
        -----------
        - Parameter 'mode' : 'KITE'

        Arguments
        ---------
        - width (Float) : socket 'Width' (id: Width)
        - bottom_height (Float) : socket 'Bottom Height' (id: Bottom Height)
        - top_height (Float) : socket 'Top Height' (id: Top Height)

        Returns
        -------
        - Curve
        """
        node = Node('Quadrilateral', sockets={'Width': width, 'Bottom Height': bottom_height, 'Top Height': top_height}, mode='KITE')
        return cls(node._out)

    @classmethod
    def QuadrilateralPoints(cls, width=None, point_1=None, point_2=None, point_3=None, point_4=None):
        """ > Node <&Node Quadrilateral>

        Information
        -----------
        - Parameter 'mode' : 'POINTS'

        Arguments
        ---------
        - width (Float) : socket 'Width' (id: Width)
        - point_1 (Vector) : socket 'Point 1' (id: Point 1)
        - point_2 (Vector) : socket 'Point 2' (id: Point 2)
        - point_3 (Vector) : socket 'Point 3' (id: Point 3)
        - point_4 (Vector) : socket 'Point 4' (id: Point 4)

        Returns
        -------
        - Curve
        """
        node = Node('Quadrilateral', sockets={'Width': width, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3, 'Point 4': point_4}, mode='POINTS')
        return cls(node._out)

    @classmethod
    def Quadrilateral(cls, width=None, height=None, mode='RECTANGLE'):
        """ > Node <&Node Quadrilateral>

        Arguments
        ---------
        - width (Float) : socket 'Width' (id: Width)
        - height (Float) : socket 'Height' (id: Height)
        - mode (str): parameter 'mode' in ['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Quadrilateral', 'mode', mode, 'Quadrilateral', ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS'))
        node = Node('Quadrilateral', sockets={'Width': width, 'Height': height}, mode=mode)
        return cls(node._out)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """ > Node <&Node Quadratic Bézier>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - start (Vector) : socket 'Start' (id: Start)
        - middle (Vector) : socket 'Middle' (id: Middle)
        - end (Vector) : socket 'End' (id: End)

        Returns
        -------
        - Curve
        """
        node = Node('Quadratic Bézier', sockets={'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end})
        return cls(node._out)

    def set_handle_type(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']
        - mode (set): parameter 'mode'

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_left_handle_type(self, handle_type='AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'LEFT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_left_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'LEFT'})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_right_handle_type(self, handle_type='AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'RIGHT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_right_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'RIGHT'})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_both_handle_type(self, handle_type='AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'LEFT', 'RIGHT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_both_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'LEFT', 'RIGHT'})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """ > Node <&Node Spiral>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - rotations (Float) : socket 'Rotations' (id: Rotations)
        - start_radius (Float) : socket 'Start Radius' (id: Start Radius)
        - end_radius (Float) : socket 'End Radius' (id: End Radius)
        - height (Float) : socket 'Height' (id: Height)
        - reverse (Boolean) : socket 'Reverse' (id: Reverse)

        Returns
        -------
        - Curve
        """
        node = Node('Spiral', sockets={'Resolution': resolution, 'Rotations': rotations, 'Start Radius': start_radius, 'End Radius': end_radius, 'Height': height, 'Reverse': reverse})
        return cls(node._out)

    def set_spline_type(self, spline_type='POLY'):
        """ > Node <&Node Set Spline Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - spline_type (str): parameter 'spline_type' in ['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Spline Type', 'spline_type', spline_type, 'set_spline_type', ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'))
        node = Node('Set Spline Type', sockets={'Curve': self, 'Selection': self._sel}, spline_type=spline_type)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """ > Node <&Node Star>

        Arguments
        ---------
        - points (Integer) : socket 'Points' (id: Points)
        - inner_radius (Float) : socket 'Inner Radius' (id: Inner Radius)
        - outer_radius (Float) : socket 'Outer Radius' (id: Outer Radius)
        - twist (Float) : socket 'Twist' (id: Twist)

        Returns
        -------
        - Curve
        """
        node = Node('Star', sockets={'Points': points, 'Inner Radius': inner_radius, 'Outer Radius': outer_radius, 'Twist': twist})
        return cls(node._out)

    def to_mesh(self, profile_curve=None, fill_caps=None):
        """ > Node <&Node Curve to Mesh>

        Information
        -----------
        - Socket 'Curve' : self

        Arguments
        ---------
        - profile_curve (Geometry) : socket 'Profile Curve' (id: Profile Curve)
        - fill_caps (Boolean) : socket 'Fill Caps' (id: Fill Caps)

        Returns
        -------
        - Mesh
        """
        node = Node('Curve to Mesh', sockets={'Curve': self, 'Profile Curve': profile_curve, 'Fill Caps': fill_caps})
        return node._out

    def to_points_evaluated(self):
        """ > Node <&Node Curve to Points>

        Information
        -----------
        - Socket 'Curve' : self
        - Parameter 'mode' : 'EVALUATED'

        Returns
        -------
        - Cloud [tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)]
        """
        node = Node('Curve to Points', sockets={'Curve': self}, mode='EVALUATED')
        return node._out

    def to_points_count(self, count=None):
        """ > Node <&Node Curve to Points>

        Information
        -----------
        - Socket 'Curve' : self
        - Parameter 'mode' : 'COUNT'

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)

        Returns
        -------
        - Cloud [tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)]
        """
        node = Node('Curve to Points', sockets={'Curve': self, 'Count': count}, mode='COUNT')
        return node._out

    def to_points_length(self, length=None):
        """ > Node <&Node Curve to Points>

        Information
        -----------
        - Socket 'Curve' : self
        - Parameter 'mode' : 'LENGTH'

        Arguments
        ---------
        - length (Float) : socket 'Length' (id: Length)

        Returns
        -------
        - Cloud [tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)]
        """
        node = Node('Curve to Points', sockets={'Curve': self, 'Length': length}, mode='LENGTH')
        return node._out

    def to_points(self, count=None, mode='COUNT'):
        """ > Node <&Node Curve to Points>

        Information
        -----------
        - Socket 'Curve' : self

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - mode (str): parameter 'mode' in ['EVALUATED', 'COUNT', 'LENGTH']

        Returns
        -------
        - Cloud [tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)]
        """
        utils.check_enum_arg('Curve to Points', 'mode', mode, 'to_points', ('EVALUATED', 'COUNT', 'LENGTH'))
        node = Node('Curve to Points', sockets={'Curve': self, 'Count': count}, mode=mode)
        return node._out

    def to_grease_pencil(self, instances_as_layers=None):
        """ > Node <&Node Curves to Grease Pencil>

        Information
        -----------
        - Socket 'Curves' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - instances_as_layers (Boolean) : socket 'Instances as Layers' (id: Instances as Layers)

        Returns
        -------
        - GreasePencil
        """
        node = Node('Curves to Grease Pencil', sockets={'Curves': self, 'Selection': self._sel, 'Instances as Layers': instances_as_layers})
        return node._out

    def deform_on_surface(self):
        """ > Node <&Node Deform Curves on Surface>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curves' : self

        Returns
        -------
        - Curve
        """
        node = Node('Deform Curves on Surface', sockets={'Curves': self})
        self._jump(node._out)
        return self._domain_to_geometry

    def fill_triangles(self, group_id=None):
        """ > Node <&Node Fill Curve>

        Information
        -----------
        - Socket 'Curve' : self
        - Parameter 'mode' : 'TRIANGLES'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Mesh
        """
        node = Node('Fill Curve', sockets={'Curve': self, 'Group ID': group_id}, mode='TRIANGLES')
        return node._out

    def fill_ngons(self, group_id=None):
        """ > Node <&Node Fill Curve>

        Information
        -----------
        - Socket 'Curve' : self
        - Parameter 'mode' : 'NGONS'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Mesh
        """
        node = Node('Fill Curve', sockets={'Curve': self, 'Group ID': group_id}, mode='NGONS')
        return node._out

    def fill(self, group_id=None, mode='TRIANGLES'):
        """ > Node <&Node Fill Curve>

        Information
        -----------
        - Socket 'Curve' : self

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - mode (str): parameter 'mode' in ['TRIANGLES', 'NGONS']

        Returns
        -------
        - Mesh
        """
        utils.check_enum_arg('Fill Curve', 'mode', mode, 'fill', ('TRIANGLES', 'NGONS'))
        node = Node('Fill Curve', sockets={'Curve': self, 'Group ID': group_id}, mode=mode)
        return node._out

    def fillet_bezier(self, radius=None, limit_radius=None):
        """ > Node <&Node Fillet Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Parameter 'mode' : 'BEZIER'

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)
        - limit_radius (Boolean) : socket 'Limit Radius' (id: Limit Radius)

        Returns
        -------
        - Curve
        """
        node = Node('Fillet Curve', sockets={'Curve': self, 'Radius': radius, 'Limit Radius': limit_radius}, mode='BEZIER')
        self._jump(node._out)
        return self._domain_to_geometry

    def fillet_poly(self, count=None, radius=None, limit_radius=None):
        """ > Node <&Node Fillet Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Parameter 'mode' : 'POLY'

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - radius (Float) : socket 'Radius' (id: Radius)
        - limit_radius (Boolean) : socket 'Limit Radius' (id: Limit Radius)

        Returns
        -------
        - Curve
        """
        node = Node('Fillet Curve', sockets={'Curve': self, 'Count': count, 'Radius': radius, 'Limit Radius': limit_radius}, mode='POLY')
        self._jump(node._out)
        return self._domain_to_geometry

    def fillet(self, radius=None, limit_radius=None, mode='BEZIER'):
        """ > Node <&Node Fillet Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)
        - limit_radius (Boolean) : socket 'Limit Radius' (id: Limit Radius)
        - mode (str): parameter 'mode' in ['BEZIER', 'POLY']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Fillet Curve', 'mode', mode, 'fillet', ('BEZIER', 'POLY'))
        node = Node('Fillet Curve', sockets={'Curve': self, 'Radius': radius, 'Limit Radius': limit_radius}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def handle_positions(cls, relative=None):
        """ > Node <&Node Curve Handle Positions>

        Arguments
        ---------
        - relative (Boolean) : socket 'Relative' (id: Relative)

        Returns
        -------
        - Vector [right_ (Vector)]
        """
        node = Node('Curve Handle Positions', sockets={'Relative': relative})
        return node._out

    @classmethod
    @property
    def tangent(cls):
        """ > Node <&Node Curve Tangent>

        Returns
        -------
        - Vector
        """
        node = Node('Curve Tangent', sockets={})
        return node._out

    @classmethod
    def Interpolate(cls, guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None):
        """ > Node <&Node Interpolate Curves>

        Arguments
        ---------
        - guide_curves (Geometry) : socket 'Guide Curves' (id: Guide Curves)
        - guide_up (Vector) : socket 'Guide Up' (id: Guide Up)
        - guide_group_id (Integer) : socket 'Guide Group ID' (id: Guide Group ID)
        - points (Geometry) : socket 'Points' (id: Points)
        - point_up (Vector) : socket 'Point Up' (id: Point Up)
        - point_group_id (Integer) : socket 'Point Group ID' (id: Point Group ID)
        - max_neighbors (Integer) : socket 'Max Neighbors' (id: Max Neighbors)

        Returns
        -------
        - Curve
        """
        node = Node('Interpolate Curves', sockets={'Guide Curves': guide_curves, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        return cls(node._out)

    def interpolate(self, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None):
        """ > Node <&Node Interpolate Curves>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Guide Curves' : self

        Arguments
        ---------
        - guide_up (Vector) : socket 'Guide Up' (id: Guide Up)
        - guide_group_id (Integer) : socket 'Guide Group ID' (id: Guide Group ID)
        - points (Geometry) : socket 'Points' (id: Points)
        - point_up (Vector) : socket 'Point Up' (id: Point Up)
        - point_group_id (Integer) : socket 'Point Group ID' (id: Point Group ID)
        - max_neighbors (Integer) : socket 'Max Neighbors' (id: Max Neighbors)

        Returns
        -------
        - Curve [closest_index_ (Integer), closest_weight_ (Float)]
        """
        node = Node('Interpolate Curves', sockets={'Guide Curves': self, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def material_selection(cls, material=None):
        """ > Node <&Node Material Selection>

        Arguments
        ---------
        - material (Material) : socket 'Material' (id: Material)

        Returns
        -------
        - Boolean
        """
        node = Node('Material Selection', sockets={'Material': material})
        return node._out

    @classmethod
    def offset_point_in_curve(cls, point_index=None, offset=None):
        """ > Node <&Node Offset Point in Curve>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)
        - offset (Integer) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Boolean [point_index_ (Integer)]
        """
        node = Node('Offset Point in Curve', sockets={'Point Index': point_index, 'Offset': offset})
        return node._out

    @classmethod
    def points_of_curve(cls, curve_index=None, weights=None, sort_index=None):
        """ > Node <&Node Points of Curve>

        Arguments
        ---------
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Points of Curve', sockets={'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    def resample_evaluated(self):
        """ > Node <&Node Resample Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'EVALUATED'

        Returns
        -------
        - Curve
        """
        node = Node('Resample Curve', sockets={'Curve': self, 'Selection': self._sel}, mode='EVALUATED')
        self._jump(node._out)
        return self._domain_to_geometry

    def resample_count(self, count=None):
        """ > Node <&Node Resample Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'COUNT'

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)

        Returns
        -------
        - Curve
        """
        node = Node('Resample Curve', sockets={'Curve': self, 'Selection': self._sel, 'Count': count}, mode='COUNT')
        self._jump(node._out)
        return self._domain_to_geometry

    def resample_length(self, length=None):
        """ > Node <&Node Resample Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'LENGTH'

        Arguments
        ---------
        - length (Float) : socket 'Length' (id: Length)

        Returns
        -------
        - Curve
        """
        node = Node('Resample Curve', sockets={'Curve': self, 'Selection': self._sel, 'Length': length}, mode='LENGTH')
        self._jump(node._out)
        return self._domain_to_geometry

    def resample(self, count=None, mode='COUNT'):
        """ > Node <&Node Resample Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - mode (str): parameter 'mode' in ['EVALUATED', 'COUNT', 'LENGTH']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Resample Curve', 'mode', mode, 'resample', ('EVALUATED', 'COUNT', 'LENGTH'))
        node = Node('Resample Curve', sockets={'Curve': self, 'Selection': self._sel, 'Count': count}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def reverse(self):
        """ > Node <&Node Reverse Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Returns
        -------
        - Curve
        """
        node = Node('Reverse Curve', sockets={'Curve': self, 'Selection': self._sel})
        self._jump(node._out)
        return self._domain_to_geometry

    def sample_factor(self, value=None, curve_index=None, factor=None, use_all_curves=False):
        """ > Node <&Node Sample Curve>

        Information
        -----------
        - Socket 'Curves' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'mode' : 'FACTOR'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - factor (Float) : socket 'Factor' (id: Factor)
        - use_all_curves (bool): parameter 'use_all_curves'

        Returns
        -------
        - Float [position_ (Vector), tangent_ (Vector), normal_ (Vector)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Curve.sample_factor', 'value')
        node = Node('Sample Curve', sockets={'Curves': self, 'Value': value, 'Curve Index': curve_index, 'Factor': factor}, data_type=data_type, mode='FACTOR', use_all_curves=use_all_curves)
        return node._out

    def sample_length(self, value=None, length=None, curve_index=None, use_all_curves=False):
        """ > Node <&Node Sample Curve>

        Information
        -----------
        - Socket 'Curves' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'mode' : 'LENGTH'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - length (Float) : socket 'Length' (id: Length)
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - use_all_curves (bool): parameter 'use_all_curves'

        Returns
        -------
        - Float [position_ (Vector), tangent_ (Vector), normal_ (Vector)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Curve.sample_length', 'value')
        node = Node('Sample Curve', sockets={'Curves': self, 'Value': value, 'Length': length, 'Curve Index': curve_index}, data_type=data_type, mode='LENGTH', use_all_curves=use_all_curves)
        return node._out

    def sample(self, value=None, curve_index=None, factor=None, mode='FACTOR', use_all_curves=False):
        """ > Node <&Node Sample Curve>

        Information
        -----------
        - Socket 'Curves' : self
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - factor (Float) : socket 'Factor' (id: Factor)
        - mode (str): parameter 'mode' in ['FACTOR', 'LENGTH']
        - use_all_curves (bool): parameter 'use_all_curves'

        Returns
        -------
        - Float [position_ (Vector), tangent_ (Vector), normal_ (Vector)]
        """
        utils.check_enum_arg('Sample Curve', 'mode', mode, 'sample', ('FACTOR', 'LENGTH'))
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Curve.sample', 'value')
        node = Node('Sample Curve', sockets={'Curves': self, 'Value': value, 'Curve Index': curve_index, 'Factor': factor}, data_type=data_type, mode=mode, use_all_curves=use_all_curves)
        return node._out

    def set_handle_positions(self, position=None, offset=None, mode='LEFT'):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - offset (Vector) : socket 'Offset' (id: Offset)
        - mode (str): parameter 'mode' in ['LEFT', 'RIGHT']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Positions', 'mode', mode, 'set_handle_positions', ('LEFT', 'RIGHT'))
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': position, 'Offset': offset}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_left_handle_positions(self, position=None, offset=None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'LEFT'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': position, 'Offset': offset}, mode='LEFT')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_right_handle_positions(self, position=None, offset=None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'RIGHT'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': position, 'Offset': offset}, mode='RIGHT')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_normal_minimum_twist(self):
        """ > Node <&Node Set Curve Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'MINIMUM_TWIST'

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Normal', sockets={'Curve': self, 'Selection': self._sel}, mode='MINIMUM_TWIST')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_normal_z_up(self):
        """ > Node <&Node Set Curve Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'Z_UP'

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Normal', sockets={'Curve': self, 'Selection': self._sel}, mode='Z_UP')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_normal_free(self, normal=None):
        """ > Node <&Node Set Curve Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'FREE'

        Arguments
        ---------
        - normal (Vector) : socket 'Normal' (id: Normal)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Normal', sockets={'Curve': self, 'Selection': self._sel, 'Normal': normal}, mode='FREE')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_normal(self, mode='MINIMUM_TWIST'):
        """ > Node <&Node Set Curve Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['MINIMUM_TWIST', 'Z_UP', 'FREE']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Curve Normal', 'mode', mode, 'set_normal', ('MINIMUM_TWIST', 'Z_UP', 'FREE'))
        node = Node('Set Curve Normal', sockets={'Curve': self, 'Selection': self._sel}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_radius(self, radius=None):
        """ > Node <&Node Set Curve Radius>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Radius', sockets={'Curve': self, 'Selection': self._sel, 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_tilt(self, tilt=None):
        """ > Node <&Node Set Curve Tilt>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - tilt (Float) : socket 'Tilt' (id: Tilt)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Tilt', sockets={'Curve': self, 'Selection': self._sel, 'Tilt': tilt})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def spline_length(cls):
        """ > Node <&Node Spline Length>

        Returns
        -------
        - Float [point_count_ (Integer)]
        """
        node = Node('Spline Length', sockets={})
        return node._out

    @classmethod
    def spline_parameter(cls):
        """ > Node <&Node Spline Parameter>

        Returns
        -------
        - Float [length_ (Float), index_ (Integer)]
        """
        node = Node('Spline Parameter', sockets={})
        return node._out

    def subdivide(self, cuts=None):
        """ > Node <&Node Subdivide Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self

        Arguments
        ---------
        - cuts (Integer) : socket 'Cuts' (id: Cuts)

        Returns
        -------
        - Curve
        """
        node = Node('Subdivide Curve', sockets={'Curve': self, 'Cuts': cuts})
        self._jump(node._out)
        return self._domain_to_geometry

    def trim_factor(self, start=None, end=None):
        """ > Node <&Node Trim Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'FACTOR'

        Arguments
        ---------
        - start (Float) : socket 'Start' (id: Start)
        - end (Float) : socket 'End' (id: End)

        Returns
        -------
        - Curve
        """
        node = Node('Trim Curve', sockets={'Curve': self, 'Selection': self._sel, 'Start': start, 'End': end}, mode='FACTOR')
        self._jump(node._out)
        return self._domain_to_geometry

    def trim_length(self, start=None, end=None):
        """ > Node <&Node Trim Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'LENGTH'

        Arguments
        ---------
        - start (Float) : socket 'Start' (id: Start_001)
        - end (Float) : socket 'End' (id: End_001)

        Returns
        -------
        - Curve
        """
        node = Node('Trim Curve', sockets={'Curve': self, 'Selection': self._sel, 'Start_001': start, 'End_001': end}, mode='LENGTH')
        self._jump(node._out)
        return self._domain_to_geometry

    def trim(self, start=None, end=None, mode='FACTOR'):
        """ > Node <&Node Trim Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - start (Float) : socket 'Start' (id: Start)
        - end (Float) : socket 'End' (id: End)
        - mode (str): parameter 'mode' in ['FACTOR', 'LENGTH']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Trim Curve', 'mode', mode, 'trim', ('FACTOR', 'LENGTH'))
        node = Node('Trim Curve', sockets={'Curve': self, 'Selection': self._sel, 'Start': start, 'End': end}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def radius(self):
        """ Property get node <Node Set Curve Radius>
        """
        return Node('Radius', sockets={})._out

    @radius.setter
    def radius(self, radius=None):
        """ > Node <&Node Set Curve Radius>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Radius', sockets={'Curve': self, 'Selection': self._sel, 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def left_handle_position(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', sockets={'Relative': False}).left

    @left_handle_position.setter
    def left_handle_position(self, position=None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Offset' : ignored
        - Parameter 'mode' : 'LEFT'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': position, 'Offset': None}, mode='LEFT')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def right_handle_position(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', sockets={'Relative': False}).right

    @right_handle_position.setter
    def right_handle_position(self, position=None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Offset' : ignored
        - Parameter 'mode' : 'RIGHT'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': position, 'Offset': None}, mode='RIGHT')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def left_handle_offset(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', sockets={'Relative': True}).left

    @left_handle_offset.setter
    def left_handle_offset(self, offset=None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Position' : ignored
        - Parameter 'mode' : 'LEFT'

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': None, 'Offset': offset}, mode='LEFT')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def right_handle_offset(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', sockets={'Relative': True}).right

    @right_handle_offset.setter
    def right_handle_offset(self, offset=None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Position' : ignored
        - Parameter 'mode' : 'RIGHT'

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': None, 'Offset': offset}, mode='RIGHT')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def handle_type(self):
        """ Write only property for node <Node Set Handle Type>
        """
        raise NodeError('Property Curve.handle_type is write only.')

    @handle_type.setter
    def handle_type(self, handle_type='AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'LEFT', 'RIGHT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'LEFT', 'RIGHT'})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def left_handle_type(self):
        """ Write only property for node <Node Set Handle Type>
        """
        raise NodeError('Property Curve.left_handle_type is write only.')

    @left_handle_type.setter
    def left_handle_type(self, handle_type='AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'LEFT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'left_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'LEFT'})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def right_handle_type(self):
        """ Write only property for node <Node Set Handle Type>
        """
        raise NodeError('Property Curve.right_handle_type is write only.')

    @right_handle_type.setter
    def right_handle_type(self, handle_type='AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'RIGHT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ['FREE', 'AUTO', 'VECTOR', 'ALIGN']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'right_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'RIGHT'})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def tilt(self):
        """ Property get node <Node Set Curve Tilt>
        """
        return Node('Curve Tilt', sockets={})._out

    @tilt.setter
    def tilt(self, tilt=None):
        """ > Node <&Node Set Curve Tilt>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - tilt (Float) : socket 'Tilt' (id: Tilt)

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Tilt', sockets={'Curve': self, 'Selection': self._sel, 'Tilt': tilt})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def normal(self):
        """ Write only property for node <Node Set Curve Normal>
        """
        raise NodeError('Property Curve.normal is write only.')

    @normal.setter
    def normal(self, mode='MINIMUM_TWIST'):
        """ > Node <&Node Set Curve Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['MINIMUM_TWIST', 'Z_UP', 'FREE']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Curve Normal', 'mode', mode, 'normal', ('MINIMUM_TWIST', 'Z_UP', 'FREE'))
        node = Node('Set Curve Normal', sockets={'Curve': self, 'Selection': self._sel}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def is_cyclic(self):
        """ Property get node <Node Set Spline Cyclic>
        """
        return Node('Is Spline Cyclic', sockets={})._out

    @is_cyclic.setter
    def is_cyclic(self, cyclic=None):
        """ > Node <&Node Set Spline Cyclic>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - cyclic (Boolean) : socket 'Cyclic' (id: Cyclic)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Spline Cyclic', sockets={'Geometry': self, 'Selection': self._sel, 'Cyclic': cyclic})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def resolution(self):
        """ Property get node <Node Set Spline Resolution>
        """
        return Node('Spline Resolution', sockets={})._out

    @resolution.setter
    def resolution(self, resolution=None):
        """ > Node <&Node Set Spline Resolution>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Spline Resolution', sockets={'Geometry': self, 'Selection': self._sel, 'Resolution': resolution})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def type(self):
        """ Write only property for node <Node Set Spline Type>
        """
        raise NodeError('Property Curve.type is write only.')

    @type.setter
    def type(self, spline_type='POLY'):
        """ > Node <&Node Set Spline Type>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - spline_type (str): parameter 'spline_type' in ['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS']

        Returns
        -------
        - Curve
        """
        utils.check_enum_arg('Set Spline Type', 'spline_type', spline_type, 'type', ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'))
        node = Node('Set Spline Type', sockets={'Curve': self, 'Selection': self._sel}, spline_type=spline_type)
        self._jump(node._out)
        return self._domain_to_geometry

