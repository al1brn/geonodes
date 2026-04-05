# Generated 2026-04-05 13:07:21

from __future__ import annotations
from .. sockettype import SocketType
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves
from .. import utils
from .. scripterror import NodeError
from typing import TYPE_CHECKING, Literal, Union, Sequence

if TYPE_CHECKING:
    class Geometry: ...
    class Mesh: ...
    class Curve: ...
    class Cloud: ...
    class Instances: ...
    class Volume: ...
    class GreasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class Curve(Socket):

    __slots__ = ()

    """"
    $DOC SET hidden
    """
    def domain_size(self):
        """ > Node <&Node Domain Size>

        **Fixed values**

        | Kind      | Name        | Value     |
        | --------- | ----------- | --------- |
        | Socket    | Geometry    | `self`    |
        | Parameter | `component` | `'CURVE'` |

        Returns
        -------
        Integer
            peer sockets: spline_count_ (Integer)

        """
        node = self._cache('Domain Size', {'Geometry': self}, component='CURVE')
        return node._out

    @classmethod
    def ArcPoints(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None,
                    offset_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None):
        """ > Node <&Node Arc>

        **Fixed values**

        | Kind      | Name   | Value      |
        | --------- | ------ | ---------- |
        | Parameter | `mode` | `'POINTS'` |

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        start : Vector, optional
            socket 'Start' (id: Start)
        
        middle : Vector, optional
            socket 'Middle' (id: Middle)
        
        end : Vector, optional
            socket 'End' (id: End)
        
        offset_angle : Float, optional
            socket 'Offset Angle' (id: Offset Angle)
        
        connect_center : Boolean, optional
            socket 'Connect Center' (id: Connect Center)
        
        invert_arc : Boolean, optional
            socket 'Invert Arc' (id: Invert Arc)
        

        Returns
        -------
        Curve
        """
        node = Node('Arc', {'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end, 'Offset Angle': offset_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode='POINTS')
        return cls(node._out)

    @classmethod
    def ArcRadius(cls,
                    resolution: Integer = None,
                    radius: Float = None,
                    start_angle: Float = None,
                    sweep_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None):
        """ > Node <&Node Arc>

        **Fixed values**

        | Kind      | Name   | Value      |
        | --------- | ------ | ---------- |
        | Parameter | `mode` | `'RADIUS'` |

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        start_angle : Float, optional
            socket 'Start Angle' (id: Start Angle)
        
        sweep_angle : Float, optional
            socket 'Sweep Angle' (id: Sweep Angle)
        
        connect_center : Boolean, optional
            socket 'Connect Center' (id: Connect Center)
        
        invert_arc : Boolean, optional
            socket 'Invert Arc' (id: Invert Arc)
        

        Returns
        -------
        Curve
        """
        node = Node('Arc', {'Resolution': resolution, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode='RADIUS')
        return cls(node._out)

    @classmethod
    def Arc(cls,
                    resolution: Integer = None,
                    radius: Float = None,
                    start_angle: Float = None,
                    sweep_angle: Float = None,
                    connect_center: Boolean = None,
                    invert_arc: Boolean = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS'):
        """ > Node <&Node Arc>

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        start_angle : Float, optional
            socket 'Start Angle' (id: Start Angle)
        
        sweep_angle : Float, optional
            socket 'Sweep Angle' (id: Sweep Angle)
        
        connect_center : Boolean, optional
            socket 'Connect Center' (id: Connect Center)
        
        invert_arc : Boolean, optional
            socket 'Invert Arc' (id: Invert Arc)
        
        mode : Literal['Points', 'Radius']
            parameter `mode`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Arc', 'mode', mode, 'Arc', ('POINTS', 'RADIUS'))
        node = Node('Arc', {'Resolution': resolution, 'Radius': radius, 'Start Angle': start_angle, 'Sweep Angle': sweep_angle, 'Connect Center': connect_center, 'Invert Arc': invert_arc}, mode=mode)
        return cls(node._out)

    @classmethod
    def endpoint_selection(cls, start_size: Integer = None, end_size: Integer = None):
        """ > Node <&Node Endpoint Selection>

        Parameters
        ----------
        start_size : Integer, optional
            socket 'Start Size' (id: Start Size)
        
        end_size : Integer, optional
            socket 'End Size' (id: End Size)
        

        Returns
        -------
        Boolean
        """
        node = Node('Endpoint Selection', {'Start Size': start_size, 'End Size': end_size})
        return node._out

    @classmethod
    def handle_type_selection(cls,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'}):
        """ > Node <&Node Handle Type Selection>

        Parameters
        ----------
        handle_type : Literal['Free', 'Auto', 'Vector', 'Align']
            parameter `handle_type`
        
        mode : set
            parameter `mode`
        

        Returns
        -------
        Boolean
        """
        utils.check_enum_arg('Handle Type Selection', 'handle_type', handle_type, 'handle_type_selection', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Handle Type Selection', handle_type=handle_type, mode=mode)
        return node._out

    def length(self):
        """ > Node <&Node Curve Length>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Curve | `self` |

        Returns
        -------
        Float
        """
        node = Node('Curve Length', {'Curve': self})
        return node._out

    @classmethod
    def curve_of_point(cls, point_index: Integer = None):
        """ > Node <&Node Curve of Point>

        Parameters
        ----------
        point_index : Integer, optional
            socket 'Point Index' (id: Point Index)
        

        Returns
        -------
        Integer
            peer sockets: index_in_curve_ (Integer)

        """
        node = Node('Curve of Point', {'Point Index': point_index})
        return node._out

    @classmethod
    def BeziersegmentPosition(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None):
        """ > Node <&Node Bézier Segment>

        **Fixed values**

        | Kind      | Name   | Value        |
        | --------- | ------ | ------------ |
        | Parameter | `mode` | `'POSITION'` |

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        start : Vector, optional
            socket 'Start' (id: Start)
        
        start_handle : Vector, optional
            socket 'Start Handle' (id: Start Handle)
        
        end_handle : Vector, optional
            socket 'End Handle' (id: End Handle)
        
        end : Vector, optional
            socket 'End' (id: End)
        

        Returns
        -------
        Curve
        """
        node = Node('Bézier Segment', {'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode='POSITION')
        return cls(node._out)

    @classmethod
    def BeziersegmentOffset(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None):
        """ > Node <&Node Bézier Segment>

        **Fixed values**

        | Kind      | Name   | Value      |
        | --------- | ------ | ---------- |
        | Parameter | `mode` | `'OFFSET'` |

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        start : Vector, optional
            socket 'Start' (id: Start)
        
        start_handle : Vector, optional
            socket 'Start Handle' (id: Start Handle)
        
        end_handle : Vector, optional
            socket 'End Handle' (id: End Handle)
        
        end : Vector, optional
            socket 'End' (id: End)
        

        Returns
        -------
        Curve
        """
        node = Node('Bézier Segment', {'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode='OFFSET')
        return cls(node._out)

    @classmethod
    def BezierSegment(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    start_handle: Vector = None,
                    end_handle: Vector = None,
                    end: Vector = None,
                    mode: Literal['POSITION', 'OFFSET'] = 'POSITION'):
        """ > Node <&Node Bézier Segment>

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        start : Vector, optional
            socket 'Start' (id: Start)
        
        start_handle : Vector, optional
            socket 'Start Handle' (id: Start Handle)
        
        end_handle : Vector, optional
            socket 'End Handle' (id: End Handle)
        
        end : Vector, optional
            socket 'End' (id: End)
        
        mode : Literal['Position', 'Offset']
            parameter `mode`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Bézier Segment', 'mode', mode, 'BezierSegment', ('POSITION', 'OFFSET'))
        node = Node('Bézier Segment', {'Resolution': resolution, 'Start': start, 'Start Handle': start_handle, 'End Handle': end_handle, 'End': end}, mode=mode)
        return cls(node._out)

    @classmethod
    def CirclePoints(cls,
                    resolution: Integer = None,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None):
        """ > Node <&Node Curve Circle>

        **Fixed values**

        | Kind      | Name   | Value      |
        | --------- | ------ | ---------- |
        | Parameter | `mode` | `'POINTS'` |

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        point_1 : Vector, optional
            socket 'Point 1' (id: Point 1)
        
        point_2 : Vector, optional
            socket 'Point 2' (id: Point 2)
        
        point_3 : Vector, optional
            socket 'Point 3' (id: Point 3)
        

        Returns
        -------
        Curve
        """
        node = Node('Curve Circle', {'Resolution': resolution, 'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3}, mode='POINTS')
        return cls(node._out)

    @classmethod
    def CircleRadius(cls, resolution: Integer = None, radius: Float = None):
        """ > Node <&Node Curve Circle>

        **Fixed values**

        | Kind      | Name   | Value      |
        | --------- | ------ | ---------- |
        | Parameter | `mode` | `'RADIUS'` |

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Curve
        """
        node = Node('Curve Circle', {'Resolution': resolution, 'Radius': radius}, mode='RADIUS')
        return cls(node._out)

    @classmethod
    def Circle(cls,
                    resolution: Integer = None,
                    radius: Float = None,
                    mode: Literal['POINTS', 'RADIUS'] = 'RADIUS'):
        """ > Node <&Node Curve Circle>

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        mode : Literal['Points', 'Radius']
            parameter `mode`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Curve Circle', 'mode', mode, 'Circle', ('POINTS', 'RADIUS'))
        node = Node('Curve Circle', {'Resolution': resolution, 'Radius': radius}, mode=mode)
        return cls(node._out)

    @classmethod
    def LinePoints(cls, start: Vector = None, end: Vector = None):
        """ > Node <&Node Curve Line>

        **Fixed values**

        | Kind      | Name   | Value      |
        | --------- | ------ | ---------- |
        | Parameter | `mode` | `'POINTS'` |

        Parameters
        ----------
        start : Vector, optional
            socket 'Start' (id: Start)
        
        end : Vector, optional
            socket 'End' (id: End)
        

        Returns
        -------
        Curve
        """
        node = Node('Curve Line', {'Start': start, 'End': end}, mode='POINTS')
        return cls(node._out)

    @classmethod
    def LineDirection(cls, start: Vector = None, direction: Vector = None, length: Float = None):
        """ > Node <&Node Curve Line>

        **Fixed values**

        | Kind      | Name   | Value         |
        | --------- | ------ | ------------- |
        | Parameter | `mode` | `'DIRECTION'` |

        Parameters
        ----------
        start : Vector, optional
            socket 'Start' (id: Start)
        
        direction : Vector, optional
            socket 'Direction' (id: Direction)
        
        length : Float, optional
            socket 'Length' (id: Length)
        

        Returns
        -------
        Curve
        """
        node = Node('Curve Line', {'Start': start, 'Direction': direction, 'Length': length}, mode='DIRECTION')
        return cls(node._out)

    @classmethod
    def Line(cls,
                    start: Vector = None,
                    end: Vector = None,
                    mode: Literal['POINTS', 'DIRECTION'] = 'POINTS'):
        """ > Node <&Node Curve Line>

        Parameters
        ----------
        start : Vector, optional
            socket 'Start' (id: Start)
        
        end : Vector, optional
            socket 'End' (id: End)
        
        mode : Literal['Points', 'Direction']
            parameter `mode`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Curve Line', 'mode', mode, 'Line', ('POINTS', 'DIRECTION'))
        node = Node('Curve Line', {'Start': start, 'End': end}, mode=mode)
        return cls(node._out)

    @classmethod
    def QuadrilateralRectangle(cls, width: Float = None, height: Float = None):
        """ > Node <&Node Quadrilateral>

        **Fixed values**

        | Kind      | Name   | Value         |
        | --------- | ------ | ------------- |
        | Parameter | `mode` | `'RECTANGLE'` |

        Parameters
        ----------
        width : Float, optional
            socket 'Width' (id: Width)
        
        height : Float, optional
            socket 'Height' (id: Height)
        

        Returns
        -------
        Curve
        """
        node = Node('Quadrilateral', {'Width': width, 'Height': height}, mode='RECTANGLE')
        return cls(node._out)

    @classmethod
    def QuadrilateralParallelogram(cls, width: Float = None, height: Float = None, offset: Float = None):
        """ > Node <&Node Quadrilateral>

        **Fixed values**

        | Kind      | Name   | Value             |
        | --------- | ------ | ----------------- |
        | Parameter | `mode` | `'PARALLELOGRAM'` |

        Parameters
        ----------
        width : Float, optional
            socket 'Width' (id: Width)
        
        height : Float, optional
            socket 'Height' (id: Height)
        
        offset : Float, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Curve
        """
        node = Node('Quadrilateral', {'Width': width, 'Height': height, 'Offset': offset}, mode='PARALLELOGRAM')
        return cls(node._out)

    @classmethod
    def QuadrilateralTrapezoid(cls,
                    height: Float = None,
                    bottom_width: Float = None,
                    top_width: Float = None,
                    offset: Float = None):
        """ > Node <&Node Quadrilateral>

        **Fixed values**

        | Kind      | Name   | Value         |
        | --------- | ------ | ------------- |
        | Parameter | `mode` | `'TRAPEZOID'` |

        Parameters
        ----------
        height : Float, optional
            socket 'Height' (id: Height)
        
        bottom_width : Float, optional
            socket 'Bottom Width' (id: Bottom Width)
        
        top_width : Float, optional
            socket 'Top Width' (id: Top Width)
        
        offset : Float, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Curve
        """
        node = Node('Quadrilateral', {'Height': height, 'Bottom Width': bottom_width, 'Top Width': top_width, 'Offset': offset}, mode='TRAPEZOID')
        return cls(node._out)

    @classmethod
    def QuadrilateralKite(cls,
                    width: Float = None,
                    bottom_height: Float = None,
                    top_height: Float = None):
        """ > Node <&Node Quadrilateral>

        **Fixed values**

        | Kind      | Name   | Value    |
        | --------- | ------ | -------- |
        | Parameter | `mode` | `'KITE'` |

        Parameters
        ----------
        width : Float, optional
            socket 'Width' (id: Width)
        
        bottom_height : Float, optional
            socket 'Bottom Height' (id: Bottom Height)
        
        top_height : Float, optional
            socket 'Top Height' (id: Top Height)
        

        Returns
        -------
        Curve
        """
        node = Node('Quadrilateral', {'Width': width, 'Bottom Height': bottom_height, 'Top Height': top_height}, mode='KITE')
        return cls(node._out)

    @classmethod
    def QuadrilateralPoints(cls,
                    point_1: Vector = None,
                    point_2: Vector = None,
                    point_3: Vector = None,
                    point_4: Vector = None):
        """ > Node <&Node Quadrilateral>

        **Fixed values**

        | Kind      | Name   | Value      |
        | --------- | ------ | ---------- |
        | Parameter | `mode` | `'POINTS'` |

        Parameters
        ----------
        point_1 : Vector, optional
            socket 'Point 1' (id: Point 1)
        
        point_2 : Vector, optional
            socket 'Point 2' (id: Point 2)
        
        point_3 : Vector, optional
            socket 'Point 3' (id: Point 3)
        
        point_4 : Vector, optional
            socket 'Point 4' (id: Point 4)
        

        Returns
        -------
        Curve
        """
        node = Node('Quadrilateral', {'Point 1': point_1, 'Point 2': point_2, 'Point 3': point_3, 'Point 4': point_4}, mode='POINTS')
        return cls(node._out)

    @classmethod
    def Quadrilateral(cls,
                    width: Float = None,
                    height: Float = None,
                    mode: Literal['RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS'] = 'RECTANGLE'):
        """ > Node <&Node Quadrilateral>

        Parameters
        ----------
        width : Float, optional
            socket 'Width' (id: Width)
        
        height : Float, optional
            socket 'Height' (id: Height)
        
        mode : Literal['Rectangle', 'Parallelogram', 'Trapezoid', 'Kite', 'Points']
            parameter `mode`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Quadrilateral', 'mode', mode, 'Quadrilateral', ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS'))
        node = Node('Quadrilateral', {'Width': width, 'Height': height}, mode=mode)
        return cls(node._out)

    @classmethod
    def QuadraticBezier(cls,
                    resolution: Integer = None,
                    start: Vector = None,
                    middle: Vector = None,
                    end: Vector = None):
        """ > Node <&Node Quadratic Bézier>

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        start : Vector, optional
            socket 'Start' (id: Start)
        
        middle : Vector, optional
            socket 'Middle' (id: Middle)
        
        end : Vector, optional
            socket 'End' (id: End)
        

        Returns
        -------
        Curve
        """
        node = Node('Quadratic Bézier', {'Resolution': resolution, 'Start': start, 'Middle': middle, 'End': end})
        return cls(node._out)

    def set_handle_type(self,
                    handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO',
                    mode = {'RIGHT', 'LEFT'}):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        handle_type : Literal['Free', 'Auto', 'Vector', 'Align']
            parameter `handle_type`
        
        mode : set
            parameter `mode`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', {'Curve': self, 'Selection': self.get_selection()}, handle_type=handle_type, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_left_handle_type(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `{'LEFT'}`        |

        Parameters
        ----------
        handle_type : Literal['Free', 'Auto', 'Vector', 'Align']
            parameter `handle_type`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_left_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', {'Curve': self, 'Selection': self.get_selection()}, handle_type=handle_type, mode={'LEFT'})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_right_handle_type(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `{'RIGHT'}`       |

        Parameters
        ----------
        handle_type : Literal['Free', 'Auto', 'Vector', 'Align']
            parameter `handle_type`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_right_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', {'Curve': self, 'Selection': self.get_selection()}, handle_type=handle_type, mode={'RIGHT'})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_both_handle_type(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value               |
        | --------- | --------- | ------------------- |
        | Socket    | Curve     | `self`              |
        | Socket    | Selection | `self[selection]`   |
        | Parameter | `mode`    | `{'RIGHT', 'LEFT'}` |

        Parameters
        ----------
        handle_type : Literal['Free', 'Auto', 'Vector', 'Align']
            parameter `handle_type`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'set_both_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', {'Curve': self, 'Selection': self.get_selection()}, handle_type=handle_type, mode={'RIGHT', 'LEFT'})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Spiral(cls,
                    resolution: Integer = None,
                    rotations: Float = None,
                    start_radius: Float = None,
                    end_radius: Float = None,
                    height: Float = None,
                    reverse: Boolean = None):
        """ > Node <&Node Spiral>

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        
        rotations : Float, optional
            socket 'Rotations' (id: Rotations)
        
        start_radius : Float, optional
            socket 'Start Radius' (id: Start Radius)
        
        end_radius : Float, optional
            socket 'End Radius' (id: End Radius)
        
        height : Float, optional
            socket 'Height' (id: Height)
        
        reverse : Boolean, optional
            socket 'Reverse' (id: Reverse)
        

        Returns
        -------
        Curve
        """
        node = Node('Spiral', {'Resolution': resolution, 'Rotations': rotations, 'Start Radius': start_radius, 'End Radius': end_radius, 'Height': height, 'Reverse': reverse})
        return cls(node._out)

    def set_spline_type(self, spline_type: Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'] = 'POLY'):
        """ > Node <&Node Set Spline Type>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        spline_type : Literal['Catmull Rom', 'Poly', 'Bézier', 'NURBS']
            parameter `spline_type`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Spline Type', 'spline_type', spline_type, 'set_spline_type', ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'))
        node = Node('Set Spline Type', {'Curve': self, 'Selection': self.get_selection()}, spline_type=spline_type)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Star(cls,
                    points: Integer = None,
                    inner_radius: Float = None,
                    outer_radius: Float = None,
                    twist: Float = None):
        """ > Node <&Node Star>

        Parameters
        ----------
        points : Integer, optional
            socket 'Points' (id: Points)
        
        inner_radius : Float, optional
            socket 'Inner Radius' (id: Inner Radius)
        
        outer_radius : Float, optional
            socket 'Outer Radius' (id: Outer Radius)
        
        twist : Float, optional
            socket 'Twist' (id: Twist)
        

        Returns
        -------
        Curve
        """
        node = Node('Star', {'Points': points, 'Inner Radius': inner_radius, 'Outer Radius': outer_radius, 'Twist': twist})
        return cls(node._out)

    def to_mesh(self,
                    profile_curve: Curve = None,
                    scale: Float = None,
                    fill_caps: Boolean = None):
        """ > Node <&Node Curve to Mesh>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Curve | `self` |

        Parameters
        ----------
        profile_curve : Curve, optional
            socket 'Profile Curve' (id: Profile Curve)
        
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        fill_caps : Boolean, optional
            socket 'Fill Caps' (id: Fill Caps)
        

        Returns
        -------
        Mesh
        """
        node = Node('Curve to Mesh', {'Curve': self, 'Profile Curve': profile_curve, 'Scale': scale, 'Fill Caps': fill_caps})
        return node._out

    def to_points_evaluated(self):
        """ > Node <&Node Curve to Points>

        **Fixed values**

        | Kind      | Name   | Value         |
        | --------- | ------ | ------------- |
        | Socket    | Curve  | `self`        |
        | Parameter | `mode` | `'EVALUATED'` |

        Returns
        -------
        Cloud
            peer sockets: tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)

        """
        node = Node('Curve to Points', {'Curve': self}, mode='EVALUATED')
        return node._out

    def to_points_count(self, count: Integer = None):
        """ > Node <&Node Curve to Points>

        **Fixed values**

        | Kind      | Name   | Value     |
        | --------- | ------ | --------- |
        | Socket    | Curve  | `self`    |
        | Parameter | `mode` | `'COUNT'` |

        Parameters
        ----------
        count : Integer, optional
            socket 'Count' (id: Count)
        

        Returns
        -------
        Cloud
            peer sockets: tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)

        """
        node = Node('Curve to Points', {'Curve': self, 'Count': count}, mode='COUNT')
        return node._out

    def to_points_length(self, length: Float = None):
        """ > Node <&Node Curve to Points>

        **Fixed values**

        | Kind      | Name   | Value      |
        | --------- | ------ | ---------- |
        | Socket    | Curve  | `self`     |
        | Parameter | `mode` | `'LENGTH'` |

        Parameters
        ----------
        length : Float, optional
            socket 'Length' (id: Length)
        

        Returns
        -------
        Cloud
            peer sockets: tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)

        """
        node = Node('Curve to Points', {'Curve': self, 'Length': length}, mode='LENGTH')
        return node._out

    def to_points(self,
                    count: Integer = None,
                    mode: Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT'):
        """ > Node <&Node Curve to Points>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Curve | `self` |

        Parameters
        ----------
        count : Integer, optional
            socket 'Count' (id: Count)
        
        mode : Literal['Evaluated', 'Count', 'Length']
            parameter `mode`
        

        Returns
        -------
        Cloud
            peer sockets: tangent_ (Vector), normal_ (Vector), rotation_ (Rotation)

        """
        utils.check_enum_arg('Curve to Points', 'mode', mode, 'to_points', ('EVALUATED', 'COUNT', 'LENGTH'))
        node = Node('Curve to Points', {'Curve': self, 'Count': count}, mode=mode)
        return node._out

    def to_grease_pencil(self, instances_as_layers: Boolean = None):
        """ > Node <&Node Curves to Grease Pencil>

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curves    | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        instances_as_layers : Boolean, optional
            socket 'Instances as Layers' (id: Instances as Layers)
        

        Returns
        -------
        GreasePencil
        """
        node = Node('Curves to Grease Pencil', {'Curves': self, 'Selection': self.get_selection(), 'Instances as Layers': instances_as_layers})
        return node._out

    def deform_on_surface(self):
        """ > Node <&Node Deform Curves on Surface>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name   | Value  |
        | ------ | ------ | ------ |
        | Socket | Curves | `self` |

        Returns
        -------
        Curve
        """
        node = Node('Deform Curves on Surface', {'Curves': self})
        self._jump(node._out)
        return self._domain_to_geometry

    def fill(self,
                    group_id: Integer = None,
                    mode: Literal['Triangles', 'N-gons'] = None,
                    fill_rule: Literal['Even-Odd', 'Non-Zero'] = None):
        """ > Node <&Node Fill Curve>

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Curve | `self` |

        Parameters
        ----------
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        
        mode : menu='Triangles', optional
            ('Triangles', 'N-gons')
        
        fill_rule : menu='Even-Odd', optional
            ('Even-Odd', 'Non-Zero')
        

        Returns
        -------
        Mesh
        """
        node = Node('Fill Curve', {'Curve': self, 'Group ID': group_id, 'Mode': mode, 'Fill Rule': fill_rule})
        return node._out

    def fillet(self,
                    radius: Float = None,
                    limit_radius: Boolean = None,
                    mode: Literal['Bézier', 'Poly'] = None,
                    count: Integer = None):
        """ > Node <&Node Fillet Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Curve | `self` |

        Parameters
        ----------
        radius : Float, optional
            socket 'Radius' (id: Radius)
        
        limit_radius : Boolean, optional
            socket 'Limit Radius' (id: Limit Radius)
        
        mode : menu='Bézier', optional
            ('Bézier', 'Poly')
        
        count : Integer, optional
            socket 'Count' (id: Count)
        

        Returns
        -------
        Curve
        """
        node = Node('Fillet Curve', {'Curve': self, 'Radius': radius, 'Limit Radius': limit_radius, 'Mode': mode, 'Count': count})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def handle_positions(cls, relative: Boolean = None):
        """ > Node <&Node Curve Handle Positions>

        Parameters
        ----------
        relative : Boolean, optional
            socket 'Relative' (id: Relative)
        

        Returns
        -------
        Vector
            peer sockets: right_ (Vector)

        """
        node = Node('Curve Handle Positions', {'Relative': relative})
        return node._out

    @utils.classproperty
    def tangent(cls):
        """ > Node <&Node Curve Tangent>

        Returns
        -------
        Vector
        """
        node = Node('Curve Tangent', )
        return node._out

    @classmethod
    def Interpolate(cls,
                    guide_curves: Curve = None,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    points: Cloud = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None):
        """ > Node <&Node Interpolate Curves>

        Parameters
        ----------
        guide_curves : Curve, optional
            socket 'Guide Curves' (id: Guide Curves)
        
        guide_up : Vector, optional
            socket 'Guide Up' (id: Guide Up)
        
        guide_group_id : Integer, optional
            socket 'Guide Group ID' (id: Guide Group ID)
        
        points : Cloud, optional
            socket 'Points' (id: Points)
        
        point_up : Vector, optional
            socket 'Point Up' (id: Point Up)
        
        point_group_id : Integer, optional
            socket 'Point Group ID' (id: Point Group ID)
        
        max_neighbors : Integer, optional
            socket 'Max Neighbors' (id: Max Neighbors)
        

        Returns
        -------
        Curve
        """
        node = Node('Interpolate Curves', {'Guide Curves': guide_curves, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        return cls(node._out)

    def interpolate(self,
                    guide_up: Vector = None,
                    guide_group_id: Integer = None,
                    points: Cloud = None,
                    point_up: Vector = None,
                    point_group_id: Integer = None,
                    max_neighbors: Integer = None):
        """ > Node <&Node Interpolate Curves>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name         | Value  |
        | ------ | ------------ | ------ |
        | Socket | Guide Curves | `self` |

        Parameters
        ----------
        guide_up : Vector, optional
            socket 'Guide Up' (id: Guide Up)
        
        guide_group_id : Integer, optional
            socket 'Guide Group ID' (id: Guide Group ID)
        
        points : Cloud, optional
            socket 'Points' (id: Points)
        
        point_up : Vector, optional
            socket 'Point Up' (id: Point Up)
        
        point_group_id : Integer, optional
            socket 'Point Group ID' (id: Point Group ID)
        
        max_neighbors : Integer, optional
            socket 'Max Neighbors' (id: Max Neighbors)
        

        Returns
        -------
        Curve
            peer sockets: closest_index_ (Integer), closest_weight_ (Float)

        """
        node = Node('Interpolate Curves', {'Guide Curves': self, 'Guide Up': guide_up, 'Guide Group ID': guide_group_id, 'Points': points, 'Point Up': point_up, 'Point Group ID': point_group_id, 'Max Neighbors': max_neighbors})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def material_selection(cls, material: Material = None):
        """ > Node <&Node Material Selection>

        Parameters
        ----------
        material : Material, optional
            socket 'Material' (id: Material)
        

        Returns
        -------
        Boolean
        """
        node = Node('Material Selection', {'Material': material})
        return node._out

    @classmethod
    def offset_point_in_curve(cls, point_index: Integer = None, offset: Integer = None):
        """ > Node <&Node Offset Point in Curve>

        Parameters
        ----------
        point_index : Integer, optional
            socket 'Point Index' (id: Point Index)
        
        offset : Integer, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Boolean
            peer sockets: point_index_ (Integer)

        """
        node = Node('Offset Point in Curve', {'Point Index': point_index, 'Offset': offset})
        return node._out

    @classmethod
    def points_of_curve(cls,
                    curve_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Points of Curve>

        Parameters
        ----------
        curve_index : Integer, optional
            socket 'Curve Index' (id: Curve Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        Integer
            peer sockets: total_ (Integer)

        """
        node = Node('Points of Curve', {'Curve Index': curve_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    def resample(self,
                    mode: Literal['Evaluated', 'Count', 'Length'] = None,
                    count: Integer = None,
                    length: Float = None,
                    keep_last_segment = True):
        """ > Node <&Node Resample Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        mode : menu='Count', optional
            ('Evaluated', 'Count', 'Length')
        
        count : Integer, optional
            socket 'Count' (id: Count)
        
        length : Float, optional
            socket 'Length' (id: Length)
        
        keep_last_segment : bool
            parameter `keep_last_segment`
        

        Returns
        -------
        Curve
        """
        node = Node('Resample Curve', {'Curve': self, 'Selection': self.get_selection(), 'Mode': mode, 'Count': count, 'Length': length}, keep_last_segment=keep_last_segment)
        self._jump(node._out)
        return self._domain_to_geometry

    def reverse(self):
        """ > Node <&Node Reverse Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Returns
        -------
        Curve
        """
        node = Node('Reverse Curve', {'Curve': self, 'Selection': self.get_selection()})
        self._jump(node._out)
        return self._domain_to_geometry

    def sample_factor(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    curve_index: Integer = None,
                    factor: Float = None,
                    use_all_curves = False):
        """ > Node <&Node Sample Curve>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Curves      | `self`            |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `mode`      | `'FACTOR'`        |

        Parameters
        ----------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        curve_index : Integer, optional
            socket 'Curve Index' (id: Curve Index)
        
        factor : Float, optional
            socket 'Factor' (id: Factor)
        
        use_all_curves : bool
            parameter `use_all_curves`
        

        Returns
        -------
        Float
            peer sockets: position_ (Vector), tangent_ (Vector), normal_ (Vector)

        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeSampleCurve')
        node = Node('Sample Curve', {'Curves': self, 'Value': value, 'Curve Index': curve_index, 'Factor': factor}, data_type=data_type, mode='FACTOR', use_all_curves=use_all_curves)
        return node._out

    def sample_length(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    length: Float = None,
                    curve_index: Integer = None,
                    use_all_curves = False):
        """ > Node <&Node Sample Curve>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Curves      | `self`            |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `mode`      | `'LENGTH'`        |

        Parameters
        ----------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        length : Float, optional
            socket 'Length' (id: Length)
        
        curve_index : Integer, optional
            socket 'Curve Index' (id: Curve Index)
        
        use_all_curves : bool
            parameter `use_all_curves`
        

        Returns
        -------
        Float
            peer sockets: position_ (Vector), tangent_ (Vector), normal_ (Vector)

        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeSampleCurve')
        node = Node('Sample Curve', {'Curves': self, 'Value': value, 'Length': length, 'Curve Index': curve_index}, data_type=data_type, mode='LENGTH', use_all_curves=use_all_curves)
        return node._out

    def sample(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    curve_index: Integer = None,
                    factor: Float = None,
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR',
                    use_all_curves = False):
        """ > Node <&Node Sample Curve>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Curves      | `self`            |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ----------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        curve_index : Integer, optional
            socket 'Curve Index' (id: Curve Index)
        
        factor : Float, optional
            socket 'Factor' (id: Factor)
        
        mode : Literal['Factor', 'Length']
            parameter `mode`
        
        use_all_curves : bool
            parameter `use_all_curves`
        

        Returns
        -------
        Float
            peer sockets: position_ (Vector), tangent_ (Vector), normal_ (Vector)

        """
        utils.check_enum_arg('Sample Curve', 'mode', mode, 'sample', ('FACTOR', 'LENGTH'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeSampleCurve')
        node = Node('Sample Curve', {'Curves': self, 'Value': value, 'Curve Index': curve_index, 'Factor': factor}, data_type=data_type, mode=mode, use_all_curves=use_all_curves)
        return node._out

    def set_handle_positions(self,
                    position: Vector = None,
                    offset: Vector = None,
                    mode: Literal['LEFT', 'RIGHT'] = 'LEFT'):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        
        mode : Literal['Left', 'Right']
            parameter `mode`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Handle Positions', 'mode', mode, 'set_handle_positions', ('LEFT', 'RIGHT'))
        node = Node('Set Handle Positions', {'Curve': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': offset}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def set_left_handle_positions(self, position: Vector = None, offset: Vector = None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'LEFT'`          |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Handle Positions', {'Curve': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': offset}, mode='LEFT')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_right_handle_positions(self, position: Vector = None, offset: Vector = None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'RIGHT'`         |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Handle Positions', {'Curve': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': offset}, mode='RIGHT')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_normal(self,
                    mode: Literal['Minimum Twist', 'Z Up', 'Free'] = None,
                    normal: Vector = None):
        """ > Node <&Node Set Curve Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        mode : menu='Minimum Twist', optional
            ('Minimum Twist', 'Z Up', 'Free')
        
        normal : Vector, optional
            socket 'Normal' (id: Normal)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Curve Normal', {'Curve': self, 'Selection': self.get_selection(), 'Mode': mode, 'Normal': normal})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_radius(self, radius: Float = None):
        """ > Node <&Node Set Curve Radius>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Curve Radius', {'Curve': self, 'Selection': self.get_selection(), 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_tilt(self, tilt: Float = None):
        """ > Node <&Node Set Curve Tilt>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        tilt : Float, optional
            socket 'Tilt' (id: Tilt)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Curve Tilt', {'Curve': self, 'Selection': self.get_selection(), 'Tilt': tilt})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_spline_cyclic(self, cyclic: Boolean = None):
        """ > Node <&Node Set Spline Cyclic>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        cyclic : Boolean, optional
            socket 'Cyclic' (id: Cyclic)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Spline Cyclic', {'Geometry': self, 'Selection': self.get_selection(), 'Cyclic': cyclic})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_spline_resolution(self, resolution: Integer = None):
        """ > Node <&Node Set Spline Resolution>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Spline Resolution', {'Geometry': self, 'Selection': self.get_selection(), 'Resolution': resolution})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def spline_length(cls):
        """ > Node <&Node Spline Length>

        Returns
        -------
        Float
            peer sockets: point_count_ (Integer)

        """
        node = Node('Spline Length', )
        return node._out

    @classmethod
    def spline_parameter(cls):
        """ > Node <&Node Spline Parameter>

        Returns
        -------
        Float
            peer sockets: length_ (Float), index_ (Integer)

        """
        node = Node('Spline Parameter', )
        return node._out

    def subdivide(self, cuts: Integer = None):
        """ > Node <&Node Subdivide Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name  | Value  |
        | ------ | ----- | ------ |
        | Socket | Curve | `self` |

        Parameters
        ----------
        cuts : Integer, optional
            socket 'Cuts' (id: Cuts)
        

        Returns
        -------
        Curve
        """
        node = Node('Subdivide Curve', {'Curve': self, 'Cuts': cuts})
        self._jump(node._out)
        return self._domain_to_geometry

    def trim_factor(self, start: Float = None, end: Float = None):
        """ > Node <&Node Trim Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'FACTOR'`        |

        Parameters
        ----------
        start : Float, optional
            socket 'Start' (id: Start)
        
        end : Float, optional
            socket 'End' (id: End)
        

        Returns
        -------
        Curve
        """
        node = Node('Trim Curve', {'Curve': self, 'Selection': self.get_selection(), 'Start': start, 'End': end}, mode='FACTOR')
        self._jump(node._out)
        return self._domain_to_geometry

    def trim_length(self, start: Float = None, end: Float = None):
        """ > Node <&Node Trim Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'LENGTH'`        |

        Parameters
        ----------
        start : Float, optional
            socket 'Start' (id: Start_001)
        
        end : Float, optional
            socket 'End' (id: End_001)
        

        Returns
        -------
        Curve
        """
        node = Node('Trim Curve', {'Curve': self, 'Selection': self.get_selection(), 'Start_001': start, 'End_001': end}, mode='LENGTH')
        self._jump(node._out)
        return self._domain_to_geometry

    def trim(self,
                    start: Float = None,
                    end: Float = None,
                    mode: Literal['FACTOR', 'LENGTH'] = 'FACTOR'):
        """ > Node <&Node Trim Curve>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        start : Float, optional
            socket 'Start' (id: Start)
        
        end : Float, optional
            socket 'End' (id: End)
        
        mode : Literal['Factor', 'Length']
            parameter `mode`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Trim Curve', 'mode', mode, 'trim', ('FACTOR', 'LENGTH'))
        node = Node('Trim Curve', {'Curve': self, 'Selection': self.get_selection(), 'Start': start, 'End': end}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def radius(self):
        """ Property get node <Node Set Curve Radius>
        """
        return Node('Radius', {})._out

    @radius.setter
    def radius(self, radius: Float = None):
        """ > Node <&Node Set Curve Radius>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Curve Radius', {'Curve': self, 'Selection': self.get_selection(), 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def left_handle_position(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', {'Relative': False}).left

    @left_handle_position.setter
    def left_handle_position(self, position: Vector = None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Socket    | Offset    | ignored           |
        | Parameter | `mode`    | `'LEFT'`          |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Handle Positions', {'Curve': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': None}, mode='LEFT')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def right_handle_position(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', {'Relative': False}).right

    @right_handle_position.setter
    def right_handle_position(self, position: Vector = None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Socket    | Offset    | ignored           |
        | Parameter | `mode`    | `'RIGHT'`         |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Handle Positions', {'Curve': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': None}, mode='RIGHT')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def left_handle_offset(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', {'Relative': True}).left

    @left_handle_offset.setter
    def left_handle_offset(self, offset: Vector = None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Socket    | Position  | ignored           |
        | Parameter | `mode`    | `'LEFT'`          |

        Parameters
        ----------
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Handle Positions', {'Curve': self, 'Selection': self.get_selection(), 'Position': None, 'Offset': offset}, mode='LEFT')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def right_handle_offset(self):
        """ Property get node <Node Set Handle Positions>
        """
        return Node('Curve Handle Positions', {'Relative': True}).right

    @right_handle_offset.setter
    def right_handle_offset(self, offset: Vector = None):
        """ > Node <&Node Set Handle Positions>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Socket    | Position  | ignored           |
        | Parameter | `mode`    | `'RIGHT'`         |

        Parameters
        ----------
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Handle Positions', {'Curve': self, 'Selection': self.get_selection(), 'Position': None, 'Offset': offset}, mode='RIGHT')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def handle_type(self):
        """ Write only property for node <Node Set Handle Type>
        """
        raise NodeError('Property Curve.handle_type is write only.')

    @handle_type.setter
    def handle_type(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value               |
        | --------- | --------- | ------------------- |
        | Socket    | Curve     | `self`              |
        | Socket    | Selection | `self[selection]`   |
        | Parameter | `mode`    | `{'RIGHT', 'LEFT'}` |

        Parameters
        ----------
        handle_type : Literal['Free', 'Auto', 'Vector', 'Align']
            parameter `handle_type`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', {'Curve': self, 'Selection': self.get_selection()}, handle_type=handle_type, mode={'RIGHT', 'LEFT'})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def left_handle_type(self):
        """ Write only property for node <Node Set Handle Type>
        """
        raise NodeError('Property Curve.left_handle_type is write only.')

    @left_handle_type.setter
    def left_handle_type(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `{'LEFT'}`        |

        Parameters
        ----------
        handle_type : Literal['Free', 'Auto', 'Vector', 'Align']
            parameter `handle_type`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'left_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', {'Curve': self, 'Selection': self.get_selection()}, handle_type=handle_type, mode={'LEFT'})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def right_handle_type(self):
        """ Write only property for node <Node Set Handle Type>
        """
        raise NodeError('Property Curve.right_handle_type is write only.')

    @right_handle_type.setter
    def right_handle_type(self, handle_type: Literal['FREE', 'AUTO', 'VECTOR', 'ALIGN'] = 'AUTO'):
        """ > Node <&Node Set Handle Type>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Curve     | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `{'RIGHT'}`       |

        Parameters
        ----------
        handle_type : Literal['Free', 'Auto', 'Vector', 'Align']
            parameter `handle_type`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Handle Type', 'handle_type', handle_type, 'right_handle_type', ('FREE', 'AUTO', 'VECTOR', 'ALIGN'))
        node = Node('Set Handle Type', {'Curve': self, 'Selection': self.get_selection()}, handle_type=handle_type, mode={'RIGHT'})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def tilt(self):
        """ Property get node <Node Set Curve Tilt>
        """
        return Node('Curve Tilt', {})._out

    @tilt.setter
    def tilt(self, tilt: Float = None):
        """ > Node <&Node Set Curve Tilt>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        tilt : Float, optional
            socket 'Tilt' (id: Tilt)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Curve Tilt', {'Curve': self, 'Selection': self.get_selection(), 'Tilt': tilt})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def normal(self):
        """ Write only property for node <Node Set Curve Normal>
        """
        raise NodeError('Property Curve.normal is write only.')

    @normal.setter
    def normal(self, mode: Literal['Minimum Twist', 'Z Up', 'Free'] = None):
        """ > Node <&Node Set Curve Normal>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |
        | Socket | Normal    | ignored           |

        Parameters
        ----------
        mode : menu='Minimum Twist', optional
            ('Minimum Twist', 'Z Up', 'Free')
        

        Returns
        -------
        Curve
        """
        node = Node('Set Curve Normal', {'Curve': self, 'Selection': self.get_selection(), 'Mode': mode, 'Normal': None})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def is_cyclic(self):
        """ Property get node <Node Set Spline Cyclic>
        """
        return Node('Is Spline Cyclic', {})._out

    @is_cyclic.setter
    def is_cyclic(self, cyclic: Boolean = None):
        """ > Node <&Node Set Spline Cyclic>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        cyclic : Boolean, optional
            socket 'Cyclic' (id: Cyclic)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Spline Cyclic', {'Geometry': self, 'Selection': self.get_selection(), 'Cyclic': cyclic})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def resolution(self):
        """ Property get node <Node Set Spline Resolution>
        """
        return Node('Spline Resolution', {})._out

    @resolution.setter
    def resolution(self, resolution: Integer = None):
        """ > Node <&Node Set Spline Resolution>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        resolution : Integer, optional
            socket 'Resolution' (id: Resolution)
        

        Returns
        -------
        Curve
        """
        node = Node('Set Spline Resolution', {'Geometry': self, 'Selection': self.get_selection(), 'Resolution': resolution})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def type(self):
        """ Write only property for node <Node Set Spline Type>
        """
        raise NodeError('Property Curve.type is write only.')

    @type.setter
    def type(self, spline_type: Literal['CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'] = 'POLY'):
        """ > Node <&Node Set Spline Type>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Curve     | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        spline_type : Literal['Catmull Rom', 'Poly', 'Bézier', 'NURBS']
            parameter `spline_type`
        

        Returns
        -------
        Curve
        """
        utils.check_enum_arg('Set Spline Type', 'spline_type', spline_type, 'type', ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS'))
        node = Node('Set Spline Type', {'Curve': self, 'Selection': self.get_selection()}, spline_type=spline_type)
        self._jump(node._out)
        return self._domain_to_geometry

