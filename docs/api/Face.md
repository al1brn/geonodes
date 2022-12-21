# class Face

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Properties

- [area](#area-property)
- [island](#island-property)
- [island_count](#island_count-property)
- [island_index](#island_index-property)
- [material](#material-property)
- [neighbors](#neighbors-property)
- [neighbors_face_count](#neighbors_face_count-property)
- [neighbors_vertex_count](#neighbors_vertex_count-property)
- [shade_smooth](#shade_smooth-property)



## Methods

- [delete_all](#delete_all)
- [delete_edges](#delete_edges)
- [delete_faces](#delete_faces)
- [distribute_points_poisson](#distribute_points_poisson)
- [distribute_points_random](#distribute_points_random)
- [domain_size](#domain_size)
- [extrude](#extrude)
- [face_set_boundaries](#face_set_boundaries)
- [flip](#flip)
- [is_planar](#is_planar)
- [pack_uv_islands](#pack_uv_islands)
- [scale_single_axis](#scale_single_axis)
- [scale_uniform](#scale_uniform)
- [set_material](#set_material)
- [set_shade_smooth](#set_shade_smooth)
- [triangulate](#triangulate)
- [uv_unwrap](#uv_unwrap)

## area <sub>*property*</sub>

```python
def area(self):

```
Node [Face Area](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html) )

#### Returns:
- node with sockets ['area']

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_all

```python
def delete_all(self):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

#### Returns:
- self

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_edges

```python
def delete_edges(self):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

#### Returns:
- self

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete_faces

```python
def delete_faces(self):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

#### Returns:
- self

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## distribute_points_poisson

```python
def distribute_points_poisson(self, distance_min=None, density_max=None, density_factor=None, seed=None):

```
Node [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html) )

#### Args:
- distance_min: Float
- density_max: Float
- density_factor: Float
- seed: Integer

#### Returns:
- tuple ('`points`', '`normal`', '`rotation`')

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## distribute_points_random

```python
def distribute_points_random(self, density=None, seed=None):

```
Node [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html) )

#### Args:
- density: Float
- seed: Integer

#### Returns:
- tuple ('`points`', '`normal`', '`rotation`')

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## domain_size

```python
def __len__(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

#### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

#### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## extrude

```python
def extrude(self, offset=None, offset_scale=None, individual=None):

```
Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html) )

#### Args:
- offset: Vector
- offset_scale: Float
- individual: Boolean

#### Returns:
- tuple ('`top`', '`side`')

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## face_set_boundaries

```python
def face_set_boundaries(self):

```
Node [Face Set Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html) )

#### Returns:
- socket `boundary_edges`

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## flip

```python
def flip(self):

```
Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html) )

#### Returns:
- self

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## is_planar

```python
def is_planar(self, threshold=None):

```
Node [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html) )

#### Args:
- threshold: Float

#### Returns:
- socket `planar`

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## island <sub>*property*</sub>

```python
def island(self):

```
Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

#### Returns:
- node with sockets ['island_index', 'island_count']

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## island_count <sub>*property*</sub>

```python
def island_count(self):

```
Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

#### Returns:
- socket `island_count`

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## island_index <sub>*property*</sub>

```python
def island_index(self):

```
Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

#### Returns:
- socket `island_index`

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## material <sub>*property*</sub>

```python
def material(self):

```
Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

'material' is a write only property.
Raise an exception if attempt to read.


<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## material <sub>*etter*</sub>

```python
def material(self, attr_value):

```
Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

Node implemented as property setter.

#### Args:
- attr_value: material


<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## neighbors <sub>*property*</sub>

```python
def neighbors(self):

```
Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html) )

#### Returns:
- node with sockets ['vertex_count', 'face_count']

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## neighbors_face_count <sub>*property*</sub>

```python
def neighbors_face_count(self):

```
Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html) )

#### Returns:
- socket `face_count`

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## neighbors_vertex_count <sub>*property*</sub>

```python
def neighbors_vertex_count(self):

```
Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html) )

#### Returns:
- socket `vertex_count`

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## pack_uv_islands

```python
def pack_uv_islands(self, uv=None, margin=None, rotate=None):

```
Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html) )

#### Args:
- uv: Vector
- margin: Float
- rotate: Boolean

#### Returns:
- socket `uv`

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale_single_axis

```python
def scale_single_axis(self, scale=None, center=None, axis=None):

```
Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

#### Args:
- scale: Float
- center: Vector
- axis: Vector

#### Returns:
- self

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## scale_uniform

```python
def scale_uniform(self, scale=None, center=None):

```
Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

#### Args:
- scale: Float
- center: Vector

#### Returns:
- self

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_material

```python
def set_material(self, material=None):

```
Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

#### Args:
- material: Material

#### Returns:
- self

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_shade_smooth

```python
def set_shade_smooth(self, shade_smooth=None):

```
Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html) )

#### Args:
- shade_smooth: Boolean

#### Returns:
- self

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## shade_smooth <sub>*property*</sub>

```python
def shade_smooth(self):

```
Node [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html) )

#### Returns:
- socket `smooth`

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## shade_smooth <sub>*etter*</sub>

```python
def shade_smooth(self, attr_value):

```
Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html) )

Node implemented as property setter.

#### Args:
- attr_value: shade_smooth


<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## triangulate

```python
def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

```
Node [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html) )

#### Args:
- minimum_vertices: Integer
- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

#### Returns:
- self

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## uv_unwrap

```python
def uv_unwrap(self, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):

```
Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html) )

#### Args:
- seam: Boolean
- margin: Float
- fill_holes: Boolean
- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

#### Returns:
- socket `uv`

<sub>Go to [top](#class-Face) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

