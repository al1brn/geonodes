
# Class Mesh

> Inherits from: ***Geometry***

## Constructors



- Circle : mesh (Mesh)
- Cone : Sockets      [mesh (Mesh), top (Boolean), bottom (Boolean), side (Boolean)]
- Cube : mesh (Mesh)
- Cylinder : Sockets      [mesh (Mesh), top (Boolean), side (Boolean), bottom (Boolean)]
- Grid : mesh (Mesh)
- IcoSphere : mesh (Mesh)
- Line : mesh (Mesh)
- UVSphere : mesh (Mesh)



## Attribute capture



- capture_edge_angle : Sockets      [unsigned_angle (Float), signed_angle (Float)]
- capture_edge_neighbors : face_count (Integer)
- capture_edge_vertices : Sockets      [vertex_index_1 (Integer), vertex_index_2 (Integer), position_1 (Vector), position_2 (Vector)]
- capture_face_area : area (Float)
- capture_face_neighbors : Sockets      [vertex_count (Integer), face_count (Integer)]
- capture_island : Sockets      [island_index (Integer), island_count (Integer)]
- capture_material_index : material_index (Integer)
- capture_material_selection : selection (Boolean)
- capture_shade_smooth : smooth (Boolean)
- capture_vertex_neighbors : Sockets      [vertex_count (Integer), face_count (Integer)]



## Attributes



- corner_ID : Float = capture_ID(domain='CORNER').unsigned_angle
- corner_index : Float = capture_index(domain='CORNER').unsigned_angle
- corner_porision : Float = capture_position(domain='CORNER').unsigned_angle
- edge_angle : Float = capture_edge_angle(domain='EDGE').unsigned_angle
- edge_neighbors : Integer = capture_edge_neighbors(domain='EDGE')
- edge_unsigned_angle : Float = capture_edge_angle(domain='EDGE').signed_angle
- edge_vertices_index1 : Integer = capture_edge_vertices(domain='EDGE').vertex_index_1
- edge_vertices_index2 : Integer = capture_edge_vertices(domain='EDGE').vertex_index_2
- edge_vertices_position1 : Vector = capture_edge_vertices(domain='EDGE').position_1
- edge_vertices_position2 : Vector = capture_edge_vertices(domain='EDGE').position_2
- egde_ID : Float = capture_ID(domain='EDGE').unsigned_angle
- egde_index : Float = capture_index(domain='EDGE').unsigned_angle
- egde_position : Float = capture_position(domain='EDGE').unsigned_angle
- face_ID : Float = capture_ID(domain='FACE').unsigned_angle
- face_area : Float = capture_face_area(domain='FACE')
- face_index : Float = capture_index(domain='FACE').unsigned_angle
- face_neighbors_face_count : Integer = capture_face_neighbors(domain='FACE').face_count
- face_neighbors_vertex_count : Integer = capture_face_neighbors(domain='FACE').vertex_count
- face_position : Float = capture_position(domain='FACE').unsigned_angle
- island : Integer = capture_island(domain='POINT').island_index
- material_index : Integer = capture_material_index(domain='FACE')
- material_selection : Boolean = capture_material_selection(domain='FACE')
- shade_smooth : Boolean = capture_shade_smooth(domain='FACE')
- vertex_neighbors_face_count : Integer = capture_vertex_neighbors(domain='POINT').face_count
- vertex_neighbors_vertex_count : Integer = capture_vertex_neighbors(domain='POINT').vertex_count



## Methods



- difference : mesh (Mesh)
- distribute_points_on_faces : Sockets      [points (Points), normal (Vector), rotation (Vector)]
- extrude : Sockets      [mesh (Mesh), top (Boolean), side (Boolean)]
- intersect : mesh (Mesh)
- to_curve : curve (Curve)
- to_points : points (Points)
- union : mesh (Mesh)



## Stacked methods



- dual : Mesh
- flip_faces : Mesh
- split_edges : Mesh
- subdivide : Mesh
- subdivision_surface : Mesh
- triangulate : Mesh



## Methods


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



#### Returns

    Integer
