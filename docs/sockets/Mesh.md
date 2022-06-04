
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


