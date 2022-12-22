# class Edge

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Properties

- [angle](#angle-property)
- [count](#count-property)
- [neighbors](#neighbors-property)
- [signed_angle](#signed_angle-property)
- [unsigned_angle](#unsigned_angle-property)
- [vertices](#vertices-property)
- [vertices_index](#vertices_index-property)
- [vertices_position](#vertices_position-property)



## Methods

- [delete](#delete)
- [delete_all](#delete_all)
- [delete_edges](#delete_edges)
- [delete_faces](#delete_faces)
- [duplicate](#duplicate)
- [edge_paths_to_curves](#edge_paths_to_curves)
- [extrude](#extrude)
- [proximity](#proximity)
- [sample_nearest](#sample_nearest)
- [scale_single_axis](#scale_single_axis)
- [scale_uniform](#scale_uniform)
- [separate](#separate)
- [split](#split)
- [to_curve](#to_curve)

## angle <sub>*property*</sub>

```python
def angle(self):

```
> Node: [Edge Angle](GeometryNodeInputMeshEdgeAngle.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

#### Returns:
- node with sockets ['unsigned_angle', 'signed_angle']

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## count <sub>*property*</sub>

```python
def count(self, geometry=None):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `edge_count`

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete

```python
def delete(self, mode='ALL'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_all

```python
def delete_all(self):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- self

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_edges

```python
def delete_edges(self):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- self

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_faces

```python
def delete_faces(self):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Returns:
- self

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## duplicate

```python
def duplicate(self, amount=None):

```
> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edge_paths_to_curves

```python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):

```
> Node: [Edge Paths to Curves](GeometryNodeEdgePathsToCurves.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)

#### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

#### Returns:
- socket `curves` of class Curve

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## neighbors <sub>*property*</sub>

```python
def neighbors(self):

```
> Node: [Edge Neighbors](GeometryNodeInputMeshEdgeNeighbors.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_neighbors.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)

#### Returns:
- socket `face_count`

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sample_nearest

```python
def sample_nearest(self, sample_position=None):

```
> Node: [Sample Nearest](GeometryNodeSampleNearest.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

#### Args:
- sample_position: Vector

#### Returns:
- socket `index`

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale_single_axis

```python
def scale_single_axis(self, scale=None, center=None, axis=None):

```
> Node: [Scale Elements](GeometryNodeScaleElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- scale: Float
- center: Vector
- axis: Vector

#### Returns:
- self

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale_uniform

```python
def scale_uniform(self, scale=None, center=None):

```
> Node: [Scale Elements](GeometryNodeScaleElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)

#### Args:
- scale: Float
- center: Vector

#### Returns:
- self

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

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

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## signed_angle <sub>*property*</sub>

```python
def signed_angle(self):

```
> Node: [Edge Angle](GeometryNodeInputMeshEdgeAngle.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

#### Returns:
- socket `signed_angle`

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## split

```python
def split(self):

```
> Node: [Split Edges](GeometryNodeSplitEdges.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)

#### Returns:
- self

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## to_curve

```python
def to_curve(self):

```
> Node: [Mesh to Curve](GeometryNodeMeshToCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)

#### Returns:
- socket `curve` of class Curve

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## unsigned_angle <sub>*property*</sub>

```python
def unsigned_angle(self):

```
> Node: [Edge Angle](GeometryNodeInputMeshEdgeAngle.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)

#### Returns:
- socket `unsigned_angle`

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## vertices <sub>*property*</sub>

```python
def vertices(self):

```
> Node: [Edge Vertices](GeometryNodeInputMeshEdgeVertices.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

#### Returns:
- node with sockets ['vertex_index_1', 'vertex_index_2', 'position_1', 'position_2']

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## vertices_index <sub>*property*</sub>

```python
def vertices_index(self):

```
> Node: [Edge Vertices](GeometryNodeInputMeshEdgeVertices.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeVertices.webp)

#### Returns:
- tuple ('`vertex_index_1`', '`vertex_index_2`')

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## vertices_position <sub>*property*</sub>

```python
def vertices_position(self):

```
> Node: [Edge Vertices](GeometryNodeInputMeshEdgeVertices.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_vertices.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeVertices.webp)

#### Returns:
- tuple ('`position_1`', '`position_2`')

<sub>Go to [top](#class-Edge) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

