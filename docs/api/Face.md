# class Face

## title

- [(gen.fname(wnode)](area-property)
- [(gen.fname(wnode)](island-property)
- [(gen.fname(wnode)](island_count-property)
- [(gen.fname(wnode)](island_index-property)
- [(gen.fname(wnode)](material-property)
- [(gen.fname(wnode)](neighbors-property)
- [(gen.fname(wnode)](neighbors_face_count-property)
- [(gen.fname(wnode)](neighbors_vertex_count-property)
- [(gen.fname(wnode)](shade_smooth-property)

## title


## title


## title

- [(gen.fname(wnode)](delete_all)
- [(gen.fname(wnode)](delete_edges)
- [(gen.fname(wnode)](delete_faces)
- [(gen.fname(wnode)](distribute_points_poisson)
- [(gen.fname(wnode)](distribute_points_random)
- [(gen.fname(wnode)](domain_size)
- [(gen.fname(wnode)](extrude)
- [(gen.fname(wnode)](face_set_boundaries)
- [(gen.fname(wnode)](flip)
- [(gen.fname(wnode)](is_planar)
- [(gen.fname(wnode)](pack_uv_islands)
- [(gen.fname(wnode)](scale_single_axis)
- [(gen.fname(wnode)](scale_uniform)
- [(gen.fname(wnode)](set_material)
- [(gen.fname(wnode)](set_shade_smooth)
- [(gen.fname(wnode)](triangulate)
- [(gen.fname(wnode)](uv_unwrap)

## area *property*

{#area}

> def area(self):

Node [Face Area](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_area.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html) )

### Returns:

- node with sockets ['area']

## delete_all

{#delete_all}

> def delete_all(self):

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Returns:

- node with sockets ['geometry']

## delete_edges

{#delete_edges}

> def delete_edges(self):

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Returns:

- node with sockets ['geometry']

## delete_faces

{#delete_faces}

> def delete_faces(self):

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

### Returns:

- node with sockets ['geometry']

## distribute_points_poisson

{#distribute_points_poisson}

> def distribute_points_poisson(self, distance_min=None, density_max=None, density_factor=None, seed=None):

Node [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html) )

        ### Args:
- distance_min: Float
- density_max: Float
- density_factor: Float
- seed: Integer

### Returns:

- tuple ('points', 'normal', 'rotation')

## distribute_points_random

{#distribute_points_random}

> def distribute_points_random(self, density=None, seed=None):

Node [Distribute Points on Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html) )

        ### Args:
- density: Float
- seed: Integer

### Returns:

- tuple ('points', 'normal', 'rotation')

## domain_size

{#domain_size}

> def __len__(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

        ### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## extrude

{#extrude}

> def extrude(self, offset=None, offset_scale=None, individual=None):

Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html) )

        ### Args:
- offset: Vector
- offset_scale: Float
- individual: Boolean

### Returns:

- tuple ('top', 'side')

## face_set_boundaries

{#face_set_boundaries}

> def face_set_boundaries(self):

Node [Face Set Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html) )

### Returns:

  socket 'boundary_edges'

## flip

{#flip}

> def flip(self):

Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html) )

### Returns:

- node with sockets ['mesh']

## is_planar

{#is_planar}

> def is_planar(self, threshold=None):

Node [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html) )

        ### Args:
- threshold: Float

### Returns:

  socket 'planar'

## island *property*

{#island}

> def island(self):

Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

### Returns:

- node with sockets ['island_index', 'island_count']

## island_count *property*

{#island_count}

> def island_count(self):

Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

### Returns:

  socket 'island_count'

## island_index *property*

{#island_index}

> def island_index(self):

Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_island.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html) )

### Returns:

  socket 'island_index'

## material *property*

{#material}

> def material(self):

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

'material' is a write only property.
Raise an exception if attempt to read.


## material *etter*

{#material}

> def material(self, attr_value):

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

Node implemented as property setter.

        ###Args:- attr_value: material


## neighbors *property*

{#neighbors}

> def neighbors(self):

Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html) )

### Returns:

- node with sockets ['vertex_count', 'face_count']

## neighbors_face_count *property*

{#neighbors_face_count}

> def neighbors_face_count(self):

Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html) )

### Returns:

  socket 'face_count'

## neighbors_vertex_count *property*

{#neighbors_vertex_count}

> def neighbors_vertex_count(self):

Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html) )

### Returns:

  socket 'vertex_count'

## pack_uv_islands

{#pack_uv_islands}

> def pack_uv_islands(self, uv=None, margin=None, rotate=None):

Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html) )

        ### Args:
- uv: Vector
- margin: Float
- rotate: Boolean

### Returns:

  socket 'uv'

## scale_single_axis

{#scale_single_axis}

> def scale_single_axis(self, scale=None, center=None, axis=None):

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

        ### Args:
- scale: Float
- center: Vector
- axis: Vector

### Returns:

- node with sockets ['geometry']

## scale_uniform

{#scale_uniform}

> def scale_uniform(self, scale=None, center=None):

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

        ### Args:
- scale: Float
- center: Vector

### Returns:

- node with sockets ['geometry']

## set_material

{#set_material}

> def set_material(self, material=None):

Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html) )

        ### Args:
- material: Material

### Returns:

- node with sockets ['geometry']

## set_shade_smooth

{#set_shade_smooth}

> def set_shade_smooth(self, shade_smooth=None):

Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html) )

        ### Args:
- shade_smooth: Boolean

### Returns:

- node with sockets ['geometry']

## shade_smooth *property*

{#shade_smooth}

> def shade_smooth(self):

Node [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html) )

### Returns:

  socket 'smooth'

## shade_smooth *etter*

{#shade_smooth}

> def shade_smooth(self, attr_value):

Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html) )

Node implemented as property setter.

        ###Args:- attr_value: shade_smooth


## triangulate

{#triangulate}

> def triangulate(self, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

Node [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html) )

        ### Args:
- minimum_vertices: Integer
- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

### Returns:

- node with sockets ['mesh']

## uv_unwrap

{#uv_unwrap}

> def uv_unwrap(self, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):

Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html) )

        ### Args:
- seam: Boolean
- margin: Float
- fill_holes: Boolean
- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

### Returns:

  socket 'uv'

