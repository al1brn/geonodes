# class Corner

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


# Class Corner

Face corner domain


## edges

Edges of corner

Node :class:`~geonodes.nodes.nodes.EdgesOfCorner`

Args:
  index: Int
  
Returns:
  Node (next_edge_index, previous_edge_index)
  
  
  

## face_of_corner

Face of corner

Node :class:`~geonodes.nodes.nodes.FaceOfCorner`

Returns:
  Node (face_index, index_in_face)
  
  
  

## offset_in_face_index

Face of corner

Node :class:`~geonodes.nodes.nodes.OffsetCornerInFace`

Args:
  offset: INt
  
Returns:
  Int
  
  

## vertex_index

Vertex of corner

Node :class:`~geonodes.nodes.nodes.VertexOfCorner`

Returns:
  Int
  
  
  > see [examples](#examples)

## Properties

- [count](#count-property)
- [face_index](#face_index-property)
- [index_in_face](#index_in_face-property)
- [next_vertex](#next_vertex-property)
- [previous_vertex](#previous_vertex-property)
- [vertex_index](#vertex_index-property)



## Methods

- [edges](#edges)
- [face](#face)
- [offset_in_face](#offset_in_face)
- [sample_nearest](#sample_nearest)

## count <sub>*property*</sub>

```python
def count(self, geometry=None):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `face_corner_count`

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## edges

```python
def edges(self):

```
> Node: [Edges of Corner](GeometryNodeEdgesOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfCorner.webp)

#### Returns:
- tuple ('`next_edge_index`', '`previous_edge_index`')

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## face

```python
def face(self):

```
> Node: [Face of Corner](GeometryNodeFaceOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFaceOfCorner.webp)

#### Returns:
- tuple ('`face_index`', '`index_in_face`')

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## face_index <sub>*property*</sub>

```python
def face_index(self):

```
> Node: [Face of Corner](GeometryNodeFaceOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)

#### Returns:
- socket `face_index`

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## index_in_face <sub>*property*</sub>

```python
def index_in_face(self):

```
> Node: [Face of Corner](GeometryNodeFaceOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/face_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)

#### Returns:
- socket `index_in_face`

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## next_vertex <sub>*property*</sub>

```python
def next_vertex(self):

```
> Node: [Edges of Corner](GeometryNodeEdgesOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)

#### Returns:
- socket `next_edge_index`

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## offset_in_face

```python
def offset_in_face(self, offset=None):

```
> Node: [Offset Corner in Face](GeometryNodeOffsetCornerInFace.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/offset_corner_in_face.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)

#### Args:
- offset: Integer

#### Returns:
- socket `corner_index`

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## previous_vertex <sub>*property*</sub>

```python
def previous_vertex(self):

```
> Node: [Edges of Corner](GeometryNodeEdgesOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/edges_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)

#### Returns:
- socket `previous_edge_index`

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sample_nearest

```python
def sample_nearest(self, sample_position=None):

```
> Node: [Sample Nearest](GeometryNodeSampleNearest.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)

#### Args:
- sample_position: Vector

#### Returns:
- socket `index`

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## vertex_index <sub>*property*</sub>

```python
def vertex_index(self):

```
> Node: [Vertex of Corner](GeometryNodeVertexOfCorner.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_topology/vertex_of_corner.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)

#### Returns:
- socket `vertex_index`

<sub>Go to [top](#class-Corner) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>


# Class Corner

Face corner domain


## edges

Edges of corner

Node :class:`~geonodes.nodes.nodes.EdgesOfCorner`

Args:
  index: Int
  
Returns:
  Node (next_edge_index, previous_edge_index)
  
  
  

## face_of_corner

Face of corner

Node :class:`~geonodes.nodes.nodes.FaceOfCorner`

Returns:
  Node (face_index, index_in_face)
  
  
  

## offset_in_face_index

Face of corner

Node :class:`~geonodes.nodes.nodes.OffsetCornerInFace`

Args:
  offset: INt
  
Returns:
  Int
  
  

## vertex_index

Vertex of corner

Node :class:`~geonodes.nodes.nodes.VertexOfCorner`

Returns:
  Int
  
  
  