# class Vertex

> [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)

## Properties

- [neighbors](#neighbors-property)
- [neighbors_face_count](#neighbors_face_count-property)
- [neighbors_vertex_count](#neighbors_vertex_count-property)



## Methods

- [delete_all](#delete_all)
- [delete_edges](#delete_edges)
- [delete_faces](#delete_faces)
- [domain_size](#domain_size)
- [extrude](#extrude)
- [instance_on_points](#instance_on_points)
- [merge_by_distance](#merge_by_distance)
- [to_points](#to_points)
- [to_volume](#to_volume)

## delete_all

```python
def delete_all(self):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Returns:
- self

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## delete_edges

```python
def delete_edges(self):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Returns:
- self

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## delete_faces

```python
def delete_faces(self):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Returns:
- self

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## domain_size

```python
def __len__(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## extrude

```python
def extrude(self, offset=None, offset_scale=None, individual=None):

```
Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html) )

### Args:
- offset: Vector
- offset_scale: Float
- individual: Boolean

### Returns:
- tuple ('`top`', '`side`')

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## instance_on_points

```python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:
- socket `instances` of class Instances

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## merge_by_distance

```python
def merge_by_distance(self, distance=None, mode='ALL'):

```
Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html) )

### Args:
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

### Returns:
- self

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## neighbors <sub>*property*</sub>

```python
def neighbors(self):

```
Node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html) )

### Returns:
- node with sockets ['vertex_count', 'face_count']

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## neighbors_face_count <sub>*property*</sub>

```python
def neighbors_face_count(self):

```
Node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html) )

### Returns:
- socket `face_count`

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## neighbors_vertex_count <sub>*property*</sub>

```python
def neighbors_vertex_count(self):

```
Node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html) )

### Returns:
- socket `vertex_count`

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## to_points

```python
def to_points(self, position=None, radius=None, mode='VERTICES'):

```
Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html) )

### Args:
- position: Vector
- radius: Float
- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

### Returns:
- socket `points` of class Points

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## to_volume

```python
def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):

```
Node [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html) )

### Args:
- density: Float
- voxel_size: Float
- voxel_amount: Float
- exterior_band_width: Float
- interior_band_width: Float
- fill_volume: Boolean
- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]

### Returns:
- socket `volume` of class Volume

<sub>Go to [top](#class-Vertex) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

