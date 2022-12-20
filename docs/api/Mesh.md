# class Mesh

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

## Circle <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def Circle(cls, vertices=None, radius=None, fill_type='NONE'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- vertices: Integer
<sub>Go to [top](#class-Mesh)</sub>

- radius: Float
<sub>Go to [top](#class-Mesh)</sub>

- fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## Circle <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def Circle(cls, segments=None, rings=None, radius=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [UV Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- segments: Integer
<sub>Go to [top](#class-Mesh)</sub>

- rings: Integer
<sub>Go to [top](#class-Mesh)</sub>

- radius: Float
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## Cone <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Cone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cone.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- vertices: Integer
<sub>Go to [top](#class-Mesh)</sub>

- side_segments: Integer
<sub>Go to [top](#class-Mesh)</sub>

- fill_segments: Integer
<sub>Go to [top](#class-Mesh)</sub>

- radius_top: Float
<sub>Go to [top](#class-Mesh)</sub>

- radius_bottom: Float
<sub>Go to [top](#class-Mesh)</sub>

- depth: Float
<sub>Go to [top](#class-Mesh)</sub>

- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- tuple ('mesh', 'top', 'bottom', 'side')
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## Cube <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- size: Vector
<sub>Go to [top](#class-Mesh)</sub>

- vertices_x: Integer
<sub>Go to [top](#class-Mesh)</sub>

- vertices_y: Integer
<sub>Go to [top](#class-Mesh)</sub>

- vertices_z: Integer
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## Cylinder <span style="color:blue">*staticmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Cylinder](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- vertices: Integer
<sub>Go to [top](#class-Mesh)</sub>

- side_segments: Integer
<sub>Go to [top](#class-Mesh)</sub>

- fill_segments: Integer
<sub>Go to [top](#class-Mesh)</sub>

- radius: Float
<sub>Go to [top](#class-Mesh)</sub>

- depth: Float
<sub>Go to [top](#class-Mesh)</sub>

- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- tuple ('mesh', 'top', 'bottom', 'side')
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## Grid <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- size_x: Float
<sub>Go to [top](#class-Mesh)</sub>

- size_y: Float
<sub>Go to [top](#class-Mesh)</sub>

- vertices_x: Integer
<sub>Go to [top](#class-Mesh)</sub>

- vertices_y: Integer
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## IcoSphere <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def IcoSphere(cls, radius=None, subdivisions=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Ico Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- radius: Float
<sub>Go to [top](#class-Mesh)</sub>

- subdivisions: Integer
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## Line <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- count: Integer
<sub>Go to [top](#class-Mesh)</sub>

- resolution: Float
<sub>Go to [top](#class-Mesh)</sub>

- start_location: Vector
<sub>Go to [top](#class-Mesh)</sub>

- offset: Vector
<sub>Go to [top](#class-Mesh)</sub>

- count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
<sub>Go to [top](#class-Mesh)</sub>

- mode (str): 'OFFSET' in [OFFSET, END_POINTS]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## LineEndPoints <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def LineEndPoints(cls, count=None, start_location=None, end_location=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- count: Integer
<sub>Go to [top](#class-Mesh)</sub>

- start_location: Vector
<sub>Go to [top](#class-Mesh)</sub>

- end_location: Vector
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## LineEndPointsResolution <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- resolution: Float
<sub>Go to [top](#class-Mesh)</sub>

- start_location: Vector
<sub>Go to [top](#class-Mesh)</sub>

- end_location: Vector
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## LineOffset <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def LineOffset(cls, count=None, start_location=None, offset=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- count: Integer
<sub>Go to [top](#class-Mesh)</sub>

- start_location: Vector
<sub>Go to [top](#class-Mesh)</sub>

- offset: Vector
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## LineOffsetResolution <span style="color:blue">*classmethod*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def LineOffsetResolution(cls, resolution=None, start_location=None, offset=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- resolution: Float
<sub>Go to [top](#class-Mesh)</sub>

- start_location: Vector
<sub>Go to [top](#class-Mesh)</sub>

- offset: Vector
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'mesh'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## boolean_difference

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- mesh_2: <m>Geometry
<sub>Go to [top](#class-Mesh)</sub>

- self_intersection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- hole_tolerant: Boolean
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'intersecting_edges'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## boolean_intersect

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- mesh_2: <m>Geometry
<sub>Go to [top](#class-Mesh)</sub>

- self_intersection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- hole_tolerant: Boolean
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'intersecting_edges'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## boolean_union

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- mesh_2: <m>Geometry
<sub>Go to [top](#class-Mesh)</sub>

- self_intersection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- hole_tolerant: Boolean
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'intersecting_edges'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## corner_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def corner_count(self):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Mesh)</sub>

Node implemented as property.

<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'face_corner_count'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## delete_all

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def delete_all(self, selection=None, domain='POINT'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## delete_edges

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def delete_edges(self, selection=None, domain='POINT'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## delete_faces

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def delete_faces(self, selection=None, domain='POINT'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## distribute_points_on_faces

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- distance_min: Float
<sub>Go to [top](#class-Mesh)</sub>

- density_max: Float
<sub>Go to [top](#class-Mesh)</sub>

- density: Float
<sub>Go to [top](#class-Mesh)</sub>

- density_factor: Float
<sub>Go to [top](#class-Mesh)</sub>

- seed: Integer
<sub>Go to [top](#class-Mesh)</sub>

- distribute_method (str): 'RANDOM' in [RANDOM, POISSON]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- tuple ('points', 'normal', 'rotation')
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## domain_size <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def domain_size(self):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Mesh)</sub>

Node implemented as property.

<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## dual_mesh

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def dual_mesh(self, mesh=None, keep_boundaries=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- mesh: Mesh
<sub>Go to [top](#class-Mesh)</sub>

- keep_boundaries: Boolean
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'dual_mesh'<sub>Go to [top](#class-Mesh)</sub>

 of class Mesh
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## edge_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def edge_count(self):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Mesh)</sub>

Node implemented as property.

<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'edge_count'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## edge_paths_to_curves

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- start_vertices: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- next_vertex_index: Integer
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'curves'<sub>Go to [top](#class-Mesh)</sub>

 of class Curve
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## edge_paths_to_selection

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Edge Paths to Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- start_vertices: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- next_vertex_index: Integer
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'selection'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## extrude

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- offset: Vector
<sub>Go to [top](#class-Mesh)</sub>

- offset_scale: Float
<sub>Go to [top](#class-Mesh)</sub>

- individual: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- mode (str): 'FACES' in [VERTICES, EDGES, FACES]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- tuple ('top', 'side')
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## face_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def face_count(self):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Mesh)</sub>

Node implemented as property.

<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'face_count'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## face_is_planar

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def face_is_planar(self, threshold=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- threshold: Float
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'planar'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## face_set_boundaries

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def face_set_boundaries(self, face_set=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Face Set Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- face_set: Integer
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'boundary_edges'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## flip_faces

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def flip_faces(self, selection=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['mesh']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## instance_on_points

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- instance: Geometry
<sub>Go to [top](#class-Mesh)</sub>

- pick_instance: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- instance_index: Integer
<sub>Go to [top](#class-Mesh)</sub>

- rotation: Vector
<sub>Go to [top](#class-Mesh)</sub>

- scale: Vector
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'instances'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## is_shade_smooth

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def is_shade_smooth(self):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'smooth'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## island <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def island(self):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['island_index', 'island_count']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## island_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def island_count(self):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'island_count'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## island_index <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def island_index(self):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'island_index'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## pack_uv_islands

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- uv: Vector
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- margin: Float
<sub>Go to [top](#class-Mesh)</sub>

- rotate: Boolean
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'uv'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## point_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def point_count(self):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Mesh)</sub>

Node implemented as property.

<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'point_count'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## sample_nearest_surface

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def sample_nearest_surface(self, value=None, sample_position=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Sample Nearest Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_nearest_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
<sub>Go to [top](#class-Mesh)</sub>

- sample_position: Vector
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'value'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## sample_uv_surface

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Sample UV Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
<sub>Go to [top](#class-Mesh)</sub>

- source_uv_map: Vector
<sub>Go to [top](#class-Mesh)</sub>

- sample_uv: Vector
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- tuple ('value', 'is_valid')
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## scale_elements

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- scale: Float
<sub>Go to [top](#class-Mesh)</sub>

- center: Vector
<sub>Go to [top](#class-Mesh)</sub>

- axis: Vector
<sub>Go to [top](#class-Mesh)</sub>

- domain (str): 'FACE' in [FACE, EDGE]
<sub>Go to [top](#class-Mesh)</sub>

- scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## scale_single_axis

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- scale: Float
<sub>Go to [top](#class-Mesh)</sub>

- center: Vector
<sub>Go to [top](#class-Mesh)</sub>

- axis: Vector
<sub>Go to [top](#class-Mesh)</sub>

- domain (str): 'FACE' in [FACE, EDGE]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## scale_uniform

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- scale: Float
<sub>Go to [top](#class-Mesh)</sub>

- center: Vector
<sub>Go to [top](#class-Mesh)</sub>

- domain (str): 'FACE' in [FACE, EDGE]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## set_shade_smooth

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def set_shade_smooth(self, selection=None, shade_smooth=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- shade_smooth: Boolean
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## shortest_edge_paths

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def shortest_edge_paths(self, end_vertex=None, edge_cost=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Shortest Edge Paths](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- end_vertex: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- edge_cost: Float
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- tuple ('next_vertex_index', 'total_cost')
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## split_edges

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def split_edges(self, selection=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['mesh']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## subdivide

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def subdivide(self, level=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Subdivide Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- level: Integer
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['mesh']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## subdivision_surface

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Subdivision Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- level: Integer
<sub>Go to [top](#class-Mesh)</sub>

- edge_crease: Float
<sub>Go to [top](#class-Mesh)</sub>

- vertex_crease: Float
<sub>Go to [top](#class-Mesh)</sub>

- boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
<sub>Go to [top](#class-Mesh)</sub>

- uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['mesh']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## to_curve

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def to_curve(self, selection=None):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'curve'<sub>Go to [top](#class-Mesh)</sub>

 of class Curve
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## to_points

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- position: Vector
<sub>Go to [top](#class-Mesh)</sub>

- radius: Float
<sub>Go to [top](#class-Mesh)</sub>

- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'points'<sub>Go to [top](#class-Mesh)</sub>

 of class Points
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## to_volume

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_volume.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- density: Float
<sub>Go to [top](#class-Mesh)</sub>

- voxel_size: Float
<sub>Go to [top](#class-Mesh)</sub>

- voxel_amount: Float
<sub>Go to [top](#class-Mesh)</sub>

- exterior_band_width: Float
<sub>Go to [top](#class-Mesh)</sub>

- interior_band_width: Float
<sub>Go to [top](#class-Mesh)</sub>

- fill_volume: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'volume'<sub>Go to [top](#class-Mesh)</sub>

 of class Volume
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## triangulate

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- minimum_vertices: Integer
<sub>Go to [top](#class-Mesh)</sub>

- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
<sub>Go to [top](#class-Mesh)</sub>

- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

- node with sockets ['mesh']
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

## uv_unwrap

<sub>Go to [top](#class-Mesh)</sub>

```python
<sub>Go to [top](#class-Mesh)</sub>

def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):

<sub>Go to [top](#class-Mesh)</sub>

```
<sub>Go to [top](#class-Mesh)</sub>

Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html) )

<sub>Go to [top](#class-Mesh)</sub>

### Args:
<sub>Go to [top](#class-Mesh)</sub>

- selection: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- seam: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- margin: Float
<sub>Go to [top](#class-Mesh)</sub>

- fill_holes: Boolean
<sub>Go to [top](#class-Mesh)</sub>

- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]
<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

### Returns:

<sub>Go to [top](#class-Mesh)</sub>

  socket 'uv'<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>


<sub>Go to [top](#class-Mesh)</sub>

