from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class SplinePoint(Socket):

    @classmethod
    @property
    def curve_of_point(cls, point_index=None):
        """ > Property Get <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)

        Returns
        -------
        - node [curve_index (Integer), index_in_curve (Integer)]
        """
        node = Node('Curve of Point', sockets={'Point Index': point_index})
        return node

    @classmethod
    @property
    def curve_index(cls, point_index=None):
        """ > Property Get <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)

        Returns
        -------
        - curve_index
        """
        node = Node('Curve of Point', sockets={'Point Index': point_index})
        return node.curve_index

    @classmethod
    @property
    def index_in_curve(cls, point_index=None):
        """ > Property Get <&Node Curve of Point>

        Arguments
        ---------
        - point_index (Integer) : socket 'Point Index' (id: Point Index)

        Returns
        -------
        - index_in_curve
        """
        node = Node('Curve of Point', sockets={'Point Index': point_index})
        return node.index_in_curve

    @classmethod
    def offset_in_curve(cls, point_index=None, offset=None):
        """ > Class Method <&Node Offset Point in Curve>

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

