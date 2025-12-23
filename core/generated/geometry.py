# Generated 2025-12-23 17:03:08

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


class Geometry(Socket):
    """"
    $DOC SET hidden
    """
    def bounding_box(self, use_radius: Boolean = None):
        """ > Node <&Node Bounding Box>

        Information
        -----------
        - Socket 'Geometry' : self

        Arguments
        ---------
        - use_radius (Boolean) : socket 'Use Radius' (id: Use Radius)

        Returns
        -------
        - Mesh [min_ (Vector), max_ (Vector)]
        """
        node = Node('Bounding Box', {'Geometry': self, 'Use Radius': use_radius})
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
        node = Node('Convex Hull', {'Geometry': self})
        return node._out

    def to_instance(self, *geometry: Geometry):
        """ > Node <&Node Geometry to Instance>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Instances
        """
        node = Node('Geometry to Instance', {'Geometry': [self] + list(geometry)})
        return node._out

    @classmethod
    def index_of_nearest(cls, position: Vector = None, group_id: Integer = None):
        """ > Node <&Node Index of Nearest>

        Arguments
        ---------
        - position (Vector) : socket 'Position' (id: Position)
        - group_id (Integer) : socket 'Group ID' (id: Group ID)

        Returns
        -------
        - Integer [has_neighbor_ (Boolean)]
        """
        node = Node('Index of Nearest', {'Position': position, 'Group ID': group_id})
        return node._out

    @classmethod
    @property
    def index(cls):
        """ > Node <&Node Index>

        Returns
        -------
        - Integer
        """
        node = Node('Index', )
        return node._out

    def instance_on_points(self,
                    instance: Instances = None,
                    pick_instance: Boolean = None,
                    instance_index: Integer = None,
                    rotation: Rotation = None,
                    scale: Vector = None):
        """ > Node <&Node Instance on Points>

        Information
        -----------
        - Socket 'Points' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - instance (Instances) : socket 'Instance' (id: Instance)
        - pick_instance (Boolean) : socket 'Pick Instance' (id: Pick Instance)
        - instance_index (Integer) : socket 'Instance Index' (id: Instance Index)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)

        Returns
        -------
        - Instances
        """
        node = Node('Instance on Points', {'Points': self, 'Selection': self.get_selection(), 'Instance': instance, 'Pick Instance': pick_instance, 'Instance Index': instance_index, 'Rotation': rotation, 'Scale': scale})
        return node._out

    def join(self, *geometry: Geometry):
        """ > Node <&Node Join Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Geometry
        """
        node = Node('Join Geometry', {'Geometry': [self] + list(geometry)})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def Join(cls, *geometry: Geometry):
        """ > Node <&Node Join Geometry>

        Arguments
        ---------
        - geometry (Geometry) : socket 'Geometry' (id: Geometry)

        Returns
        -------
        - Geometry
        """
        node = Node('Join Geometry', {'Geometry': list(geometry)})
        return cls(node._out)

    def merge_by_distance(self, mode: Literal['All', 'Connected'] = None, distance: Float = None):
        """ > Node <&Node Merge by Distance>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - mode (menu='All') : ('All', 'Connected')
        - distance (Float) : socket 'Distance' (id: Distance)

        Returns
        -------
        - Geometry
        """
        node = Node('Merge by Distance', {'Geometry': self, 'Selection': self.get_selection(), 'Mode': mode, 'Distance': distance})
        self._jump(node._out)
        return self._domain_to_geometry

    def merge(self, mode: Literal['All', 'Connected'] = None, distance: Float = None):
        """ > Node <&Node Merge by Distance>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self
        - Socket 'Selection' : self[selection]

        Arguments
        ---------
        - mode (menu='All') : ('All', 'Connected')
        - distance (Float) : socket 'Distance' (id: Distance)

        Returns
        -------
        - Geometry
        """
        node = Node('Merge by Distance', {'Geometry': self, 'Selection': self.get_selection(), 'Mode': mode, 'Distance': distance})
        self._jump(node._out)
        return self._domain_to_geometry

    def proximity(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None,
                    target_element: Literal['POINTS', 'EDGES', 'FACES'] = 'FACES'):
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
        node = Node('Geometry Proximity', {'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element=target_element)
        return node._out

    def proximity_points(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None):
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
        node = Node('Geometry Proximity', {'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element='POINTS')
        return node._out

    def proximity_edges(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None):
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
        node = Node('Geometry Proximity', {'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element='EDGES')
        return node._out

    def proximity_faces(self,
                    group_id: Integer = None,
                    sample_position: Vector = None,
                    sample_group_id: Integer = None):
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
        node = Node('Geometry Proximity', {'Target': self, 'Group ID': group_id, 'Source Position': sample_position, 'Sample Group ID': sample_group_id}, target_element='FACES')
        return node._out

    def raycast(self,
                    attribute: Float | Integer | Boolean | Vector | Color | Rotation | Matrix = None,
                    interpolation: Literal['Interpolated', 'Nearest'] = None,
                    source_position: Vector = None,
                    ray_direction: Vector = None,
                    ray_length: Float = None):
        """ > Node <&Node Raycast>

        Information
        -----------
        - Socket 'Target Geometry' : self
        - Parameter 'data_type' : depending on 'attribute' type

        Arguments
        ---------
        - attribute (Float | Integer | Boolean | Vector | Color | Rotation | Matrix) : socket 'Attribute' (id: Attribute)
        - interpolation (menu='Interpolated') : ('Interpolated', 'Nearest')
        - source_position (Vector) : socket 'Source Position' (id: Source Position)
        - ray_direction (Vector) : socket 'Ray Direction' (id: Ray Direction)
        - ray_length (Float) : socket 'Ray Length' (id: Ray Length)

        Returns
        -------
        - Boolean [hit_position_ (Vector), hit_normal_ (Vector), hit_distance_ (Float), attribute_ (Float)]
        """
        data_type = utils.get_data_type_from_argument('GeometryNodeTree', 'GeometryNodeRaycast', attribute)
        node = Node('Raycast', {'Target Geometry': self, 'Attribute': attribute, 'Interpolation': interpolation, 'Source Position': source_position, 'Ray Direction': ray_direction, 'Ray Length': ray_length}, data_type=data_type)
        return node._out

    def realize(self, realize_all: Boolean = None, depth: Integer = None):
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
        node = Node('Realize Instances', {'Geometry': self, 'Selection': self.get_selection(), 'Realize All': realize_all, 'Depth': depth})
        return node._out

    def remove_named_attribute(self, pattern_mode: Literal['Exact', 'Wildcard'] = None, name: String = None):
        """ > Node <&Node Remove Named Attribute>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self

        Arguments
        ---------
        - pattern_mode (menu='Exact') : ('Exact', 'Wildcard')
        - name (String) : socket 'Name' (id: Name)

        Returns
        -------
        - Geometry
        """
        node = Node('Remove Named Attribute', {'Geometry': self, 'Pattern Mode': pattern_mode, 'Name': name})
        self._jump(node._out)
        return self._domain_to_geometry

    def replace_material(self, old: Material = None, new: Material = None):
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
        node = Node('Replace Material', {'Geometry': self, 'Old': old, 'New': new})
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
        node = self._cache('Separate Components', {'Geometry': self})
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
        node = self._cache('Separate Components', {'Geometry': self})
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
        node = self._cache('Separate Components', {'Geometry': self})
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
        node = self._cache('Separate Components', {'Geometry': self})
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
        node = self._cache('Separate Components', {'Geometry': self})
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
        node = self._cache('Separate Components', {'Geometry': self})
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
        node = self._cache('Separate Components', {'Geometry': self})
        return node.instances

    def set_name(self, name: String = None):
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
        node = Node('Set Geometry Name', {'Geometry': self, 'Name': name})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_id(self, id: Integer = None):
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
        node = Node('Set ID', {'Geometry': self, 'Selection': self.get_selection(), 'ID': id})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_material(self, material: Material = None):
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

    def set_material_index(self, material_index: Integer = None):
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
        node = Node('Set Material Index', {'Geometry': self, 'Selection': self.get_selection(), 'Material Index': material_index})
        self._jump(node._out)
        return self._domain_to_geometry

    def set_position(self, position: Vector = None, offset: Vector = None):
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
        node = Node('Set Position', {'Geometry': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': offset})
        self._jump(node._out)
        return self._domain_to_geometry

    def transform(self,
                    mode: Literal['Components', 'Matrix'] = None,
                    translation: Vector = None,
                    rotation: Rotation = None,
                    scale: Vector = None,
                    transform: Matrix = None):
        """ > Node <&Node Transform Geometry>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Geometry' : self

        Arguments
        ---------
        - mode (menu='Components') : ('Components', 'Matrix')
        - translation (Vector) : socket 'Translation' (id: Translation)
        - rotation (Rotation) : socket 'Rotation' (id: Rotation)
        - scale (Vector) : socket 'Scale' (id: Scale)
        - transform (Matrix) : socket 'Transform' (id: Transform)

        Returns
        -------
        - Geometry
        """
        node = Node('Transform Geometry', {'Geometry': self, 'Mode': mode, 'Translation': translation, 'Rotation': rotation, 'Scale': scale, 'Transform': transform})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def viewer(cls, named_sockets: dict = {}, ui_shortcut = 0, **sockets):
        """ > Node <&Node Viewer>

        Information
        -----------
        - Parameter 'domain' : 'AUTO'

        Arguments
        ---------
        - ui_shortcut (int): parameter 'ui_shortcut'

        """
        node = Node('Viewer', named_sockets, domain='AUTO', ui_shortcut=ui_shortcut, **sockets)
        return

    def enable_output(self, enable: Boolean = None):
        """ > Node <&Node Enable Output>

        > ***Jump*** : Socket refers to node output socket after the call

        Information
        -----------
        - Socket 'Value' : self
        - Parameter 'data_type' : 'GEOMETRY'

        Arguments
        ---------
        - enable (Boolean) : socket 'Enable' (id: Enable)

        Returns
        -------
        - Geometry
        """
        node = Node('Enable Output', {'Enable': enable, 'Value': self}, data_type='GEOMETRY')
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def position(self):
        """ Property get node <Node Set Position>
        """
        return Node('Position', {})._out

    @position.setter
    def position(self, position: Vector = None):
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
        node = Node('Set Position', {'Geometry': self, 'Selection': self.get_selection(), 'Position': position, 'Offset': None})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def offset(self):
        """ Write only property for node <Node Set Position>
        """
        raise NodeError('Property Geometry.offset is write only.')

    @offset.setter
    def offset(self, offset: Vector = None):
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
        node = Node('Set Position', {'Geometry': self, 'Selection': self.get_selection(), 'Position': None, 'Offset': offset})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def id(self):
        """ Property get node <Node Set ID>
        """
        return Node('ID', {})._out

    @id.setter
    def id(self, id: Integer = None):
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
        node = Node('Set ID', {'Geometry': self, 'Selection': self.get_selection(), 'ID': id})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def material(self):
        """ Write only property for node <Node Set Material>
        """
        raise NodeError('Property Geometry.material is write only.')

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
    def name(self):
        """ Write only property for node <Node Set Geometry Name>
        """
        raise NodeError('Property Geometry.name is write only.')

    @name.setter
    def name(self, name: String = None):
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
        node = Node('Set Geometry Name', {'Geometry': self, 'Name': name})
        self._jump(node._out)
        return self._domain_to_geometry

    @property
    def material_index(self):
        """ Property get node <Node Set Material Index>
        """
        return Node('Material Index', {})._out

    @material_index.setter
    def material_index(self, material_index: Integer = None):
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
        node = Node('Set Material Index', {'Geometry': self, 'Selection': self.get_selection(), 'Material Index': material_index})
        self._jump(node._out)
        return self._domain_to_geometry

    @classmethod
    def _create_input_socket(cls,
        name: str = 'Geometry',
        tip: str = '',
        panel: str = "",
        optional_label: bool = False,
        hide_value: bool = False,
        hide_in_modifier: bool = False,
         ):
        """ > Geometry Input

        New <#Geometry> input with subtype 'NONE'.

        Aguments
        --------
        - name  (str = 'Geometry') : Input socket name
        - tip  (str = '') : Property description
        - panel (str = "") : Panel name
        - optional_label  (bool = False) : Property optional_label
        - hide_value  (bool = False) : Property hide_value
        - hide_in_modifier  (bool = False) : Property hide_in_modifier

        Returns
        -------
        - Geometry
        """
        from ..treeclass import Tree

        return Tree.current_tree().create_input_socket('NodeSocketGeometry', name=name, tip=tip,
            panel=panel, optional_label=optional_label, hide_value=hide_value,
            hide_in_modifier=hide_in_modifier)

