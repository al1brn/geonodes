# class Vertex

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

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def delete_all(self):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## delete_edges

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def delete_edges(self):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## delete_faces

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def delete_faces(self):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## domain_size

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def __len__(self):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Args:
<sub>Go to [top](#class-Vertex)</sub>

- geometry: Geometry
<sub>Go to [top](#class-Vertex)</sub>

- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## extrude

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def extrude(self, offset=None, offset_scale=None, individual=None):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Args:
<sub>Go to [top](#class-Vertex)</sub>

- offset: Vector
<sub>Go to [top](#class-Vertex)</sub>

- offset_scale: Float
<sub>Go to [top](#class-Vertex)</sub>

- individual: Boolean
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

- tuple ('top', 'side')
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## instance_on_points

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Args:
<sub>Go to [top](#class-Vertex)</sub>

- instance: Geometry
<sub>Go to [top](#class-Vertex)</sub>

- pick_instance: Boolean
<sub>Go to [top](#class-Vertex)</sub>

- instance_index: Integer
<sub>Go to [top](#class-Vertex)</sub>

- rotation: Vector
<sub>Go to [top](#class-Vertex)</sub>

- scale: Vector
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

  socket 'instances'<sub>Go to [top](#class-Vertex)</sub>

 of class Instances
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## merge_by_distance

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def merge_by_distance(self, distance=None, mode='ALL'):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/merge_by_distance.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Args:
<sub>Go to [top](#class-Vertex)</sub>

- distance: Float
<sub>Go to [top](#class-Vertex)</sub>

- mode (str): 'ALL' in [ALL, CONNECTED]
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## neighbors <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def neighbors(self):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

- node with sockets ['vertex_count', 'face_count']
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## neighbors_face_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def neighbors_face_count(self):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

  socket 'face_count'<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## neighbors_vertex_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def neighbors_vertex_count(self):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/vertex_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

  socket 'vertex_count'<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## to_points

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def to_points(self, position=None, radius=None, mode='VERTICES'):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Args:
<sub>Go to [top](#class-Vertex)</sub>

- position: Vector
<sub>Go to [top](#class-Vertex)</sub>

- radius: Float
<sub>Go to [top](#class-Vertex)</sub>

- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

  socket 'points'<sub>Go to [top](#class-Vertex)</sub>

 of class Points
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

## to_volume

<sub>Go to [top](#class-Vertex)</sub>

```python
<sub>Go to [top](#class-Vertex)</sub>

def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):

<sub>Go to [top](#class-Vertex)</sub>

```
<sub>Go to [top](#class-Vertex)</sub>

Node [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html) )

<sub>Go to [top](#class-Vertex)</sub>

### Args:
<sub>Go to [top](#class-Vertex)</sub>

- density: Float
<sub>Go to [top](#class-Vertex)</sub>

- voxel_size: Float
<sub>Go to [top](#class-Vertex)</sub>

- voxel_amount: Float
<sub>Go to [top](#class-Vertex)</sub>

- exterior_band_width: Float
<sub>Go to [top](#class-Vertex)</sub>

- interior_band_width: Float
<sub>Go to [top](#class-Vertex)</sub>

- fill_volume: Boolean
<sub>Go to [top](#class-Vertex)</sub>

- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

### Returns:

<sub>Go to [top](#class-Vertex)</sub>

  socket 'volume'<sub>Go to [top](#class-Vertex)</sub>

 of class Volume
<sub>Go to [top](#class-Vertex)</sub>


<sub>Go to [top](#class-Vertex)</sub>

