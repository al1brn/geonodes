# class Edge

## Properties

- [angle](#angle-property)
- [neighbors](#neighbors-property)
- [signed_angle](#signed_angle-property)
- [unsigned_angle](#unsigned_angle-property)
- [vertices](#vertices-property)
- [vertices_index](#vertices_index-property)
- [vertices_position](#vertices_position-property)



## Methods

- [delete_all](#delete_all)
- [delete_edges](#delete_edges)
- [delete_faces](#delete_faces)
- [domain_size](#domain_size)
- [edge_paths_to_curves](#edge_paths_to_curves)
- [extrude](#extrude)
- [scale_single_axis](#scale_single_axis)
- [scale_uniform](#scale_uniform)
- [split](#split)
- [to_curve](#to_curve)

## angle <span style="color:blue">*property*</span>

```python
def angle(self):

```
Node [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html) )

### Returns:

- node with sockets ['unsigned_angle', 'signed_angle']

<sub>Go to [top](#class-Edge)</sub>

## delete_all

```python
def delete_all(self):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Returns:

- node with sockets ['geometry']

<sub>Go to [top](#class-Edge)</sub>

## delete_edges

```python
def delete_edges(self):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Returns:

- node with sockets ['geometry']

<sub>Go to [top](#class-Edge)</sub>

## delete_faces

```python
def delete_faces(self):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Returns:

- node with sockets ['geometry']

<sub>Go to [top](#class-Edge)</sub>

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

<sub>Go to [top](#class-Edge)</sub>

## edge_paths_to_curves

```python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):

```
Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html) )

### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

### Returns:

  socket 'curves' of class Curve

<sub>Go to [top](#class-Edge)</sub>

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

- tuple ('top', 'side')

<sub>Go to [top](#class-Edge)</sub>

## neighbors <span style="color:blue">*property*</span>

```python
def neighbors(self):

```
Node [Edge Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html) )

### Returns:

  socket 'face_count'

<sub>Go to [top](#class-Edge)</sub>

## scale_single_axis

```python
def scale_single_axis(self, scale=None, center=None, axis=None):

```
Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

### Args:
- scale: Float
- center: Vector
- axis: Vector

### Returns:

- node with sockets ['geometry']

<sub>Go to [top](#class-Edge)</sub>

## scale_uniform

```python
def scale_uniform(self, scale=None, center=None):

```
Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

### Args:
- scale: Float
- center: Vector

### Returns:

- node with sockets ['geometry']

<sub>Go to [top](#class-Edge)</sub>

## signed_angle <span style="color:blue">*property*</span>

```python
def signed_angle(self):

```
Node [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html) )

### Returns:

  socket 'signed_angle'

<sub>Go to [top](#class-Edge)</sub>

## split

```python
def split(self):

```
Node [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html) )

### Returns:

- node with sockets ['mesh']

<sub>Go to [top](#class-Edge)</sub>

## to_curve

```python
def to_curve(self):

```
Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html) )

### Returns:

  socket 'curve' of class Curve

<sub>Go to [top](#class-Edge)</sub>

## unsigned_angle <span style="color:blue">*property*</span>

```python
def unsigned_angle(self):

```
Node [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html) )

### Returns:

  socket 'unsigned_angle'

<sub>Go to [top](#class-Edge)</sub>

## vertices <span style="color:blue">*property*</span>

```python
def vertices(self):

```
Node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html) )

### Returns:

- node with sockets ['vertex_index_1', 'vertex_index_2', 'position_1', 'position_2']

<sub>Go to [top](#class-Edge)</sub>

## vertices_index <span style="color:blue">*property*</span>

```python
def vertices_index(self):

```
Node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html) )

### Returns:

- tuple ('vertex_index_1', 'vertex_index_2')

<sub>Go to [top](#class-Edge)</sub>

## vertices_position <span style="color:blue">*property*</span>

```python
def vertices_position(self):

```
Node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html) )

### Returns:

- tuple ('position_1', 'position_2')

<sub>Go to [top](#class-Edge)</sub>

