# Generated 2025-12-04 08:23:30

from __future__ import annotations
from .. socket_class import Socket
from .. nodeclass import Node, ColorRamp, NodeCurves, MenuNode, IndexSwitchNode
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
    class GrasePencil: ...
    class Boolean: ...
    class Integer: ...
    class Float: ...
    class Vector: ...
    class Color: ...
    class Matrix: ...
    class Rotation: ...
    class String: ...


class SplinePoint(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def curve_of_point(cls, point_index: Integer = None):
        """ > Node <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)

        Returns
        -------
        - node [curve_index (Integer), index_in_curve (Integer)]
        """
        node = Node('Curve of Point', {'Point Index': point_index})
        return node

    @classmethod
    def curve_index(cls, point_index: Integer = None):
        """ > Node <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)

        Returns
        -------
        - curve_index
        """
        node = Node('Curve of Point', {'Point Index': point_index})
        return node.curve_index

    @classmethod
    def index_in_curve(cls, point_index: Integer = None):
        """ > Node <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)

        Returns
        -------
        - index_in_curve
        """
        node = Node('Curve of Point', {'Point Index': point_index})
        return node.index_in_curve

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
        node = Node('Curve to Points', {'Curve': self}, mode='EVALUATED')
        return node._out

    def to_points_count(self, count: Integer = None):
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
        node = Node('Curve to Points', {'Curve': self, 'Count': count}, mode='COUNT')
        return node._out

    def to_points_length(self, length: Float = None):
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
        node = Node('Curve to Points', {'Curve': self, 'Length': length}, mode='LENGTH')
        return node._out

    def to_points(self,
                    count: Integer = None,
                    mode: Literal['EVALUATED', 'COUNT', 'LENGTH'] = 'COUNT'):
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
        node = Node('Curve to Points', {'Curve': self, 'Count': count}, mode=mode)
        return node._out

    @classmethod
    def offset_in_curve(cls, point_index: Integer = None, offset: Integer = None):
        """ > Node <&Node Offset Point in Curve>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)
        - offset (Integer) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Boolean [point_index_ (Integer)]
        """
        node = Node('Offset Point in Curve', {'Point Index': point_index, 'Offset': offset})
        return node._out

    @property
    def radius(self):
        """ Property get node <Node Set Curve Radius>
        """
        return Node('Radius', {})._out

    @radius.setter
    def radius(self, radius: Float = None):
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
        node = Node('Set Curve Radius', {'Curve': self, 'Selection': self._sel, 'Radius': radius})
        self._jump(node._out)
        return self._domain_to_geometry

