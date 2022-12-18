
# Data socket Mesh

> Inherits from gn.Geometry
  
<sub>go to [index](/docs/index.md)</sub>



## Constructors

- [Circle](#circle) : mesh (Mesh)
- [Cone](#cone) : Sockets      [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
- [Cube](#cube) : mesh (Mesh)
- [Cylinder](#cylinder) : Sockets      [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
- [Grid](#grid) : mesh (Mesh)
- [IcoSphere](#icosphere) : mesh (Mesh)
- [Line](#line) : mesh (Mesh)
- [UVSphere](#uvsphere) : mesh (Mesh)

## Properties

- [corner_count](#corner_count) : face_corner_count (Integer) = domain_size.face_corner_count
- [domain_size](#domain_size) : Sockets      [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
- [edge_count](#edge_count) : edge_count (Integer) = domain_size.edge_count
- [face_count](#face_count) : face_count (Integer) = domain_size.face_count
- [point_count](#point_count) : point_count (Integer) = domain_size.point_count

## Methods

- [difference](#difference) : Sockets      [mesh (Mesh), intersecting_edges (Boolean)]
- [distribute_points_on_faces](#distribute_points_on_faces) : Sockets      [points (Points), normal (Vector), rotation (Vector)]
- [dual](#dual) : dual_mesh (Geometry)
- [duplicate_edges](#duplicate_edges) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [duplicate_faces](#duplicate_faces) : Sockets      [geometry (Geometry), duplicate_index (Integer)]
- [edge_paths_to_curves](#edge_paths_to_curves) : curves (Curve)
- [extrude](#extrude) : Sockets      [mesh (Mesh), top (Boolean), side (Boolean)]
- [flip_faces](#flip_faces) : mesh (Mesh)
- [intersect](#intersect) : Sockets      [mesh (Mesh), intersecting_edges (Boolean)]
- [split_edges](#split_edges) : mesh (Mesh)
- [subdivide](#subdivide) : mesh (Mesh)
- [subdivision_surface](#subdivision_surface) : mesh (Mesh)
- [to_curve](#to_curve) : curve (Curve)
- [to_points](#to_points) : points (Points)
- [to_volume](#to_volume) : volume (Volume)
- [triangulate](#triangulate) : mesh (Mesh)
- [union](#union) : Sockets      [mesh (Mesh), intersecting_edges (Boolean)]

## Circle

Geometry node [*Mesh Circle*].


  Args:
    vertices: Integer
    radius: Float
    fill_type (str): 'NONE' in [NONE, NGON, TRIANGLE_FAN]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MeshCircle`
  
  
  .. blid:: GeometryNodeMeshCircle
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type, label=node_label, node_color=node_color)
    

## Cone

Geometry node [*Cone*].


  Args:
    vertices: Integer
    side_segments: Integer
    fill_segments: Integer
    radius_top: Float
    radius_bottom: Float
    depth: Float
    fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Cone`
  
  
  .. blid:: GeometryNodeMeshCone
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)
    

## Cube

Geometry node [*Cube*].


  Args:
    size: Vector
    vertices_x: Integer
    vertices_y: Integer
    vertices_z: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Cube`
  
  
  .. blid:: GeometryNodeMeshCube
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z, label=node_label, node_color=node_color)
    

## Cylinder

Geometry node [*Cylinder*].


  Args:
    vertices: Integer
    side_segments: Integer
    fill_segments: Integer
    radius: Float
    depth: Float
    fill_type (str): 'NGON' in [NONE, NGON, TRIANGLE_FAN]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Cylinder`
  
  
  .. blid:: GeometryNodeMeshCylinder
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type, label=node_label, node_color=node_color)
    

## Grid

Geometry node [*Grid*].


  Args:
    size_x: Float
    size_y: Float
    vertices_x: Integer
    vertices_y: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Grid`
  
  
  .. blid:: GeometryNodeMeshGrid
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y, label=node_label, node_color=node_color)
    

## IcoSphere

Geometry node [*Ico Sphere*].


  Args:
    radius: Float
    subdivisions: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.IcoSphere`
  
  
  .. blid:: GeometryNodeMeshIcoSphere
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.IcoSphere(radius=radius, subdivisions=subdivisions, label=node_label, node_color=node_color)
    

## Line

Geometry node [*Mesh Line*].


  Args:
    count: Integer
    start_location: Vector
    offset: Vector
    count_mode (str): 'TOTAL' in [TOTAL, RESOLUTION]
    mode (str): 'OFFSET' in [OFFSET, END_POINTS]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MeshLine`
  
  
  .. blid:: GeometryNodeMeshLine
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode, label=node_label, node_color=node_color)
    

## UVSphere

Geometry node [*UV Sphere*].


  Args:
    segments: Integer
    rings: Integer
    radius: Float
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.UvSphere`
  
  
  .. blid:: GeometryNodeMeshUVSphere
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.UvSphere(segments=segments, rings=rings, radius=radius, label=node_label, node_color=node_color)
    

## domain_size

Geometry node [*Domain Size*].



  Returns:
    Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'MESH'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.domain_size")
    

## point_count

Geometry node [*Domain Size*].



  Returns:
    Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'MESH'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.point_count")
    

## edge_count

Geometry node [*Domain Size*].



  Returns:
    Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'MESH'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.edge_count")
    

## face_count

Geometry node [*Domain Size*].



  Returns:
    Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'MESH'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.face_count")
    

## corner_count

Geometry node [*Domain Size*].



  Returns:
    Sockets [point_count (Integer), edge_count (Integer), face_count (Integer), face_corner_count (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DomainSize`
  
  - component = 'MESH'
    
  .. blid:: GeometryNodeAttributeDomainSize
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DomainSize(geometry=self, component='MESH', label=f"{self.node_chain_label}.corner_count")
    

## intersect

Geometry node [*Mesh Boolean*].


  Args:
    self_intersection: Boolean
    hole_tolerant: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [mesh (Mesh), intersecting_edges (Boolean)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MeshBoolean`
  
  - operation = 'INTERSECT'
    
  .. blid:: GeometryNodeMeshBoolean
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT', label=node_label, node_color=node_color)
    

## union

Geometry node [*Mesh Boolean*].


  Args:
    self_intersection: Boolean
    hole_tolerant: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [mesh (Mesh), intersecting_edges (Boolean)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MeshBoolean`
  
  - operation = 'UNION'
    
  .. blid:: GeometryNodeMeshBoolean
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MeshBoolean(self, *mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION', label=node_label, node_color=node_color)
    

## difference

Geometry node [*Mesh Boolean*].


  Args:
    mesh_2: <m>Geometry
    self_intersection: Boolean
    hole_tolerant: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [mesh (Mesh), intersecting_edges (Boolean)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MeshBoolean`
  
  - operation = 'DIFFERENCE'
    
  .. blid:: GeometryNodeMeshBoolean
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE', label=node_label, node_color=node_color)
    

## split_edges

Geometry node [*Split Edges*].


  Args:
    selection: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SplitEdges`
  
  
  .. blid:: GeometryNodeSplitEdges
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SplitEdges(mesh=self, selection=selection, label=node_label, node_color=node_color)
    

## subdivide

Geometry node [*Subdivide Mesh*].


  Args:
    level: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SubdivideMesh`
  
  
  .. blid:: GeometryNodeSubdivideMesh
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SubdivideMesh(mesh=self, level=level, label=node_label, node_color=node_color)
    

## subdivision_surface

Geometry node [*Subdivision Surface*].


  Args:
    level: Integer
    edge_crease: Float
    vertex_crease: Float
    boundary_smooth (str): 'ALL' in [PRESERVE_CORNERS, ALL]
    uv_smooth (str): 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.SubdivisionSurface`
  
  
  .. blid:: GeometryNodeSubdivisionSurface
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.SubdivisionSurface(mesh=self, level=level, edge_crease=edge_crease, vertex_crease=vertex_crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth, label=node_label, node_color=node_color)
    

## triangulate

Geometry node [*Triangulate*].


  Args:
    selection: Boolean
    minimum_vertices: Integer
    ngon_method (str): 'BEAUTY' in [BEAUTY, CLIP]
    quad_method (str): 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.Triangulate`
  
  
  .. blid:: GeometryNodeTriangulate
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method, label=node_label, node_color=node_color)
    

## dual

Geometry node [*Dual Mesh*].


  Args:
    keep_boundaries: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Geometry
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DualMesh`
  
  
  .. blid:: GeometryNodeDualMesh
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DualMesh(mesh=self, keep_boundaries=keep_boundaries, label=node_label, node_color=node_color)
    

## flip_faces

Geometry node [*Flip Faces*].


  Args:
    selection: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Mesh
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.FlipFaces`
  
  
  .. blid:: GeometryNodeFlipFaces
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.FlipFaces(mesh=self, selection=selection, label=node_label, node_color=node_color)
    

## duplicate_edges

Geometry node [*Duplicate Elements*].


  Args:
    selection: Boolean
    amount: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [geometry (Geometry), duplicate_index (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DuplicateElements`
  
  - domain = 'EDGE'
    
  .. blid:: GeometryNodeDuplicateElements
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='EDGE', label=node_label, node_color=node_color)
    

## duplicate_faces

Geometry node [*Duplicate Elements*].


  Args:
    selection: Boolean
    amount: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [geometry (Geometry), duplicate_index (Integer)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DuplicateElements`
  
  - domain = 'FACE'
    
  .. blid:: GeometryNodeDuplicateElements
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='FACE', label=node_label, node_color=node_color)
    

## extrude

Geometry node [*Extrude Mesh*].


  Args:
    selection: Boolean
    offset: Vector
    offset_scale: Float
    individual: Boolean
    mode (str): 'FACES' in [VERTICES, EDGES, FACES]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [mesh (Mesh), top (Boolean), side (Boolean)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.ExtrudeMesh`
  
  
  .. blid:: GeometryNodeExtrudeMesh
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode, label=node_label, node_color=node_color)
    

## to_curve

Geometry node [*Mesh to Curve*].


  Args:
    selection: Boolean
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MeshToCurve`
  
  
  .. blid:: GeometryNodeMeshToCurve
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MeshToCurve(mesh=self, selection=selection, label=node_label, node_color=node_color)
    

## to_volume

Geometry node [*Mesh to Volume*].


  Args:
    density: Float
    voxel_size: Float
    voxel_amount: Float
    exterior_band_width: Float
    interior_band_width: Float
    fill_volume: Boolean
    resolution_mode (str): 'VOXEL_AMOUNT' in [VOXEL_AMOUNT, VOXEL_SIZE]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Volume
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MeshToVolume`
  
  
  .. blid:: GeometryNodeMeshToVolume
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MeshToVolume(mesh=self, density=density, voxel_size=voxel_size, voxel_amount=voxel_amount, exterior_band_width=exterior_band_width, interior_band_width=interior_band_width, fill_volume=fill_volume, resolution_mode=resolution_mode, label=node_label, node_color=node_color)
    

## to_points

Geometry node [*Mesh to Points*].


  Args:
    selection: Boolean
    position: Vector
    radius: Float
    mode (str): 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Points
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.MeshToPoints`
  
  
  .. blid:: GeometryNodeMeshToPoints
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode, label=node_label, node_color=node_color)
    

## distribute_points_on_faces

Geometry node [*Distribute Points on Faces*].


  Args:
    selection: Boolean
    distance_min: Float
    density_max: Float
    density: Float
    density_factor: Float
    seed: Integer
    distribute_method (str): 'RANDOM' in [RANDOM, POISSON]
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Sockets [points (Points), normal (Vector), rotation (Vector)]
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.DistributePointsOnFaces`
  
  
  .. blid:: GeometryNodeDistributePointsOnFaces
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method, label=node_label, node_color=node_color)
    

## edge_paths_to_curves

Geometry node [*Edge Paths to Curves*].


  Args:
    start_vertices: Boolean
    next_vertex_index: Integer
    node_label (str): Node label
    node_color (color): Node background color
    
  Returns:
    Curve
    
  **Node creation**
  
  Node :class:`~geonodes.nodes.nodes.EdgePathsToCurves`
  
  
  .. blid:: GeometryNodeEdgePathsToCurves
  
  .. code-block:: python
  
    from geonodes import nodes
    nodes.EdgePathsToCurves(mesh=self, start_vertices=start_vertices, next_vertex_index=next_vertex_index, label=node_label, node_color=node_color)
    
