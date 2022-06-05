
# Class Mesh

> Inherits from: ***Geometry***

## Constructors



- [Circle](#circle) : mesh (Mesh)
- [Cone](#cone) : Sockets      [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
- [Cube](#cube) : mesh (Mesh)
- [Cylinder](#cylinder) : Sockets      [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
- [Grid](#grid) : mesh (Mesh)
- [IcoSphere](#icosphere) : mesh (Mesh)
- [Line](#line) : mesh (Mesh)
- [UVSphere](#uvsphere) : mesh (Mesh)



## Attribute capture



- [capture_edge_angle](#capture_edge_angle) : Sockets      [unsigned_angle (Float), signed_angle (Float)]
- [capture_edge_neighbors](#capture_edge_neighbors) : face_count (Integer)
- [capture_edge_vertices](#capture_edge_vertices) : Sockets      [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
- [capture_face_area](#capture_face_area) : area (Float)
- [capture_face_neighbors](#capture_face_neighbors) : Sockets      [vertex_count (Integer), face_count (Integer)]
- [capture_island](#capture_island) : Sockets      [island_index (Integer), island_count (Integer)]
- [capture_material_index](#capture_material_index) : material_index (Integer)
- [capture_material_selection](#capture_material_selection) : selection (Boolean)
- [capture_shade_smooth](#capture_shade_smooth) : smooth (Boolean)
- [capture_vertex_neighbors](#capture_vertex_neighbors) : Sockets      [vertex_count (Integer), face_count (Integer)]



## Attributes



- [corner_ID](#corner_id) : Float = capture_ID(domain='CORNER').unsigned_angle
- [corner_index](#corner_index) : Float = capture_index(domain='CORNER').unsigned_angle
- [corner_porision](#corner_porision) : Float = capture_position(domain='CORNER').unsigned_angle
- [edge_angle](#edge_angle) : Float = capture_edge_angle(domain='EDGE').unsigned_angle
- [edge_neighbors](#edge_neighbors) : Integer = capture_edge_neighbors(domain='EDGE')
- [edge_unsigned_angle](#edge_unsigned_angle) : Float = capture_edge_angle(domain='EDGE').signed_angle
- [edge_vertices_index1](#edge_vertices_index1) : Integer = capture_edge_vertices(domain='EDGE').vertex_index_1
- [edge_vertices_index2](#edge_vertices_index2) : Integer = capture_edge_vertices(domain='EDGE').vertex_index_2
- [edge_vertices_position1](#edge_vertices_position1) : Vector = capture_edge_vertices(domain='EDGE').position_1
- [edge_vertices_position2](#edge_vertices_position2) : Vector = capture_edge_vertices(domain='EDGE').position_2
- [egde_ID](#egde_id) : Float = capture_ID(domain='EDGE').unsigned_angle
- [egde_index](#egde_index) : Float = capture_index(domain='EDGE').unsigned_angle
- [egde_position](#egde_position) : Float = capture_position(domain='EDGE').unsigned_angle
- [face_ID](#face_id) : Float = capture_ID(domain='FACE').unsigned_angle
- [face_area](#face_area) : Float = capture_face_area(domain='FACE')
- [face_index](#face_index) : Float = capture_index(domain='FACE').unsigned_angle
- [face_neighbors_face_count](#face_neighbors_face_count) : Integer = capture_face_neighbors(domain='FACE').face_count
- [face_neighbors_vertex_count](#face_neighbors_vertex_count) : Integer = capture_face_neighbors(domain='FACE').vertex_count
- [face_position](#face_position) : Float = capture_position(domain='FACE').unsigned_angle
- [island](#island) : Integer = capture_island(domain='POINT').island_index
- [material_index](#material_index) : Integer = capture_material_index(domain='FACE')
- [material_selection](#material_selection) : Boolean = capture_material_selection(domain='FACE')
- [shade_smooth](#shade_smooth) : Boolean = capture_shade_smooth(domain='FACE')
- [vertex_neighbors_face_count](#vertex_neighbors_face_count) : Integer = capture_vertex_neighbors(domain='POINT').face_count
- [vertex_neighbors_vertex_count](#vertex_neighbors_vertex_count) : Integer = capture_vertex_neighbors(domain='POINT').vertex_count



## Methods



- [difference](#difference) : mesh (Mesh)
- [distribute_points_on_faces](#distribute_points_on_faces) : Sockets      [points (Points), normal (Vector), rotation (Vector)]
- [extrude](#extrude) : Sockets      [mesh (Mesh), top (Boolean), side (Boolean)]
- [intersect](#intersect) : mesh (Mesh)
- [to_curve](#to_curve) : curve (Curve)
- [to_points](#to_points) : points (Points)
- [union](#union) : mesh (Mesh)



## Stacked methods



- [dual](#dual) : Mesh
- [flip_faces](#flip_faces) : Mesh
- [split_edges](#split_edges) : Mesh
- [subdivide](#subdivide) : Mesh
- [subdivision_surface](#subdivision_surface) : Mesh
- [triangulate](#triangulate) : Mesh



## Methods reference


### Circle

> Node: [MeshCircle](../nodes/{self.node_name}.md)

```python
v = Mesh.Circle(vertices, radius, fill_type)
```


#### Arguments


##### Sockets arguments



- vertices : Integer
- radius : Float



##### Parameters arguments



- fill_type : 'NONE' in [NONE, NGON, TRIANGLE_FAN]



#### Node creation


```python
node = nodes.MeshCircle(vertices=vertices, radius=radius, fill_type=fill_type)
```


#### Returns

    Mesh

### Cone

> Node: [Cone](../nodes/{self.node_name}.md)

```python
v = Mesh.Cone(vertices, side_segments, fill_segments, radius_top, radius_bottom, depth, fill_type)
```


#### Arguments


##### Sockets arguments



- vertices : Integer
- side_segments : Integer
- fill_segments : Integer
- radius_top : Float
- radius_bottom : Float
- depth : Float



##### Parameters arguments



- fill_type : 'NGON' in [NONE, NGON, TRIANGLE_FAN]



#### Node creation


```python
node = nodes.Cone(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius_top=radius_top, radius_bottom=radius_bottom, depth=depth, fill_type=fill_type)
```


#### Returns

    Sockets [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]

### Cube

> Node: [Cube](../nodes/{self.node_name}.md)

```python
v = Mesh.Cube(size, vertices_x, vertices_y, vertices_z)
```


#### Arguments


##### Sockets arguments



- size : Vector
- vertices_x : Integer
- vertices_y : Integer
- vertices_z : Integer



#### Node creation


```python
node = nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z)
```


#### Returns

    Mesh

### Cylinder

> Node: [Cylinder](../nodes/{self.node_name}.md)

```python
v = Mesh.Cylinder(vertices, side_segments, fill_segments, radius, depth, fill_type)
```


#### Arguments


##### Sockets arguments



- vertices : Integer
- side_segments : Integer
- fill_segments : Integer
- radius : Float
- depth : Float



##### Parameters arguments



- fill_type : 'NGON' in [NONE, NGON, TRIANGLE_FAN]



#### Node creation


```python
node = nodes.Cylinder(vertices=vertices, side_segments=side_segments, fill_segments=fill_segments, radius=radius, depth=depth, fill_type=fill_type)
```


#### Returns

    Sockets [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]

### Grid

> Node: [Grid](../nodes/{self.node_name}.md)

```python
v = Mesh.Grid(size_x, size_y, vertices_x, vertices_y)
```


#### Arguments


##### Sockets arguments



- size_x : Float
- size_y : Float
- vertices_x : Integer
- vertices_y : Integer



#### Node creation


```python
node = nodes.Grid(size_x=size_x, size_y=size_y, vertices_x=vertices_x, vertices_y=vertices_y)
```


#### Returns

    Mesh

### IcoSphere

> Node: [IcoSphere](../nodes/{self.node_name}.md)

```python
v = Mesh.IcoSphere(radius, subdivisions)
```


#### Arguments


##### Sockets arguments



- radius : Float
- subdivisions : Integer



#### Node creation


```python
node = nodes.IcoSphere(radius=radius, subdivisions=subdivisions)
```


#### Returns

    Mesh

### Line

> Node: [MeshLine](../nodes/{self.node_name}.md)

```python
v = Mesh.Line(count, start_location, offset, count_mode, mode)
```


#### Arguments


##### Sockets arguments



- count : Integer
- start_location : Vector
- offset : Vector



##### Parameters arguments



- count_mode : 'TOTAL' in [TOTAL, RESOLUTION]
- mode : 'OFFSET' in [OFFSET, END_POINTS]



#### Node creation


```python
node = nodes.MeshLine(count=count, start_location=start_location, offset=offset, count_mode=count_mode, mode=mode)
```


#### Returns

    Mesh

### UVSphere

> Node: [UvSphere](../nodes/{self.node_name}.md)

```python
v = Mesh.UVSphere(segments, rings, radius)
```


#### Arguments


##### Sockets arguments



- segments : Integer
- rings : Integer
- radius : Float



#### Node creation


```python
node = nodes.UvSphere(segments=segments, rings=rings, radius=radius)
```


#### Returns

    Mesh

### capture_edge_angle

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.capture_edge_angle(self, domain='EDGE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'EDGE'



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Sockets [unsigned_angle (Float), signed_angle (Float)]

### capture_edge_neighbors

> Node: [EdgeNeighbors](../nodes/{self.node_name}.md)

```python
v = mesh.capture_edge_neighbors(self, domain='EDGE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'EDGE'



#### Node creation


```python
node = nodes.EdgeNeighbors()
```


#### Returns

    Integer

### capture_edge_vertices

> Node: [EdgeVertices](../nodes/{self.node_name}.md)

```python
v = mesh.capture_edge_vertices(self, domain='EDGE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'EDGE'



#### Node creation


```python
node = nodes.EdgeVertices()
```


#### Returns

    Sockets [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]

### capture_face_area

> Node: [FaceArea](../nodes/{self.node_name}.md)

```python
v = mesh.capture_face_area(self, domain='FACE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'FACE'



#### Node creation


```python
node = nodes.FaceArea()
```


#### Returns

    Float

### capture_face_neighbors

> Node: [FaceNeighbors](../nodes/{self.node_name}.md)

```python
v = mesh.capture_face_neighbors(self, domain='FACE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'FACE'



#### Node creation


```python
node = nodes.FaceNeighbors()
```


#### Returns

    Sockets [vertex_count (Integer), face_count (Integer)]

### capture_island

> Node: [MeshIsland](../nodes/{self.node_name}.md)

```python
v = mesh.capture_island(self, domain='POINT')
```


#### Arguments


##### Parameters arguments



- self
- domain:'POINT'



#### Node creation


```python
node = nodes.MeshIsland()
```


#### Returns

    Sockets [island_index (Integer), island_count (Integer)]

### capture_material_index

> Node: [MaterialIndex](../nodes/{self.node_name}.md)

```python
v = mesh.capture_material_index(self, domain='FACE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'FACE'



#### Node creation


```python
node = nodes.MaterialIndex()
```


#### Returns

    Integer

### capture_material_selection

> Node: [MaterialSelection](../nodes/{self.node_name}.md)

```python
v = mesh.capture_material_selection(self, material, domain='FACE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'FACE'



##### Sockets arguments



- material : Material



#### Node creation


```python
node = nodes.MaterialSelection(material=material)
```


#### Returns

    Boolean

### capture_shade_smooth

> Node: [IsShadeSmooth](../nodes/{self.node_name}.md)

```python
v = mesh.capture_shade_smooth(self, domain='FACE')
```


#### Arguments


##### Parameters arguments



- self
- domain:'FACE'



#### Node creation


```python
node = nodes.IsShadeSmooth()
```


#### Returns

    Boolean

### capture_vertex_neighbors

> Node: [VertexNeighbors](../nodes/{self.node_name}.md)

```python
v = mesh.capture_vertex_neighbors(self, domain='POINT')
```


#### Arguments


##### Parameters arguments



- self
- domain:'POINT'



#### Node creation


```python
node = nodes.VertexNeighbors()
```


#### Returns

    Sockets [vertex_count (Integer), face_count (Integer)]

### corner_ID

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.corner_ID(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### corner_index

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.corner_index(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### corner_porision

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.corner_porision(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### difference

> Node: [MeshBoolean](../nodes/{self.node_name}.md)

```python
v = mesh.difference(mesh_2_1, mesh_2_2, mesh_2_3, self_intersection, hole_tolerant)
```


#### Arguments


##### Sockets arguments



- mesh_1 : Geometry (self)
- mesh_2 : *Geometry
- self_intersection : Boolean
- hole_tolerant : Boolean



##### Fixed parameters



- operation : 'DIFFERENCE'



#### Node creation


```python
node = nodes.MeshBoolean(*mesh_2, mesh_1=self, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='DIFFERENCE')
```


#### Returns

    Mesh

### distribute_points_on_faces

> Node: [DistributePointsOnFaces](../nodes/{self.node_name}.md)

```python
v = mesh.distribute_points_on_faces(selection, distance_min, density_max, density, density_factor, seed, distribute_method)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- selection : Boolean
- distance_min : Float
- density_max : Float
- density : Float
- density_factor : Float
- seed : Integer



##### Parameters arguments



- distribute_method : 'RANDOM' in [RANDOM, POISSON]



#### Node creation


```python
node = nodes.DistributePointsOnFaces(mesh=self, selection=selection, distance_min=distance_min, density_max=density_max, density=density, density_factor=density_factor, seed=seed, distribute_method=distribute_method)
```


#### Returns

    Sockets [points (Points), normal (Vector), rotation (Vector)]

### dual

> Node: [DualMesh](../nodes/{self.node_name}.md)

```python
mesh.dual(keep_boundaries)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- keep_boundaries : Boolean



#### Node creation


```python
node = nodes.DualMesh(mesh=self, keep_boundaries=keep_boundaries)
```


#### Returns

    self

### edge_angle

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.edge_angle(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### edge_neighbors

> Node: [EdgeNeighbors](../nodes/{self.node_name}.md)

```python
v = mesh.edge_neighbors(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeNeighbors()
```


#### Returns

    Integer

### edge_unsigned_angle

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.edge_unsigned_angle(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### edge_vertices_index1

> Node: [EdgeVertices](../nodes/{self.node_name}.md)

```python
v = mesh.edge_vertices_index1(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeVertices()
```


#### Returns

    Integer

### edge_vertices_index2

> Node: [EdgeVertices](../nodes/{self.node_name}.md)

```python
v = mesh.edge_vertices_index2(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeVertices()
```


#### Returns

    Integer

### edge_vertices_position1

> Node: [EdgeVertices](../nodes/{self.node_name}.md)

```python
v = mesh.edge_vertices_position1(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeVertices()
```


#### Returns

    Vector

### edge_vertices_position2

> Node: [EdgeVertices](../nodes/{self.node_name}.md)

```python
v = mesh.edge_vertices_position2(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeVertices()
```


#### Returns

    Vector

### egde_ID

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.egde_ID(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### egde_index

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.egde_index(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### egde_position

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.egde_position(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### extrude

> Node: [ExtrudeMesh](../nodes/{self.node_name}.md)

```python
v = mesh.extrude(selection, offset, offset_scale, individual, mode)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- selection : Boolean
- offset : Vector
- offset_scale : Float
- individual : Boolean



##### Parameters arguments



- mode : 'FACES' in [VERTICES, EDGES, FACES]



#### Node creation


```python
node = nodes.ExtrudeMesh(mesh=self, selection=selection, offset=offset, offset_scale=offset_scale, individual=individual, mode=mode)
```


#### Returns

    Sockets [mesh (Mesh), top (Boolean), side (Boolean)]

### face_ID

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.face_ID(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### face_area

> Node: [FaceArea](../nodes/{self.node_name}.md)

```python
v = mesh.face_area(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.FaceArea()
```


#### Returns

    Float

### face_index

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.face_index(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### face_neighbors_face_count

> Node: [FaceNeighbors](../nodes/{self.node_name}.md)

```python
v = mesh.face_neighbors_face_count(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.FaceNeighbors()
```


#### Returns

    Integer

### face_neighbors_vertex_count

> Node: [FaceNeighbors](../nodes/{self.node_name}.md)

```python
v = mesh.face_neighbors_vertex_count(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.FaceNeighbors()
```


#### Returns

    Integer

### face_position

> Node: [EdgeAngle](../nodes/{self.node_name}.md)

```python
v = mesh.face_position(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.EdgeAngle()
```


#### Returns

    Float

### flip_faces

> Node: [FlipFaces](../nodes/{self.node_name}.md)

```python
mesh.flip_faces(selection)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- selection : Boolean



#### Node creation


```python
node = nodes.FlipFaces(mesh=self, selection=selection)
```


#### Returns

    self

### intersect

> Node: [MeshBoolean](../nodes/{self.node_name}.md)

```python
v = mesh.intersect(mesh_2_1, mesh_2_2, mesh_2_3, self_intersection, hole_tolerant)
```


#### Arguments


##### Sockets arguments



- mesh_2 : *Geometry
- self_intersection : Boolean
- hole_tolerant : Boolean



##### Fixed parameters



- operation : 'INTERSECT'



#### Node creation


```python
node = nodes.MeshBoolean(*mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='INTERSECT')
```


#### Returns

    Mesh

### island

> Node: [MeshIsland](../nodes/{self.node_name}.md)

```python
v = mesh.island(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.MeshIsland()
```


#### Returns

    Integer

### material_index

> Node: [MaterialIndex](../nodes/{self.node_name}.md)

```python
v = mesh.material_index(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.MaterialIndex()
```


#### Returns

    Integer

### material_selection

> Node: [MaterialSelection](../nodes/{self.node_name}.md)

```python
v = mesh.material_selection(self, material)
```


#### Arguments


##### Parameters arguments



- self



##### Sockets arguments



- material : Material



#### Node creation


```python
node = nodes.MaterialSelection(material=material)
```


#### Returns

    Boolean

### shade_smooth

> Node: [IsShadeSmooth](../nodes/{self.node_name}.md)

```python
v = mesh.shade_smooth(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.IsShadeSmooth()
```


#### Returns

    Boolean

### split_edges

> Node: [SplitEdges](../nodes/{self.node_name}.md)

```python
mesh.split_edges(selection)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- selection : Boolean



#### Node creation


```python
node = nodes.SplitEdges(mesh=self, selection=selection)
```


#### Returns

    self

### subdivide

> Node: [SubdivideMesh](../nodes/{self.node_name}.md)

```python
mesh.subdivide(level)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- level : Integer



#### Node creation


```python
node = nodes.SubdivideMesh(mesh=self, level=level)
```


#### Returns

    self

### subdivision_surface

> Node: [SubdivisionSurface](../nodes/{self.node_name}.md)

```python
mesh.subdivision_surface(level, crease, boundary_smooth, uv_smooth)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- level : Integer
- crease : Float



##### Parameters arguments



- boundary_smooth : 'ALL' in [PRESERVE_CORNERS, ALL]
- uv_smooth : 'PRESERVE_BOUNDARIES' in [NONE, PRESERVE_CORNERS, PRESERVE_CORNERS_AND_JUNCTIONS, PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE, PRESERVE_BOUNDARIES, SMOOTH_ALL]



#### Node creation


```python
node = nodes.SubdivisionSurface(mesh=self, level=level, crease=crease, boundary_smooth=boundary_smooth, uv_smooth=uv_smooth)
```


#### Returns

    self

### to_curve

> Node: [MeshToCurve](../nodes/{self.node_name}.md)

```python
v = mesh.to_curve(selection)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- selection : Boolean



#### Node creation


```python
node = nodes.MeshToCurve(mesh=self, selection=selection)
```


#### Returns

    Curve

### to_points

> Node: [MeshToPoints](../nodes/{self.node_name}.md)

```python
v = mesh.to_points(selection, position, radius, mode)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- selection : Boolean
- position : Vector
- radius : Float



##### Parameters arguments



- mode : 'VERTICES' in [VERTICES, EDGES, FACES, CORNERS]



#### Node creation


```python
node = nodes.MeshToPoints(mesh=self, selection=selection, position=position, radius=radius, mode=mode)
```


#### Returns

    Points

### triangulate

> Node: [Triangulate](../nodes/{self.node_name}.md)

```python
mesh.triangulate(selection, minimum_vertices, ngon_method, quad_method)
```


#### Arguments


##### Sockets arguments



- mesh : Mesh (self)
- selection : Boolean
- minimum_vertices : Integer



##### Parameters arguments



- ngon_method : 'BEAUTY' in [BEAUTY, CLIP]
- quad_method : 'SHORTEST_DIAGONAL' in [BEAUTY, FIXED, FIXED_ALTERNATE, SHORTEST_DIAGONAL, LONGEST_DIAGONAL]



#### Node creation


```python
node = nodes.Triangulate(mesh=self, selection=selection, minimum_vertices=minimum_vertices, ngon_method=ngon_method, quad_method=quad_method)
```


#### Returns

    self

### union

> Node: [MeshBoolean](../nodes/{self.node_name}.md)

```python
v = mesh.union(mesh_2_1, mesh_2_2, mesh_2_3, self_intersection, hole_tolerant)
```


#### Arguments


##### Sockets arguments



- mesh_2 : *Geometry
- self_intersection : Boolean
- hole_tolerant : Boolean



##### Fixed parameters



- operation : 'UNION'



#### Node creation


```python
node = nodes.MeshBoolean(*mesh_2, self_intersection=self_intersection, hole_tolerant=hole_tolerant, operation='UNION')
```


#### Returns

    Mesh

### vertex_neighbors_face_count

> Node: [VertexNeighbors](../nodes/{self.node_name}.md)

```python
v = mesh.vertex_neighbors_face_count(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.VertexNeighbors()
```


#### Returns

    Integer

### vertex_neighbors_vertex_count

> Node: [VertexNeighbors](../nodes/{self.node_name}.md)

```python
v = mesh.vertex_neighbors_vertex_count(self)
```


#### Arguments


##### Parameters arguments



- self



#### Node creation


```python
node = nodes.VertexNeighbors()
```


#### Returns

    Integer
