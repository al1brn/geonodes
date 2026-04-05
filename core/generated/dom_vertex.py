# Generated 2026-04-05 13:26:22

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


class Vertex:
    """"
    $DOC SET hidden
    """
    @classmethod
    def corners(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Vertex>

        Parameters
        ----------
        vertex_index : Integer, optional
            socket 'Vertex Index' (id: Vertex Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        Integer
            peer sockets: total_ (Integer)

        """
        node = Node('Corners of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corner_index(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Vertex>

        Parameters
        ----------
        vertex_index : Integer, optional
            socket 'Vertex Index' (id: Vertex Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        corner_index
        """
        node = Node('Corners of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.corner_index

    @classmethod
    def corners_total(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Vertex>

        Parameters
        ----------
        vertex_index : Integer, optional
            socket 'Vertex Index' (id: Vertex Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        total
        """
        node = Node('Corners of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.total

    @classmethod
    def edges(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Edges of Vertex>

        Parameters
        ----------
        vertex_index : Integer, optional
            socket 'Vertex Index' (id: Vertex Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        Integer
            peer sockets: total_ (Integer)

        """
        node = Node('Edges of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def edge_index(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Edges of Vertex>

        Parameters
        ----------
        vertex_index : Integer, optional
            socket 'Vertex Index' (id: Vertex Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        edge_index
        """
        node = Node('Edges of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.edge_index

    @classmethod
    def edges_total(cls,
                    vertex_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Edges of Vertex>

        Parameters
        ----------
        vertex_index : Integer, optional
            socket 'Vertex Index' (id: Vertex Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        total
        """
        node = Node('Edges of Vertex', {'Vertex Index': vertex_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.total

    def extrude(self, offset: Vector = None, offset_scale: Float = None):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'VERTICES'`      |

        Parameters
        ----------
        offset : Vector, optional
            socket 'Offset' (id: Offset)
        
        offset_scale : Float, optional
            socket 'Offset Scale' (id: Offset Scale)
        

        Returns
        -------
        Mesh
            peer sockets: top_ (Boolean), side_ (Boolean)

        """
        node = Node('Extrude Mesh', {'Mesh': self, 'Selection': self.get_selection(), 'Offset': offset, 'Offset Scale': offset_scale}, mode='VERTICES')
        self._jump(node._out)
        return self._domain_to_geometry

    @utils.classproperty
    def neighbors(cls):
        """ > Node <&Node Vertex Neighbors>

        Returns
        -------
        Integer
            peer sockets: face_count_ (Integer)

        """
        node = Node('Vertex Neighbors', )
        return node._out

    @utils.classproperty
    def neighbors_vertex_count(cls):
        """ > Node <&Node Vertex Neighbors>

        Returns
        -------
        vertex_count
        """
        node = Node('Vertex Neighbors', )
        return node.vertex_count

    @utils.classproperty
    def neighbors_face_count(cls):
        """ > Node <&Node Vertex Neighbors>

        Returns
        -------
        face_count
        """
        node = Node('Vertex Neighbors', )
        return node.face_count

    def to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Mesh to Points>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'VERTICES'`      |

        Parameters
        ----------
        position : Vector, optional
            socket 'Position' (id: Position)
        
        radius : Float, optional
            socket 'Radius' (id: Radius)
        

        Returns
        -------
        Cloud
        """
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode='VERTICES')
        return node._out

