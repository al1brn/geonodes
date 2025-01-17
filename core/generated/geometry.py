from .. socket_class import Socket
from .. treeclass import Node, ColorRamp, NodeCurves
from .. treeclass import utils
from .. scripterror import NodeError

class Geometry(Socket):
    """"
    $DOC SET hidden
    """
    def bounding_box(self):
        """ > Node <&Node Bounding Box>

        Information
        -----------
        - Socket 'Geometry' : self

        Returns
        -------
        - Mesh [min_ (Vector), max_ (Vector)]
        """
        node = Node('Bounding Box', sockets={'Geometry': self})
        return node._out

    def convex_hull(self):
        """ > Node <&Node Convex Hull>

        Information
        -----------
        - Socket 'Geometry' : self

        Returns
        -------
        - Mesh
        """
        node = Node('Convex Hull', sockets={'Geometry': self})
        return node._out

    def to_instance(self, *geometry):
        """ > Node <&Node Geometry to Instance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Instances
        """
        node = Node('Geometry to Instance', sockets={'Geometry': [self] + list(geometry)})
        return node._out

    @classmethod
    def index_of_nearest(cls, position=None, group_id=None):
        """ > Node <&Node Index of Nearest>

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Integer [has_neighbor_ (Boolean)]
        """
        node = Node('Index of Nearest', sockets={'Position': position, 'Group ID': group_id})
        return node._out

    @classmethod
    @property
    def index(cls):
        """ > Node <&Node Index>

        Returns
        -------
        - Integer
        """
        node = Node('Index', sockets={})
        return node._out

    def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):
        """ > Node <&Node Instance on Points>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - instance (Geometry) : socket 'Instance' (id: Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (id: Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (id: Instance Index)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Instances
        """
        node = Node('Instance on Points', sockets={'Points': self, 'Selection': self._sel, 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out

    def join(self, *geometry):
        """ > Node <&Node Join Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Geometry
        """
        node = Node('Join Geometry', sockets={'Geometry': [self] + list(geometry)})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Join(cls, *geometry):
        """ > Node <&Node Join Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Geometry
        """
        node = Node('Join Geometry', sockets={'Geometry': list(geometry)})
        return cls(node._out)

    def merge_by_distance(self, distance=None, mode='ALL'):
        """ > Node <&Node Merge by Distance>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - distance (Float) : socket 'Distance' (id: Distance)
        - mode (str): parameter 'mode' in ['ALL', 'CONNECTED']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Merge by Distance', 'mode', mode, 'merge_by_distance', ('ALL', 'CONNECTED'))
        node = Node('Merge by Distance', sockets={'Geometry': self, 'Selection': self._sel, 'Distance': distance}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def merge_all(self, distance=None):
        """ > Node <&Node Merge by Distance>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'ALL'

        Arguments
        ---------
        - distance (Float) : socket 'Distance' (id: Distance)

        Returns
        -------
        - Geometry
        """
        node = Node('Merge by Distance', sockets={'Geometry': self, 'Selection': self._sel, 'Distance': distance}, mode='ALL')
        self._jump(node._out)
        return self._domain_to_geometry

    def merge_connected(self, distance=None):
        """ > Node <&Node Merge by Distance>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Parameter 'mode' : 'CONNECTED'

        Arguments
        ---------
        - distance (Float) : socket 'Distance' (id: Distance)

        Returns
        -------
        - Geometry
        """
        node = Node('Merge by Distance', sockets={'Geometry': self, 'Selection': self._sel, 'Distance': distance}, mode='CONNECTED')
        self._jump(node._out)
        return self._domain_to_geometry

    def merge(self, distance=None, mode='ALL'):
        """ > Node <&Node Merge by Distance>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - distance (Float) : socket 'Distance' (id: Distance)
        - mode (str): parameter 'mode' in ['ALL', 'CONNECTED']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Merge by Distance', 'mode', mode, 'merge', ('ALL', 'CONNECTED'))
        node = Node('Merge by Distance', sockets={'Geometry': self, 'Selection': self._sel, 'Distance': distance}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def proximity(self, group_id=None, sample_position=None, sample_group_id=None, target_element='FACES'):
        """ > Node <&Node Geometry Proximity>

        Information
        -----------
        - Socket 'Geometry' : self

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sample_position (Vector) : socket 'Sample Position' (id: Source Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (id: Sample Group ID)
        - target_element (str): parameter 'target_element' in ['POINTS', 'EDGES', 'FACES']

        Returns
        -------
        - Vector [distance_ (Float), is_valid_ (Boolean)]
        """
        utils.check_enum_arg('Geometry Proximity', 'target_element', target_element, 'proximity', ('POINTS', 'EDGES', 'FACES'))
        node = Node('Geometry Proximity', sockets={'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=target_element)
        return node._out

    def proximity_points(self, group_id=None, sample_position=None, sample_group_id=None):
        """ > Node <&Node Geometry Proximity>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'target_element' : 'POINTS'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sample_position (Vector) : socket 'Sample Position' (id: Source Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (id: Sample Group ID)

        Returns
        -------
        - Vector [distance_ (Float), is_valid_ (Boolean)]
        """
        node = Node('Geometry Proximity', sockets={'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element='POINTS')
        return node._out

    def proximity_edges(self, group_id=None, sample_position=None, sample_group_id=None):
        """ > Node <&Node Geometry Proximity>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'target_element' : 'EDGES'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sample_position (Vector) : socket 'Sample Position' (id: Source Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (id: Sample Group ID)

        Returns
        -------
        - Vector [distance_ (Float), is_valid_ (Boolean)]
        """
        node = Node('Geometry Proximity', sockets={'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element='EDGES')
        return node._out

    def proximity_faces(self, group_id=None, sample_position=None, sample_group_id=None):
        """ > Node <&Node Geometry Proximity>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'target_element' : 'FACES'

        Arguments
        ---------
        - group_id (Integer) : socket 'Group ID' (id: Group ID)
        - sample_position (Vector) : socket 'Sample Position' (id: Source Position)
        - sample_group_id (Integer) : socket 'Sample Group ID' (id: Sample Group ID)

        Returns
        -------
        - Vector [distance_ (Float), is_valid_ (Boolean)]
        """
        node = Node('Geometry Proximity', sockets={'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element='FACES')
        return node._out

    def raycast(self, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED'):
        """ > Node <&Node Raycast>

        Information
        -----------
        - Socket 'Target Geometry' : self
        - Parameter 'data_type' : depending on 'attribute' type

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (id: Attribute)
        - source_position (Vector) : socket 'Source Position' (id: Source Position)
        - ray_direction (Vector) : socket 'Ray Direction' (id: Ray Direction)
        - ray_length (Float) : socket 'Ray Length' (id: Ray Length)
        - mapping (str): parameter 'mapping' in ['INTERPOLATED', 'NEAREST']

        Returns
        -------
        - node [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
        """
        utils.check_enum_arg('Raycast', 'mapping', mapping, 'raycast', ('INTERPOLATED', 'NEAREST'))
        data_type = utils.get_argument_data_type(attribute, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Geometry.raycast', 'attribute')
        node = Node('Raycast', sockets={'Target Geometry': self, 'Attribute': attribute, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length}, data_type=data_type, mapping=mapping)
        return node

    def raycast_interpolated(self, attribute=None, source_position=None, ray_direction=None, ray_length=None):
        """ > Node <&Node Raycast>

        Information
        -----------
        - Socket 'Target Geometry' : self
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'mapping' : 'INTERPOLATED'

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (id: Attribute)
        - source_position (Vector) : socket 'Source Position' (id: Source Position)
        - ray_direction (Vector) : socket 'Ray Direction' (id: Ray Direction)
        - ray_length (Float) : socket 'Ray Length' (id: Ray Length)

        Returns
        -------
        - node [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
        """
        data_type = utils.get_argument_data_type(attribute, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Geometry.raycast_interpolated', 'attribute')
        node = Node('Raycast', sockets={'Target Geometry': self, 'Attribute': attribute, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length}, data_type=data_type, mapping='INTERPOLATED')
        return node

    def raycast_nearest(self, attribute=None, source_position=None, ray_direction=None, ray_length=None):
        """ > Node <&Node Raycast>

        Information
        -----------
        - Socket 'Target Geometry' : self
        - Parameter 'data_type' : depending on 'attribute' type
        - Parameter 'mapping' : 'NEAREST'

        Arguments
        ---------
        - attribute (Float) : socket 'Attribute' (id: Attribute)
        - source_position (Vector) : socket 'Source Position' (id: Source Position)
        - ray_direction (Vector) : socket 'Ray Direction' (id: Ray Direction)
        - ray_length (Float) : socket 'Ray Length' (id: Ray Length)

        Returns
        -------
        - node [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]
        """
        data_type = utils.get_argument_data_type(attribute, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Geometry.raycast_nearest', 'attribute')
        node = Node('Raycast', sockets={'Target Geometry': self, 'Attribute': attribute, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length}, data_type=data_type, mapping='NEAREST')
        return node

    def realize(self, realize_all=None, depth=None):
        """ > Node <&Node Realize Instances>

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - realize_all (Boolean) : socket 'Realize All' (id: Realize All)
        - depth (Integer) : socket 'Depth' (id: Depth)

        Returns
        -------
        - Geometry
        """
        node = Node('Realize Instances', sockets={'Geometry': self, 'Selection': self._sel, 'Realize All': realize_all, 'Depth': depth})
        return node._out

    def remove_named_attribute(self, name=None, pattern_mode='EXACT'):
        """ > Node <&Node Remove Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)
        - pattern_mode (str): parameter 'pattern_mode' in ['EXACT', 'WILDCARD']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Remove Named Attribute', 'pattern_mode', pattern_mode, 'remove_named_attribute', ('EXACT', 'WILDCARD'))
        node = Node('Remove Named Attribute', sockets={'Geometry': self, 'Name': name}, pattern_mode=pattern_mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def remove_names(self, name=None):
        """ > Node <&Node Remove Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'pattern_mode' : 'WILDCARD'

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Geometry
        """
        node = Node('Remove Named Attribute', sockets={'Geometry': self, 'Name': name}, pattern_mode='WILDCARD')
        self._jump(node._out)
        return self._domain_to_geometry

    def replace_material(self, old=None, new=None):
        """ > Node <&Node Replace Material>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self

        Arguments
        ---------
        - old (Material) : socket 'Old' (id: Old)
        - new (Material) : socket 'New' (id: New)

        Returns
        -------
        - Geometry
        """
        node = Node('Replace Material', sockets={'Geometry': self, 'Old': old, 'New': new})
        self._jump(node._out)
        return self._domain_to_geometry

    def separate_components(self):
        """ > Node <&Node Separate Components>

        Information
        -----------
        - Socket 'Geometry' : self

        Returns
        -------
        - node [mesh (Mesh), curve (Curve), grease_pencil (GreasePencil), point_cloud (Cloud), volume (Volume), instances (Instances)]
        """
        node = self._cache('Separate Components', sockets={'Geometry': self})
        return node

    @property
    def mesh(self):
        """ > Node <&Node Separate Components>

        Information
        -----------
        - Socket 'Geometry' : self

        Returns
        -------
        - mesh
        """
        node = self._cache('Separate Components', sockets={'Geometry': self})
        return node.mesh

    @property
    def curve(self):
        """ > Node <&Node Separate Components>

        Information
        -----------
        - Socket 'Geometry' : self

        Returns
        -------
        - curve
        """
        node = self._cache('Separate Components', sockets={'Geometry': self})
        return node.curve

    @property
    def grease_pencil(self):
        """ > Node <&Node Separate Components>

        Information
        -----------
        - Socket 'Geometry' : self

        Returns
        -------
        - grease_pencil
        """
        node = self._cache('Separate Components', sockets={'Geometry': self})
        return node.grease_pencil

    @property
    def point_cloud(self):
        """ > Node <&Node Separate Components>

        Information
        -----------
        - Socket 'Geometry' : self

        Returns
        -------
        - point_cloud
        """
        node = self._cache('Separate Components', sockets={'Geometry': self})
        return node.point_cloud

    @property
    def volume(self):
        """ > Node <&Node Separate Components>

        Information
        -----------
        - Socket 'Geometry' : self

        Returns
        -------
        - volume
        """
        node = self._cache('Separate Components', sockets={'Geometry': self})
        return node.volume

    @property
    def instances(self):
        """ > Node <&Node Separate Components>

        Information
        -----------
        - Socket 'Geometry' : self

        Returns
        -------
        - instances
        """
        node = self._cache('Separate Components', sockets={'Geometry': self})
        return node.instances

    def set_name(self, name=None):
        """ > Node <&Node Set Geometry Name>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Geometry Name', sockets={'Geometry': self, 'Name': name})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_id(self, id=None):
        """ > Node <&Node Set ID>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - id (Integer) : socket 'ID' (id: ID)

        Returns
        -------
        - Geometry
        """
        node = Node('Set ID', sockets={'Geometry': self, 'Selection': self._sel, 'ID': id})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_material(self, material=None):
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

    def set_material_index(self, material_index=None):
        """ > Node <&Node Set Material Index>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - material_index (Integer) : socket 'Material Index' (id: Material Index)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Material Index', sockets={'Geometry': self, 'Selection': self._sel, 'Material Index': material_index})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_position(self, position=None, offset=None):
        """ > Node <&Node Set Position>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Position', sockets={'Geometry': self, 'Selection': self._sel, 'Position': position, 'Offset': offset})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_spline_cyclic(self, cyclic=None):
        """ > Node <&Node Set Spline Cyclic>

        > ***Jump*** : Socket refers to node output socket after the call

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
        return self._domain_to_geometry

    def set_spline_resolution(self, resolution=None):
        """ > Node <&Node Set Spline Resolution>

        > ***Jump*** : Socket refers to node output socket after the call

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
        return self._domain_to_geometry

    def transform_components(self, translation=None, rotation=None, scale=None, transform=None):
        """ > Node <&Node Transform Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'mode' : 'COMPONENTS'

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (id: Translation)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Geometry
        """
        node = Node('Transform Geometry', sockets={'Geometry': self, 'Translation': translation, 'Rotation': rotation, 'Scale': scale, 'Transform': transform}, mode='COMPONENTS')
        self._jump(node._out)
        return self._domain_to_geometry

    def transform_matrix(self, translation=None, rotation=None, scale=None, transform=None):
        """ > Node <&Node Transform Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'mode' : 'MATRIX'

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (id: Translation)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Geometry
        """
        node = Node('Transform Geometry', sockets={'Geometry': self, 'Translation': translation, 'Rotation': rotation, 'Scale': scale, 'Transform': transform}, mode='MATRIX')
        self._jump(node._out)
        return self._domain_to_geometry

    def transform(self, translation=None, rotation=None, scale=None, transform=None, mode='COMPONENTS'):
        """ > Node <&Node Transform Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self

        Arguments
        ---------
        - translation (Vector) : socket 'Translation' (id: Translation)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - transform (Matrix) : socket 'Transform' (id: Transform)
        - mode (str): parameter 'mode' in ['COMPONENTS', 'MATRIX']

        Returns
        -------
        - Geometry
        """
        utils.check_enum_arg('Transform Geometry', 'mode', mode, 'transform', ('COMPONENTS', 'MATRIX'))
        node = Node('Transform Geometry', sockets={'Geometry': self, 'Translation': translation, 'Rotation': rotation, 'Scale': scale, 'Transform': transform}, mode=mode)
        self._jump(node._out)
        return self._domain_to_geometry

    def viewer(self, value=None):
        """ > Node <&Node Viewer>

        Information
        -----------
        - Socket 'Geometry' : self
        - Parameter 'data_type' : depending on 'value' type
        - Parameter 'domain' : 'AUTO'

        Arguments
        ---------
        - value (Float) : socket 'Value' (id: Value)

        """
        data_type = utils.get_argument_data_type(value, {'VALUE': 'FLOAT', 'INT': 'INT', 'VECTOR': 'FLOAT_VECTOR', 'RGBA': 'FLOAT_COLOR', 'BOOLEAN': 'BOOLEAN', 'ROTATION': 'QUATERNION', 'MATRIX': 'FLOAT4X4'}, 'Geometry.viewer', 'value')
        node = Node('Viewer', sockets={'Geometry': self, 'Value': value}, data_type=data_type, domain='AUTO')
        return

    @property
    def position(self):
        """ Property get node <Node Set Position>
        """
        return Node('Position', sockets={})._out

    @position.setter
    def position(self, position=None):
        """ > Node <&Node Set Position>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Offset' : ignored

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Position', sockets={'Geometry': self, 'Selection': self._sel, 'Position': position, 'Offset': None})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def offset(self):
        """ Write only property for node <Node Set Position>
        """
        raise NodeError('Property Geometry.offset is write only.')

    @offset.setter
    def offset(self, offset=None):
        """ > Node <&Node Set Position>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]
        - Socket 'Position' : ignored

        Arguments
        ---------
        - offset (Vector) : socket 'Offset' (id: Offset)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Position', sockets={'Geometry': self, 'Selection': self._sel, 'Position': None, 'Offset': offset})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def id(self):
        """ Property get node <Node Set ID>
        """
        return Node('ID', sockets={})._out

    @id.setter
    def id(self, id=None):
        """ > Node <&Node Set ID>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - id (Integer) : socket 'ID' (id: ID)

        Returns
        -------
        - Geometry
        """
        node = Node('Set ID', sockets={'Geometry': self, 'Selection': self._sel, 'ID': id})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def material(self):
        """ Write only property for node <Node Set Material>
        """
        raise NodeError('Property Geometry.material is write only.')

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
    def name(self):
        """ Write only property for node <Node Set Geometry Name>
        """
        raise NodeError('Property Geometry.name is write only.')

    @name.setter
    def name(self, name=None):
        """ > Node <&Node Set Geometry Name>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self

        Arguments
        ---------
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Geometry Name', sockets={'Geometry': self, 'Name': name})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def material_index(self):
        """ Property get node <Node Set Material Index>
        """
        return Node('Material Index', sockets={})._out

    @material_index.setter
    def material_index(self, material_index=None):
        """ > Node <&Node Set Material Index>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - material_index (Integer) : socket 'Material Index' (id: Material Index)

        Returns
        -------
        - Geometry
        """
        node = Node('Set Material Index', sockets={'Geometry': self, 'Selection': self._sel, 'Material Index': material_index})
        self._jump(node._out)
        return self._domain_to_geometry

