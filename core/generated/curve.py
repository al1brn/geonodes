from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Curve(Socket):

    @property
    def domain_size(self):
        """ > Property Get <&Node Domain Size>

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
    def ArcPOINTS(cls, resolution=None, start=None, middle=None, end=None, offset_angle=None, connect_center=None, invert_arc=None):
        """ > Constructor <&Node Arc>

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
    def ArcRADIUS(cls, resolution=None, radius=None, start_angle=None, sweep_angle=None, connect_center=None, invert_arc=None):
        """ > Constructor <&Node Arc>

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
        """ > Constructor <&Node Arc>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - radius (Float) : socket 'Radius' (id: Radius)
        - start_angle (Float) : socket 'Start Angle' (id: Start Angle)
        - sweep_angle (Float) : socket 'Sweep Angle' (id: Sweep Angle)
        - connect_center (Boolean) : socket 'Connect Center' (id: Connect Center)
        - invert_arc (Boolean) : socket 'Invert Arc' (id: Invert Arc)
        - mode (str): parameter 'mode' in ('POINTS', 'RADIUS')

        Returns
        -------
        - Curve
        """
        node = Node('Arc', sockets={'Resolution': resolution, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode=mode)
        return cls(node._out)

    @property
    def length(self):
        """ > Property Get <&Node Curve Length>

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
    def BeziersegmentPOSITION(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None):
        """ > Constructor <&Node Bézier Segment>

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
    def BeziersegmentOFFSET(cls, resolution=None, start=None, start_handle=None, end_handle=None, end=None):
        """ > Constructor <&Node Bézier Segment>

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
        """ > Constructor <&Node Bézier Segment>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - start (Vector) : socket 'Start' (id: Start)
        - start_handle (Vector) : socket 'Start Handle' (id: Start Handle)
        - end_handle (Vector) : socket 'End Handle' (id: End Handle)
        - end (Vector) : socket 'End' (id: End)
        - mode (str): parameter 'mode' in ('POSITION', 'OFFSET')

        Returns
        -------
        - Curve
        """
        node = Node('Bézier Segment', sockets={'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode=mode)
        return cls(node._out)

    @classmethod
    def CirclePOINTS(cls, resolution=None, point_1=None, point_2=None, point_3=None):
        """ > Constructor <&Node Curve Circle>

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
    def CircleRADIUS(cls, resolution=None, radius=None):
        """ > Constructor <&Node Curve Circle>

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
        """ > Constructor <&Node Curve Circle>

        Arguments
        ---------
        - resolution (Integer) : socket 'Resolution' (id: Resolution)
        - radius (Float) : socket 'Radius' (id: Radius)
        - mode (str): parameter 'mode' in ('POINTS', 'RADIUS')

        Returns
        -------
        - Curve
        """
        node = Node('Curve Circle', sockets={'Resolution': resolution, 'Radius': radius}, mode=mode)
        return cls(node._out)

    @classmethod
    def LinePOINTS(cls, start=None, end=None):
        """ > Constructor <&Node Curve Line>

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
    def LineDIRECTION(cls, start=None, direction=None, length=None):
        """ > Constructor <&Node Curve Line>

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
        """ > Constructor <&Node Curve Line>

        Arguments
        ---------
        - start (Vector) : socket 'Start' (id: Start)
        - end (Vector) : socket 'End' (id: End)
        - mode (str): parameter 'mode' in ('POINTS', 'DIRECTION')

        Returns
        -------
        - Curve
        """
        node = Node('Curve Line', sockets={'Start': start, 'End': end}, mode=mode)
        return cls(node._out)

    @classmethod
    def QuadrilateralRECTANGLE(cls, width=None, height=None):
        """ > Constructor <&Node Quadrilateral>

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
    def QuadrilateralPARALLELOGRAM(cls, width=None, height=None, offset=None):
        """ > Constructor <&Node Quadrilateral>

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
    def QuadrilateralTRAPEZOID(cls, width=None, height=None, bottom_width=None, top_width=None, offset=None):
        """ > Constructor <&Node Quadrilateral>

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
    def QuadrilateralKITE(cls, width=None, bottom_height=None, top_height=None):
        """ > Constructor <&Node Quadrilateral>

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
    def QuadrilateralPOINTS(cls, width=None, point_1=None, point_2=None, point_3=None, point_4=None):
        """ > Constructor <&Node Quadrilateral>

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
        """ > Constructor <&Node Quadrilateral>

        Arguments
        ---------
        - width (Float) : socket 'Width' (id: Width)
        - height (Float) : socket 'Height' (id: Height)
        - mode (str): parameter 'mode' in ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')

        Returns
        -------
        - Curve
        """
        node = Node('Quadrilateral', sockets={'Width': width, 'Height': height}, mode=mode)
        return cls(node._out)

    @classmethod
    def QuadraticBezier(cls, resolution=None, start=None, middle=None, end=None):
        """ > Constructor <&Node Quadratic Bézier>

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

    def set_handle_type(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """ > Jump Method <&Node Set Handle Type>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        - mode (set): parameter 'mode'

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode=mode)
        self._jump(node._out)
        return self

    def set_left_handle_type(self, handle_type='AUTO'):
        """ > Jump Method <&Node Set Handle Type>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'LEFT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'LEFT'})
        self._jump(node._out)
        return self

    def set_right_handle_type(self, handle_type='AUTO'):
        """ > Jump Method <&Node Set Handle Type>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'RIGHT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'RIGHT'})
        self._jump(node._out)
        return self

    def set_both_handle_type(self, handle_type='AUTO'):
        """ > Jump Method <&Node Set Handle Type>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'RIGHT', 'LEFT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'RIGHT', 'LEFT'})
        self._jump(node._out)
        return self

    @classmethod
    def Spiral(cls, resolution=None, rotations=None, start_radius=None, end_radius=None, height=None, reverse=None):
        """ > Constructor <&Node Spiral>

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
        """ > Jump Method <&Node Set Spline Type>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - spline_type (str): parameter 'spline_type' in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')

        Returns
        -------
        - Curve
        """
        node = Node('Set Spline Type', sockets={'Curve': self, 'Selection': self._sel}, spline_type=spline_type)
        self._jump(node._out)
        return self

    @classmethod
    def Star(cls, points=None, inner_radius=None, outer_radius=None, twist=None):
        """ > Constructor <&Node Star>

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
        """ > Method <&Node Curve to Mesh>

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
        """ > Method <&Node Curve to Points>

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
        """ > Method <&Node Curve to Points>

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
        """ > Method <&Node Curve to Points>

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
        """ > Method <&Node Curve to Points>

        Information
        -----------
        - Socket 'Curve' : self

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - mode (str): parameter 'mode' in ('EVALUATED', 'COUNT', 'LENGTH')

        Returns
        -------
        - Cloud [tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)]
        """
        node = Node('Curve to Points', sockets={'Curve': self, 'Count': count}, mode=mode)
        return node._out

    def to_grease_pencil(self, instances_as_layers=None):
        """ > Method <&Node Curves to Grease Pencil>

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
        """ > Jump Method <&Node Deform Curves on Surface>

        Information
        -----------
        - Socket 'Curves' : self

        Returns
        -------
        - Curve
        """
        node = Node('Deform Curves on Surface', sockets={'Curves': self})
        self._jump(node._out)
        return self

    def fill_triangles(self, group_id=None):
        """ > Method <&Node Fill Curve>

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
        """ > Method <&Node Fill Curve>

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
        """ > Method <&Node Fill Curve>

        Information
        -----------
        - Socket 'Curve' : self

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - mode (str): parameter 'mode' in ('TRIANGLES', 'NGONS')

        Returns
        -------
        - Mesh
        """
        node = Node('Fill Curve', sockets={'Curve': self, 'Group ID': group_id}, mode=mode)
        return node._out

    def fillet_bezier(self, radius=None, limit_radius=None):
        """ > Jump Method <&Node Fillet Curve>

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
        return self

    def fillet_poly(self, count=None, radius=None, limit_radius=None):
        """ > Jump Method <&Node Fillet Curve>

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
        return self

    def fillet(self, radius=None, limit_radius=None, mode='BEZIER'):
        """ > Jump Method <&Node Fillet Curve>

        Information
        -----------
        - Socket 'Curve' : self

        Arguments
        ---------
        - radius (Float) : socket 'Radius' (id: Radius)
        - limit_radius (Boolean) : socket 'Limit Radius' (id: Limit Radius)
        - mode (str): parameter 'mode' in ('BEZIER', 'POLY')

        Returns
        -------
        - Curve
        """
        node = Node('Fillet Curve', sockets={'Curve': self, 'Radius': radius, 'Limit Radius': limit_radius}, mode=mode)
        self._jump(node._out)
        return self

    @classmethod
    def Interpolate(cls, guide_curves=None, guide_up=None, guide_group_id=None, points=None, point_up=None, point_group_id=None, max_neighbors=None):
        """ > Constructor <&Node Interpolate Curves>

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
        """ > Jump Method <&Node Interpolate Curves>

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
        return self

    def resample_evaluated(self):
        """ > Jump Method <&Node Resample Curve>

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
        return self

    def resample_count(self, count=None):
        """ > Jump Method <&Node Resample Curve>

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
        return self

    def resample_length(self, length=None):
        """ > Jump Method <&Node Resample Curve>

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
        return self

    def resample(self, count=None, mode='COUNT'):
        """ > Jump Method <&Node Resample Curve>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - count (Integer) : socket 'Count' (id: Count)
        - mode (str): parameter 'mode' in ('EVALUATED', 'COUNT', 'LENGTH')

        Returns
        -------
        - Curve
        """
        node = Node('Resample Curve', sockets={'Curve': self, 'Selection': self._sel, 'Count': count}, mode=mode)
        self._jump(node._out)
        return self

    def reverse(self):
        """ > Jump Method <&Node Reverse Curve>

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
        return self

    def sample_factor(self, value=None, curve_index=None, factor=None, use_all_curves=False):
        """ > Method <&Node Sample Curve>

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
        """ > Method <&Node Sample Curve>

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
        """ > Method <&Node Sample Curve>

        Information
        -----------
        - Socket 'Curves' : self
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - curve_index (Integer) : socket 'Curve Index' (id: Curve Index)
        - factor (Float) : socket 'Factor' (id: Factor)
        - mode (str): parameter 'mode' in ('FACTOR', 'LENGTH')
        - use_all_curves (bool): parameter 'use_all_curves'

        Returns
        -------
        - Float [position_ (Vector), tangent_ (Vector), normal_ (Vector)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Curve.sample', 'value')
        node = Node('Sample Curve', sockets={'Curves': self, 'Value': value, 'Curve Index': curve_index, 'Factor': factor}, data_type=data_type, mode=mode, use_all_curves=use_all_curves)
        return node._out

    def set_handle_positions(self, position=None, offset=None, mode='LEFT'):
        """ > Jump Method <&Node Set Handle Positions>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - offset (Vector) : socket 'Offset' (id: Offset)
        - mode (str): parameter 'mode' in ('LEFT', 'RIGHT')

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': position, 'Offset': offset}, mode=mode)
        self._jump(node._out)
        return self

    def set_left_handle_positions(self, position=None, offset=None):
        """ > Jump Method <&Node Set Handle Positions>

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
        return self

    def set_right_handle_positions(self, position=None, offset=None):
        """ > Jump Method <&Node Set Handle Positions>

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
        return self

    def set_normal_minimum_twist(self):
        """ > Jump Method <&Node Set Curve Normal>

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
        return self

    def set_normal_z_up(self):
        """ > Jump Method <&Node Set Curve Normal>

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
        return self

    def set_normal_free(self, normal=None):
        """ > Jump Method <&Node Set Curve Normal>

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
        return self

    def set_normal(self, mode='MINIMUM_TWIST'):
        """ > Jump Method <&Node Set Curve Normal>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - mode (str): parameter 'mode' in ('MINIMUM_TWIST', 'Z_UP', 'FREE')

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Normal', sockets={'Curve': self, 'Selection': self._sel}, mode=mode)
        self._jump(node._out)
        return self

    def set_radius(self, radius=None):
        """ > Jump Method <&Node Set Curve Radius>

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
        return self

    def set_tilt(self, tilt=None):
        """ > Jump Method <&Node Set Curve Tilt>

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
        return self

    def subdivide(self, cuts=None):
        """ > Jump Method <&Node Subdivide Curve>

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
        return self

    def trim_factor(self, start=None, end=None):
        """ > Jump Method <&Node Trim Curve>

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
        return self

    def trim_length(self, start=None, end=None):
        """ > Jump Method <&Node Trim Curve>

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
        return self

    def trim(self, start=None, end=None, mode='FACTOR'):
        """ > Jump Method <&Node Trim Curve>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - start (Float) : socket 'Start' (id: Start)
        - end (Float) : socket 'End' (id: End)
        - mode (str): parameter 'mode' in ('FACTOR', 'LENGTH')

        Returns
        -------
        - Curve
        """
        node = Node('Trim Curve', sockets={'Curve': self, 'Selection': self._sel, 'Start': start, 'End': end}, mode=mode)
        self._jump(node._out)
        return self

    @property
    def radius(self):
        """ Property get node <Node Set Curve Radius>
        """
        return Node('Radius', sockets={})._out

    @radius.setter
    def radius(self, radius=None):
        """ > Jump Method <&Node Set Curve Radius>

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
        return self

    @property
    def left_handle_position(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', sockets={'Relative': False}).left

    @left_handle_position.setter
    def left_handle_position(self, position=None):
        """ > Jump Method <&Node Set Handle Positions>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'LEFT'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': position}, mode='LEFT')
        self._jump(node._out)
        return self

    @property
    def right_handle_position(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', sockets={'Relative': False}).right

    @right_handle_position.setter
    def right_handle_position(self, position=None):
        """ > Jump Method <&Node Set Handle Positions>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'RIGHT'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Position': position}, mode='RIGHT')
        self._jump(node._out)
        return self

    @property
    def left_handle_offset(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', sockets={'Relative': True}).left

    @left_handle_offset.setter
    def left_handle_offset(self, offset=None):
        """ > Jump Method <&Node Set Handle Positions>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'LEFT'

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Offset': offset}, mode='LEFT')
        self._jump(node._out)
        return self

    @property
    def right_handle_offset(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', sockets={'Relative': True}).right

    @right_handle_offset.setter
    def right_handle_offset(self, offset=None):
        """ > Jump Method <&Node Set Handle Positions>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'RIGHT'

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Positions', sockets={'Curve': self, 'Selection': self._sel, 'Offset': offset}, mode='RIGHT')
        self._jump(node._out)
        return self

    @property
    def handle_type(self):
        """ Write only property for node <Node Set Handle Type>
        """
        raise NodeError('Property Curve.handle_type is write only.')

    @handle_type.setter
    def handle_type(self, handle_type='AUTO'):
        """ > Jump Method <&Node Set Handle Type>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'RIGHT', 'LEFT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'RIGHT', 'LEFT'})
        self._jump(node._out)
        return self

    @property
    def left_handle_type(self):
        """ Write only property for node <Node Set Handle Type>
        """
        raise NodeError('Property Curve.left_handle_type is write only.')

    @left_handle_type.setter
    def left_handle_type(self, handle_type='AUTO'):
        """ > Jump Method <&Node Set Handle Type>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'LEFT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'LEFT'})
        self._jump(node._out)
        return self

    @property
    def right_handle_type(self):
        """ Write only property for node <Node Set Handle Type>
        """
        raise NodeError('Property Curve.right_handle_type is write only.')

    @right_handle_type.setter
    def right_handle_type(self, handle_type='AUTO'):
        """ > Jump Method <&Node Set Handle Type>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : {'RIGHT'}

        Arguments
        ---------
        - handle_type (str): parameter 'handle_type' in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')

        Returns
        -------
        - Curve
        """
        node = Node('Set Handle Type', sockets={'Curve': self, 'Selection': self._sel}, handle_type=handle_type, mode={'RIGHT'})
        self._jump(node._out)
        return self

    @property
    def tilt(self):
        """ Property get node <Node Set Curve Tilt>
        """
        return Node('Curve Tilt', sockets={})._out

    @tilt.setter
    def tilt(self, tilt=None):
        """ > Jump Method <&Node Set Curve Tilt>

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
        return self

    @property
    def normal(self):
        """ Write only property for node <Node Set Curve Normal>
        """
        raise NodeError('Property Curve.normal is write only.')

    @normal.setter
    def normal(self, mode='MINIMUM_TWIST'):
        """ > Jump Method <&Node Set Curve Normal>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - mode (str): parameter 'mode' in ('MINIMUM_TWIST', 'Z_UP', 'FREE')

        Returns
        -------
        - Curve
        """
        node = Node('Set Curve Normal', sockets={'Curve': self, 'Selection': self._sel}, mode=mode)
        self._jump(node._out)
        return self

    @property
    def is_cyclic(self):
        """ Property get node <Node Set Spline Cyclic>
        """
        return Node('Is Spline Cyclic', sockets={})._out

    @is_cyclic.setter
    def is_cyclic(self, cyclic=None):
        """ > Jump Method <&Node Set Spline Cyclic>

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
        return self

    @property
    def resolution(self):
        """ Property get node <Node Set Spline Resolution>
        """
        return Node('Spline Resolution', sockets={})._out

    @resolution.setter
    def resolution(self, resolution=None):
        """ > Jump Method <&Node Set Spline Resolution>

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
        return self

    @property
    def type(self):
        """ Write only property for node <Node Set Spline Type>
        """
        raise NodeError('Property Curve.type is write only.')

    @type.setter
    def type(self, spline_type='POLY'):
        """ > Jump Method <&Node Set Spline Type>

        Information
        -----------
        - Socket 'Curve' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - spline_type (str): parameter 'spline_type' in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')

        Returns
        -------
        - Curve
        """
        node = Node('Set Spline Type', sockets={'Curve': self, 'Selection': self._sel}, spline_type=spline_type)
        self._jump(node._out)
        return self

