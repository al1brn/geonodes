# Class Mesh

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[ID](#ID) - [bl_idname](#bl_idname) - [bnode](#bnode) - [bounding_box](#bounding_box) - [bounding_box_min](#bounding_box_min) - [convex_hull](#convex_hull) - [corner_count](#corner_count) - [curve_component](#curve_component) - [domain_size](#domain_size) - [edge_count](#edge_count) - [face_count](#face_count) - [index](#index) - [instances_component](#instances_component) - [is_multi_input](#is_multi_input) - [is_output](#is_output) - [is_viewport](#is_viewport) - [island](#island) - [island_count](#island_count) - [island_index](#island_index) - [links](#links) - [material_index](#material_index) - [mesh_component](#mesh_component) - [name](#name) - [node_chain_label](#node_chain_label) - [normal](#normal) - [point_count](#point_count) - [points_component](#points_component) - [position](#position) - [radius](#radius) - [separate_components](#separate_components) - [socket_index](#socket_index) - [volume_component](#volume_component)

**Class and static methods**

[Circle](#Circle) - [Collection](#Collection) - [Cone](#Cone) - [Cube](#Cube) - [Cylinder](#Cylinder) - [FromCollection](#FromCollection) - [Grid](#Grid) - [IcoSphere](#IcoSphere) - [Input](#Input) - [Line](#Line) - [LineEndPoints](#LineEndPoints) - [LineEndPointsResolution](#LineEndPointsResolution) - [LineOffset](#LineOffset) - [LineOffsetResolution](#LineOffsetResolution) - [UVSphere](#UVSphere) - [get_bl_idname](#get_bl_idname) - [get_class_name](#get_class_name) - [gives_bsocket](#gives_bsocket) - [is_socket](#is_socket) - [is_vector](#is_vector) - [value_data_type](#value_data_type)

**Methods**

[attribute_statistic](#attribute_statistic) - [boolean_difference](#boolean_difference) - [boolean_intersect](#boolean_intersect) - [boolean_union](#boolean_union) - [capture_attribute](#capture_attribute) - [capture_attribute_node](#capture_attribute_node) - [connected_sockets](#connected_sockets) - [corners_of_face](#corners_of_face) - [corners_of_vertex](#corners_of_vertex) - [delete](#delete) - [delete_all](#delete_all) - [delete_edges](#delete_edges) - [delete_faces](#delete_faces) - [distribute_points_on_faces](#distribute_points_on_faces) - [dual_mesh](#dual_mesh) - [duplicate](#duplicate) - [edge_paths_to_curves](#edge_paths_to_curves) - [edge_paths_to_selection](#edge_paths_to_selection) - [edges_of_corner](#edges_of_corner) - [edges_of_vertex](#edges_of_vertex) - [extrude](#extrude) - [face_is_planar](#face_is_planar) - [face_of_corner](#face_of_corner) - [face_set_boundaries](#face_set_boundaries) - [field_at_index](#field_at_index) - [flip_faces](#flip_faces) - [get_blender_socket](#get_blender_socket) - [get_named_boolean](#get_named_boolean) - [get_named_color](#get_named_color) - [get_named_float](#get_named_float) - [get_named_integer](#get_named_integer) - [get_named_vector](#get_named_vector) - [init_domains](#init_domains) - [init_socket](#init_socket) - [instance_on_points](#instance_on_points) - [instantiate](#instantiate) - [interpolate_domain](#interpolate_domain) - [is_shade_smooth](#is_shade_smooth) - [join](#join) - [material_selection](#material_selection) - [merge_by_distance](#merge_by_distance) - [named_attribute](#named_attribute) - [offset_corner_in_face](#offset_corner_in_face) - [pack_uv_islands](#pack_uv_islands) - [plug](#plug) - [proximity](#proximity) - [proximity_edges](#proximity_edges) - [proximity_faces](#proximity_faces) - [proximity_points](#proximity_points) - [random_boolean](#random_boolean) - [random_float](#random_float) - [random_integer](#random_integer) - [random_vector](#random_vector) - [raycast](#raycast) - [raycast_interpolated](#raycast_interpolated) - [raycast_nearest](#raycast_nearest) - [remove_named_attribute](#remove_named_attribute) - [replace_material](#replace_material) - [reroute](#reroute) - [reset_properties](#reset_properties) - [sample_index](#sample_index) - [sample_nearest](#sample_nearest) - [sample_nearest_surface](#sample_nearest_surface) - [sample_uv_surface](#sample_uv_surface) - [scale_elements](#scale_elements) - [scale_single_axis](#scale_single_axis) - [scale_uniform](#scale_uniform) - [separate](#separate) - [set_ID](#set_ID) - [set_material](#set_material) - [set_material_index](#set_material_index) - [set_named_boolean](#set_named_boolean) - [set_named_color](#set_named_color) - [set_named_float](#set_named_float) - [set_named_integer](#set_named_integer) - [set_named_vector](#set_named_vector) - [set_position](#set_position) - [set_shade_smooth](#set_shade_smooth) - [shortest_edge_paths](#shortest_edge_paths) - [show_handles](#show_handles) - [split_edges](#split_edges) - [stack](#stack) - [store_named_attribute](#store_named_attribute) - [subdivide](#subdivide) - [subdivision_surface](#subdivision_surface) - [switch](#switch) - [to_curve](#to_curve) - [to_instance](#to_instance) - [to_output](#to_output) - [to_points](#to_points) - [to_volume](#to_volume) - [transform](#transform) - [triangulate](#triangulate) - [uv_unwrap](#uv_unwrap) - [vertex_of_corner](#vertex_of_corner) - [view](#view)

## Properties

### ID

 Node ID.

Node reference [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html)
Developer reference [GeometryNodeInputID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

#### Returns:
- socket `ID`



### bl_idname

 Shortcut for `self.bsocket.bl_idname`



### bnode

 Shortcut for `self.bsocket.node`



### bounding_box

 Node BoundingBox.

Node reference [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html)
Developer reference [GeometryNodeBoundBox](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

#### Returns:
- socket `bounding_box` [Mesh](Mesh.md)



### bounding_box_min

 Node BoundingBox.

Node reference [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html)
Developer reference [GeometryNodeBoundBox](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

#### Returns:
- socket `max`



### convex_hull

 Node ConvexHull.

Node reference [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html)
Developer reference [GeometryNodeConvexHull](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)

#### Returns:
- socket `convex_hull` [Mesh](Mesh.md)



### corner_count

 Node DomainSize.

Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `face_corner_count`



### curve_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `curve` [Curve](Curve.md)



### domain_size

 Node DomainSize.

Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']



### edge_count

 Node DomainSize.

Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `edge_count`



### face_count

 Node DomainSize.

Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `face_count`



### index

 Node Index.

Node reference [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html)
Developer reference [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`



### instances_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `instances` [Instances](Instances.md)



### is_multi_input

 Shortcut for `self.bsocket.is_multi_output`



### is_output

 Shortcut for `self.bsocket.is_output`



### is_viewport

 Node IsViewport.

Node reference [Is Viewport](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html)
Developer reference [GeometryNodeIsViewport](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)

#### Returns:
- socket `is_viewport`



### island

 Node MeshIsland.

Node reference [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html)
Developer reference [GeometryNodeInputMeshIsland](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

#### Returns:
- node with sockets ['island_index', 'island_count']



### island_count

 Node MeshIsland.

Node reference [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html)
Developer reference [GeometryNodeInputMeshIsland](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

#### Returns:
- socket `island_count`



### island_index

 Node MeshIsland.

Node reference [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html)
Developer reference [GeometryNodeInputMeshIsland](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

#### Returns:
- socket `island_index`



### links

 Shortcut for `self.bsocket.links`



### material_index

 Node MaterialIndex.

Node reference [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html)
Developer reference [GeometryNodeInputMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

#### Returns:
- socket `material_index`



### mesh_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `mesh` [Mesh](Mesh.md)



### name

 Shortcut for `self.bsocket.name`



### node_chain_label

 Shortcut for *self.node.chain_label*



### normal

 Node Normal.

Node reference [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html)
Developer reference [GeometryNodeInputNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`



### point_count

 Node DomainSize.

Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`



### points_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `point_cloud` [Points](Points.md)



### position

 Node Position.

Node reference [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html)
Developer reference [GeometryNodeInputPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

#### Returns:
- socket `position`



### radius

 Node Radius.

Node reference [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html)
Developer reference [GeometryNodeInputRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

#### Returns:
- socket `radius`



### separate_components

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- node with sockets ['mesh', 'point_cloud', 'curve', 'volume', 'instances']



### socket_index

#### Returns:

Depending on the _is_output_ property, the socket belongs either to *node.inputs* or
*node.outputs*.




### volume_component

 Node SeparateComponents.

Node reference [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
Developer reference [GeometryNodeSeparateComponents](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `volume` [Volume](Volume.md)



## Class and static methods

### Circle

```python
@classmethod
def Circle(cls, vertices=None, radius=None, fill_type='NONE')
```

 Node MeshCircle.

Node reference [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html)
Developer reference [GeometryNodeMeshCircle](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)

#### Args:
- vertices: Integer
- radius: Float
- fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]

#### Returns:
- socket `mesh`



### Collection

```python
@classmethod
def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```

 Node CollectionInfo.

Node reference [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html)
Developer reference [GeometryNodeCollectionInfo](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)

#### Args:
- collection: Collection
- separate_children: Boolean
- reset_children: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `geometry`



### Cone

```python
@staticmethod
def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON')
```

 Node Cone.

Node reference [Cone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html)
Developer reference [GeometryNodeMeshCone](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)

#### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius_top: Float
- radius_bottom: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

#### Returns:
- tuple ('mesh', 'top', 'bottom', 'side')



### Cube

```python
@classmethod
def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None)
```

 Node Cube.

Node reference [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html)
Developer reference [GeometryNodeMeshCube](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)

#### Args:
- size: Vector
- vertices_x: Integer
- vertices_y: Integer
- vertices_z: Integer

#### Returns:
- socket `mesh`



### Cylinder

```python
@staticmethod
def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON')
```

 Node Cylinder.

Node reference [Cylinder](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html)
Developer reference [GeometryNodeMeshCylinder](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)

#### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

#### Returns:
- tuple ('mesh', 'top', 'bottom', 'side')



### FromCollection

```python
@classmethod
def FromCollection(cls, collection=None, separate_children
```

 Get the geometry from a collection

.. blid:: GeometryNodeCollectionInfo



### Grid

```python
@classmethod
def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None)
```

 Node Grid.

Node reference [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html)
Developer reference [GeometryNodeMeshGrid](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)

#### Args:
- size_x: Float
- size_y: Float
- vertices_x: Integer
- vertices_y: Integer

#### Returns:
- socket `mesh`



### IcoSphere

```python
@classmethod
def IcoSphere(cls, radius=None, subdivisions=None)
```

 Node IcoSphere.

Node reference [Ico Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html)
Developer reference [GeometryNodeMeshIcoSphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)

#### Args:
- radius: Float
- subdivisions: Integer

#### Returns:
- socket `mesh`



### Input

```python
@classmethod
def Input(cls, name = None, description = "")
```

 Create a Geometry input socket in the Group Input Node

#### Args:
- name: The socket name
- description: User tip
    
#### Returns:
- Geometry: The Geometry data socket
    
Note
----
    This method create a new input socket in the Group Input node. To get the **default** input geometry,
    use :attr:`Tree.input_geometry`.
    



### Line

```python
@classmethod
def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET')
```

 Node MeshLine.

Node reference [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)
Developer reference [GeometryNodeMeshLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- count: Integer
- resolution: Float
- start_location: Vector
- offset: Vector
- count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
- mode (str): 'OFFSET' in [OFFSET, END_POINTS]

#### Returns:
- socket `mesh`



### LineEndPoints

```python
@classmethod
def LineEndPoints(cls, count=None, start_location=None, end_location=None)
```

 Node MeshLine.

Node reference [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)
Developer reference [GeometryNodeMeshLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- count: Integer
- start_location: Vector
- end_location: Vector

#### Returns:
- socket `mesh`



### LineEndPointsResolution

```python
@classmethod
def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None)
```

 Node MeshLine.

Node reference [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)
Developer reference [GeometryNodeMeshLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- resolution: Float
- start_location: Vector
- end_location: Vector

#### Returns:
- socket `mesh`



### LineOffset

```python
@classmethod
def LineOffset(cls, count=None, start_location=None, offset=None)
```

 Node MeshLine.

Node reference [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)
Developer reference [GeometryNodeMeshLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- count: Integer
- start_location: Vector
- offset: Vector

#### Returns:
- socket `mesh`



### LineOffsetResolution

```python
@classmethod
def LineOffsetResolution(cls, resolution=None, start_location=None, offset=None)
```

 Node MeshLine.

Node reference [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html)
Developer reference [GeometryNodeMeshLine](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- resolution: Float
- start_location: Vector
- offset: Vector

#### Returns:
- socket `mesh`



### UVSphere

```python
@classmethod
def UVSphere(cls, segments=None, rings=None, radius=None)
```

 Node UvSphere.

Node reference [UV Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html)
Developer reference [GeometryNodeMeshUVSphere](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)

#### Args:
- segments: Integer
- rings: Integer
- radius: Float

#### Returns:
- socket `mesh`



### get_bl_idname

```python
@staticmethod
def get_bl_idname(class_name)
```

 Get the node socket bl_idname name from the Socket class

:param class_name: The class name
:type class_name: str
:return: The bl_idname associated to this class name
:rtype: str

Used to create a new group input socket. Called in `DataClass.Input` method to determine
which socket type must be created.

Note that here the class_name argument accepts additional values which correspond to *sub classes*:
    
.. list-table:: 
   :widths: 20 40
   :header-rows: 0

   * - Unsigned
     - Integer sub class (NodeSocketIntUnsigned)
   * - Factor
     - Float sub class (NodeSocketFloatFactor)
   * - Angle
     - Float sub class  (NodeSocketFloatAngle)
   * - Distance
     - Float sub class (NodeSocketFloatDistance)
   * - Rotation
     - Vector sub class (NodeSocketVectorEuler)
   * - xyz
     - Vector sub class (NodeSocketVectorXYZ)
   * - Translation
     - Vector sub class (NodeSocketVectorTranslation)
  
These additional values allow to enter angle, distance, factor... as group input values.




### get_class_name

```python
@staticmethod
def get_class_name(socket, with_sub_class = False)
```

 Get the DataSocket class name corresponding to the socket type and name.

:param socket: The socket to determine the class of
:param with_sub_class: Return the sub class if True
:typ socket: bpy.types.NodeSocket, Socket
:type with_sub_class: bool
:return: The name of the class associated to the bl_idname of the socket
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20 20
   :header-rows: 1
   
   * - NodeSocket
     - class name
     - sub class name
   * - NodeSocketBool 
     - 'Boolean'
     - 
   * - NodeSocketInt 
     - 'Integer'
     - 
   * - NodeSocketIntUnsigned 
     - 'Integer'
     - 'Unsigned'
   * - NodeSocketFloat 
     - 'Float' 
     - 
   * - NodeSocketFloatFactor 
     - 'Float'
     - 'Factor'
   * - NodeSocketFloatAngle  
     - 'Float'
     - 'Angle'
   * - NodeSocketFloatDistance 
     - 'Float'
     - 'Distance'
   * - NodeSocketVector 
     - 'Vector'
     - 
   * - NodeSocketVectorEuler 
     - 'Vector'
     - 'Rotation'
   * - NodeSocketVectorXYZ 
     - 'Vector'
     - 'xyz'
   * - NodeSocketVectorTranslation 
     - 'Vector'
     - 'Translation'
   * - NodeSocketColor 
     - 'Color'
     - 
   * - NodeSocketString' 
     - 'String'
     - 
   * - NodeSocketCollection 
     - 'Collection'
     - 
   * - NodeSocketImage 
     - 'Image'
     - 
   * - NodeSocketMaterial 
     - 'Material'
     - 
   * - NodeSocketObject 
     - 'Object'
     - 
   * - NodeSocketTexture 
     - 'Texture'
     - 
   * - NodeSocketGeometry
     - 'Geometry'
     - 
  
  
If the name of the socket is in ['Mesh', 'Points', 'Instances', 'Volume', 'Spline', 'Curve', 'Curves'],
the name is chosen as the class name.



### gives_bsocket

```python
@staticmethod
def gives_bsocket(value)
```

 Test if the argument provides a valid output socket.

:param value: The value to test
:type value: any
:return: True if *value* is or wraps a socket
:rtype: bool

#### Returns:
    
- A Blender Geometry Node Socket
- An instance of Socket        




### is_socket

```python
@staticmethod
def is_socket(value)
```

 An alternative to isinstance(value, Socket)

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool



### is_vector

```python
@staticmethod
def is_vector(value)
```

 Determine is the parameter is a vector.

:param value: The value to test
:type value: any
:return: True if *value* is an instance of Socket
:rtype: bool




### value_data_type

```python
@staticmethod
def value_data_type(value, default='FLOAT', color_domain='FLOAT_COLOR')
```

#### Returns:

:param value: The socket
:type value: any
:return: data type in ['BOOLEAN', 'INT', 'FLOAT', 'FLOAT_VECTOR', 'FLOAT_COLOR']
:rtype: str

.. list-table:: Correspondance table
   :widths: 30 20
   :header-rows: 1

   * - Socket bl_idname
     - Domain code
   * - NodeSocketBool
     - 'BOOLEAN'
   * - NodeSocketInt               
     - 'INT'
   * - NodeSocketIntUnsigned       
     - 'INT'
   * - NodeSocketFloat            
     - 'FLOAT'
   * - NodeSocketFloatFactor       
     - 'FLOAT'
   * - NodeSocketFloatAngle        
     - 'FLOAT'
   * - NodeSocketFloatDistance     
     - 'FLOAT'         
   * - NodeSocketVector            
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorEuler       
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorXYZ         
     - 'FLOAT_VECTOR'
   * - NodeSocketVectorTranslation
     - 'FLOAT_VECTOR'
   * - NodeSocketColor      
     - 'FLOAT_COLOR'
   * - NodeSocketString           
     - 'FLOAT_COLOR'





## Methods

### attribute_statistic

```python
def attribute_statistic(self, selection=None, attribute=None, domain='POINT')
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- selection: Boolean
- attribute: ['Float', 'Vector']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']



### boolean_difference

```python
def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None)
```

 Node MeshBoolean.

Node reference [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html)
Developer reference [GeometryNodeMeshBoolean](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

#### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Returns:
- socket `intersecting_edges`



### boolean_intersect

```python
def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None)
```

 Node MeshBoolean.

Node reference [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html)
Developer reference [GeometryNodeMeshBoolean](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

#### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Returns:
- socket `intersecting_edges`



### boolean_union

```python
def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None)
```

 Node MeshBoolean.

Node reference [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html)
Developer reference [GeometryNodeMeshBoolean](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

#### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Returns:
- socket `intersecting_edges`



### capture_attribute

```python
def capture_attribute(self, value=None, domain='POINT')
```

 Node CaptureAttribute.

Node reference [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)
Developer reference [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `attribute`



### capture_attribute_node

```python
def capture_attribute_node(self, geometry=None, value=None, data_type='FLOAT', domain='POINT')
```

 Node CaptureAttribute.

Node reference [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)
Developer reference [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- geometry: Geometry
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry', 'attribute']



### connected_sockets

```python
def connected_sockets(self)
```

#### Returns:




### corners_of_face

```python
def corners_of_face(self, face_index=None, weights=None, sort_index=None)
```

 Node CornersOfFace.

Node reference [Corners of Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_face.html)
Developer reference [GeometryNodeCornersOfFace](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)

#### Args:
- face_index: Integer
- weights: Float
- sort_index: Integer

#### Returns:
- tuple ('corner_index', 'total')



### corners_of_vertex

```python
def corners_of_vertex(self, vertex_index=None, weights=None, sort_index=None)
```

 Node CornersOfVertex.

Node reference [Corners of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html)
Developer reference [GeometryNodeCornersOfVertex](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)

#### Args:
- vertex_index: Integer
- weights: Float
- sort_index: Integer

#### Returns:
- tuple ('corner_index', 'total')



### delete

```python
def delete(self, selection=None, domain='POINT', mode='ALL')
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- node with sockets ['geometry']



### delete_all

```python
def delete_all(self, selection=None, domain='POINT')
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry']



### delete_edges

```python
def delete_edges(self, selection=None, domain='POINT')
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry']



### delete_faces

```python
def delete_faces(self, selection=None, domain='POINT')
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry']



### distribute_points_on_faces

```python
def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM')
```

 Node DistributePointsOnFaces.

Node reference [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html)
Developer reference [GeometryNodeDistributePointsOnFaces](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

#### Args:
- selection: Boolean
- distance_min: Float
- density_max: Float
- density: Float
- density_factor: Float
- seed: Integer
- distribute_method (str): 'RANDOM' in [RANDOM, POISSON]

#### Returns:
- tuple ('points', 'normal', 'rotation')



### dual_mesh

```python
def dual_mesh(self, mesh=None, keep_boundaries=None)
```

 Node DualMesh.

Node reference [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html)
Developer reference [GeometryNodeDualMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)

#### Args:
- mesh: Mesh
- keep_boundaries: Boolean

#### Returns:
- socket `dual_mesh` [Mesh](Mesh.md)



### duplicate

```python
def duplicate(self, selection=None, amount=None, domain='POINT')
```

 Node DuplicateElements.

Node reference [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)
Developer reference [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- selection: Boolean
- amount: Integer
- domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]

#### Returns:
- socket `duplicate_index`



### edge_paths_to_curves

```python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None)
```

 Node EdgePathsToCurves.

Node reference [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html)
Developer reference [GeometryNodeEdgePathsToCurves](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)

#### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

#### Returns:
- socket `curves` [Curve](Curve.md)



### edge_paths_to_selection

```python
def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None)
```

 Node EdgePathsToSelection.

Node reference [Edge Paths to Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_selection.html)
Developer reference [GeometryNodeEdgePathsToSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html)

#### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

#### Returns:
- socket `selection`



### edges_of_corner

```python
def edges_of_corner(self, corner_index=None)
```

 Node EdgesOfCorner.

Node reference [Edges of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html)
Developer reference [GeometryNodeEdgesOfCorner](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)

#### Args:
- corner_index: Integer

#### Returns:
- tuple ('next_edge_index', 'previous_edge_index')



### edges_of_vertex

```python
def edges_of_vertex(self, vertex_index=None, weights=None, sort_index=None)
```

 Node EdgesOfVertex.

Node reference [Edges of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html)
Developer reference [GeometryNodeEdgesOfVertex](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)

#### Args:
- vertex_index: Integer
- weights: Float
- sort_index: Integer

#### Returns:
- tuple ('edge_index', 'total')



### extrude

```python
def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES')
```

 Node ExtrudeMesh.

Node reference [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html)
Developer reference [GeometryNodeExtrudeMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

#### Args:
- selection: Boolean
- offset: Vector
- offset_scale: Float
- individual: Boolean
- mode (str): 'FACES' in [VERTICES, EDGES, FACES]

#### Returns:
- tuple ('top', 'side')



### face_is_planar

```python
def face_is_planar(self, threshold=None)
```

 Node FaceIsPlanar.

Node reference [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html)
Developer reference [GeometryNodeInputMeshFaceIsPlanar](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)

#### Args:
- threshold: Float

#### Returns:
- socket `planar`



### face_of_corner

```python
def face_of_corner(self, corner_index=None)
```

 Node FaceOfCorner.

Node reference [Face of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html)
Developer reference [GeometryNodeFaceOfCorner](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)

#### Args:
- corner_index: Integer

#### Returns:
- tuple ('face_index', 'index_in_face')



### face_set_boundaries

```python
def face_set_boundaries(self, face_set=None)
```

 Node FaceSetBoundaries.

Node reference [Face Set Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html)
Developer reference [GeometryNodeMeshFaceSetBoundaries](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)

#### Args:
- face_set: Integer

#### Returns:
- socket `boundary_edges`



### field_at_index

```python
def field_at_index(self, index=None, value=None, domain='POINT')
```

 Node FieldAtIndex.

Node reference [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html)
Developer reference [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

#### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`



### flip_faces

```python
def flip_faces(self, selection=None)
```

 Node FlipFaces.

Node reference [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html)
Developer reference [GeometryNodeFlipFaces](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)

#### Args:
- selection: Boolean

#### Returns:
- node with sockets ['mesh']



### get_blender_socket

```python
def get_blender_socket(self)
```

#### Returns:

:return: self.bsocket
:rtype: bpy.types.NodeSocket




### get_named_boolean

```python
def get_named_boolean(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### get_named_color

```python
def get_named_color(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### get_named_float

```python
def get_named_float(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### get_named_integer

```python
def get_named_integer(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### get_named_vector

```python
def get_named_vector(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



### init_domains

```python
def init_domains(self)
```

 Initialize the geometry domains

To be overloaded by sub classes.        



### init_socket

```python
def init_socket(self)
```

 Complementary init

Called at the end of initialization for further operations.



### instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

 Node InstanceOnPoints.

Node reference [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
Developer reference [GeometryNodeInstanceOnPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances`



### instantiate

```python
def instantiate(self, count = 1, realize = False)
```

 Instantiate the geometry

#### Args:
- count: Number of instances to create
- realize: True to realize the instances
    
#### Returns:
- Instances or Geometry
    
The duplication is performed by instantiating the geometry along the vertices
of a Mesh Line initialized with `count` points.

The operator ``*`` can be used to operate this method with `realize = False`:
    
.. code-block::
    
    curves = curve * 10
    
    # is equivalent to
    
    curves = curve.duplicate(10, realize=False)
    




### interpolate_domain

```python
def interpolate_domain(self, value=None, domain='POINT')
```

 Node InterpolateDomain.

Node reference [Interpolate Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html)
Developer reference [GeometryNodeFieldOnDomain](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`



### is_shade_smooth

```python
def is_shade_smooth(self)
```

 Node IsShadeSmooth.

Node reference [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html)
Developer reference [GeometryNodeInputShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)

#### Returns:
- socket `smooth`



### join

```python
def join(*geometry)
```

 Node JoinGeometry.

Node reference [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)
Developer reference [GeometryNodeJoinGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- node with sockets ['geometry']



### material_selection

```python
def material_selection(self, material=None)
```

 Node MaterialSelection.

Node reference [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)
Developer reference [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

#### Args:
- material: Material

#### Returns:
- socket `selection`



### merge_by_distance

```python
def merge_by_distance(self, selection=None, distance=None, mode='ALL')
```

 Node MergeByDistance.

Node reference [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html)
Developer reference [GeometryNodeMergeByDistance](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

#### Args:
- selection: Boolean
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

#### Returns:
- node with sockets ['geometry']



### named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT')
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

#### Returns:
- socket `attribute`



### offset_corner_in_face

```python
def offset_corner_in_face(self, corner_index=None, offset=None)
```

 Node OffsetCornerInFace.

Node reference [Offset Corner in Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/offset_corner_in_face.html)
Developer reference [GeometryNodeOffsetCornerInFace](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)

#### Args:
- corner_index: Integer
- offset: Integer

#### Returns:
- socket `corner_index`



### pack_uv_islands

```python
def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None)
```

 Node PackUvIslands.

Node reference [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html)
Developer reference [GeometryNodeUVPackIslands](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)

#### Args:
- uv: Vector
- selection: Boolean
- margin: Float
- rotate: Boolean

#### Returns:
- socket `uv`



### plug

```python
def plug(self, *values)
```

 Plug values in the socket (input sockets only)

:param values: The output sockets. More than one values can be passed
    if the input socket is multi input.
:type values: array of bpy.types.NodeSocket, Socket, values

see :func:`plug_bsocket`



### proximity

```python
def proximity(self, target=None, source_position=None, target_element='FACES')
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector
- target_element (str): 'FACES' in [POINTS, EDGES, FACES]

#### Returns:
- socket `distance`



### proximity_edges

```python
def proximity_edges(self, target=None, source_position=None)
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`



### proximity_faces

```python
def proximity_faces(self, target=None, source_position=None)
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`



### proximity_points

```python
def proximity_points(self, target=None, source_position=None)
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`



### random_boolean

```python
def random_boolean(self, probability=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



### random_float

```python
def random_float(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



### random_integer

```python
def random_integer(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



### random_vector

```python
def random_vector(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



### raycast

```python
def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED')
```

 Node Raycast.

Node reference [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html)
Developer reference [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float
- mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']



### raycast_interpolated

```python
def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```

 Node Raycast.

Node reference [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html)
Developer reference [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']



### raycast_nearest

```python
def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```

 Node Raycast.

Node reference [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html)
Developer reference [GeometryNodeRaycast](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']



### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```

 Node RemoveNamedAttribute.

Node reference [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)
Developer reference [GeometryNodeRemoveAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- node with sockets ['geometry']



### replace_material

```python
def replace_material(self, old=None, new=None)
```

 Node ReplaceMaterial.

Node reference [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)
Developer reference [GeometryNodeReplaceMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)

#### Args:
- old: Material
- new: Material

#### Returns:
- node with sockets ['geometry']



### reroute

```python
def reroute(self)
```

 Reroute all output links



### reset_properties

```python
def reset_properties(self)
```

 Reset the properties

Properties such as components are cached.

After a node is called, the wrapped socket changes and this makes the cache obsolete.
After a change, the cache is erased.

:example:

.. code-block:: python

    class Vector(...):
        def __init__(self, ...):
             ...
             self.reset_properties()
             ...
    
         def reset_properties(self):
             super().reset_properties()
             self.separate_ = None      # Created by property self.seperate() with node SeparateXyz






### sample_index

```python
def sample_index(self, value=None, index=None, clamp=False, domain='POINT')
```

 Node SampleIndex.

Node reference [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html)
Developer reference [GeometryNodeSampleIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`



### sample_nearest

```python
def sample_nearest(self, sample_position=None, domain='POINT')
```

 Node SampleNearest.

Node reference [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html)
Developer reference [GeometryNodeSampleNearest](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

#### Args:
- sample_position: Vector
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

#### Returns:
- socket `index`



### sample_nearest_surface

```python
def sample_nearest_surface(self, value=None, sample_position=None)
```

 Node SampleNearestSurface.

Node reference [Sample Nearest Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_nearest_surface.html)
Developer reference [GeometryNodeSampleNearestSurface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- sample_position: Vector

#### Returns:
- socket `value`



### sample_uv_surface

```python
def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None)
```

 Node SampleUvSurface.

Node reference [Sample UV Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html)
Developer reference [GeometryNodeSampleUVSurface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- source_uv_map: Vector
- sample_uv: Vector

#### Returns:
- tuple ('value', 'is_valid')



### scale_elements

```python
def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM')
```

 Node ScaleElements.

Node reference [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
Developer reference [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]
- scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]

#### Returns:
- node with sockets ['geometry']



### scale_single_axis

```python
def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE')
```

 Node ScaleElements.

Node reference [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
Developer reference [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]

#### Returns:
- node with sockets ['geometry']



### scale_uniform

```python
def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE')
```

 Node ScaleElements.

Node reference [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html)
Developer reference [GeometryNodeScaleElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- selection: Boolean
- scale: Float
- center: Vector
- domain (str): 'FACE' in [FACE, EDGE]

#### Returns:
- node with sockets ['geometry']



### separate

```python
def separate(self, geometry=None, selection=None, domain='POINT')
```

 Node SeparateGeometry.

Node reference [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)
Developer reference [GeometryNodeSeparateGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- geometry: Geometry
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- tuple ('selection', 'inverted')



### set_ID

```python
def set_ID(self, selection=None, ID=None)
```

 Node SetID.

Node reference [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
Developer reference [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- selection: Boolean
- ID: Integer

#### Returns:
- node with sockets ['geometry']



### set_material

```python
def set_material(self, selection=None, material=None)
```

 Node SetMaterial.

Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

#### Args:
- selection: Boolean
- material: Material

#### Returns:
- node with sockets ['geometry']



### set_material_index

```python
def set_material_index(self, selection=None, material_index=None)
```

 Node SetMaterialIndex.

Node reference [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)
Developer reference [GeometryNodeSetMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

#### Args:
- selection: Boolean
- material_index: Integer

#### Returns:
- node with sockets ['geometry']



### set_named_boolean

```python
def set_named_boolean(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry']



### set_named_color

```python
def set_named_color(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry']



### set_named_float

```python
def set_named_float(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry']



### set_named_integer

```python
def set_named_integer(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry']



### set_named_vector

```python
def set_named_vector(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry']



### set_position

```python
def set_position(self, selection=None, position=None, offset=None)
```

 Node SetPosition.

Node reference [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
Developer reference [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- selection: Boolean
- position: Vector
- offset: Vector

#### Returns:
- node with sockets ['geometry']



### set_shade_smooth

```python
def set_shade_smooth(self, selection=None, shade_smooth=None)
```

 Node SetShadeSmooth.

Node reference [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html)
Developer reference [GeometryNodeSetShadeSmooth](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

#### Args:
- selection: Boolean
- shade_smooth: Boolean

#### Returns:
- node with sockets ['geometry']



### shortest_edge_paths

```python
def shortest_edge_paths(self, end_vertex=None, edge_cost=None)
```

 Node ShortestEdgePaths.

Node reference [Shortest Edge Paths](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html)
Developer reference [GeometryNodeInputShortestEdgePaths](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)

#### Args:
- end_vertex: Boolean
- edge_cost: Float

#### Returns:
- tuple ('next_vertex_index', 'total_cost')



### show_handles

```python
def show_handles(self)
```

 Generate a mesh and cloud points to visualize the control points and handles

#### Returns:
- Geometry: The geometry can be joined to the output
    
Example:
    
    .. code-block:: python
    
        curve = ... # Curve initialization
        
        visu = curve.show_handles()
        
        tree.output_geometry = curve + visu
    




### split_edges

```python
def split_edges(self, selection=None)
```

 Node SplitEdges.

Node reference [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html)
Developer reference [GeometryNodeSplitEdges](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)

#### Args:
- selection: Boolean

#### Returns:
- node with sockets ['mesh']



### stack

```python
def stack(self, node, socket_name=None)
```

 Change the wrapped socket

:param node: The new node owning the output socket to wrap
:type node: Node
:return: self

Methods are implemented in two modes:

- Creation
- Transformation

In **creation mode**, the node is considered as creating new data. The result is a new instance of DataSocket.

In **transformation mode**, the node is considered as transforming data which is kept in the result of the method.
After the method returns, the calling DataSocket instance refers to a new Blender output socket.
The stack method changes the socket the instance refers to and reinitialize properties

.. code-block:: python

    # 1. Creation mode
    # 
    # to_mesh method creates a new mesh from a curve.
    # The curve instance refers to the same output node socket
    # We need to get the result of the method in a new variable
    
    new_mesh = curve.to_mesh(profile_curve=circle)
    
    # 2. Transformation mode
    #
    # set_shade_smooth method transforms the mesh.
    # After the call, the mesh instance refers to the output socket of the
    # newly created node "Set Shade Smooth". There is no need to get the result
    # of the method.
    
    mesh.set_shade_smooth()
    
    # Note that a transformation method returns self and so, the following line
    # is equivallent:
    
    mesh = mesh.set_shade_smooth()





### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None, domain='POINT')
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry']



### subdivide

```python
def subdivide(self, level=None)
```

 Node SubdivideMesh.

Node reference [Subdivide Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html)
Developer reference [GeometryNodeSubdivideMesh](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)

#### Args:
- level: Integer

#### Returns:
- node with sockets ['mesh']



### subdivision_surface

```python
def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES')
```

 Node SubdivisionSurface.

Node reference [Subdivision Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html)
Developer reference [GeometryNodeSubdivisionSurface](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)

#### Args:
- level: Integer
- edge_crease: Float
- vertex_crease: Float
- boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
- uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]

#### Returns:
- node with sockets ['mesh']



### switch

```python
def switch(self, switch=None, true=None)
```

 Node Switch.

Node reference [Switch](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html)
Developer reference [GeometryNodeSwitch](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Geometry

#### Returns:
- socket `output`



### to_curve

```python
def to_curve(self, selection=None)
```

 Node MeshToCurve.

Node reference [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html)
Developer reference [GeometryNodeMeshToCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)

#### Args:
- selection: Boolean

#### Returns:
- socket `curve` [Curve](Curve.md)



### to_instance

```python
def to_instance(*geometry)
```

 Node GeometryToInstance.

Node reference [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)
Developer reference [GeometryNodeGeometryToInstance](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `instances` [Instances](Instances.md)



### to_output

```python
def to_output(self, name=None)
```

 Plug the data socket to the group output

:param name: The name to give to the modifier output
:type name: str

The socket is added to the outputs of the geometry nodes tree.

.. Note:: To define a data socket as the result geometry of the tree, use ``tree.output_geometry = my_geometry``.




### to_points

```python
def to_points(self, selection=None, position=None, radius=None, mode='VERTICES')
```

 Node MeshToPoints.

Node reference [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html)
Developer reference [GeometryNodeMeshToPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)

#### Args:
- selection: Boolean
- position: Vector
- radius: Float
- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

#### Returns:
- socket `points` [Points](Points.md)



### to_volume

```python
def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT')
```

 Node MeshToVolume.

Node reference [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html)
Developer reference [GeometryNodeMeshToVolume](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)

#### Args:
- density: Float
- voxel_size: Float
- voxel_amount: Float
- exterior_band_width: Float
- interior_band_width: Float
- fill_volume: Boolean
- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

#### Returns:
- socket `volume` [Volume](Volume.md)



### transform

```python
def transform(self, translation=None, rotation=None, scale=None)
```

 Node Transform.

Node reference [Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html)
Developer reference [GeometryNodeTransform](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)

#### Args:
- translation: Vector
- rotation: Vector
- scale: Vector

#### Returns:
- node with sockets ['geometry']



### triangulate

```python
def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL')
```

 Node Triangulate.

Node reference [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html)
Developer reference [GeometryNodeTriangulate](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)

#### Args:
- selection: Boolean
- minimum_vertices: Integer
- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

#### Returns:
- node with sockets ['mesh']



### uv_unwrap

```python
def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED')
```

 Node UvUnwrap.

Node reference [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html)
Developer reference [GeometryNodeUVUnwrap](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)

#### Args:
- selection: Boolean
- seam: Boolean
- margin: Float
- fill_holes: Boolean
- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

#### Returns:
- socket `uv`



### vertex_of_corner

```python
def vertex_of_corner(self, corner_index=None)
```

 Node VertexOfCorner.

Node reference [Vertex of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/vertex_of_corner.html)
Developer reference [GeometryNodeVertexOfCorner](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)

#### Args:
- corner_index: Integer

#### Returns:
- socket `vertex_index`



### view

```python
def view(self, domain='AUTO', label=None, node_color=None)
```

 Link the data socket to the viewer

If the data socket is a geometry (Curve, Mesh...) it is linked to the geometry input of the viewer.

If it ias a value (Integer, Float,...) it is linked to the value socket and the viewer is configured
accordingly.



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

