# Generated 2026-01-03 16:39:50

from __future__ import annotations
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
    class GrasePencil: ...
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

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float | Integer | Vector | Matrix) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAccumulateField', value)
        node = Node('Accumulate Field', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain='EDGE')
        return node._out

    def attribute_statistic(self, attribute: Float | Vector = None):
        """ > Node <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - attribute (Float | Vector) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - Float [median_ (Float), sum_ (Float), min_ (Float), max_ (Float), range_ (Float), standard_deviation_ (Float), variance_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeAttributeStatistic', attribute)
        node = Node('Attribute Statistic', {'Geometry': self, 'Selection': self.get_selection(), 'Attribute': attribute}, data_type=data_type, domain='EDGE')
        return node._out

    @classmethod
    def field_average(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Average>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float | Vector) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [median_ (Float)]
        """
        utils.check_enum_arg('Field Average', 'domain', domain, 'field_average', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldAverage', value)
        node = Node('Field Average', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_min_max(cls,
                    value: Float | Integer | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Min & Max>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float | Integer | Vector) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [max_ (Float)]
        """
        utils.check_enum_arg('Field Min & Max', 'domain', domain, 'field_min_max', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldMinAndMax', value)
        node = Node('Field Min & Max', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def field_variance(cls,
                    value: Float | Vector = None,
                    group_id: Integer = None,
                    domain: Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'] = 'POINT'):
        """ > Node <&Node Field Variance>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type

        Arguments
        ---------
        - value (Float | Vector) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)
        - domain (str): parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']

        Returns
        -------
        - Float [variance_ (Float)]
        """
        utils.check_enum_arg('Field Variance', 'domain', domain, 'field_variance', ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER'))
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldVariance', value)
        node = Node('Field Variance', {'Value': value, 'Group Index': group_id}, data_type=data_type, domain=domain)
        return node._out

    @classmethod
    def corners(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Edge>

        Arguments
        ---------
        - edge_index (Integer) : socket 'Edge Index' (id: Edge Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - Integer [total_ (Integer)]
        """
        node = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node._out

    @classmethod
    def corner_index(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Edge>

        Arguments
        ---------
        - edge_index (Integer) : socket 'Edge Index' (id: Edge Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - corner_index
        """
        node = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.corner_index

    @classmethod
    def corners_total(cls,
                    edge_index: Integer = None,
                    weights: Float = None,
                    sort_index: Integer = None):
        """ > Node <&Node Corners of Edge>

        Arguments
        ---------
        - edge_index (Integer) : socket 'Edge Index' (id: Edge Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - total
        """
        node = Node('Corners of Edge', {'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.total

    def delete_geometry_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'mode' : 'ALL'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'mode' : 'EDGE_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'mode' : 'ONLY_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete_geometry', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_all(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'mode' : 'ALL'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_edge_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'mode' : 'EDGE_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='EDGE_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_only_face(self):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'mode' : 'ONLY_FACE'

        Returns
        -------
        - Geometry
        """
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete(self, mode: Literal['ALL', 'EDGE_FACE', 'ONLY_FACE'] = 'ALL'):
        """ > Node <&Node Delete Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - mode (str): parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Delete Geometry', 'mode', mode, 'delete', ('ALL', 'EDGE_FACE', 'ONLY_FACE'))
        node = Node('Delete Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def duplicate(self, amount: Integer = None):
        """ > Node <&Node Duplicate Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - amount (Integer) : socket 'Amount' (id: Amount)

        Returns
        -------
        - Geometry [duplicate_index_ (Integer)]
        """
        node = Node('Duplicate Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Amount': amount}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def paths_to_curves(self, start_vertices: Boolean = None, next_vertex_index: Integer = None):
        """ > Node <&Node Edge Paths to Curves>

        Information
        -----------
        - Socket 'Mesh' : self

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Curve
        """
        node = Node('Edge Paths to Curves', {'Mesh': self, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def paths_to_selection(cls, start_vertices: Boolean = None, next_vertex_index: Integer = None):
        """ > Node <&Node Edge Paths to Selection>

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Boolean
        """
        node = Node('Edge Paths to Selection', {'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def to_face_groups(cls, boundary_edges: Boolean = None):
        """ > Node <&Node Edges to Face Groups>

        Arguments
        ---------
        - boundary_edges (Boolean) : socket 'Boundary Edges' (id: Boundary Edges)

        Returns
        -------
        - Integer
        """
        node = Node('Edges to Face Groups', {'Boundary Edges': boundary_edges})
        return node._out

    def extrude(self, offset: Vector = None, offset_scale: Float = None):
        """ > Node <&Node Extrude Mesh>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'EDGES'

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)
        - offset_scale (Float) : socket 'Offset Scale' (id: Offset Scale)

        Returns
        -------
        - Mesh [top_ (Boolean), side_ (Boolean)]
        """
        node = Node('Extrude Mesh', {'Mesh': self, 'Selection': self.get_selection(), 'Offset': offset, 'Offset Scale': offset_scale}, mode='EDGES')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def evaluate_at_index(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None):
        """ > Node <&Node Evaluate at Index>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldAtIndex', value)
        node = Node('Evaluate at Index', {'Value': value, 'Index': index}, data_type=data_type, domain='EDGE')
        return node._out

    @classmethod
    def evaluate_on_domain(cls,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None):
        """ > Node <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeFieldOnDomain', value)
        node = Node('Evaluate on Domain', {'Value': value}, data_type=data_type, domain='EDGE')
        return node._out

    @classmethod
    @property
    def edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - Float [signed_angle_ (Float)]
        """
        node = Node('Edge Angle', )
        return node._out

    @classmethod
    @property
    def unsigned_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - unsigned_angle
        """
        node = Node('Edge Angle', )
        return node.unsigned_angle

    @classmethod
    @property
    def signed_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - signed_angle
        """
        node = Node('Edge Angle', )
        return node.signed_angle

    @classmethod
    @property
    def face_count(cls):
        """ > Node <&Node Edge Neighbors>

        Returns
        -------
        - Integer
        """
        node = Node('Edge Neighbors', )
        return node._out

    @classmethod
    @property
    def edge_vertices(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - Integer [vertex_index_2_ (Integer), position_1_ (Vector), position_2_ (Vector)]
        """
        node = Node('Edge Vertices', )
        return node._out

    @classmethod
    @property
    def vertex_index_1(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - vertex_index_1
        """
        node = Node('Edge Vertices', )
        return node.vertex_index_1

    @classmethod
    @property
    def vertex_index_2(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - vertex_index_2
        """
        node = Node('Edge Vertices', )
        return node.vertex_index_2

    @classmethod
    @property
    def position_1(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - position_1
        """
        node = Node('Edge Vertices', )
        return node.position_1

    @classmethod
    @property
    def position_2(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - position_2
        """
        node = Node('Edge Vertices', )
        return node.position_2

    @classmethod
    def shortest_paths(cls, end_vertex: Boolean = None, edge_cost: Float = None):
        """ > Node <&Node Shortest Edge Paths>

        Arguments
        ---------
        - end_vertex (Boolean) : socket 'End Vertex' (id: End Vertex)
        - edge_cost (Float) : socket 'Edge Cost' (id: Edge Cost)

        Returns
        -------
        - Integer [total_cost_ (Float)]
        """
        node = Node('Shortest Edge Paths', {'End Vertex': end_vertex, 'Edge Cost': edge_cost})
        return node._out

    def to_points(self, position: Vector = None, radius: Float = None):
        """ > Node <&Node Mesh to Points>

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'EDGES'

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - radius (Float) : socket 'Radius' (id: Radius)

        Returns
        -------
        - Cloud
        """
        node = Node('Mesh to Points', {'Mesh': self, 'Selection': self.get_selection(), 'Position': position, 'Radius': radius}, mode='EDGES')
        return node._out

    def sample_index(self,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    index: Integer = None,
                    clamp = False):
        """ > Node <&Node Sample Index>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeSampleIndex', value)
        node = Node('Sample Index', {'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='EDGE')
        return node._out

    def sample_nearest(self, sample_position: Vector = None):
        """ > Node <&Node Sample Nearest>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - sample_position (Vector) : socket 'Sample Position' (id: Sample Position)

        Returns
        -------
        - Integer
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

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)
        - scale_mode (menu='Uniform') : ('Uniform', 'Single Axis')
        - axis (Vector) : socket 'Axis' (id: Axis)

        Returns
        -------
        - Geometry
        """
        node = Node('Scale Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Scale': scale, 'Center': center, 'Scale Mode': scale_mode, 'Axis': axis}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def separate(self):
        """ > Node <&Node Separate Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Returns
        -------
        - node [selection (Geometry), inverted (Geometry)]
        """
        node = Node('Separate Geometry', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE')
        self._jump(node._out)
        return node

    def set_shade_smooth(self, shade_smooth: Boolean = None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)

        Returns
        -------
        - Mesh
        """
        node = Node('Set Shade Smooth', {'Geometry': self, 'Selection': self.get_selection(), 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def sort(self, group_id: Integer = None, sort_weight: Float = None):
        """ > Node <&Node Sort Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sort_weight (Float) : socket 'Sort Weight' (id: Sort Weight)

        Returns
        -------
        - Geometry
        """
        node = Node('Sort Elements', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id, 'Sort Weight': sort_weight}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def split(self):
        """ > Node <&Node Split Edges>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]

        Returns
        -------
        - Mesh
        """
        node = Node('Split Edges', {'Mesh': self, 'Selection': self.get_selection()})
        self._jump(node._out)
        return self._domain_to_geometry

    def split_to_instances(self, group_id: Integer = None):
        """ > Node <&Node Split to Instances>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Instances [group_id_ (Integer)]
        """
        node = Node('Split to Instances', {'Geometry': self, 'Selection': self.get_selection(), 'Group ID': group_id}, domain='EDGE')
        return node._out

    def store_named_attribute(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def store(self,
                    name: String = None,
                    value: Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color = None):
        """ > Node <&Node Store Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - value (Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeStoreNamedAttribute', value)
        node = Node('Store Named Attribute', {'Geometry': self, 'Selection': self.get_selection(), 'Name': name, 'Value': value}, data_type=data_type, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def active_element(cls):
        """ > Node <&Node Active Element>

        Information
        -----------
        - Parameter 'domain' : 'EDGE'

        Returns
        -------
        - Integer [exists_ (Boolean)]
        """
        node = Node('Active Element', domain='EDGE')
        return node._out

    def set_selection(self):
        """ > Node <&Node Set Selection>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'selection_type' : depending on 'selection' type

        Returns
        -------
        - Geometry
        """
        selection_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeToolSetSelection', selection)
        node = Node('Set Selection', {'Geometry': self, 'Selection': self.get_selection()}, domain='EDGE', selection_type=selection_type)
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        Information
        -----------
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - ui_shortcut (int): parameter 'ui_shortcut'

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

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - material (Material) : socket 'Material' (id: Material)

        Returns
        -------
        - Geometry
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

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)

        Returns
        -------
        - Mesh
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

        Information
        -----------
        - Socket 'Mesh' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)

        Returns
        -------
        - Mesh
        """
        node = Node('Set Shade Smooth', {'Geometry': self, 'Selection': self.get_selection(), 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

