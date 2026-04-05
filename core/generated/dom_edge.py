# Generated 2026-04-05 14:24:03

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


class Edge:
    """"
    $DOC SET hidden
    """
    @classmethod
    def accumulate_field(cls, value: Float | Integer | Vector | Matrix = None, group_id: Integer = None):
        """ > Node <&Node Accumulate Field>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'EDGE'`          |

        Parameters
        ----------
        value : Float | Integer | Vector | Matrix, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        

        Returns
        -------
        Float
            peer sockets: trailing_ (Float), total_ (Float)

        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeAccumulateField')
        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain='EDGE')
        return node._out

    def attribute_statistic(self, attribute: Float | Vector = None):
        """ > Node <&Node Attribute Statistic>

        **Fixed values**

        | Kind      | Name        | Value                 |
        | --------- | ----------- | --------------------- |
        | Socket    | Geometry    | `self`                |
        | Socket    | Selection   | `self[selection]`     |
        | Parameter | `data_type` | from `attribute` type |
        | Parameter | `domain`    | `'EDGE'`              |

        Parameters
        ----------
        attribute : Float | Vector, optional
            socket 'Attribute' (id: Attribute)
        

        Returns
        -------
        Float
            peer sockets: median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)

        """
        data_type = SocketType.get_data_type_for_node(attribute, 'GeometryNodeAttributeStatistic')
        node = Node('Attribute Statistic', {'Geometry': self, 'Selection': self.get_selection(), 'Attribute': attribute}, data_type=data_type, domain='EDGE')
        return node._out

    @classmethod
    def field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Average>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ----------
        value : Float | Vector, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        
        domain : Literal['Point', 'Edge', 'Face', 'Face Corner', 'Spline', 'Instance', 'Layer']
            parameter `domain`
        

        Returns
        -------
        Float
            peer sockets: median_ (Float)

        """
        utils.check_enum_arg('Field Average', 'domain', domain, 'field_average', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldAverage')
        node = Node('Field Average', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Min & Max>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ----------
        value : Float | Integer | Vector, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        
        domain : Literal['Point', 'Edge', 'Face', 'Face Corner', 'Spline', 'Instance', 'Layer']
            parameter `domain`
        

        Returns
        -------
        Float
            peer sockets: max_ (Float)

        """
        utils.check_enum_arg('Field Min & Max', 'domain', domain, 'field_min_max', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldMinAndMax')
        node = Node('Field Min & Max', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Variance>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |

        Parameters
        ----------
        value : Float | Vector, optional
            socket 'Value' (id: Value)
        
        group_id : Integer, optional
            socket 'Group ID' (id: Group Index)
        
        domain : Literal['Point', 'Edge', 'Face', 'Face Corner', 'Spline', 'Instance', 'Layer']
            parameter `domain`
        

        Returns
        -------
        Float
            peer sockets: variance_ (Float)

        """
        utils.check_enum_arg('Field Variance', 'domain', domain, 'field_variance', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldVariance')
        node = Node('Field Variance', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def corners(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Edge>

        Parameters
        ----------
        edge_index : Integer, optional
            socket 'Edge Index' (id: Edge Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        Integer
            peer sockets: total_ (Integer)

        """
        node = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corner_index(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Edge>

        Parameters
        ----------
        edge_index : Integer, optional
            socket 'Edge Index' (id: Edge Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        corner_index
        """
        node = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.corner_index

    @classmethod
    def corners_total(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Edge>

        Parameters
        ----------
        edge_index : Integer, optional
            socket 'Edge Index' (id: Edge Index)
        
        weights : Float, optional
            socket 'Weights' (id: Weights)
        
        sort_index : Integer, optional
            socket 'Sort Index' (id: Sort Index)
        

        Returns
        -------
        total
        """
        node = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.total

    def delete_geometry_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |
        | Parameter | `mode`    | `'ALL'`           |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |
        | Parameter | `mode`    | `'EDGE_FACE'`     |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |
        | Parameter | `mode`    | `'ONLY_FACE'`     |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Parameters
        ----------
        mode : Literal['All', 'Only Edges & Faces', 'Only Faces']
            parameter `mode`
        

        Returns
        -------
        Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete_geometry', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |
        | Parameter | `mode`    | `'ALL'`           |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |
        | Parameter | `mode`    | `'EDGE_FACE'`     |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |
        | Parameter | `mode`    | `'ONLY_FACE'`     |

        Returns
        -------
        Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Parameters
        ----------
        mode : Literal['All', 'Only Edges & Faces', 'Only Faces']
            parameter `mode`
        

        Returns
        -------
        Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def duplicate(self, amount: Integer = None):
        """ > Node <&Node Duplicate Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Parameters
        ----------
        amount : Integer, optional
            socket 'Amount' (id: Amount)
        

        Returns
        -------
        Geometry
            peer sockets: duplicate_index_ (Integer)

        """
        node = Node('Duplicate Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Amount': amount}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def paths_to_curves(self, start_vertices: Boolean = None, next_vertex_index: Integer = None):
        """ > Node <&Node Edge Paths to Curves>

        **Fixed values**

        | Kind   | Name | Value  |
        | ------ | ---- | ------ |
        | Socket | Mesh | `self` |

        Parameters
        ----------
        start_vertices : Boolean, optional
            socket 'Start Vertices' (id: Start Vertices)
        
        next_vertex_index : Integer, optional
            socket 'Next Vertex Index' (id: Next Vertex Index)
        

        Returns
        -------
        Curve
        """
        node = Node('Edge Paths to Curves', {'Mesh': self, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def paths_to_selection(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None):
        """ > Node <&Node Edge Paths to Selection>

        Parameters
        ----------
        start_vertices : Boolean, optional
            socket 'Start Vertices' (id: Start Vertices)
        
        next_vertex_index : Integer, optional
            socket 'Next Vertex Index' (id: Next Vertex Index)
        

        Returns
        -------
        Boolean
        """
        node = Node('Edge Paths to Selection', {'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def to_face_groups(cls, boundary_edges: Boolean = None):
        """ > Node <&Node Edges to Face Groups>

        Parameters
        ----------
        boundary_edges : Boolean, optional
            socket 'Boundary Edges' (id: Boundary Edges)
        

        Returns
        -------
        Integer
        """
        node = Node('Edges to Face Groups', {'Boundary Edges': boundary_edges})
        return node._out

    def extrude(self, offset: Vector = None, offset_scale: Float = None):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'EDGES'`         |

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
        node = Node('Extrude Mesh', {'Mesh': self, 'Selection': self.get_selection(), 'Offset': offset, 'Offset Scale': offset_scale}, mode='EDGES')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None):
        """ > Node <&Node Evaluate at Index>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'EDGE'`          |

        Parameters
        ----------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        index : Integer, optional
            socket 'Index' (id: Index)
        

        Returns
        -------
        Float
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldAtIndex')
        node = Node('Evaluate at Index', {'Value': value, 'Index': index}, data_type=data_type, domain='EDGE')
        return node._out

    @classmethod
    def evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None):
        """ > Node <&Node Evaluate on Domain>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'EDGE'`          |

        Parameters
        ----------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Float
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeFieldOnDomain')
        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain='EDGE')
        return node._out

    @utils.classproperty
    def edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        Float
            peer sockets: signed_angle_ (Float)

        """
        node = Node('Edge Angle', )
        return node._out

    @utils.classproperty
    def unsigned_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        unsigned_angle
        """
        node = Node('Edge Angle', )
        return node.unsigned_angle

    @utils.classproperty
    def signed_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        signed_angle
        """
        node = Node('Edge Angle', )
        return node.signed_angle

    @utils.classproperty
    def face_count(cls):
        """ > Node <&Node Edge Neighbors>

        Returns
        -------
        Integer
        """
        node = Node('Edge Neighbors', )
        return node._out

    @utils.classproperty
    def edge_vertices(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        Integer
            peer sockets: vertex_index_2_ (Integer), position_1_ (Vector), position_2_ (Vector)

        """
        node = Node('Edge Vertices', )
        return node._out

    @utils.classproperty
    def vertex_index_1(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        vertex_index_1
        """
        node = Node('Edge Vertices', )
        return node.vertex_index_1

    @utils.classproperty
    def vertex_index_2(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        vertex_index_2
        """
        node = Node('Edge Vertices', )
        return node.vertex_index_2

    @utils.classproperty
    def position_1(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        position_1
        """
        node = Node('Edge Vertices', )
        return node.position_1

    @utils.classproperty
    def position_2(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        position_2
        """
        node = Node('Edge Vertices', )
        return node.position_2

    @classmethod
    def shortest_paths(cls, end_vertex: Boolean = None, edge_cost: Float = None):
        """ > Node <&Node Shortest Edge Paths>

        Parameters
        ----------
        end_vertex : Boolean, optional
            socket 'End Vertex' (id: End Vertex)
        
        edge_cost : Float, optional
            socket 'Edge Cost' (id: Edge Cost)
        

        Returns
        -------
        Integer
            peer sockets: total_cost_ (Float)

        """
        node = Node('Shortest Edge Paths', {'End Vertex': end_vertex, 'Edge Cost': edge_cost})
        return node._out

    def to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Mesh to Points>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `mode`    | `'EDGES'`         |

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
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode='EDGES')
        return node._out

    def sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False):
        """ > Node <&Node Sample Index>

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'EDGE'`          |

        Parameters
        ----------
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix, optional
            socket 'Value' (id: Value)
        
        index : Integer, optional
            socket 'Index' (id: Index)
        
        clamp : bool
            parameter `clamp`
        

        Returns
        -------
        Float
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeSampleIndex')
        node = Node('Sample Index', {'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='EDGE')
        return node._out

    def sample_nearest(self, sample_position: Vector = None):
        """ > Node <&Node Sample Nearest>

        **Fixed values**

        | Kind      | Name     | Value    |
        | --------- | -------- | -------- |
        | Socket    | Geometry | `self`   |
        | Parameter | `domain` | `'EDGE'` |

        Parameters
        ----------
        sample_position : Vector, optional
            socket 'Sample Position' (id: Sample Position)
        

        Returns
        -------
        Integer
        """
        node = Node('Sample Nearest', {'Geometry': self, 'Sample Position': sample_position}, domain='EDGE')
        return node._out

    def scale(self,
                    scale: Float = None,
                    center: Vector = None,
                    scale_mode: Literal['Uniform', 'Single Axis'] = None,
                    axis: Vector = None):
        """ > Node <&Node Scale Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Parameters
        ----------
        scale : Float, optional
            socket 'Scale' (id: Scale)
        
        center : Vector, optional
            socket 'Center' (id: Center)
        
        scale_mode : menu='Uniform', optional
            ('Uniform', 'Single Axis')
        
        axis : Vector, optional
            socket 'Axis' (id: Axis)
        

        Returns
        -------
        Geometry
        """
        node = Node('Scale Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Scale': scale, 'Center': center, 'Scale Mode': scale_mode, 'Axis': axis}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def separate(self):
        """ > Node <&Node Separate Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Returns
        -------
        node [selection (Geometry), inverted (Geometry)]
        """
        node = Node('Separate Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE')
        self._jump(node._out)
        return node

    def set_shade_smooth(self, shade_smooth: Boolean = None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Parameters
        ----------
        shade_smooth : Boolean, optional
            socket 'Shade Smooth' (id: Shade Smooth)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Shade Smooth', {'Geometry': self, 'Selection': self.get_selection(), 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def sort(self, group_id: Integer = None, sort_weight: Float = None):
        """ > Node <&Node Sort Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Parameters
        ----------
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        
        sort_weight : Float, optional
            socket 'Sort Weight' (id: Sort Weight)
        

        Returns
        -------
        Geometry
        """
        node = Node('Sort Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id, 'Sort Weight': sort_weight}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def split(self):
        """ > Node <&Node Split Edges>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Mesh      | `self`            |
        | Socket | Selection | `self[selection]` |

        Returns
        -------
        Mesh
        """
        node = Node('Split Edges', {'Mesh': self, 'Selection': self.get_selection()})
        self._jump(node._out)
        return self._domain_to_geometry

    def split_to_instances(self, group_id: Integer = None):
        """ > Node <&Node Split to Instances>

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Geometry  | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Parameters
        ----------
        group_id : Integer, optional
            socket 'Group ID' (id: Group ID)
        

        Returns
        -------
        Instances
            peer sockets: group_id_ (Integer)

        """
        node = Node('Split to Instances', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id}, domain='EDGE')
        return node._out

    def store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Socket    | Selection   | `self[selection]` |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'EDGE'`          |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Geometry
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeStoreNamedAttribute')
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name        | Value             |
        | --------- | ----------- | ----------------- |
        | Socket    | Geometry    | `self`            |
        | Socket    | Selection   | `self[selection]` |
        | Parameter | `data_type` | from `value` type |
        | Parameter | `domain`    | `'EDGE'`          |

        Parameters
        ----------
        name : String, optional
            socket 'Name' (id: Name)
        
        value : Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color, optional
            socket 'Value' (id: Value)
        

        Returns
        -------
        Geometry
        """
        data_type = SocketType.get_data_type_for_node(value, 'GeometryNodeStoreNamedAttribute')
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def active_element(cls):
        """ > Node <&Node Active Element>

        **Fixed values**

        | Kind      | Name     | Value    |
        | --------- | -------- | -------- |
        | Parameter | `domain` | `'EDGE'` |

        Returns
        -------
        Integer
            peer sockets: exists_ (Boolean)

        """
        node = Node('Active Element', domain='EDGE')
        return node._out

    def set_selection(self):
        """ > Node <&Node Set Selection>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name             | Value                 |
        | --------- | ---------------- | --------------------- |
        | Socket    | Geometry         | `self`                |
        | Socket    | Selection        | `self[selection]`     |
        | Parameter | `domain`         | `'EDGE'`              |
        | Parameter | `selection_type` | from `selection` type |

        Returns
        -------
        Geometry
        """
        selection_type = SocketType.get_data_type_for_node(selection, 'GeometryNodeToolSetSelection')
        node = Node('Set Selection', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', selection_type=selection_type)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        **Fixed values**

        | Kind      | Name     | Value    |
        | --------- | -------- | -------- |
        | Parameter | `domain` | `'EDGE'` |

        Parameters
        ----------
        named_sockets : dict, default={}
            Sockets created with string names
        
        ui_shortcut : int
            parameter `ui_shortcut`
        
        sockets : dict, default={}
            Socket created with python name attributes

        """
        node = Node('Viewer', named_sockets, domain='EDGE', ui_shortcut=ui_shortcut, **sockets)
        return

    @property
    def material(self):
        """ Write only property for node <Node Set Material>
        """
        raise NodeError('Property Edge.material is write only.')

    @material.setter
    def material(self, material: Material = None):
        """ > Node <&Node Set Material>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind   | Name      | Value             |
        | ------ | --------- | ----------------- |
        | Socket | Geometry  | `self`            |
        | Socket | Selection | `self[selection]` |

        Parameters
        ----------
        material : Material, optional
            socket 'Material' (id: Material)
        

        Returns
        -------
        Geometry
        """
        node = Node('Set Material', {'Geometry': self, 'Selection': self.get_selection(), 'Material': material})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def shade_smooth(self):
        """ Property get node <Node Set Shade Smooth>
        """
        return Node('Is Edge Smooth', {})._out

    @shade_smooth.setter
    def shade_smooth(self, shade_smooth: Boolean = None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Parameters
        ----------
        shade_smooth : Boolean, optional
            socket 'Shade Smooth' (id: Shade Smooth)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Shade Smooth', {'Geometry': self, 'Selection': self.get_selection(), 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def smooth(self):
        """ Property get node <Node Set Shade Smooth>
        """
        return Node('Is Edge Smooth', {})._out

    @smooth.setter
    def smooth(self, shade_smooth: Boolean = None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        **Fixed values**

        | Kind      | Name      | Value             |
        | --------- | --------- | ----------------- |
        | Socket    | Mesh      | `self`            |
        | Socket    | Selection | `self[selection]` |
        | Parameter | `domain`  | `'EDGE'`          |

        Parameters
        ----------
        shade_smooth : Boolean, optional
            socket 'Shade Smooth' (id: Shade Smooth)
        

        Returns
        -------
        Mesh
        """
        node = Node('Set Shade Smooth', {'Geometry': self, 'Selection': self.get_selection(), 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

