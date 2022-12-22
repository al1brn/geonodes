# class Vertex

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


# Class Vertex

**Vertex** is a [Domain](Domain.md) belonging to [Mesh](Mesh.md).
- Node domain value: *'POINT'*
- [Mesh](Mesh.md) property: `verts`



Detai


vertex: the point domain of meshes


## neighbors

Neighbors

Returns:
  Node *VertexNeighbors*
  
- getter: :class:`~geonodes.nodes.nodes.VertexNeighbors`
- setter: read only
  
  
  

## neighbors_vertices

Neighbors vertices attribute

Returns:
  Integer: The output socket *vertices* of the *VertexNeighbors* node.
  
- getter: :class:`~geonodes.nodes.nodes.VertexNeighbors`
- setter: read only
  
  
  

## neighbors_faces

Neighbors faces attribute

Returns:
  Integer: The output socket *faces* of the *VertexNeighbors* node.
  
- getter: :class:`~geonodes.nodes.nodes.VertexNeighbors`
- setter: read only
  
  
  

## shortest_edge_paths

Shortest edge paths

Returns:
  tuple next_vertex_index, total_cost
  
- getter: :class:`~geonodes.nodes.nodes.ShortestEdgePaths`
- setter: read only
  
  
  

## edge_paths_to_curves

Shortest edge paths

Returns:
  Node Curves
  
- getter: :class:`~geonodes.nodes.nodes.ShortestEdgePaths`
- setter: read only
  
  
  

## edge_paths_to_selection

edges paths to selectin

Returns:
  Boolean
  
- getter: :class:`~geonodes.nodes.nodes.EdgePathsToSelection`
- setter: read only
  
  
  

## merge

Merge vertices by distance.

Node :class:`~geonodes.nodes.nodes.MergeByDistance`

Args:
  distance (Float): The merge distance
  mode (str): str (default = 'ALL') in ('ALL', 'CONNECTED')        
  
Returns:
  self
  
.. code-block:: python

  mesh.verts().merge()
  
  

## merge_connected

Merge connected vertices by distance.

call :func:`merge` with mode = 'CONNECTED'

Args:
  distance (Float): The merge distance
  
Returns:
  self
  
.. code-block:: python

  mesh.verts().merge_connected()
  
  

## weighted_corners

Corners or Vertex

Node :class:`~geonodes.nodes.nodes.CornersOfVertex`

Args:
  weights: Float
  
Returns:
  WeightedList
  
  

## weighted_edges

Edges or Vertex

Node :class:`~geonodes.nodes.nodes.EdgesOfVertex`

Args:
  weights: Float
  
Returns:
  WeightedList
  
  
  
## Properties

