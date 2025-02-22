from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Edge(Socket):
    """"
    $DOC SET hidden
    """
    @classmethod
    def accumulate_field(cls, value=None, group_id=None):
        """ > Node <&Node Accumulate Field>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - group_id (Integer) : socket 'Group ID' (id: Group Index)

        Returns
        -------
        - Float [trailing_ (Float), total_ (Float)]
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'MATRIX': 'TRANSFORM'}, 'Edge.accumulate_field', 'value')
        node = Node('Accumulate Field', sockets={'Value': value, 'Group Index': group_id}, data_type=data_type, domain='EDGE')
        return node._out

    def attribute_statistic(self, attribute=None):
        """ > Node <&Node Attribute Statistic>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (id: Attribute)

        Returns
        -------
        - node [mean (Float), median (Float), sum (Float), min (Float), max (Float), range (Float), standard_deviation (Float), variance (Float)]
        """
        data_type = utils.get_argument_data_type(attribute, {'VALUE': 'FLOAT', 'VECTOR': 'FLOAT_VECTOR'}, 'Edge.attribute_statistic', 'attribute')
        node = Node('Attribute Statistic', sockets={'Geometry': self, 'Selection': self._sel, 'Attribute': attribute}, data_type=data_type, domain='EDGE')
        return node

    @classmethod
    def corners(cls, edge_index=None, weights=None, sort_index=None):
        """ > Node <&Node Corners of Edge>

        Arguments
        ---------
        - edge_index (Integer) : socket 'Edge Index' (id: Edge Index)
        - weights (Float) : socket 'Weights' (id: Weights)
        - sort_index (Integer) : socket 'Sort Index' (id: Sort Index)

        Returns
        -------
        - node [corner_index (Integer), total (Integer)]
        """
        node = Node('Corners of Edge', sockets={'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node

    @classmethod
    def corner_index(cls, edge_index=None, weights=None, sort_index=None):
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
        node = Node('Corners of Edge', sockets={'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
        return node.corner_index

    @classmethod
    def corners_total(cls, edge_index=None, weights=None, sort_index=None):
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
        node = Node('Corners of Edge', sockets={'Edge Index': edge_index, 'Weights': weights, 'Sort Index': sort_index})
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode='ALL')
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode='EDGE_FACE')
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete_geometry(self, mode='ALL'):
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode=mode)
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode='ALL')
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode='EDGE_FACE')
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode='ONLY_FACE')
        self._jump(node._out)
        return self._domain_to_geometry

    def delete(self, mode='ALL'):
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
        node = Node('Delete Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def duplicate(self, amount=None):
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
        node = Node('Duplicate Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Amount': amount}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def paths_to_curves(self, start_vertices=None, next_vertex_index=None):
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
        node = Node('Edge Paths to Curves', sockets={'Mesh': self, 'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def paths_to_selection(cls, start_vertices=None, next_vertex_index=None):
        """ > Node <&Node Edge Paths to Selection>

        Arguments
        ---------
        - start_vertices (Boolean) : socket 'Start Vertices' (id: Start Vertices)
        - next_vertex_index (Integer) : socket 'Next Vertex Index' (id: Next Vertex Index)

        Returns
        -------
        - Boolean
        """
        node = Node('Edge Paths to Selection', sockets={'Start Vertices': start_vertices, 'Next Vertex Index': next_vertex_index})
        return node._out

    @classmethod
    def to_face_groups(cls, boundary_edges=None):
        """ > Node <&Node Edges to Face Groups>

        Arguments
        ---------
        - boundary_edges (Boolean) : socket 'Boundary Edges' (id: Boundary Edges)

        Returns
        -------
        - Integer
        """
        node = Node('Edges to Face Groups', sockets={'Boundary Edges': boundary_edges})
        return node._out

    def extrude(self, offset=None, offset_scale=None):
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
        node = Node('Extrude Mesh', sockets={'Mesh': self, 'Selection': self._sel, 'Offset': offset, 'Offset Scale': offset_scale}, mode='EDGES')
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def evaluate_at_index(cls, index=None, value=None):
        """ > Node <&Node Evaluate at Index>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - index (Integer) : socket 'Index' (id: Index)
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.evaluate_at_index', 'value')
        node = Node('Evaluate at Index', sockets={'Index': index, 'Value': value}, data_type=data_type, domain='EDGE')
        return node._out

    @classmethod
    def evaluate_on_domain(cls, value=None):
        """ > Node <&Node Evaluate on Domain>

        Information
        -----------
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.evaluate_on_domain', 'value')
        node = Node('Evaluate on Domain', sockets={'Value': value}, data_type=data_type, domain='EDGE')
        return node._out

    @classmethod
    def edge_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - node [unsigned_angle (Float), signed_angle (Float)]
        """
        node = Node('Edge Angle', sockets={})
        return node

    @classmethod
    @property
    def unsigned_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - unsigned_angle
        """
        node = Node('Edge Angle', sockets={})
        return node.unsigned_angle

    @classmethod
    @property
    def signed_angle(cls):
        """ > Node <&Node Edge Angle>

        Returns
        -------
        - signed_angle
        """
        node = Node('Edge Angle', sockets={})
        return node.signed_angle

    @classmethod
    @property
    def face_count(cls):
        """ > Node <&Node Edge Neighbors>

        Returns
        -------
        - Integer
        """
        node = Node('Edge Neighbors', sockets={})
        return node._out

    @classmethod
    def edge_vertices(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - node [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
        """
        node = Node('Edge Vertices', sockets={})
        return node

    @classmethod
    @property
    def vertex_index_1(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - vertex_index_1
        """
        node = Node('Edge Vertices', sockets={})
        return node.vertex_index_1

    @classmethod
    @property
    def vertex_index_2(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - vertex_index_2
        """
        node = Node('Edge Vertices', sockets={})
        return node.vertex_index_2

    @classmethod
    @property
    def position_1(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - position_1
        """
        node = Node('Edge Vertices', sockets={})
        return node.position_1

    @classmethod
    @property
    def position_2(cls):
        """ > Node <&Node Edge Vertices>

        Returns
        -------
        - position_2
        """
        node = Node('Edge Vertices', sockets={})
        return node.position_2

    @classmethod
    def shortest_paths(cls, end_vertex=None, edge_cost=None):
        """ > Node <&Node Shortest Edge Paths>

        Arguments
        ---------
        - end_vertex (Boolean) : socket 'End Vertex' (id: End Vertex)
        - edge_cost (Float) : socket 'Edge Cost' (id: Edge Cost)

        Returns
        -------
        - Integer [total_cost_ (Float)]
        """
        node = Node('Shortest Edge Paths', sockets={'End Vertex': end_vertex, 'Edge Cost': edge_cost})
        return node._out

    def to_points(self, position=None, radius=None):
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
        node = Node('Mesh to Points', sockets={'Mesh': self, 'Selection': self._sel, 'Position': position, 'Radius': radius}, mode='EDGES')
        return node._out

    def sample_index(self, value=None, index=None, clamp=False):
        """ > Node <&Node Sample Index>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)
        - index (Integer) : socket 'Index' (id: Index)
        - clamp (bool): parameter 'clamp'

        Returns
        -------
        - Float
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.sample_index', 'value')
        node = Node('Sample Index', sockets={'Geometry': self, 'Value': value, 'Index': index}, clamp=clamp, data_type=data_type, domain='EDGE')
        return node._out

    def sample_nearest(self, sample_position=None):
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
        node = Node('Sample Nearest', sockets={'Geometry': self, 'Sample Position': sample_position}, domain='EDGE')
        return node._out

    def scale(self, scale=None, center=None, scale_mode='UNIFORM'):
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
        - scale_mode (str): parameter 'scale_mode' in ['UNIFORM', 'SINGLE_AXIS']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Scale Elements', 'scale_mode', scale_mode, 'scale', ('UNIFORM', 'SINGLE_AXIS'))
        node = Node('Scale Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Scale': scale, 'Center': center}, domain='EDGE', scale_mode=scale_mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def scale_uniform(self, scale=None, center=None):
        """ > Node <&Node Scale Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'scale_mode' : 'UNIFORM'

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)

        Returns
        -------
        - Geometry
        """
        node = Node('Scale Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Scale': scale, 'Center': center}, domain='EDGE', scale_mode='UNIFORM')
        self._jump(node._out)
        return self._domain_to_geometry

    def scale_single_axis(self, scale=None, center=None, axis=None):
        """ > Node <&Node Scale Elements>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'
        - Parameter 'scale_mode' : 'SINGLE_AXIS'

        Arguments
        ---------
        - scale (Float) : socket 'Scale' (id: Scale)
        - center (Vector) : socket 'Center' (id: Center)
        - axis (Vector) : socket 'Axis' (id: Axis)

        Returns
        -------
        - Geometry
        """
        node = Node('Scale Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Scale': scale, 'Center': center, 'Axis': axis}, domain='EDGE', scale_mode='SINGLE_AXIS')
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
        - Geometry [inverted_ (Geometry)]
        """
        node = Node('Separate Geometry', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def set_shade_smooth(self, shade_smooth=None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Shade Smooth', sockets={'Geometry': self, 'Selection': self._sel, 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def sort(self, group_id=None, sort_weight=None):
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
        node = Node('Sort Elements', sockets={'Geometry': self, 'Selection': self._sel, 'Group ID': group_id, 'Sort Weight': sort_weight}, domain='EDGE')
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
        node = Node('Split Edges', sockets={'Mesh': self, 'Selection': self._sel})
        self._jump(node._out)
        return self._domain_to_geometry

    def split_to_instances(self, group_id=None):
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
        node = Node('Split to Instances', sockets={'Geometry': self, 'Selection': self._sel, 'Group ID': group_id}, domain='EDGE')
        return node._out

    def store_named_attribute(self, name=None, value=None):
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
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.store_named_attribute', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    def store(self, name=None, value=None):
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
        - value (Float) : socket 'Value' (id: Value)

        Returns
        -------
        - Geometry
        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.store', 'value')
        node = Node('Store Named Attribute', sockets={'Geometry': self, 'Selection': self._sel, 'Name': name, 'Value': value}, data_type=data_type, domain='EDGE')
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
        node = Node('Active Element', sockets={}, domain='EDGE')
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
        selection_type = utils.get_argument_data_type(selection, {'BOOLEAN': 'BOOLEAN', 'VALUE': 'FLOAT'}, 'Edge.set_selection', 'selection')
        node = Node('Set Selection', sockets={'Geometry': self, 'Selection': self._sel}, domain='EDGE', selection_type=selection_type)
        self._jump(node._out)
        return self._domain_to_geometry

    def viewer(self, value=None):
        """ > Node <&Node Viewer>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Edge.viewer', 'value')
        node = Node('Viewer', sockets={'Geometry': self, 'Value': value}, data_type=data_type, domain='EDGE')
        return

    @property
    def material(self):
        """ Write only property for node <Node Set Material>
        """
        raise NodeError('Property Edge.material is write only.')

    @material.setter
    def material(self, material=None):
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
        node = Node('Set Material', sockets={'Geometry': self, 'Selection': self._sel, 'Material': material})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def shade_smooth(self):
        """ Property get node <Node Set Shade Smooth>
        """
        return Node('Is Edge Smooth', sockets={})._out

    @shade_smooth.setter
    def shade_smooth(self, shade_smooth=None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Shade Smooth', sockets={'Geometry': self, 'Selection': self._sel, 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def smooth(self):
        """ Property get node <Node Set Shade Smooth>
        """
        return Node('Is Edge Smooth', sockets={})._out

    @smooth.setter
    def smooth(self, shade_smooth=None):
        """ > Node <&Node Set Shade Smooth>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'domain' : 'EDGE'

        Arguments
        ---------
        - shade_smooth (Boolean) : socket 'Shade Smooth' (id: Shade Smooth)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Shade Smooth', sockets={'Geometry': self, 'Selection': self._sel, 'Shade Smooth': shade_smooth}, domain='EDGE')
        self._jump(node._out)
        return self._domain_to_geometry

