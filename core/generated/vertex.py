from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Vertex(Socket):

    @classmethod
    def corners(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Class Method <&Node Corners of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - node [corner_index (Integer), total (Integer)]
        """
        node = Node('Corners of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node

    @classmethod
    def corner_index(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Class Method <&Node Corners of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - corner_index
        """
        node = Node('Corners of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.corner_index

    @classmethod
    def corners_total(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Class Method <&Node Corners of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - total
        """
        node = Node('Corners of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.total

    @classmethod
    def edges(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Class Method <&Node Edges of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - node [edge_index (Integer), total (Integer)]
        """
        node = Node('Edges of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node

    @classmethod
    def edge_index(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Class Method <&Node Edges of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - edge_index
        """
        node = Node('Edges of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.edge_index

    @classmethod
    def edges_total(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Class Method <&Node Edges of Vertex>

        Arguments
        ---------
        - vertex_index (Integer) : socket 'Vertex Index' (id: Vertex Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - total
        """
        node = Node('Edges of Vertex', sockets={'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.total

    @classmethod
    @property
    def neighbors(cls):
        """ > Property Get <&Node Vertex Neighbors>

        Returns
        -------
        - node [vertex_count (Integer), face_count (Integer)]
        """
        node = Node('Vertex Neighbors', sockets={})
        return node

    @classmethod
    @property
    def neighbors_vertex_count(cls):
        """ > Property Get <&Node Vertex Neighbors>

        Returns
        -------
        - vertex_count
        """
        node = Node('Vertex Neighbors', sockets={})
        return node.vertex_count

    @classmethod
    @property
    def neighbors_face_count(cls):
        """ > Property Get <&Node Vertex Neighbors>

        Returns
        -------
        - face_count
        """
        node = Node('Vertex Neighbors', sockets={})
        return node.face_count

    def to_points(self, position=None, radius=None):
        """ > Method <&Node Mesh to Points>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'VERTICES'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Mesh to Points', sockets={'Mesh': self, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode='VERTICES')
        return node._out
