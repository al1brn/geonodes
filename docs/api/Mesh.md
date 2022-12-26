# Class Mesh

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 > **Mesh** sub class of [Geometry](Geometry.md)

A **Mesh** has four domains:
- `verts` of type [Vertex](Vertex.md)
- `edges` of type [Edge](Edge.md)
- `faces` of type [Face](Face.md)
- `corners` of type [Corner](Corner.md)

### Constructors

Constructors come from the Blender menu *Mesh primitives*:        
- [Cone](#Cone), returns the quadruplet: (cone(Mesh), top, bottom, side)
- [Cube](#Cube)
- [Cylinder](#Cylinder), returns the quadruplet: (cone(Mesh), top, bottom, side)
- [Grid](#Grid)
- [IcoSphere](#IcoSphere)
- [Circle](#Circle)
- [Line](#Line)
- [UVSphere](#UVSphere)
         
The `Line` constructor is also available with the different ways to initialize a line:
- [LineEndPoints](#LineEndPoints):  line is defined by its end points, the number of points is provided
- [LineEndPointsResolution](#LineEndPointsResolution): same as previous but resolution is given rather than the number of points
- [LineOffset](#LineOffset): line is defined by a starting point, a direction and a number of points




### Constructor

```python
Mesh(self, socket, node=None, label=None)
```

rom geonodes.nodes import domains

elf.points = Vertex(self) # Initialized before super().__init__ which can override points


## Content

**Properties**

[ID](#ID) | [bounding_box](#bounding_box) | [bounding_box_min](#bounding_box_min) | [convex_hull](#convex_hull) | [corner_count](#corner_count) | [curve_component](#curve_component) | [domain_size](#domain_size) | [edge_count](#edge_count) | [face_count](#face_count) | [index](#index) | [instances_component](#instances_component) | [is_viewport](#is_viewport) | [island](#island) | [island_count](#island_count) | [island_index](#island_index) | [material_index](#material_index) | [mesh_component](#mesh_component) | [normal](#normal) | [point_count](#point_count) | [points_component](#points_component) | [position](#position) | [radius](#radius) | [separate_components](#separate_components) | [volume_component](#volume_component)

***Inherited***

[bl_idname](DataSocket.md#bl_idname) | [bnode](DataSocket.md#bnode) | [is_multi_input](DataSocket.md#is_multi_input) | [is_output](DataSocket.md#is_output) | [is_plugged](DataSocket.md#is_plugged) | [links](DataSocket.md#links) | [name](DataSocket.md#name) | [node_chain_label](DataSocket.md#node_chain_label) | [socket_index](DataSocket.md#socket_index)

**Class and static methods**

[Circle](#Circle) | [Collection](#Collection) | [Cone](#Cone) | [Cube](#Cube) | [Cylinder](#Cylinder) | [FromCollection](#FromCollection) | [Grid](#Grid) | [IcoSphere](#IcoSphere) | [Input](#Input) | [Line](#Line) | [LineEndPoints](#LineEndPoints) | [LineEndPointsResolution](#LineEndPointsResolution) | [LineOffset](#LineOffset) | [UVSphere](#UVSphere) | [capture_attribute_node](#capture_attribute_node) | [random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector)

***Inherited***

[get_bl_idname](DataSocket.md#get_bl_idname) | [get_class_name](DataSocket.md#get_class_name) | [gives_bsocket](DataSocket.md#gives_bsocket) | [is_socket](DataSocket.md#is_socket) | [is_vector](DataSocket.md#is_vector) | [python_type_to_socket](DataSocket.md#python_type_to_socket) | [value_data_type](DataSocket.md#value_data_type)

**Methods**

[attribute_statistic](#attribute_statistic) | [boolean_difference](#boolean_difference) | [boolean_intersect](#boolean_intersect) | [boolean_union](#boolean_union) | [capture_attribute](#capture_attribute) | [corners_of_face](#corners_of_face) | [corners_of_vertex](#corners_of_vertex) | [delete](#delete) | [delete_all](#delete_all) | [delete_edges](#delete_edges) | [delete_faces](#delete_faces) | [distribute_points_on_faces](#distribute_points_on_faces) | [dual_mesh](#dual_mesh) | [duplicate](#duplicate) | [edge_paths_to_curves](#edge_paths_to_curves) | [edge_paths_to_selection](#edge_paths_to_selection) | [edges_of_corner](#edges_of_corner) | [edges_of_vertex](#edges_of_vertex) | [extrude](#extrude) | [face_is_planar](#face_is_planar) | [face_of_corner](#face_of_corner) | [face_set_boundaries](#face_set_boundaries) | [field_at_index](#field_at_index) | [flip_faces](#flip_faces) | [instance_on_points](#instance_on_points) | [instantiate](#instantiate) | [interpolate_domain](#interpolate_domain) | [is_shade_smooth](#is_shade_smooth) | [join](#join) | [material_selection](#material_selection) | [merge_by_distance](#merge_by_distance) | [named_attribute](#named_attribute) | [named_boolean](#named_boolean) | [named_color](#named_color) | [named_float](#named_float) | [named_integer](#named_integer) | [named_vector](#named_vector) | [offset_corner_in_face](#offset_corner_in_face) | [pack_uv_islands](#pack_uv_islands) | [proximity](#proximity) | [proximity_edges](#proximity_edges) | [proximity_faces](#proximity_faces) | [proximity_points](#proximity_points) | [raycast](#raycast) | [raycast_interpolated](#raycast_interpolated) | [raycast_nearest](#raycast_nearest) | [remove_named_attribute](#remove_named_attribute) | [replace_material](#replace_material) | [sample_index](#sample_index) | [sample_nearest](#sample_nearest) | [sample_nearest_surface](#sample_nearest_surface) | [sample_uv_surface](#sample_uv_surface) | [scale_elements](#scale_elements) | [scale_single_axis](#scale_single_axis) | [scale_uniform](#scale_uniform) | [separate](#separate) | [set_ID](#set_ID) | [set_material](#set_material) | [set_material_index](#set_material_index) | [set_position](#set_position) | [set_shade_smooth](#set_shade_smooth) | [shortest_edge_paths](#shortest_edge_paths) | [show_handles](#show_handles) | [split_edges](#split_edges) | [store_named_attribute](#store_named_attribute) | [store_named_boolean](#store_named_boolean) | [store_named_color](#store_named_color) | [store_named_float](#store_named_float) | [store_named_integer](#store_named_integer) | [store_named_vector](#store_named_vector) | [subdivide](#subdivide) | [subdivision_surface](#subdivision_surface) | [switch](#switch) | [to_curve](#to_curve) | [to_instance](#to_instance) | [to_points](#to_points) | [to_volume](#to_volume) | [transform](#transform) | [triangulate](#triangulate) | [uv_unwrap](#uv_unwrap) | [vertex_of_corner](#vertex_of_corner) | [view](#view) | [viewer](#viewer)

***Inherited***

[connected_sockets](DataSocket.md#connected_sockets) | [get_blender_socket](DataSocket.md#get_blender_socket) | [init_domains](DataSocket.md#init_domains) | [init_socket](DataSocket.md#init_socket) | [plug](DataSocket.md#plug) | [reroute](DataSocket.md#reroute) | [reset_properties](DataSocket.md#reset_properties) | [stack](DataSocket.md#stack) | [to_output](DataSocket.md#to_output)

## Properties

### ID



> Node: [ID](GeometryNodeInputID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

#### Returns:
- socket `ID`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### bounding_box



> Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

#### Returns:
- socket `bounding_box` of class Mesh






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### bounding_box_min



> Node: [Bounding Box](GeometryNodeBoundBox.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/bounding_box.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)

#### Returns:
- socket `max`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### convex_hull



> Node: [Convex Hull](GeometryNodeConvexHull.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)

#### Returns:
- socket `convex_hull` of class Mesh






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### corner_count



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `face_corner_count`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### curve_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `curve` of class Curve






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### domain_size



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### edge_count



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `edge_count`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### face_count



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `face_count`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### index



> Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instances_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `instances` of class Instances






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_viewport



> Node: [Is Viewport](GeometryNodeIsViewport.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/is_viewport.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)

#### Returns:
- socket `is_viewport`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### island



> Node: [Mesh Island](GeometryNodeInputMeshIsland.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

#### Returns:
- node with sockets ['island_index', 'island_count']






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### island_count



> Node: [Mesh Island](GeometryNodeInputMeshIsland.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

#### Returns:
- socket `island_count`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### island_index



> Node: [Mesh Island](GeometryNodeInputMeshIsland.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)

#### Returns:
- socket `island_index`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material_index



> Node: [Material Index](GeometryNodeInputMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

#### Returns:
- socket `material_index`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### mesh_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `mesh` of class Mesh






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### normal



> Node: [Normal](GeometryNodeInputNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### point_count



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### points_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `point_cloud` of class Points






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### position



> Node: [Position](GeometryNodeInputPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

#### Returns:
- socket `position`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### radius



> Node: [Radius](GeometryNodeInputRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

#### Returns:
- socket `radius`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate_components



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- node with sockets ['mesh', 'point_cloud', 'curve', 'volume', 'instances']






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### volume_component



> Node: [Separate Components](GeometryNodeSeparateComponents.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)

#### Returns:
- socket `volume` of class Volume






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### Circle

```python
@classmethod
def Circle(cls, vertices=None, radius=None, fill_type='NONE')
```



> Node: [Mesh Circle](GeometryNodeMeshCircle.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)

#### Args:
- vertices: Integer
- radius: Float
- fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]

#### Returns:
- socket `mesh`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Collection

```python
@classmethod
def Collection(cls, collection=None, separate_children=None, reset_children=None, transform_space='ORIGINAL')
```



> Node: [Collection Info](GeometryNodeCollectionInfo.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/collection_info.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)

#### Args:
- collection: Collection
- separate_children: Boolean
- reset_children: Boolean
- transform_space (str): 'ORIGINAL' in [ORIGINAL, RELATIVE]

#### Returns:
- socket `geometry`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Cone

```python
@staticmethod
def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON')
```



> Node: [Cone](GeometryNodeMeshCone.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)

#### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius_top: Float
- radius_bottom: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCone.webp)

#### Returns:
- tuple ('`mesh`', '`top`', '`bottom`', '`side`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Cube

```python
@classmethod
def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None)
```



> Node: [Cube](GeometryNodeMeshCube.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)

#### Args:
- size: Vector
- vertices_x: Integer
- vertices_y: Integer
- vertices_z: Integer

#### Returns:
- socket `mesh`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Cylinder

```python
@staticmethod
def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON')
```



> Node: [Cylinder](GeometryNodeMeshCylinder.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)

#### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCylinder.webp)

#### Returns:
- tuple ('`mesh`', '`top`', '`bottom`', '`side`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### FromCollection

```python
@classmethod
def FromCollection(cls, collection=None, separate_children
```

 Get the geometry from a collection



<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Grid

```python
@classmethod
def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None)
```



> Node: [Grid](GeometryNodeMeshGrid.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)

#### Args:
- size_x: Float
- size_y: Float
- vertices_x: Integer
- vertices_y: Integer

#### Returns:
- socket `mesh`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### IcoSphere

```python
@classmethod
def IcoSphere(cls, radius=None, subdivisions=None)
```



> Node: [Ico Sphere](GeometryNodeMeshIcoSphere.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)

#### Args:
- radius: Float
- subdivisions: Integer

#### Returns:
- socket `mesh`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
    
> Note: This method create a new input socket in the Group Input node. To get the **default** input geometry,
  use [Tree.input_geometry](#Tree.md#input_geometry) property.
    



<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### Line

```python
@classmethod
def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET')
```



> Node: [Mesh Line](GeometryNodeMeshLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- count: Integer
- resolution: Float
- start_location: Vector
- offset: Vector
- count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
- mode (str): 'OFFSET' in [OFFSET, END_POINTS]

#### Returns:
- socket `mesh`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### LineEndPoints

```python
@classmethod
def LineEndPoints(cls, count=None, start_location=None, end_location=None)
```



> Node: [Mesh Line](GeometryNodeMeshLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- count: Integer
- start_location: Vector
- end_location: Vector

#### Returns:
- socket `mesh`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### LineEndPointsResolution

```python
@classmethod
def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None)
```



> Node: [Mesh Line](GeometryNodeMeshLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- resolution: Float
- start_location: Vector
- end_location: Vector

#### Returns:
- socket `mesh`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### LineOffset

```python
@classmethod
def LineOffset(cls, count=None, start_location=None, offset=None)
```



> Node: [Mesh Line](GeometryNodeMeshLine.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)

#### Args:
- count: Integer
- start_location: Vector
- offset: Vector

#### Returns:
- socket `mesh`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### UVSphere

```python
@classmethod
def UVSphere(cls, segments=None, rings=None, radius=None)
```



> Node: [UV Sphere](GeometryNodeMeshUVSphere.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)

#### Args:
- segments: Integer
- rings: Integer
- radius: Float

#### Returns:
- socket `mesh`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute_node

```python
@staticmethod
def capture_attribute_node(geometry=None, value=None, data_type='FLOAT', domain='POINT')
```



> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- geometry: Geometry
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['geometry', 'attribute']






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_boolean

```python
@staticmethod
def random_boolean(probability=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_float

```python
@staticmethod
def random_float(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_integer

```python
@staticmethod
def random_integer(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_vector

```python
@staticmethod
def random_vector(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### attribute_statistic

```python
def attribute_statistic(self, selection=None, attribute=None, domain='POINT')
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- selection: Boolean
- attribute: ['Float', 'Vector']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### boolean_difference

```python
def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None)
```



> Node: [Mesh Boolean](GeometryNodeMeshBoolean.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

#### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Returns:
- socket `intersecting_edges`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### boolean_intersect

```python
def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None)
```



> Node: [Mesh Boolean](GeometryNodeMeshBoolean.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

#### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Returns:
- socket `intersecting_edges`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### boolean_union

```python
def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None)
```



> Node: [Mesh Boolean](GeometryNodeMeshBoolean.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)

#### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

#### Returns:
- socket `intersecting_edges`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute

```python
def capture_attribute(self, value=None, domain='POINT')
```



> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### corners_of_face

```python
def corners_of_face(self, face_index=None, weights=None, sort_index=None)
```



> Node: [Corners of Face](GeometryNodeCornersOfFace.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_face.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)

#### Args:
- face_index: Integer
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfFace.webp)

#### Returns:
- tuple ('`corner_index`', '`total`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### corners_of_vertex

```python
def corners_of_vertex(self, vertex_index=None, weights=None, sort_index=None)
```



> Node: [Corners of Vertex](GeometryNodeCornersOfVertex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)

#### Args:
- vertex_index: Integer
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfVertex.webp)

#### Returns:
- tuple ('`corner_index`', '`total`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete

```python
def delete(self, selection=None, domain='POINT', mode='ALL')
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete_all

```python
def delete_all(self, selection=None, domain='POINT')
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete_edges

```python
def delete_edges(self, selection=None, domain='POINT')
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete_faces

```python
def delete_faces(self, selection=None, domain='POINT')
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### distribute_points_on_faces

```python
def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM')
```



> Node: [Distribute Points on Faces](GeometryNodeDistributePointsOnFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)

#### Args:
- selection: Boolean
- distance_min: Float
- density_max: Float
- density: Float
- density_factor: Float
- seed: Integer
- distribute_method (str): 'RANDOM' in [RANDOM, POISSON]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

#### Returns:
- tuple ('`points`', '`normal`', '`rotation`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### dual_mesh

```python
def dual_mesh(self, keep_boundaries=None)
```



> Node: [Dual Mesh](GeometryNodeDualMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)

#### Args:
- keep_boundaries: Boolean

#### Returns:
- socket `dual_mesh` of class Mesh






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### duplicate

```python
def duplicate(self, selection=None, amount=None, domain='POINT')
```



> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- selection: Boolean
- amount: Integer
- domain (str): 'POINT' in [POINT, EDGE, FACE, SPLINE, INSTANCE]

#### Returns:
- socket `duplicate_index`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### edge_paths_to_curves

```python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None)
```



> Node: [Edge Paths to Curves](GeometryNodeEdgePathsToCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)

#### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

#### Returns:
- socket `curves` of class Curve






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### edge_paths_to_selection

```python
def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None)
```



> Node: [Edge Paths to Selection](GeometryNodeEdgePathsToSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html)

#### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

#### Returns:
- socket `selection`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### edges_of_corner

```python
def edges_of_corner(self, corner_index=None)
```



> Node: [Edges of Corner](GeometryNodeEdgesOfCorner.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)

#### Args:
- corner_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfCorner.webp)

#### Returns:
- tuple ('`next_edge_index`', '`previous_edge_index`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### edges_of_vertex

```python
def edges_of_vertex(self, vertex_index=None, weights=None, sort_index=None)
```



> Node: [Edges of Vertex](GeometryNodeEdgesOfVertex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)

#### Args:
- vertex_index: Integer
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfVertex.webp)

#### Returns:
- tuple ('`edge_index`', '`total`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### extrude

```python
def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES')
```



> Node: [Extrude Mesh](GeometryNodeExtrudeMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

#### Args:
- selection: Boolean
- offset: Vector
- offset_scale: Float
- individual: Boolean
- mode (str): 'FACES' in [VERTICES, EDGES, FACES]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

#### Returns:
- tuple ('`top`', '`side`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### face_is_planar

```python
def face_is_planar(self, threshold=None)
```



> Node: [Face is Planar](GeometryNodeInputMeshFaceIsPlanar.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)

#### Args:
- threshold: Float

#### Returns:
- socket `planar`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### face_of_corner

```python
def face_of_corner(self, corner_index=None)
```



> Node: [Face of Corner](GeometryNodeFaceOfCorner.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)

#### Args:
- corner_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFaceOfCorner.webp)

#### Returns:
- tuple ('`face_index`', '`index_in_face`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### face_set_boundaries

```python
def face_set_boundaries(self, face_set=None)
```



> Node: [Face Set Boundaries](GeometryNodeMeshFaceSetBoundaries.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)

#### Args:
- face_set: Integer

#### Returns:
- socket `boundary_edges`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### field_at_index

```python
def field_at_index(self, index=None, value=None, domain='POINT')
```



> Node: [Field at Index](GeometryNodeFieldAtIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

#### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### flip_faces

```python
def flip_faces(self, selection=None)
```



> Node: [Flip Faces](GeometryNodeFlipFaces.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)

#### Args:
- selection: Boolean

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```



> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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
    
```python
    
curves = curve * 10

# is equivalent to

curves = curve.duplicate(10, realize=False)
```




<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### interpolate_domain

```python
def interpolate_domain(self, value=None, domain='POINT')
```



> Node: [Interpolate Domain](GeometryNodeFieldOnDomain.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### is_shade_smooth

```python
def is_shade_smooth(self)
```



> Node: [Is Shade Smooth](GeometryNodeInputShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)

#### Returns:
- socket `smooth`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### join

```python
def join(*geometry)
```



> Node: [Join Geometry](GeometryNodeJoinGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `geometry`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material_selection

```python
def material_selection(self, material=None)
```



> Node: [Material Selection](GeometryNodeMaterialSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

#### Args:
- material: Material

#### Returns:
- socket `selection`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### merge_by_distance

```python
def merge_by_distance(self, selection=None, distance=None, mode='ALL')
```



> Node: [Merge by Distance](GeometryNodeMergeByDistance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

#### Args:
- selection: Boolean
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT')
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_boolean

```python
def named_boolean(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_color

```python
def named_color(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_float

```python
def named_float(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_integer

```python
def named_integer(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_vector

```python
def named_vector(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### offset_corner_in_face

```python
def offset_corner_in_face(self, corner_index=None, offset=None)
```



> Node: [Offset Corner in Face](GeometryNodeOffsetCornerInFace.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/offset_corner_in_face.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)

#### Args:
- corner_index: Integer
- offset: Integer

#### Returns:
- socket `corner_index`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### pack_uv_islands

```python
def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None)
```



> Node: [Pack UV Islands](GeometryNodeUVPackIslands.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)

#### Args:
- uv: Vector
- selection: Boolean
- margin: Float
- rotate: Boolean

#### Returns:
- socket `uv`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity

```python
def proximity(self, target=None, source_position=None, target_element='FACES')
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector
- target_element (str): 'FACES' in [POINTS, EDGES, FACES]

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_edges

```python
def proximity_edges(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_faces

```python
def proximity_faces(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_points

```python
def proximity_points(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast

```python
def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED')
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float
- mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_interpolated

```python
def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_nearest

```python
def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```



> Node: [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### replace_material

```python
def replace_material(self, old=None, new=None)
```



> Node: [Replace Material](GeometryNodeReplaceMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)

#### Args:
- old: Material
- new: Material

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_index

```python
def sample_index(self, value=None, index=None, clamp=False, domain='POINT')
```



> Node: [Sample Index](GeometryNodeSampleIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- socket `value`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_nearest

```python
def sample_nearest(self, sample_position=None, domain='POINT')
```



> Node: [Sample Nearest](GeometryNodeSampleNearest.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

#### Args:
- sample_position: Vector
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER]

#### Returns:
- socket `index`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_nearest_surface

```python
def sample_nearest_surface(self, value=None, sample_position=None)
```



> Node: [Sample Nearest Surface](GeometryNodeSampleNearestSurface.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_nearest_surface.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- sample_position: Vector

#### Returns:
- socket `value`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_uv_surface

```python
def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None)
```



> Node: [Sample UV Surface](GeometryNodeSampleUVSurface.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- source_uv_map: Vector
- sample_uv: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleUVSurface.webp)

#### Returns:
- tuple ('`value`', '`is_valid`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scale_elements

```python
def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM')
```



> Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]
- scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scale_single_axis

```python
def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE')
```



> Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### scale_uniform

```python
def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE')
```



> Node: [Scale Elements](GeometryNodeScaleElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- selection: Boolean
- scale: Float
- center: Vector
- domain (str): 'FACE' in [FACE, EDGE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate

```python
def separate(self, selection=None, domain='POINT')
```



> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- tuple ('`selection`', '`inverted`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_ID

```python
def set_ID(self, selection=None, ID=None)
```



> Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- selection: Boolean
- ID: Integer

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material

```python
def set_material(self, selection=None, material=None)
```



> Node: [Set Material](GeometryNodeSetMaterial.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

#### Args:
- selection: Boolean
- material: Material

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material_index

```python
def set_material_index(self, selection=None, material_index=None)
```



> Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

#### Args:
- selection: Boolean
- material_index: Integer

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_position

```python
def set_position(self, selection=None, position=None, offset=None)
```



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- selection: Boolean
- position: Vector
- offset: Vector

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_shade_smooth

```python
def set_shade_smooth(self, selection=None, shade_smooth=None)
```



> Node: [Set Shade Smooth](GeometryNodeSetShadeSmooth.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)

#### Args:
- selection: Boolean
- shade_smooth: Boolean

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### shortest_edge_paths

```python
def shortest_edge_paths(self, end_vertex=None, edge_cost=None)
```



> Node: [Shortest Edge Paths](GeometryNodeInputShortestEdgePaths.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)

#### Args:
- end_vertex: Boolean
- edge_cost: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputShortestEdgePaths.webp)

#### Returns:
- tuple ('`next_vertex_index`', '`total_cost`')






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### show_handles

```python
def show_handles(self)
```

 Generate a mesh and cloud points to visualize the control points and handles

#### Returns:
- Geometry: The geometry can be joined to the output
    
Example:
    
```python
curve = ... # Curve initialization

visu = curve.show_handles()

tree.output_geometry = curve + visu
```
    




<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### split_edges

```python
def split_edges(self, selection=None)
```



> Node: [Split Edges](GeometryNodeSplitEdges.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)

#### Args:
- selection: Boolean

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_boolean

```python
def store_named_boolean(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_color

```python
def store_named_color(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_float

```python
def store_named_float(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_integer

```python
def store_named_integer(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_vector

```python
def store_named_vector(self, name=None, value=None, domain='POINT')
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- domain (str): 'POINT' in [POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### subdivide

```python
def subdivide(self, level=None)
```



> Node: [Subdivide Mesh](GeometryNodeSubdivideMesh.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)

#### Args:
- level: Integer

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### subdivision_surface

```python
def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES')
```



> Node: [Subdivision Surface](GeometryNodeSubdivisionSurface.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)

#### Args:
- level: Integer
- edge_crease: Float
- vertex_crease: Float
- boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
- uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### switch

```python
def switch(self, switch=None, true=None)
```



> Node: [Switch](GeometryNodeSwitch.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)

#### Args:
- switch: Boolean
- true: Geometry

#### Returns:
- socket `output`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_curve

```python
def to_curve(self, selection=None)
```



> Node: [Mesh to Curve](GeometryNodeMeshToCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)

#### Args:
- selection: Boolean

#### Returns:
- socket `curve` of class Curve






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_instance

```python
def to_instance(*geometry)
```



> Node: [Geometry to Instance](GeometryNodeGeometryToInstance.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)

#### Args:
- geometry: <m>Geometry

#### Returns:
- socket `instances` of class Instances






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_points

```python
def to_points(self, selection=None, position=None, radius=None, mode='VERTICES')
```



> Node: [Mesh to Points](GeometryNodeMeshToPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)

#### Args:
- selection: Boolean
- position: Vector
- radius: Float
- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

#### Returns:
- socket `points` of class Points






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### to_volume

```python
def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT')
```



> Node: [Mesh to Volume](GeometryNodeMeshToVolume.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)

#### Args:
- density: Float
- voxel_size: Float
- voxel_amount: Float
- exterior_band_width: Float
- interior_band_width: Float
- fill_volume: Boolean
- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

#### Returns:
- socket `volume` of class Volume






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### transform

```python
def transform(self, translation=None, rotation=None, scale=None)
```



> Node: [Transform](GeometryNodeTransform.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/transform.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)

#### Args:
- translation: Vector
- rotation: Vector
- scale: Vector

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### triangulate

```python
def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL')
```



> Node: [Triangulate](GeometryNodeTriangulate.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)

#### Args:
- selection: Boolean
- minimum_vertices: Integer
- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

#### Returns:
- self






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### uv_unwrap

```python
def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED')
```



> Node: [UV Unwrap](GeometryNodeUVUnwrap.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)

#### Args:
- selection: Boolean
- seam: Boolean
- margin: Float
- fill_holes: Boolean
- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

#### Returns:
- socket `uv`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### vertex_of_corner

```python
def vertex_of_corner(self, corner_index=None)
```



> Node: [Vertex of Corner](GeometryNodeVertexOfCorner.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/vertex_of_corner.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)

#### Args:
- corner_index: Integer

#### Returns:
- socket `vertex_index`






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### view

```python
def view(self, value=None, domain='AUTO')
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']
- domain (str): 'AUTO' in [AUTO, POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets []






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### viewer

```python
def viewer(self, value=None, domain='AUTO')
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']
- domain (str): 'AUTO' in [AUTO, POINT, EDGE, FACE, CORNER, CURVE, INSTANCE]

#### Returns:
- node with sockets []






<sub>Go to [top](#class-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

