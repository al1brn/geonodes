# Mesh

``` python
Mesh(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', optional_label: bool = False, hide_value: bool = False, hide_in_modifier: bool = False)
```

> Mesh Geometry

The **Mesh** exposes all methods specific to meshes.
Since there is no ambiguity, the word **mesh** is omitted in the **snake_case** name of
the methods:

``` python
mesh = Mesh.Line() # Node 'Mesh Line'
cloud = mesh.to_points() # Node 'Mesh to Points'
```

Nodes requiring a domain parameter, are implemented in one of the four domains of Mesh: [points](mesh.md#points),
[faces](mesh.md#faces), [edges](mesh.md#edges) or [corners](mesh.md#corners).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **optional_label** (_bool_ = False) : Property optional_label
- **hide_value** (_bool_ = False) : Property hide_value
- **hide_in_modifier** (_bool_ = False) : Property hide_in_modifier

### Inherited

[\_\_add__](boolean.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [bounding_box](core-gener-geome-geometry.md#bounding_box) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_classes_test](core-socke-socket.md#_classes_test) :black_small_square: [convex_hull](core-gener-geome-geometry.md#convex_hull) :black_small_square: [\_create_input_socket](core-gener-geome-geometry.md#_create_input_socket) :black_small_square: [curve](core-gener-geome-geometry.md#curve) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [enable_output](core-gener-geome-geometry.md#enable_output) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_geo](cloudpoint.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](geom.md#get_selection) :black_small_square: [grease_pencil](core-gener-geome-geometry.md#grease_pencil) :black_small_square: [id](core-gener-geome-geometry.md#id) :black_small_square: [index_of_nearest](core-gener-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](boolean.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [instance_on_points](core-gener-geome-geometry.md#instance_on_points) :black_small_square: [instances](core-gener-geome-geometry.md#instances) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [Join](core-gener-geome-geometry.md#join) :black_small_square: [join](core-gener-geome-geometry.md#join) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_from](core-socke-socket.md#link_from) :black_small_square: [material](core-gener-geome-geometry.md#material) :black_small_square: [material_index](core-gener-geome-geometry.md#material_index) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [merge](core-gener-geome-geometry.md#merge) :black_small_square: [merge_by_distance](core-gener-geome-geometry.md#merge_by_distance) :black_small_square: [mesh](core-gener-geome-geometry.md#mesh) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [name](core-gener-geome-geometry.md#name) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [offset](core-gener-geome-geometry.md#offset) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [point_cloud](core-gener-geome-geometry.md#point_cloud) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [position](core-gener-geome-geometry.md#position) :black_small_square: [proximity](core-gener-geome-geometry.md#proximity) :black_small_square: [proximity_edges](core-gener-geome-geometry.md#proximity_edges) :black_small_square: [proximity_faces](core-gener-geome-geometry.md#proximity_faces) :black_small_square: [proximity_points](core-gener-geome-geometry.md#proximity_points) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [raycast](core-gener-geome-geometry.md#raycast) :black_small_square: [realize](core-gener-geome-geometry.md#realize) :black_small_square: [remove_named_attribute](core-gener-geome-geometry.md#remove_named_attribute) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [replace_material](core-gener-geome-geometry.md#replace_material) :black_small_square: ['_selection' not found]() :black_small_square: [separate_components](core-gener-geome-geometry.md#separate_components) :black_small_square: [set_id](core-gener-geome-geometry.md#set_id) :black_small_square: [set_material](core-gener-geome-geometry.md#set_material) :black_small_square: [set_material_index](core-gener-geome-geometry.md#set_material_index) :black_small_square: [set_name](core-gener-geome-geometry.md#set_name) :black_small_square: [set_position](core-gener-geome-geometry.md#set_position) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: ['_socket_type' not found]() :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: [to_instance](core-gener-geome-geometry.md#to_instance) :black_small_square: [transform](core-gener-geome-geometry.md#transform) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square: [viewer](core-gener-geome-geometry.md#viewer) :black_small_square: [volume](core-gener-geome-geometry.md#volume) :black_small_square:

## Content

- **B** : [Boolean](mesh.md#boolean) :black_small_square: [boolean](mesh.md#boolean)
- **C** : [Circle](mesh.md#circle) :black_small_square: [Cone](mesh.md#cone) :black_small_square: [corners](mesh.md#corners) :black_small_square: [corners_of_edge](mesh.md#corners_of_edge) :black_small_square: [corners_of_face](mesh.md#corners_of_face) :black_small_square: [corners_of_vertex](mesh.md#corners_of_vertex) :black_small_square: [corners_to_points](mesh.md#corners_to_points) :black_small_square: [Cube](mesh.md#cube) :black_small_square: [Cylinder](mesh.md#cylinder)
- **D** : [Difference](mesh.md#difference) :black_small_square: [difference](mesh.md#difference) :black_small_square: [distribute_points_on_faces](mesh.md#distribute_points_on_faces) :black_small_square: [distribute_points_on_faces_poisson](mesh.md#distribute_points_on_faces_poisson) :black_small_square: [distribute_points_on_faces_random](mesh.md#distribute_points_on_faces_random) :black_small_square: [domain_size](mesh.md#domain_size) :black_small_square: [dual](mesh.md#dual)
- **E** : [edge_paths_to_curves](mesh.md#edge_paths_to_curves) :black_small_square: [edge_paths_to_selection](mesh.md#edge_paths_to_selection) :black_small_square: [edges](mesh.md#edges) :black_small_square: [edges_of_corner](mesh.md#edges_of_corner) :black_small_square: [edges_of_vertex](mesh.md#edges_of_vertex) :black_small_square: [edges_to_face_groups](mesh.md#edges_to_face_groups) :black_small_square: [edges_to_points](mesh.md#edges_to_points) :black_small_square: [extrude](mesh.md#extrude) :black_small_square: [extrude_edges](mesh.md#extrude_edges) :black_small_square: [extrude_faces](mesh.md#extrude_faces) :black_small_square: [extrude_vertices](mesh.md#extrude_vertices)
- **F** : [face_group_boundaries](mesh.md#face_group_boundaries) :black_small_square: [face_of_corner](mesh.md#face_of_corner) :black_small_square: [faces](mesh.md#faces) :black_small_square: [faces_to_points](mesh.md#faces_to_points) :black_small_square: [flip_faces](mesh.md#flip_faces)
- **G** : [Grid](mesh.md#grid)
- **I** : [IcoSphere](mesh.md#icosphere) :black_small_square: [ImportPLY](mesh.md#importply) :black_small_square: [ImportSTL](mesh.md#importstl) :black_small_square: [Intersect](mesh.md#intersect) :black_small_square: [intersect](mesh.md#intersect) :black_small_square: [is_face_planar](mesh.md#is_face_planar)
- **L** : [Line](mesh.md#line) :black_small_square: [LineEndPoints](mesh.md#lineendpoints) :black_small_square: [LineOffset](mesh.md#lineoffset)
- **M** : [material_selection](mesh.md#material_selection)
- **N** : [normal](mesh.md#normal)
- **O** : [offset_corner_in_face](mesh.md#offset_corner_in_face)
- **P** : [points](mesh.md#points)
- **S** : [sample_nearest_surface](mesh.md#sample_nearest_surface) :black_small_square: [sample_uv_surface](mesh.md#sample_uv_surface) :black_small_square: [set_face_set](mesh.md#set_face_set) :black_small_square: [set_normal](mesh.md#set_normal) :black_small_square: [set_normal_free](mesh.md#set_normal_free) :black_small_square: [set_normal_sharpness](mesh.md#set_normal_sharpness) :black_small_square: [set_normal_tangent_space](mesh.md#set_normal_tangent_space) :black_small_square: [shortest_edge_paths](mesh.md#shortest_edge_paths) :black_small_square: [split_edges](mesh.md#split_edges) :black_small_square: [subdivide](mesh.md#subdivide) :black_small_square: [subdivision_surface](mesh.md#subdivision_surface)
- **T** : [to_curve](mesh.md#to_curve) :black_small_square: [to_curve_edges](mesh.md#to_curve_edges) :black_small_square: [to_curve_faces](mesh.md#to_curve_faces) :black_small_square: [to_density_grid](mesh.md#to_density_grid) :black_small_square: [to_points](mesh.md#to_points) :black_small_square: [to_sdf_grid](mesh.md#to_sdf_grid) :black_small_square: [to_volume](mesh.md#to_volume) :black_small_square: [triangulate](mesh.md#triangulate)
- **U** : [Union](mesh.md#union) :black_small_square: [union](mesh.md#union) :black_small_square: [UVSphere](mesh.md#uvsphere)
- **V** : [vertex_of_corner](mesh.md#vertex_of_corner) :black_small_square: [vertices_to_points](mesh.md#vertices_to_points)

## Properties



### corners

> _type_: **Corner**
>

CORNER domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Properties](mesh.md#properties)</sub>

### edges

> _type_: **Edge**
>

EDGE domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Properties](mesh.md#properties)</sub>

### faces

> _type_: **Face**
>

FACE domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Properties](mesh.md#properties)</sub>

### normal

> _type_: **?**
>

Write only property for node <Node Set Mesh Normal>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Properties](mesh.md#properties)</sub>

### points

> _type_: **Vertex**
>

POINT domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Properties](mesh.md#properties)</sub>

## Methods



----------
### Boolean()

> classmethod

``` python
Boolean(*mesh_2: 'Mesh', mesh_1: 'Mesh' = None, operation: "Literal['INTERSECT', 'UNION', 'DIFFERENCE']" = 'DIFFERENCE', solver: "Literal['EXACT', 'FLOAT', 'MANIFOLD']" = 'FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

#### Arguments:
- **mesh_2** (_Mesh_) : socket 'Mesh 2' (id: Mesh 2)
- **mesh_1** (_Mesh_ = None) : socket 'Mesh 1' (id: Mesh 1)
- **operation** (_Literal['INTERSECT', 'UNION', 'DIFFERENCE']_ = DIFFERENCE) : parameter 'operation' in ['INTERSECT', 'UNION', 'DIFFERENCE']
- **solver** (_Literal['EXACT', 'FLOAT', 'MANIFOLD']_ = FLOAT) : parameter 'solver' in ['EXACT', 'FLOAT', 'MANIFOLD']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### boolean()

> method

``` python
boolean(*mesh_2: 'Mesh', operation: "Literal['INTERSECT', 'UNION', 'DIFFERENCE']" = 'DIFFERENCE', solver: "Literal['EXACT', 'FLOAT', 'MANIFOLD']" = 'FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **mesh_2** (_Mesh_) : socket 'Mesh 2' (id: Mesh 2)
- **operation** (_Literal['INTERSECT', 'UNION', 'DIFFERENCE']_ = DIFFERENCE) : parameter 'operation' in ['INTERSECT', 'UNION', 'DIFFERENCE']
- **solver** (_Literal['EXACT', 'FLOAT', 'MANIFOLD']_ = FLOAT) : parameter 'solver' in ['EXACT', 'FLOAT', 'MANIFOLD']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### Circle()

> classmethod

``` python
Circle(vertices: 'Integer' = None, radius: 'Float' = None, fill_type: "Literal['NONE', 'NGON', 'TRIANGLE_FAN']" = 'NONE')
```

> Node [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_circle.html)

#### Arguments:
- **vertices** (_Integer_ = None) : socket 'Vertices' (id: Vertices)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **fill_type** (_Literal['NONE', 'NGON', 'TRIANGLE_FAN']_ = NONE) : parameter 'fill_type' in ['NONE', 'NGON', 'TRIANGLE_FAN']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### Cone()

> classmethod

``` python
Cone(vertices: 'Integer' = None, side_segments: 'Integer' = None, fill_segments: 'Integer' = None, radius_top: 'Float' = None, radius_bottom: 'Float' = None, depth: 'Float' = None, fill_type: "Literal['NONE', 'NGON', 'TRIANGLE_FAN']" = 'NGON')
```

> Node [Cone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cone.html)

#### Arguments:
- **vertices** (_Integer_ = None) : socket 'Vertices' (id: Vertices)
- **side_segments** (_Integer_ = None) : socket 'Side Segments' (id: Side Segments)
- **fill_segments** (_Integer_ = None) : socket 'Fill Segments' (id: Fill Segments)
- **radius_top** (_Float_ = None) : socket 'Radius Top' (id: Radius Top)
- **radius_bottom** (_Float_ = None) : socket 'Radius Bottom' (id: Radius Bottom)
- **depth** (_Float_ = None) : socket 'Depth' (id: Depth)
- **fill_type** (_Literal['NONE', 'NGON', 'TRIANGLE_FAN']_ = NGON) : parameter 'fill_type' in ['NONE', 'NGON', 'TRIANGLE_FAN']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### corners_of_edge()

> classmethod

``` python
corners_of_edge(edge_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
```

> Node [Corners of Edge](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_edge.html)

#### Arguments:
- **edge_index** (_Integer_ = None) : socket 'Edge Index' (id: Edge Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### corners_of_face()

> classmethod

``` python
corners_of_face(face_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
```

> Node [Corners of Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_face.html)

#### Arguments:
- **face_index** (_Integer_ = None) : socket 'Face Index' (id: Face Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### corners_of_vertex()

> classmethod

``` python
corners_of_vertex(vertex_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
```

> Node [Corners of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (id: Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### corners_to_points()

> method

``` python
corners_to_points(position: 'Vector' = None, radius: 'Float' = None)
```

> Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'CORNERS'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### Cube()

> classmethod

``` python
Cube(size: 'Vector' = None, vertices_x: 'Integer' = None, vertices_y: 'Integer' = None, vertices_z: 'Integer' = None)
```

> Node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cube.html)

#### Arguments:
- **size** (_Vector_ = None) : socket 'Size' (id: Size)
- **vertices_x** (_Integer_ = None) : socket 'Vertices X' (id: Vertices X)
- **vertices_y** (_Integer_ = None) : socket 'Vertices Y' (id: Vertices Y)
- **vertices_z** (_Integer_ = None) : socket 'Vertices Z' (id: Vertices Z)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### Cylinder()

> classmethod

``` python
Cylinder(vertices: 'Integer' = None, side_segments: 'Integer' = None, fill_segments: 'Integer' = None, radius: 'Float' = None, depth: 'Float' = None, fill_type: "Literal['NONE', 'NGON', 'TRIANGLE_FAN']" = 'NGON')
```

> Node [Cylinder](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cylinder.html)

#### Arguments:
- **vertices** (_Integer_ = None) : socket 'Vertices' (id: Vertices)
- **side_segments** (_Integer_ = None) : socket 'Side Segments' (id: Side Segments)
- **fill_segments** (_Integer_ = None) : socket 'Fill Segments' (id: Fill Segments)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **depth** (_Float_ = None) : socket 'Depth' (id: Depth)
- **fill_type** (_Literal['NONE', 'NGON', 'TRIANGLE_FAN']_ = NGON) : parameter 'fill_type' in ['NONE', 'NGON', 'TRIANGLE_FAN']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### Difference()

> classmethod

``` python
Difference(*mesh_2: 'Mesh', mesh_1: 'Mesh' = None, solver: "Literal['EXACT', 'FLOAT', 'MANIFOLD']" = 'FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

#### Information:
- **Parameter** : 'DIFFERENCE'



#### Arguments:
- **mesh_2** (_Mesh_) : socket 'Mesh 2' (id: Mesh 2)
- **mesh_1** (_Mesh_ = None) : socket 'Mesh 1' (id: Mesh 1)
- **solver** (_Literal['EXACT', 'FLOAT', 'MANIFOLD']_ = FLOAT) : parameter 'solver' in ['EXACT', 'FLOAT', 'MANIFOLD']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### difference()

> method

``` python
difference(*mesh_2: 'Mesh', solver: "Literal['EXACT', 'FLOAT', 'MANIFOLD']" = 'FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'DIFFERENCE'



#### Arguments:
- **mesh_2** (_Mesh_) : socket 'Mesh 2' (id: Mesh 2)
- **solver** (_Literal['EXACT', 'FLOAT', 'MANIFOLD']_ = FLOAT) : parameter 'solver' in ['EXACT', 'FLOAT', 'MANIFOLD']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### distribute_points_on_faces()

> method

``` python
distribute_points_on_faces(density: 'Float' = None, seed: 'Integer' = None, distribute_method: "Literal['RANDOM', 'POISSON']" = 'RANDOM')
```

> Node ERROR: Node 'Distribute Points on Faces' not found

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)
- **distribute_method** (_Literal['RANDOM', 'POISSON']_ = RANDOM) : parameter 'distribute_method' in ['RANDOM', 'POISSON']



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### distribute_points_on_faces_poisson()

> method

``` python
distribute_points_on_faces_poisson(distance_min: 'Float' = None, density_max: 'Float' = None, density_factor: 'Float' = None, seed: 'Integer' = None)
```

> Node ERROR: Node 'Distribute Points on Faces' not found

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POISSON'



#### Arguments:
- **distance_min** (_Float_ = None) : socket 'Distance Min' (id: Distance Min)
- **density_max** (_Float_ = None) : socket 'Density Max' (id: Density Max)
- **density_factor** (_Float_ = None) : socket 'Density Factor' (id: Density Factor)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### distribute_points_on_faces_random()

> method

``` python
distribute_points_on_faces_random(density: 'Float' = None, seed: 'Integer' = None)
```

> Node ERROR: Node 'Distribute Points on Faces' not found

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'RANDOM'



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### domain_size()

> method

``` python
domain_size()
```

> Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MESH'



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### dual()

> method

``` python
dual(keep_boundaries: 'Boolean' = None)
```

> Node [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/dual_mesh.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **keep_boundaries** (_Boolean_ = None) : socket 'Keep Boundaries' (id: Keep Boundaries)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### edge_paths_to_curves()

> method

``` python
edge_paths_to_curves(start_vertices: 'Boolean' = None, next_vertex_index: 'Integer' = None)
```

> Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **start_vertices** (_Boolean_ = None) : socket 'Start Vertices' (id: Start Vertices)
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (id: Next Vertex Index)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### edge_paths_to_selection()

> classmethod

``` python
edge_paths_to_selection(start_vertices: 'Boolean' = None, next_vertex_index: 'Integer' = None)
```

> Node [Edge Paths to Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_selection.html)

#### Arguments:
- **start_vertices** (_Boolean_ = None) : socket 'Start Vertices' (id: Start Vertices)
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (id: Next Vertex Index)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### edges_of_corner()

> classmethod

``` python
edges_of_corner(corner_index: 'Integer' = None)
```

> Node [Edges of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### edges_of_vertex()

> classmethod

``` python
edges_of_vertex(vertex_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
```

> Node [Edges of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (id: Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### edges_to_face_groups()

> classmethod

``` python
edges_to_face_groups(boundary_edges: 'Boolean' = None)
```

> Node [Edges to Face Groups](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edges_to_face_groups.html)

#### Arguments:
- **boundary_edges** (_Boolean_ = None) : socket 'Boundary Edges' (id: Boundary Edges)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### edges_to_points()

> method

``` python
edges_to_points(position: 'Vector' = None, radius: 'Float' = None)
```

> Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGES'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### extrude()

> method

``` python
extrude(offset: 'Vector' = None, offset_scale: 'Float' = None, individual: 'Boolean' = None, mode: "Literal['VERTICES', 'EDGES', 'FACES']" = 'FACES')
```

> Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **offset_scale** (_Float_ = None) : socket 'Offset Scale' (id: Offset Scale)
- **individual** (_Boolean_ = None) : socket 'Individual' (id: Individual)
- **mode** (_Literal['VERTICES', 'EDGES', 'FACES']_ = FACES) : parameter 'mode' in ['VERTICES', 'EDGES', 'FACES']



#### Returns:
- **Mesh** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### extrude_edges()

> method

``` python
extrude_edges(offset: 'Vector' = None, offset_scale: 'Float' = None)
```

> Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGES'



#### Arguments:
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **offset_scale** (_Float_ = None) : socket 'Offset Scale' (id: Offset Scale)



#### Returns:
- **Mesh** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### extrude_faces()

> method

``` python
extrude_faces(offset: 'Vector' = None, offset_scale: 'Float' = None, individual: 'Boolean' = None)
```

> Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACES'



#### Arguments:
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **offset_scale** (_Float_ = None) : socket 'Offset Scale' (id: Offset Scale)
- **individual** (_Boolean_ = None) : socket 'Individual' (id: Individual)



#### Returns:
- **Mesh** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### extrude_vertices()

> method

``` python
extrude_vertices(offset: 'Vector' = None, offset_scale: 'Float' = None)
```

> Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'VERTICES'



#### Arguments:
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **offset_scale** (_Float_ = None) : socket 'Offset Scale' (id: Offset Scale)



#### Returns:
- **Mesh** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### face_group_boundaries()

> classmethod

``` python
face_group_boundaries(face_group_id: 'Integer' = None)
```

> Node [Face Group Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_group_boundaries.html)

#### Arguments:
- **face_group_id** (_Integer_ = None) : socket 'Face Group ID' (id: Face Set)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### face_of_corner()

> classmethod

``` python
face_of_corner(corner_index: 'Integer' = None)
```

> Node [Face of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/face_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### faces_to_points()

> method

``` python
faces_to_points(position: 'Vector' = None, radius: 'Float' = None)
```

> Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACES'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### flip_faces()

> method

``` python
flip_faces()
```

> Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/flip_faces.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### Grid()

> classmethod

``` python
Grid(size_x: 'Float' = None, size_y: 'Float' = None, vertices_x: 'Integer' = None, vertices_y: 'Integer' = None)
```

> Node [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/grid.html)

#### Arguments:
- **size_x** (_Float_ = None) : socket 'Size X' (id: Size X)
- **size_y** (_Float_ = None) : socket 'Size Y' (id: Size Y)
- **vertices_x** (_Integer_ = None) : socket 'Vertices X' (id: Vertices X)
- **vertices_y** (_Integer_ = None) : socket 'Vertices Y' (id: Vertices Y)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### IcoSphere()

> classmethod

``` python
IcoSphere(radius: 'Float' = None, subdivisions: 'Integer' = None)
```

> Node ERROR: Node 'Ico Sphere' not found

#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **subdivisions** (_Integer_ = None) : socket 'Subdivisions' (id: Subdivisions)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### ImportPLY()

> classmethod

``` python
ImportPLY(path: 'String' = None)
```

> Node ERROR: Node 'Import PLY' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### ImportSTL()

> classmethod

``` python
ImportSTL(path: 'String' = None)
```

> Node ERROR: Node 'Import STL' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### Intersect()

> classmethod

``` python
Intersect(*mesh: 'Mesh', solver: "Literal['EXACT', 'FLOAT', 'MANIFOLD']" = 'FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

#### Information:
- **Parameter** : 'INTERSECT'



#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (id: Mesh 2)
- **solver** (_Literal['EXACT', 'FLOAT', 'MANIFOLD']_ = FLOAT) : parameter 'solver' in ['EXACT', 'FLOAT', 'MANIFOLD']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### intersect()

> method

``` python
intersect(*mesh: 'Mesh', solver: "Literal['EXACT', 'FLOAT', 'MANIFOLD']" = 'FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Parameter** : 'INTERSECT'



#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (id: Mesh 2)
- **solver** (_Literal['EXACT', 'FLOAT', 'MANIFOLD']_ = FLOAT) : parameter 'solver' in ['EXACT', 'FLOAT', 'MANIFOLD']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### is_face_planar()

> classmethod

``` python
is_face_planar(threshold: 'Float' = None)
```

> Node [Is Face Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_is_planar.html)

#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### Line()

> classmethod

``` python
Line(count: 'Integer' = None, start_location: 'Vector' = None, offset: 'Vector' = None, count_mode: "Literal['TOTAL', 'RESOLUTION']" = 'TOTAL', mode: "Literal['OFFSET', 'END_POINTS']" = 'OFFSET')
```

> Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_line.html)

#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **start_location** (_Vector_ = None) : socket 'Start Location' (id: Start Location)
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **count_mode** (_Literal['TOTAL', 'RESOLUTION']_ = TOTAL) : parameter 'count_mode' in ['TOTAL', 'RESOLUTION']
- **mode** (_Literal['OFFSET', 'END_POINTS']_ = OFFSET) : parameter 'mode' in ['OFFSET', 'END_POINTS']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### LineEndPoints()

> classmethod

``` python
LineEndPoints(count: 'Integer' = None, start_location: 'Vector' = None, end_location: 'Vector' = None, count_mode: "Literal['TOTAL', 'RESOLUTION']" = 'TOTAL')
```

> Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_line.html)

#### Information:
- **Parameter** : 'END_POINTS'



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **start_location** (_Vector_ = None) : socket 'Start Location' (id: Start Location)
- **end_location** (_Vector_ = None) : socket 'End Location' (id: Offset)
- **count_mode** (_Literal['TOTAL', 'RESOLUTION']_ = TOTAL) : parameter 'count_mode' in ['TOTAL', 'RESOLUTION']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### LineOffset()

> classmethod

``` python
LineOffset(count: 'Integer' = None, start_location: 'Vector' = None, offset: 'Vector' = None, count_mode: "Literal['TOTAL', 'RESOLUTION']" = 'TOTAL')
```

> Node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_line.html)

#### Information:
- **Parameter** : 'OFFSET'



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **start_location** (_Vector_ = None) : socket 'Start Location' (id: Start Location)
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **count_mode** (_Literal['TOTAL', 'RESOLUTION']_ = TOTAL) : parameter 'count_mode' in ['TOTAL', 'RESOLUTION']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### material_selection()

> classmethod

``` python
material_selection(material: 'Material' = None)
```

> Node [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/material/material_selection.html)

#### Arguments:
- **material** (_Material_ = None) : socket 'Material' (id: Material)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### offset_corner_in_face()

> classmethod

``` python
offset_corner_in_face(corner_index: 'Integer' = None, offset: 'Integer' = None)
```

> Node [Offset Corner in Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/offset_corner_in_face.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)
- **offset** (_Integer_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### sample_nearest_surface()

> method

``` python
sample_nearest_surface(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, group_id: 'Integer' = None, sample_position: 'Vector' = None, sample_group_id: 'Integer' = None)
```

> Node [Sample Nearest Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_nearest_surface.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Sample Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (id: Sample Group ID)



#### Returns:
- **Float** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### sample_uv_surface()

> method

``` python
sample_uv_surface(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, uv_map: 'Vector' = None, sample_uv: 'Vector' = None)
```

> Node [Sample UV Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_uv_surface.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **uv_map** (_Vector_ = None) : socket 'UV Map' (id: Source UV Map)
- **sample_uv** (_Vector_ = None) : socket 'Sample UV' (id: Sample UV)



#### Returns:
- **Float** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### set_face_set()

> method

``` python
set_face_set(face_set: 'Integer' = None)
```

> Node [Set Face Set](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_face_set.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **face_set** (_Integer_ = None) : socket 'Face Set' (id: Face Set)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### set_normal()

> method

``` python
set_normal(remove_custom: 'Boolean' = None, edge_sharpness: 'Boolean' = None, face_sharpness: 'Boolean' = None, domain: "Literal['POINT', 'FACE', 'CORNER']" = 'POINT', mode: "Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE']" = 'SHARPNESS')
```

> Node [Set Mesh Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_mesh_normal.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **remove_custom** (_Boolean_ = None) : socket 'Remove Custom' (id: Remove Custom)
- **edge_sharpness** (_Boolean_ = None) : socket 'Edge Sharpness' (id: Edge Sharpness)
- **face_sharpness** (_Boolean_ = None) : socket 'Face Sharpness' (id: Face Sharpness)
- **domain** (_Literal['POINT', 'FACE', 'CORNER']_ = POINT) : parameter 'domain' in ['POINT', 'FACE', 'CORNER']
- **mode** (_Literal['SHARPNESS', 'FREE', 'TANGENT_SPACE']_ = SHARPNESS) : parameter 'mode' in ['SHARPNESS', 'FREE', 'TANGENT_SPACE']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### set_normal_free()

> method

``` python
set_normal_free(custom_normal: 'Vector' = None, domain: "Literal['POINT', 'FACE', 'CORNER']" = 'POINT')
```

> Node [Set Mesh Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_mesh_normal.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'FREE'



#### Arguments:
- **custom_normal** (_Vector_ = None) : socket 'Custom Normal' (id: Custom Normal)
- **domain** (_Literal['POINT', 'FACE', 'CORNER']_ = POINT) : parameter 'domain' in ['POINT', 'FACE', 'CORNER']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### set_normal_sharpness()

> method

``` python
set_normal_sharpness(remove_custom: 'Boolean' = None, edge_sharpness: 'Boolean' = None, face_sharpness: 'Boolean' = None, domain: "Literal['POINT', 'FACE', 'CORNER']" = 'POINT')
```

> Node [Set Mesh Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_mesh_normal.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'SHARPNESS'



#### Arguments:
- **remove_custom** (_Boolean_ = None) : socket 'Remove Custom' (id: Remove Custom)
- **edge_sharpness** (_Boolean_ = None) : socket 'Edge Sharpness' (id: Edge Sharpness)
- **face_sharpness** (_Boolean_ = None) : socket 'Face Sharpness' (id: Face Sharpness)
- **domain** (_Literal['POINT', 'FACE', 'CORNER']_ = POINT) : parameter 'domain' in ['POINT', 'FACE', 'CORNER']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### set_normal_tangent_space()

> method

``` python
set_normal_tangent_space(custom_normal: 'Vector' = None, domain: "Literal['POINT', 'FACE', 'CORNER']" = 'POINT')
```

> Node [Set Mesh Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_mesh_normal.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'TANGENT_SPACE'



#### Arguments:
- **custom_normal** (_Vector_ = None) : socket 'Custom Normal' (id: Custom Normal)
- **domain** (_Literal['POINT', 'FACE', 'CORNER']_ = POINT) : parameter 'domain' in ['POINT', 'FACE', 'CORNER']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### shortest_edge_paths()

> classmethod

``` python
shortest_edge_paths(end_vertex: 'Boolean' = None, edge_cost: 'Float' = None)
```

> Node [Shortest Edge Paths](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/shortest_edge_paths.html)

#### Arguments:
- **end_vertex** (_Boolean_ = None) : socket 'End Vertex' (id: End Vertex)
- **edge_cost** (_Float_ = None) : socket 'Edge Cost' (id: Edge Cost)



#### Returns:
- **Integer** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### split_edges()

> method

``` python
split_edges()
```

> Node [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/split_edges.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### subdivide()

> method

``` python
subdivide(level: 'Integer' = None)
```

> Node [Subdivide Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivide_mesh.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **level** (_Integer_ = None) : socket 'Level' (id: Level)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### subdivision_surface()

> method

``` python
subdivision_surface(level: 'Integer' = None, edge_crease: 'Float' = None, vertex_crease: 'Float' = None, limit_surface: 'Boolean' = None, uv_smooth: "Literal['None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All']" = None, boundary_smooth: "Literal['Keep Corners', 'All']" = None)
```

> Node [Subdivision Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivision_surface.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **level** (_Integer_ = None) : socket 'Level' (id: Level)
- **edge_crease** (_Float_ = None) : socket 'Edge Crease' (id: Edge Crease)
- **vertex_crease** (_Float_ = None) : socket 'Vertex Crease' (id: Vertex Crease)
- **limit_surface** (_Boolean_ = None) : socket 'Limit Surface' (id: Limit Surface)
- **uv_smooth** (_Literal['None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All']_ = None) : ('None', 'Keep Corners', 'Keep Corners, Junctions', 'Keep Corners, Junctions, Concave', 'Keep Boundaries', 'All')
- **boundary_smooth** (_Literal['Keep Corners', 'All']_ = None) : ('Keep Corners', 'All')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### to_curve()

> method

``` python
to_curve(mode: "Literal['EDGES', 'FACES']" = 'EDGES')
```

> Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_curve.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **mode** (_Literal['EDGES', 'FACES']_ = EDGES) : parameter 'mode' in ['EDGES', 'FACES']



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### to_curve_edges()

> method

``` python
to_curve_edges()
```

> Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_curve.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGES'



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### to_curve_faces()

> method

``` python
to_curve_faces()
```

> Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_curve.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACES'



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### to_density_grid()

> method

``` python
to_density_grid(density: 'Float' = None, voxel_size: 'Float' = None, gradient_width: 'Float' = None)
```

> Node [Mesh to Density Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_density_grid.html)

#### Information:
- **Socket** : self



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (id: Voxel Size)
- **gradient_width** (_Float_ = None) : socket 'Gradient Width' (id: Gradient Width)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position: 'Vector' = None, radius: 'Float' = None, mode: "Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS']" = 'VERTICES')
```

> Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **mode** (_Literal['VERTICES', 'EDGES', 'FACES', 'CORNERS']_ = VERTICES) : parameter 'mode' in ['VERTICES', 'EDGES', 'FACES', 'CORNERS']



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### to_sdf_grid()

> method

``` python
to_sdf_grid(voxel_size: 'Float' = None, band_width: 'Integer' = None)
```

> Node [Mesh to SDF Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_sdf_grid.html)

#### Information:
- **Socket** : self



#### Arguments:
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (id: Voxel Size)
- **band_width** (_Integer_ = None) : socket 'Band Width' (id: Band Width)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### to_volume()

> method

``` python
to_volume(density: 'Float' = None, resolution_mode: "Literal['Amount', 'Size']" = None, voxel_size: 'Float' = None, voxel_amount: 'Float' = None, interior_band_width: 'Float' = None)
```

> Node [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_volume.html)

#### Information:
- **Socket** : self



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **resolution_mode** (_Literal['Amount', 'Size']_ = None) : ('Amount', 'Size')
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (id: Voxel Size)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (id: Voxel Amount)
- **interior_band_width** (_Float_ = None) : socket 'Interior Band Width' (id: Interior Band Width)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### triangulate()

> method

``` python
triangulate(quad_method: "Literal['Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal']" = None, n_gon_method: "Literal['Beauty', 'Clip']" = None)
```

> Node [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/triangulate.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **quad_method** (_Literal['Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal']_ = None) : ('Beauty', 'Fixed', 'Fixed Alternate', 'Shortest Diagonal', 'Longest Diagonal')
- **n_gon_method** (_Literal['Beauty', 'Clip']_ = None) : ('Beauty', 'Clip')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### Union()

> classmethod

``` python
Union(*mesh: 'Mesh', solver: "Literal['EXACT', 'FLOAT', 'MANIFOLD']" = 'FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

#### Information:
- **Parameter** : 'UNION'



#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (id: Mesh 2)
- **solver** (_Literal['EXACT', 'FLOAT', 'MANIFOLD']_ = FLOAT) : parameter 'solver' in ['EXACT', 'FLOAT', 'MANIFOLD']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### union()

> method

``` python
union(*mesh: 'Mesh', solver: "Literal['EXACT', 'FLOAT', 'MANIFOLD']" = 'FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Parameter** : 'UNION'



#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (id: Mesh 2)
- **solver** (_Literal['EXACT', 'FLOAT', 'MANIFOLD']_ = FLOAT) : parameter 'solver' in ['EXACT', 'FLOAT', 'MANIFOLD']



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### UVSphere()

> classmethod

``` python
UVSphere(segments: 'Integer' = None, rings: 'Integer' = None, radius: 'Float' = None)
```

> Node [UV Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/uv_sphere.html)

#### Arguments:
- **segments** (_Integer_ = None) : socket 'Segments' (id: Segments)
- **rings** (_Integer_ = None) : socket 'Rings' (id: Rings)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### vertex_of_corner()

> classmethod

``` python
vertex_of_corner(corner_index: 'Integer' = None)
```

> Node [Vertex of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/vertex_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>

----------
### vertices_to_points()

> method

``` python
vertices_to_points(position: 'Vector' = None, radius: 'Float' = None)
```

> Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'VERTICES'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](mesh.md#mesh) :black_small_square: [Content](mesh.md#content) :black_small_square: [Methods](mesh.md#methods)</sub>