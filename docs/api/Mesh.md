# class {class_name}

## Circle *classmethod* {#Circle}

> def Circle(cls, vertices=None, radius=None, fill_type='NONE'):

Node [Mesh Circle](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vertices: Integer
- radius: Float
- fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]

### Returns:

  socket 'mesh'

## Circle *classmethod* {#Circle}

> def Circle(cls, segments=None, rings=None, radius=None):

Node [UV Sphere](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- segments: Integer
- rings: Integer
- radius: Float

### Returns:

  socket 'mesh'

## Cone *staticmethod* {#Cone}

> def Cone(vertices=None, side_segments=None, fill_segments=None, radius_top=None, radius_bottom=None, depth=None, fill_type='NGON'):

Node [Cone](node.blender_ref) ( [api](node.blender_python_ref) )

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

## Cube *classmethod* {#Cube}

> def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):

Node [Cube](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- size: Vector
- vertices_x: Integer
- vertices_y: Integer
- vertices_z: Integer

### Returns:

  socket 'mesh'

## Cylinder *staticmethod* {#Cylinder}

> def Cylinder(vertices=None, side_segments=None, fill_segments=None, radius=None, depth=None, fill_type='NGON'):

Node [Cylinder](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- vertices: Integer
- side_segments: Integer
- fill_segments: Integer
- radius: Float
- depth: Float
- fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]

### Returns:

- tuple ('mesh', 'top', 'bottom', 'side')

## Grid *classmethod* {#Grid}

> def Grid(cls, size_x=None, size_y=None, vertices_x=None, vertices_y=None):

Node [Grid](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- size_x: Float
- size_y: Float
- vertices_x: Integer
- vertices_y: Integer

### Returns:

  socket 'mesh'

## IcoSphere *classmethod* {#IcoSphere}

> def IcoSphere(cls, radius=None, subdivisions=None):

Node [Ico Sphere](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- radius: Float
- subdivisions: Integer

### Returns:

  socket 'mesh'

## Line *classmethod* {#Line}

> def Line(cls, count=None, resolution=None, start_location=None, offset=None, count_mode='TOTAL', mode='OFFSET'):

Node [Mesh Line](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer
- resolution: Float
- start_location: Vector
- offset: Vector
- count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
- mode (str): 'OFFSET' in [OFFSET, END_POINTS]

### Returns:

  socket 'mesh'

## LineEndPoints *classmethod* {#LineEndPoints}

> def LineEndPoints(cls, count=None, start_location=None, end_location=None):

Node [Mesh Line](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer
- start_location: Vector
- end_location: Vector

### Returns:

  socket 'mesh'

## LineEndPointsResolution *classmethod* {#LineEndPointsResolution}

> def LineEndPointsResolution(cls, resolution=None, start_location=None, end_location=None):

Node [Mesh Line](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Float
- start_location: Vector
- end_location: Vector

### Returns:

  socket 'mesh'

## LineOffset *classmethod* {#LineOffset}

> def LineOffset(cls, count=None, start_location=None, offset=None):

Node [Mesh Line](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- count: Integer
- start_location: Vector
- offset: Vector

### Returns:

  socket 'mesh'

## LineOffsetResolution *classmethod* {#LineOffsetResolution}

> def LineOffsetResolution(cls, resolution=None, start_location=None, offset=None):

Node [Mesh Line](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- resolution: Float
- start_location: Vector
- offset: Vector

### Returns:

  socket 'mesh'

## boolean_difference {#boolean_difference}

> def boolean_difference(self, *mesh_2, self_intersection=None, hole_tolerant=None):

Node [Mesh Boolean](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

### Returns:

  socket 'intersecting_edges'

## boolean_intersect {#boolean_intersect}

> def boolean_intersect(*mesh_2, self_intersection=None, hole_tolerant=None):

Node [Mesh Boolean](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

### Returns:

  socket 'intersecting_edges'

## boolean_union {#boolean_union}

> def boolean_union(*mesh_2, self_intersection=None, hole_tolerant=None):

Node [Mesh Boolean](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- mesh_2: <m>Geometry
- self_intersection: Boolean
- hole_tolerant: Boolean

### Returns:

  socket 'intersecting_edges'

## corner_count *property* {#corner_count}

> def corner_count(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'face_corner_count'

## delete_all {#delete_all}

> def delete_all(self, selection=None, domain='POINT'):

Node [Delete Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## delete_edges {#delete_edges}

> def delete_edges(self, selection=None, domain='POINT'):

Node [Delete Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## delete_faces {#delete_faces}

> def delete_faces(self, selection=None, domain='POINT'):

Node [Delete Geometry](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- domain (str): 'POINT' in [POINT, EDGE, FACE, CURVE, INSTANCE]

### Returns:

- node with sockets ['geometry']

## distribute_points_on_faces {#distribute_points_on_faces}

> def distribute_points_on_faces(self, selection=None, distance_min=None, density_max=None, density=None, density_factor=None, seed=None, distribute_method='RANDOM'):

Node [Distribute Points on Faces](node.blender_ref) ( [api](node.blender_python_ref) )

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

## domain_size *property* {#domain_size}

> def domain_size(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

## dual_mesh {#dual_mesh}

> def dual_mesh(self, mesh=None, keep_boundaries=None):

Node [Dual Mesh](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- mesh: Mesh
- keep_boundaries: Boolean

### Returns:

  socket 'dual_mesh' of class Mesh

## edge_count *property* {#edge_count}

> def edge_count(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'edge_count'

## edge_paths_to_curves {#edge_paths_to_curves}

> def edge_paths_to_curves(self, start_vertices=None, next_vertex_index=None):

Node [Edge Paths to Curves](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

### Returns:

  socket 'curves' of class Curve

## edge_paths_to_selection {#edge_paths_to_selection}

> def edge_paths_to_selection(self, start_vertices=None, next_vertex_index=None):

Node [Edge Paths to Selection](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- start_vertices: Boolean
- next_vertex_index: Integer

### Returns:

  socket 'selection'

## extrude {#extrude}

> def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):

Node [Extrude Mesh](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- offset: Vector
- offset_scale: Float
- individual: Boolean
- mode (str): 'FACES' in [VERTICES, EDGES, FACES]

### Returns:

- tuple ('top', 'side')

## face_count *property* {#face_count}

> def face_count(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'face_count'

## face_is_planar {#face_is_planar}

> def face_is_planar(self, threshold=None):

Node [Face is Planar](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- threshold: Float

### Returns:

  socket 'planar'

## face_set_boundaries {#face_set_boundaries}

> def face_set_boundaries(self, face_set=None):

Node [Face Set Boundaries](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- face_set: Integer

### Returns:

  socket 'boundary_edges'

## flip_faces {#flip_faces}

> def flip_faces(self, selection=None):

Node [Flip Faces](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean

### Returns:

- node with sockets ['mesh']

## instance_on_points {#instance_on_points}

> def instance_on_points(self, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

Node [Instance on Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:

  socket 'instances'

## is_shade_smooth {#is_shade_smooth}

> def is_shade_smooth(self):

Node [Is Shade Smooth](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'smooth'

## island *property* {#island}

> def island(self):

Node [Mesh Island](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

- node with sockets ['island_index', 'island_count']

## island_count *property* {#island_count}

> def island_count(self):

Node [Mesh Island](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'island_count'

## island_index *property* {#island_index}

> def island_index(self):

Node [Mesh Island](node.blender_ref) ( [api](node.blender_python_ref) )

### Returns:

  socket 'island_index'

## pack_uv_islands {#pack_uv_islands}

> def pack_uv_islands(self, uv=None, selection=None, margin=None, rotate=None):

Node [Pack UV Islands](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- uv: Vector
- selection: Boolean
- margin: Float
- rotate: Boolean

### Returns:

  socket 'uv'

## point_count *property* {#point_count}

> def point_count(self):

Node [Domain Size](node.blender_ref) ( [api](node.blender_python_ref) )

Node implemented as property.

### Returns:

  socket 'point_count'

## sample_nearest_surface {#sample_nearest_surface}

> def sample_nearest_surface(self, value=None, sample_position=None):

Node [Sample Nearest Surface](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- sample_position: Vector

### Returns:

  socket 'value'

## sample_uv_surface {#sample_uv_surface}

> def sample_uv_surface(self, value=None, source_uv_map=None, sample_uv=None):

Node [Sample UV Surface](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- source_uv_map: Vector
- sample_uv: Vector

### Returns:

- tuple ('value', 'is_valid')

## scale_elements {#scale_elements}

> def scale_elements(self, selection=None, scale=None, center=None, axis=None, domain='FACE', scale_mode='UNIFORM'):

Node [Scale Elements](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]
- scale_mode (str): 'UNIFORM' in [UNIFORM, SINGLE_AXIS]

### Returns:

- node with sockets ['geometry']

## scale_single_axis {#scale_single_axis}

> def scale_single_axis(self, selection=None, scale=None, center=None, axis=None, domain='FACE'):

Node [Scale Elements](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- scale: Float
- center: Vector
- axis: Vector
- domain (str): 'FACE' in [FACE, EDGE]

### Returns:

- node with sockets ['geometry']

## scale_uniform {#scale_uniform}

> def scale_uniform(self, selection=None, scale=None, center=None, domain='FACE'):

Node [Scale Elements](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- scale: Float
- center: Vector
- domain (str): 'FACE' in [FACE, EDGE]

### Returns:

- node with sockets ['geometry']

## set_shade_smooth {#set_shade_smooth}

> def set_shade_smooth(self, selection=None, shade_smooth=None):

Node [Set Shade Smooth](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- shade_smooth: Boolean

### Returns:

- node with sockets ['geometry']

## shortest_edge_paths {#shortest_edge_paths}

> def shortest_edge_paths(self, end_vertex=None, edge_cost=None):

Node [Shortest Edge Paths](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- end_vertex: Boolean
- edge_cost: Float

### Returns:

- tuple ('next_vertex_index', 'total_cost')

## split_edges {#split_edges}

> def split_edges(self, selection=None):

Node [Split Edges](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean

### Returns:

- node with sockets ['mesh']

## subdivide {#subdivide}

> def subdivide(self, level=None):

Node [Subdivide Mesh](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- level: Integer

### Returns:

- node with sockets ['mesh']

## subdivision_surface {#subdivision_surface}

> def subdivision_surface(self, level=None, edge_crease=None, vertex_crease=None, boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES'):

Node [Subdivision Surface](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- level: Integer
- edge_crease: Float
- vertex_crease: Float
- boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
- uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]

### Returns:

- node with sockets ['mesh']

## to_curve {#to_curve}

> def to_curve(self, selection=None):

Node [Mesh to Curve](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean

### Returns:

  socket 'curve' of class Curve

## to_points {#to_points}

> def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):

Node [Mesh to Points](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- position: Vector
- radius: Float
- mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]

### Returns:

  socket 'points' of class Points

## to_volume {#to_volume}

> def to_volume(self, density=None, voxel_size=None, voxel_amount=None, exterior_band_width=None, interior_band_width=None, fill_volume=None, resolution_mode='VOXEL_AMOUNT'):

Node [Mesh to Volume](node.blender_ref) ( [api](node.blender_python_ref) )

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

## triangulate {#triangulate}

> def triangulate(self, selection=None, minimum_vertices=None, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL'):

Node [Triangulate](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- minimum_vertices: Integer
- ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
- quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]

### Returns:

- node with sockets ['mesh']

## uv_unwrap {#uv_unwrap}

> def uv_unwrap(self, selection=None, seam=None, margin=None, fill_holes=None, method='ANGLE_BASED'):

Node [UV Unwrap](node.blender_ref) ( [api](node.blender_python_ref) )

        ### Args:
- selection: Boolean
- seam: Boolean
- margin: Float
- fill_holes: Boolean
- method (str): 'ANGLE_BASED' in [ANGLE_BASED, CONFORMAL]

### Returns:

  socket 'uv'

