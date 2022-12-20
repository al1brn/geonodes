# class Face

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

## area <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def area(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Face Area](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['area']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## delete_all

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def delete_all(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## delete_edges

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def delete_edges(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## delete_faces

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def delete_faces(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## distribute_points_poisson

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def distribute_points_poisson(self, distance_min=None, density_max=None, density_factor=None, seed=None):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- distance_min: Float
<sub>Go to [top](#class-Face)</sub>

- density_max: Float
<sub>Go to [top](#class-Face)</sub>

- density_factor: Float
<sub>Go to [top](#class-Face)</sub>

- seed: Integer
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- tuple ('points', 'normal', 'rotation')
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## distribute_points_random

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def distribute_points_random(self, density=None, seed=None):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- density: Float
<sub>Go to [top](#class-Face)</sub>

- seed: Integer
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- tuple ('points', 'normal', 'rotation')
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## domain_size

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def __len__(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- geometry: Geometry
<sub>Go to [top](#class-Face)</sub>

- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## extrude

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def extrude(self, offset=None, offset_scale=None, individual=None):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- offset: Vector
<sub>Go to [top](#class-Face)</sub>

- offset_scale: Float
<sub>Go to [top](#class-Face)</sub>

- individual: Boolean
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- tuple ('top', 'side')
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## face_set_boundaries

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def face_set_boundaries(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Face Set Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

  socket 'boundary_edges'<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## flip

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def flip(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['mesh']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## is_planar

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def is_planar(self, threshold=None):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- threshold: Float
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

  socket 'planar'<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## island <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def island(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['island_index', 'island_count']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## island_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def island_count(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

  socket 'island_count'<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## island_index <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def island_index(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

  socket 'island_index'<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## material <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def material(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

<sub>Go to [top](#class-Face)</sub>

'material' is a write only property.
Raise an exception if attempt to read.

<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## material <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def material(self, attr_value):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

<sub>Go to [top](#class-Face)</sub>

Node implemented as property setter.

<sub>Go to [top](#class-Face)</sub>

        ###Args:<sub>Go to [top](#class-Face)</sub>

- attr_value: material
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## neighbors <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def neighbors(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['vertex_count', 'face_count']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## neighbors_face_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def neighbors_face_count(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

  socket 'face_count'<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## neighbors_vertex_count <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def neighbors_vertex_count(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

  socket 'vertex_count'<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## pack_uv_islands

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def pack_uv_islands(self, uv=None, margin=None, rotate=None):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- uv: Vector
<sub>Go to [top](#class-Face)</sub>

- margin: Float
<sub>Go to [top](#class-Face)</sub>

- rotate: Boolean
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

  socket 'uv'<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## scale_single_axis

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def scale_single_axis(self, scale=None, center=None, axis=None):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- scale: Float
<sub>Go to [top](#class-Face)</sub>

- center: Vector
<sub>Go to [top](#class-Face)</sub>

- axis: Vector
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## scale_uniform

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def scale_uniform(self, scale=None, center=None):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- scale: Float
<sub>Go to [top](#class-Face)</sub>

- center: Vector
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## set_material

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def set_material(self, material=None):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- material: Material
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## set_shade_smooth

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def set_shade_smooth(self, shade_smooth=None):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- shade_smooth: Boolean
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## shade_smooth <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def shade_smooth(self):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html) )

<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

  socket 'smooth'<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## shade_smooth <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def shade_smooth(self, attr_value):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html) )

<sub>Go to [top](#class-Face)</sub>

Node implemented as property setter.

<sub>Go to [top](#class-Face)</sub>

        ###Args:<sub>Go to [top](#class-Face)</sub>

- attr_value: shade_smooth
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## triangulate

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- minimum_vertices: Integer
<sub>Go to [top](#class-Face)</sub>

- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
<sub>Go to [top](#class-Face)</sub>

- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

- node with sockets ['mesh']
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

## uv_unwrap

<sub>Go to [top](#class-Face)</sub>

```python
<sub>Go to [top](#class-Face)</sub>

def uv_unwrap(self, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):

<sub>Go to [top](#class-Face)</sub>

```
<sub>Go to [top](#class-Face)</sub>

Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html) )

<sub>Go to [top](#class-Face)</sub>

### Args:
<sub>Go to [top](#class-Face)</sub>

- seam: Boolean
<sub>Go to [top](#class-Face)</sub>

- margin: Float
<sub>Go to [top](#class-Face)</sub>

- fill_holes: Boolean
<sub>Go to [top](#class-Face)</sub>

- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]
<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

### Returns:

<sub>Go to [top](#class-Face)</sub>

  socket 'uv'<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>


<sub>Go to [top](#class-Face)</sub>