- [count](#count-property)
- [neighbors](#neighbors-property)
- [neighbors_face_count](#neighbors_face_count-property)
- [neighbors_vertex_count](#neighbors_vertex_count-property)



## Methods

- [corners](#corners)
- [corners_index](#corners_index)
- [corners_total](#corners_total)
- [delete](#delete)
- [delete_all](#delete_all)
- [delete_edges](#delete_edges)
- [delete_faces](#delete_faces)
- [duplicate](#duplicate)
- [edges](#edges)
- [edges_index](#edges_index)
- [edges_total](#edges_total)
- [extrude](#extrude)
- [instance_on_points](#instance_on_points)
- [merge_by_distance](#merge_by_distance)
- [proximity](#proximity)
- [sample_nearest](#sample_nearest)
- [separate](#separate)
- [to_points](#to_points)
- [to_volume](#to_volume)

## corners

```python
def corners(self, weights=None, sort_index=None):

```
> Node: [Corners of Vertex](GeometryNodeCornersOfVertex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)

#### Args:
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfVertex.webp)

#### Returns:
- tuple ('`corner_index`', '`total`')

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## corners_index

```python
def corners_index(self, weights=None, sort_index=None):

```
> Node: [Corners of Vertex](GeometryNodeCornersOfVertex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)

#### Args:
- weights: Float
- sort_index: Integer

#### Returns:
- socket `corner_index`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## corners_total

```python
def corners_total(self, weights=None, sort_index=None):

```
> Node: [Corners of Vertex](GeometryNodeCornersOfVertex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/corners_of_vertex.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)

#### Args:
- weights: Float
- sort_index: Integer

#### Returns:
- socket `total`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## count <sub>*property*</sub>

```python
def count(self, geometry=None):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete

```python
def delete(self, mode='ALL'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_all

```python
def delete_all(self):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- self

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_edges

```python
def delete_edges(self):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- self

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_faces

```python
def delete_faces(self):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- self

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## duplicate

```python
def duplicate(self, amount=None):

```
> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edges

```python
def edges(self, weights=None, sort_index=None):

```
> Node: [Edges of Vertex](GeometryNodeEdgesOfVertex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)

#### Args:
- weights: Float
- sort_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfVertex.webp)

#### Returns:
- tuple ('`edge_index`', '`total`')

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edges_index

```python
def edges_index(self, weights=None, sort_index=None):

```
> Node: [Edges of Vertex](GeometryNodeEdgesOfVertex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)

#### Args:
- weights: Float
- sort_index: Integer

#### Returns:
- socket `edge_index`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edges_total

```python
def edges_total(self, weights=None, sort_index=None):

```
> Node: [Edges of Vertex](GeometryNodeEdgesOfVertex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_vertex.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)

#### Args:
- weights: Float
- sort_index: Integer

#### Returns:
- socket `total`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## extrude

```python
def extrude(self, offset=None, offset_scale=None, individual=None):

```
> Node: [Extrude Mesh](GeometryNodeExtrudeMesh.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)

#### Args:
- offset: Vector
- offset_scale: Float
- individual: Boolean

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

#### Returns:
- tuple ('`top`', '`side`')

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## instance_on_points

```python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances` of class Instances

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## merge_by_distance

```python
def merge_by_distance(self, distance=None, mode='ALL'):

```
> Node: [Merge by Distance](GeometryNodeMergeByDistance.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)

#### Args:
- distance: Float
- mode (str): 'ALL' in [ALL, CONNECTED]

#### Returns:
- self

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## neighbors <sub>*property*</sub>

```python
def neighbors(self):

```
> Node: [Vertex Neighbors](GeometryNodeInputMeshVertexNeighbors.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)

#### Returns:
- node with sockets ['vertex_count', 'face_count']

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## neighbors_face_count <sub>*property*</sub>

```python
def neighbors_face_count(self):

```
> Node: [Vertex Neighbors](GeometryNodeInputMeshVertexNeighbors.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)

#### Returns:
- socket `face_count`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## neighbors_vertex_count <sub>*property*</sub>

```python
def neighbors_vertex_count(self):

```
> Node: [Vertex Neighbors](GeometryNodeInputMeshVertexNeighbors.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)

#### Returns:
- socket `vertex_count`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## proximity

```python
def proximity(self, target=None, source_position=None):

```
> Node: [Geometry Proximity](GeometryNodeProximity.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sample_nearest

```python
def sample_nearest(self, sample_position=None):

```
> Node: [Sample Nearest](GeometryNodeSampleNearest.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

#### Args:
- sample_position: Vector

#### Returns:
- socket `index`

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## separate

```python
def separate(self, geometry=None):

```
> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- geometry: Geometry

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- tuple ('`selection`', '`inverted`')

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_points

```python
def to_points(self, position=None, radius=None, mode='VERTICES'):

```
> Node: [Mesh to Points](GeometryNodeMeshToPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)

#### Args:
- position: Vector
- radius: Float
- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

#### Returns:
- socket `points` of class Points

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_volume

```python
def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):

```
> Node: [Mesh to Volume](GeometryNodeMeshToVolume.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)

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

<sub>Go to [top](#class-Vertex) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

