# class Mesh

## title

- [(gen.fname(wnode)](corner_count-property)
- [(gen.fname(wnode)](domain_size-property)
- [(gen.fname(wnode)](edge_count-property)
- [(gen.fname(wnode)](face_count-property)
- [(gen.fname(wnode)](island-property)
- [(gen.fname(wnode)](island_count-property)
- [(gen.fname(wnode)](island_index-property)
- [(gen.fname(wnode)](point_count-property)

## title

- [(gen.fname(wnode)](Circle-classmethod)
- [(gen.fname(wnode)](Circle-classmethod)
- [(gen.fname(wnode)](Cube-classmethod)
- [(gen.fname(wnode)](Grid-classmethod)
- [(gen.fname(wnode)](IcoSphere-classmethod)
- [(gen.fname(wnode)](Line-classmethod)
- [(gen.fname(wnode)](LineEndPoints-classmethod)
- [(gen.fname(wnode)](LineEndPointsResolution-classmethod)
- [(gen.fname(wnode)](LineOffset-classmethod)
- [(gen.fname(wnode)](LineOffsetResolution-classmethod)

## title

- [(gen.fname(wnode)](Cone-staticmethod)
- [(gen.fname(wnode)](Cylinder-staticmethod)

## title

- [(gen.fname(wnode)](boolean_difference)
- [(gen.fname(wnode)](boolean_intersect)
- [(gen.fname(wnode)](boolean_union)
- [(gen.fname(wnode)](delete_all)
- [(gen.fname(wnode)](delete_edges)
- [(gen.fname(wnode)](delete_faces)
- [(gen.fname(wnode)](distribute_points_on_faces)
- [(gen.fname(wnode)](dual_mesh)
- [(gen.fname(wnode)](edge_paths_to_curves)
- [(gen.fname(wnode)](edge_paths_to_selection)
- [(gen.fname(wnode)](extrude)
- [(gen.fname(wnode)](face_is_planar)
- [(gen.fname(wnode)](face_set_boundaries)
- [(gen.fname(wnode)](flip_faces)
- [(gen.fname(wnode)](instance_on_points)
- [(gen.fname(wnode)](is_shade_smooth)
- [(gen.fname(wnode)](pack_uv_islands)
- [(gen.fname(wnode)](sample_nearest_surface)
- [(gen.fname(wnode)](sample_uv_surface)
- [(gen.fname(wnode)](scale_elements)
- [(gen.fname(wnode)](scale_single_axis)
- [(gen.fname(wnode)](scale_uniform)
- [(gen.fname(wnode)](set_shade_smooth)
- [(gen.fname(wnode)](shortest_edge_paths)
- [(gen.fname(wnode)](split_edges)
- [(gen.fname(wnode)](subdivide)
- [(gen.fname(wnode)](subdivision_surface)
- [(gen.fname(wnode)](to_curve)
- [(gen.fname(wnode)](to_points)
- [(gen.fname(wnode)](to_volume)
- [(gen.fname(wnode)](triangulate)
- [(gen.fname(wnode)](uv_unwrap)

## Circle *classmethod*

{#Circle}

> def Circle(cls, vertices=None, radius=None, fill_type='NONE'):

Node [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html) )

        ### Args:
- vertices: Integer
- radius: Float
- fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]

### Returns:

  socket 'mesh'

## Circle *classmethod*

{#Circle}

> def Circle(cls, segments=None, rings=None, radius=None):

Node [UV Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html) )

        ### Args:
- segments: Integer
- rings: Integer
- radius: Float

### Returns:

  socket 'mesh'

## Cone *staticmethod*

{#Cone}

> def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):

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

- tuple ('mesh', 'top', 'bottom', 'side')

## Cube *classmethod*

{#Cube}

> def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):

Node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html) )

        ### Args:
- size: Vector
- vertices_x: Integer
- vertices_y: Integer
- vertices_z: Integer

### Returns:

  socket 'mesh'

## Cylinder *staticmethod*

{#Cylinder}

> def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):

Node [Cylinder](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cylinder.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html) )

        ### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

### Returns:

- tuple ('mesh', 'top', 'bottom', 'side')

## Grid *classmethod*

{#Grid}

> def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):

Node [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/grid.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html) )

        ### Args:
- size_x: Float
- size_y: Float
- vertices_x: Integer
- vertices_y: Integer

### Returns:

  socket 'mesh'

## IcoSphere *classmethod*

{#IcoSphere}

> def IcoSphere(cls, radius=None, subdivisions=None):

Node [Ico Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html) )

        ### Args:
- radius: Float
- subdivisions: Integer

### Returns:

  socket 'mesh'

## Line *classmethod*

{#Line}

> def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

        ### Args:
- count: Integer
- resolution: Float
- start_location: Vector
- offset: Vector
- count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
- mode (str): 'OFFSET' in [OFFSET, END_POINTS]

### Returns:

  socket 'mesh'

## LineEndPoints *classmethod*

{#LineEndPoints}

> def LineEndPoints(cls, count=None, start_location=None, end_location=None):

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

        ### Args:
- count: Integer
- start_location: Vector
- end_location: Vector

### Returns:

  socket 'mesh'

## LineEndPointsResolution *classmethod*

{#LineEndPointsResolution}

> def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None):

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

        ### Args:
- resolution: Float
- start_location: Vector
- end_location: Vector

### Returns:

  socket 'mesh'

## LineOffset *classmethod*

{#LineOffset}

> def LineOffset(cls, count=None, start_location=None, offset=None):

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

        ### Args:
- count: Integer
- start_location: Vector
- offset: Vector

### Returns:

  socket 'mesh'

## LineOffsetResolution *classmethod*

{#LineOffsetResolution}

> def LineOffsetResolution(cls, resolution=None, start_location=None, offset=None):

Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_line.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html) )

        ### Args:
- resolution: Float
- start_location: Vector
- offset: Vector

### Returns:

  socket 'mesh'

## boolean_difference

{#boolean_difference}

> def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):

Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html) )

        ### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

### Returns:

  socket 'intersecting_edges'

## boolean_intersect

{#boolean_intersect}

> def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None):

Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html) )

        ### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

### Returns:

  socket 'intersecting_edges'

## boolean_union

{#boolean_union}

> def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None):

Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_boolean.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html) )

        ### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

### Returns:

  socket 'intersecting_edges'

## corner_count *property*

{#corner_count}

> def corner_count(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

Node implemented as property.

### Returns:

  socket 'face_corner_count'

## delete_all

{#delete_all}

> def delete_all(self, selection=None, domain='POINT'):

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

        ### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## delete_edges

{#delete_edges}

> def delete_edges(self, selection=None, domain='POINT'):

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

        ### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## delete_faces

{#delete_faces}

> def delete_faces(self, selection=None, domain='POINT'):

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

        ### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## distribute_points_on_faces

{#distribute_points_on_faces}

> def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):

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

- tuple ('points', 'normal', 'rotation')

## domain_size *property*

{#domain_size}

> def domain_size(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

Node implemented as property.

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## dual_mesh

{#dual_mesh}

> def dual_mesh(self, mesh=None, keep_boundaries=None):

Node [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html) )

        ### Args:
- mesh: Mesh
- keep_boundaries: Boolean

### Returns:

  socket 'dual_mesh' of class Mesh

## edge_count *property*

{#edge_count}

> def edge_count(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

Node implemented as property.

### Returns:

  socket 'edge_count'

## edge_paths_to_curves

{#edge_paths_to_curves}

> def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):

Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_curves.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html) )

        ### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

### Returns:

  socket 'curves' of class Curve

## edge_paths_to_selection

{#edge_paths_to_selection}

> def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None):

Node [Edge Paths to Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_paths_to_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html) )

        ### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

### Returns:

  socket 'selection'

## extrude

{#extrude}

> def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):

Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html) )

        ### Args:
- selection: Boolean
- offset: Vector
- offset_scale: Float
- individual: Boolean
- mode (str): 'FACES' in [VERTICES, EDGES, FACES]

### Returns:

- tuple ('top', 'side')

## face_count *property*

{#face_count}

> def face_count(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

Node implemented as property.

### Returns:

  socket 'face_count'

## face_is_planar

{#face_is_planar}

> def face_is_planar(self, threshold=None):

Node [Face is Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_is_planar.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html) )

        ### Args:
- threshold: Float

### Returns:

  socket 'planar'

## face_set_boundaries

{#face_set_boundaries}

> def face_set_boundaries(self, face_set=None):

Node [Face Set Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_set_boundaries.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html) )

        ### Args:
- face_set: Integer

### Returns:

  socket 'boundary_edges'

## flip_faces

{#flip_faces}

> def flip_faces(self, selection=None):

Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/flip_faces.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html) )

        ### Args:
- selection: Boolean

### Returns:

- node with sockets ['mesh']

## instance_on_points

{#instance_on_points}

> def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

        ### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:

  socket 'instances'

## is_shade_smooth

{#is_shade_smooth}

> def is_shade_smooth(self):

Node [Is Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/is_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html) )

### Returns:

  socket 'smooth'

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

## pack_uv_islands

{#pack_uv_islands}

> def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None):

Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/pack_uv_islands.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html) )

        ### Args:
- uv: Vector
- selection: Boolean
- margin: Float
- rotate: Boolean

### Returns:

  socket 'uv'

## point_count *property*

{#point_count}

> def point_count(self):

Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

Node implemented as property.

### Returns:

  socket 'point_count'

## sample_nearest_surface

{#sample_nearest_surface}

> def sample_nearest_surface(self, value=None, sample_position=None):

Node [Sample Nearest Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_nearest_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html) )

        ### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- sample_position: Vector

### Returns:

  socket 'value'

## sample_uv_surface

{#sample_uv_surface}

> def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None):

Node [Sample UV Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample_uv_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html) )

        ### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- source_uv_map: Vector
- sample_uv: Vector

### Returns:

- tuple ('value', 'is_valid')

## scale_elements

{#scale_elements}

> def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

        ### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]
- scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]

### Returns:

- node with sockets ['geometry']

## scale_single_axis

{#scale_single_axis}

> def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE'):

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

        ### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]

### Returns:

- node with sockets ['geometry']

## scale_uniform

{#scale_uniform}

> def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE'):

Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/scale_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html) )

        ### Args:
- selection: Boolean
- scale: Float
- center: Vector
- domain (str): 'FACE' in [FACE, EDGE]

### Returns:

- node with sockets ['geometry']

## set_shade_smooth

{#set_shade_smooth}

> def set_shade_smooth(self, selection=None, shade_smooth=None):

Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/set_shade_smooth.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html) )

        ### Args:
- selection: Boolean
- shade_smooth: Boolean

### Returns:

- node with sockets ['geometry']

## shortest_edge_paths

{#shortest_edge_paths}

> def shortest_edge_paths(self, end_vertex=None, edge_cost=None):

Node [Shortest Edge Paths](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/shortest_edge_paths.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html) )

        ### Args:
- end_vertex: Boolean
- edge_cost: Float

### Returns:

- tuple ('next_vertex_index', 'total_cost')

## split_edges

{#split_edges}

> def split_edges(self, selection=None):

Node [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/split_edges.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html) )

        ### Args:
- selection: Boolean

### Returns:

- node with sockets ['mesh']

## subdivide

{#subdivide}

> def subdivide(self, level=None):

Node [Subdivide Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html) )

        ### Args:
- level: Integer

### Returns:

- node with sockets ['mesh']

## subdivision_surface

{#subdivision_surface}

> def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):

Node [Subdivision Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivision_surface.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html) )

        ### Args:
- level: Integer
- edge_crease: Float
- vertex_crease: Float
- boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
- uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]

### Returns:

- node with sockets ['mesh']

## to_curve

{#to_curve}

> def to_curve(self, selection=None):

Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html) )

        ### Args:
- selection: Boolean

### Returns:

  socket 'curve' of class Curve

## to_points

{#to_points}

> def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):

Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html) )

        ### Args:
- selection: Boolean
- position: Vector
- radius: Float
- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

### Returns:

  socket 'points' of class Points

## to_volume

{#to_volume}

> def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):

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

  socket 'volume' of class Volume

## triangulate

{#triangulate}

> def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

Node [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/triangulate.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html) )

        ### Args:
- selection: Boolean
- minimum_vertices: Integer
- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

### Returns:

- node with sockets ['mesh']

## uv_unwrap

{#uv_unwrap}

> def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):

Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/uv/uv_unwrap.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html) )

        ### Args:
- selection: Boolean
- seam: Boolean
- margin: Float
- fill_holes: Boolean
- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

### Returns:

  socket 'uv'

