from .. socket_class import Socket
from .. treeclass import Node
from .. treeclass import utils
from .. scripterror import NodeError

class Vertex(Socket):

    @classmethod
    @property
    def corners(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Property Get <&Node Corners of Vertex>

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
    @property
    def corner_index(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Property Get <&Node Corners of Vertex>

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
    @property
    def corners_total(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Property Get <&Node Corners of Vertex>

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
    @property
    def edges(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Property Get <&Node Edges of Vertex>

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
    @property
    def edge_index(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Property Get <&Node Edges of Vertex>

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
    @property
    def edges_total(cls, vertex_index=None, weights=None, sort_index=None):
        """ > Property Get <&Node Edges of Vertex>

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

