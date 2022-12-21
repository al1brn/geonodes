# class Mesh

> [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)

## Properties

- [corner_count](#corner_count-property)
- [domain_size](#domain_size-property)
- [edge_count](#edge_count-property)
- [face_count](#face_count-property)
- [island](#island-property)
- [island_count](#island_count-property)
- [island_index](#island_index-property)
- [point_count](#point_count-property)

## Class methods

- [Circle](#Circle-classmethod)
- [Circle](#Circle-classmethod)
- [Cube](#Cube-classmethod)
- [Grid](#Grid-classmethod)
- [IcoSphere](#IcoSphere-classmethod)
- [Line](#Line-classmethod)
- [LineEndPoints](#LineEndPoints-classmethod)
- [LineEndPointsResolution](#LineEndPointsResolution-classmethod)
- [LineOffset](#LineOffset-classmethod)
- [LineOffsetResolution](#LineOffsetResolution-classmethod)

## Static methods

- [Cone](#Cone-staticmethod)
- [Cylinder](#Cylinder-staticmethod)

## Methods

- [boolean_difference](#boolean_difference)
- [boolean_intersect](#boolean_intersect)
- [boolean_union](#boolean_union)
- [delete_all](#delete_all)
- [delete_edges](#delete_edges)
- [delete_faces](#delete_faces)
- [distribute_points_on_faces](#distribute_points_on_faces)
- [dual_mesh](#dual_mesh)
- [edge_paths_to_curves](#edge_paths_to_curves)
- [edge_paths_to_selection](#edge_paths_to_selection)
- [extrude](#extrude)
- [face_is_planar](#face_is_planar)
- [face_set_boundaries](#face_set_boundaries)
- [flip_faces](#flip_faces)
- [instance_on_points](#instance_on_points)
- [is_shade_smooth](#is_shade_smooth)
- [pack_uv_islands](#pack_uv_islands)
- [sample_nearest_surface](#sample_nearest_surface)
- [sample_uv_surface](#sample_uv_surface)
- [scale_elements](#scale_elements)
- [scale_single_axis](#scale_single_axis)
- [scale_uniform](#scale_uniform)
- [set_shade_smooth](#set_shade_smooth)
- [shortest_edge_paths](#shortest_edge_paths)
- [split_edges](#split_edges)
- [subdivide](#subdivide)
- [subdivision_surface](#subdivision_surface)
- [to_curve](#to_curve)
- [to_points](#to_points)
- [to_volume](#to_volume)
- [triangulate](#triangulate)
- [uv_unwrap](#uv_unwrap)

## Circle <sub>*classmethod*</sub>

```python
def Circle(cls, vertices=None, radius=None, fill_type='NONE'):

```
Node [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html) )

### Args:
- vertices: Integer
- radius: Float
- fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## Circle <sub>*classmethod*</sub>

```python
def Circle(cls, segments=None, rings=None, radius=None):

```
Node [UV Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html) )

### Args:
- segments: Integer
- rings: Integer
- radius: Float

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## Cone <sub>*staticmethod*</sub>

```python
def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):

```
Node [Cone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html) )

### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius_top: Float
- radius_bottom: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

### Returns:
- tuple ('`mesh`', '`top`', '`bottom`', '`side`')

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## Cube <sub>*classmethod*</sub>

```python
def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):

```
Node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html) )

### Args:
- size: Vector
- vertices_x: Integer
- vertices_y: Integer
- vertices_z: Integer

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## Cylinder <sub>*staticmethod*</sub>

```python
def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):

```
Node [Cylinder](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html) )

### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

### Returns:
- tuple ('`mesh`', '`top`', '`bottom`', '`side`')

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## Grid <sub>*classmethod*</sub>

```python
def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):

```
Node [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html) )

### Args:
- size_x: Float
- size_y: Float
- vertices_x: Integer
- vertices_y: Integer

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## IcoSphere <sub>*classmethod*</sub>

```python
def IcoSphere(cls, radius=None, subdivisions=None):

```
Node [Ico Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html) )

### Args:
- radius: Float
- subdivisions: Integer

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## Line <sub>*classmethod*</sub>

```python
def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):

```
Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

### Args:
- count: Integer
- resolution: Float
- start_location: Vector
- offset: Vector
- count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
- mode (str): 'OFFSET' in [OFFSET, END_POINTS]

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## LineEndPoints <sub>*classmethod*</sub>

```python
def LineEndPoints(cls, count=None, start_location=None, end_location=None):

```
Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

### Args:
- count: Integer
- start_location: Vector
- end_location: Vector

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## LineEndPointsResolution <sub>*classmethod*</sub>

```python
def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None):

```
Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

### Args:
- resolution: Float
- start_location: Vector
- end_location: Vector

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## LineOffset <sub>*classmethod*</sub>

```python
def LineOffset(cls, count=None, start_location=None, offset=None):

```
Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

### Args:
- count: Integer
- start_location: Vector
- offset: Vector

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## LineOffsetResolution <sub>*classmethod*</sub>

```python
def LineOffsetResolution(cls, resolution=None, start_location=None, offset=None):

```
Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

### Args:
- resolution: Float
- start_location: Vector
- offset: Vector

### Returns:
- socket `mesh`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## boolean_difference

```python
def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):

```
Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html) )

### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

### Returns:
- socket `intersecting_edges`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## boolean_intersect

```python
def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None):

```
Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html) )

### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

### Returns:
- socket `intersecting_edges`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## boolean_union

```python
def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None):

```
Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html) )

### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

### Returns:
- socket `intersecting_edges`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## corner_count <sub>*property*</sub>

```python
def corner_count(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Returns:
- socket `face_corner_count`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## delete_all

```python
def delete_all(self, selection=None, domain='POINT'):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## delete_edges

```python
def delete_edges(self, selection=None, domain='POINT'):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## delete_faces

```python
def delete_faces(self, selection=None, domain='POINT'):

```
Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## distribute_points_on_faces

```python
def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):

```
Node [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html) )

### Args:
- selection: Boolean
- distance_min: Float
- density_max: Float
- density: Float
- density_factor: Float
- seed: Integer
- distribute_method (str): 'RANDOM' in [RANDOM, POISSON]

### Returns:
- tuple ('`points`', '`normal`', '`rotation`')

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## domain_size <sub>*property*</sub>

```python
def domain_size(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## dual_mesh

```python
def dual_mesh(self, mesh=None, keep_boundaries=None):

```
Node [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html) )

### Args:
- mesh: Mesh
- keep_boundaries: Boolean

### Returns:
- socket `dual_mesh` of class Mesh

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## edge_count <sub>*property*</sub>

```python
def edge_count(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Returns:
- socket `edge_count`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## edge_paths_to_curves

```python
def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):

```
Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html) )

### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

### Returns:
- socket `curves` of class Curve

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## edge_paths_to_selection

```python
def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None):

```
Node [Edge Paths to Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html) )

### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

### Returns:
- socket `selection`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## extrude

```python
def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):

```
Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html) )

### Args:
- selection: Boolean
- offset: Vector
- offset_scale: Float
- individual: Boolean
- mode (str): 'FACES' in [VERTICES, EDGES, FACES]

### Returns:
- tuple ('`top`', '`side`')

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## face_count <sub>*property*</sub>

```python
def face_count(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Returns:
- socket `face_count`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## face_is_planar

```python
def face_is_planar(self, threshold=None):

```
Node [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html) )

### Args:
- threshold: Float

### Returns:
- socket `planar`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## face_set_boundaries

```python
def face_set_boundaries(self, face_set=None):

```
Node [Face Set Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html) )

### Args:
- face_set: Integer

### Returns:
- socket `boundary_edges`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## flip_faces

```python
def flip_faces(self, selection=None):

```
Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html) )

### Args:
- selection: Boolean

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## instance_on_points

```python
def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:
- socket `instances`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## is_shade_smooth

```python
def is_shade_smooth(self):

```
Node [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html) )

### Returns:
- socket `smooth`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## island <sub>*property*</sub>

```python
def island(self):

```
Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

### Returns:
- node with sockets ['island_index', 'island_count']

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## island_count <sub>*property*</sub>

```python
def island_count(self):

```
Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

### Returns:
- socket `island_count`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## island_index <sub>*property*</sub>

```python
def island_index(self):

```
Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

### Returns:
- socket `island_index`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## pack_uv_islands

```python
def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None):

```
Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html) )

### Args:
- uv: Vector
- selection: Boolean
- margin: Float
- rotate: Boolean

### Returns:
- socket `uv`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## point_count <sub>*property*</sub>

```python
def point_count(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Returns:
- socket `point_count`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## sample_nearest_surface

```python
def sample_nearest_surface(self, value=None, sample_position=None):

```
Node [Sample Nearest Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_nearest_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html) )

### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- sample_position: Vector

### Returns:
- socket `value`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## sample_uv_surface

```python
def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None):

```
Node [Sample UV Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html) )

### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- source_uv_map: Vector
- sample_uv: Vector

### Returns:
- tuple ('`value`', '`is_valid`')

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## scale_elements

```python
def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):

```
Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]
- scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## scale_single_axis

```python
def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE'):

```
Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## scale_uniform

```python
def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE'):

```
Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

### Args:
- selection: Boolean
- scale: Float
- center: Vector
- domain (str): 'FACE' in [FACE, EDGE]

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## set_shade_smooth

```python
def set_shade_smooth(self, selection=None, shade_smooth=None):

```
Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html) )

### Args:
- selection: Boolean
- shade_smooth: Boolean

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## shortest_edge_paths

```python
def shortest_edge_paths(self, end_vertex=None, edge_cost=None):

```
Node [Shortest Edge Paths](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html) )

### Args:
- end_vertex: Boolean
- edge_cost: Float

### Returns:
- tuple ('`next_vertex_index`', '`total_cost`')

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## split_edges

```python
def split_edges(self, selection=None):

```
Node [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html) )

### Args:
- selection: Boolean

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## subdivide

```python
def subdivide(self, level=None):

```
Node [Subdivide Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html) )

### Args:
- level: Integer

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## subdivision_surface

```python
def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):

```
Node [Subdivision Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html) )

### Args:
- level: Integer
- edge_crease: Float
- vertex_crease: Float
- boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
- uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## to_curve

```python
def to_curve(self, selection=None):

```
Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html) )

### Args:
- selection: Boolean

### Returns:
- socket `curve` of class Curve

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## to_points

```python
def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):

```
Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html) )

### Args:
- selection: Boolean
- position: Vector
- radius: Float
- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

### Returns:
- socket `points` of class Points

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

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

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## triangulate

```python
def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

```
Node [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html) )

### Args:
- selection: Boolean
- minimum_vertices: Integer
- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

### Returns:
- self

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>

## uv_unwrap

```python
def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):

```
Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html) )

### Args:
- selection: Boolean
- seam: Boolean
- margin: Float
- fill_holes: Boolean
- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

### Returns:
- socket `uv`

<sub>Go to [top](#class-Mesh) - [main](./structure.md) - [nodes](nodes.md) - [nodes menu](nodes_menus.md)</sub>
