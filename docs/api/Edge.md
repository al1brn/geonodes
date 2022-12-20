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

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def angle(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- node with sockets ['unsigned_angle', 'signed_angle']
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## delete_all

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def delete_all(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## delete_edges

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def delete_edges(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## delete_faces

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def delete_faces(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## domain_size

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def __len__(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Edge)</sub>### Args:
<sub>Go to [top](#class-Edge)</sub>- geometry: Geometry
<sub>Go to [top](#class-Edge)</sub>- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## edge_paths_to_curves

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html) )

<sub>Go to [top](#class-Edge)</sub>### Args:
<sub>Go to [top](#class-Edge)</sub>- start_vertices: Boolean
<sub>Go to [top](#class-Edge)</sub>- next_vertex_index: Integer
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>  socket 'curves'<sub>Go to [top](#class-Edge)</sub> of class Curve
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## extrude

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def extrude(self, offset=None, offset_scale=None, individual=None):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html) )

<sub>Go to [top](#class-Edge)</sub>### Args:
<sub>Go to [top](#class-Edge)</sub>- offset: Vector
<sub>Go to [top](#class-Edge)</sub>- offset_scale: Float
<sub>Go to [top](#class-Edge)</sub>- individual: Boolean
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- tuple ('top', 'side')
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## neighbors <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def neighbors(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Edge Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>  socket 'face_count'<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## scale_single_axis

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def scale_single_axis(self, scale=None, center=None, axis=None):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

<sub>Go to [top](#class-Edge)</sub>### Args:
<sub>Go to [top](#class-Edge)</sub>- scale: Float
<sub>Go to [top](#class-Edge)</sub>- center: Vector
<sub>Go to [top](#class-Edge)</sub>- axis: Vector
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## scale_uniform

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def scale_uniform(self, scale=None, center=None):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

<sub>Go to [top](#class-Edge)</sub>### Args:
<sub>Go to [top](#class-Edge)</sub>- scale: Float
<sub>Go to [top](#class-Edge)</sub>- center: Vector
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- node with sockets ['geometry']
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## signed_angle <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def signed_angle(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>  socket 'signed_angle'<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## split

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def split(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- node with sockets ['mesh']
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## to_curve

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def to_curve(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>  socket 'curve'<sub>Go to [top](#class-Edge)</sub> of class Curve
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## unsigned_angle <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def unsigned_angle(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>  socket 'unsigned_angle'<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## vertices <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def vertices(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- node with sockets ['vertex_index_1', 'vertex_index_2', 'position_1', 'position_2']
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## vertices_index <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def vertices_index(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- tuple ('vertex_index_1', 'vertex_index_2')
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>## vertices_position <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Edge)</sub>```python
<sub>Go to [top](#class-Edge)</sub>def vertices_position(self):

<sub>Go to [top](#class-Edge)</sub>```
<sub>Go to [top](#class-Edge)</sub>Node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html) )

<sub>Go to [top](#class-Edge)</sub>### Returns:

<sub>Go to [top](#class-Edge)</sub>- tuple ('position_1', 'position_2')
<sub>Go to [top](#class-Edge)</sub>
<sub>Go to [top](#class-Edge)</sub>