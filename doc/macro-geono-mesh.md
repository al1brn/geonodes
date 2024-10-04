# Mesh

> Bases classes: [Geometry](geono-geometry.md#geometry)

``` python
Mesh(value=None, name=None, tip=None)
```

> Mesh Geometry

The **Mesh** exposes all methods specific to meshes.
Since there is no ambiguity, the word **mesh** is omitted in the **snake_case** name of
the methods:

``` python
mesh = Mesh.Line() # Node 'Mesh Line'
cloud = mesh.to_points() # Node 'Mesh to Points'
```

Nodes requiring a domain parameter, are implemented in one of the four domains of Mesh: [points](macro-geono-mesh.md#points),
[faces](macro-geono-mesh.md#faces), [edges](macro-geono-mesh.md#edges) or [corners](macro-geono-mesh.md#corners).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geono-geometry.md#__add__) :black_small_square: [bake](geono-geometry.md#bake) :black_small_square: [blur](geono-socket.md#blur) :black_small_square: [bounding_box](geono-geometry.md#bounding_box) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [convex_hull](geono-geometry.md#convex_hull) :black_small_square: [curve](geono-geometry.md#curve) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geo](geono-geometry.md#_geo) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_geo_type](geono-geobase.md#_geo_type) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [\_\_getitem__](geono-geobase.md#__getitem__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [id](geono-geobase.md#id) :black_small_square: [index_of_nearest](geono-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [instances](geono-geometry.md#instances) :black_small_square: [join](geono-geometry.md#join) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [material](geono-geobase.md#material) :black_small_square: [material_index](geono-geobase.md#material_index) :black_small_square: [material_selection](geono-geobase.md#material_selection) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [merge_by_distance](geono-geometry.md#merge_by_distance) :black_small_square: [mesh](geono-geometry.md#mesh) :black_small_square: [\_node](geono-geometry.md#_node) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [offset](geono-geobase.md#offset) :black_small_square: [out](geono-socket.md#out) :black_small_square: [point_cloud](geono-geometry.md#point_cloud) :black_small_square: [position](geono-geobase.md#position) :black_small_square: [\_raw_sel](geono-geobase.md#_raw_sel) :black_small_square: [raycast](geono-geometry.md#raycast) :black_small_square: [remove_named_attribute](geono-geometry.md#remove_named_attribute) :black_small_square: [replace_material](geono-geobase.md#replace_material) :black_small_square: [\_sel](geono-geobase.md#_sel) :black_small_square: [separate_components](geono-geometry.md#separate_components) :black_small_square: [set_id](geono-geometry.md#set_id) :black_small_square: [set_material](geono-geometry.md#set_material) :black_small_square: [set_position](geono-geometry.md#set_position) :black_small_square: [set_shade_smooth](geono-geometry.md#set_shade_smooth) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_instance](geono-geometry.md#to_instance) :black_small_square: [out](geono-socket.md#out) :black_small_square: [transform](geono-geometry.md#transform) :black_small_square: [viewer](geono-geometry.md#viewer) :black_small_square: [volume](geono-geometry.md#volume) :black_small_square:

## Content

- **B** : [boolean](macro-geono-mesh.md#boolean)
- **C** : [Circle](macro-geono-mesh.md#circle) :black_small_square: [Cone](macro-geono-mesh.md#cone) :black_small_square: [corners](macro-geono-mesh.md#corners) :black_small_square: [Cube](macro-geono-mesh.md#cube) :black_small_square: [Cylinder](macro-geono-mesh.md#cylinder)
- **D** : [difference](macro-geono-mesh.md#difference) :black_small_square: [Disk](macro-geono-mesh.md#disk) :black_small_square: [distribute_points_on_faces](macro-geono-mesh.md#distribute_points_on_faces) :black_small_square: [domain_size](macro-geono-mesh.md#domain_size) :black_small_square: [dual](macro-geono-mesh.md#dual)
- **E** : [edges](macro-geono-mesh.md#edges)
- **F** : [faces](macro-geono-mesh.md#faces) :black_small_square: [FromCurve](macro-geono-mesh.md#fromcurve) :black_small_square: [FromPoints](macro-geono-mesh.md#frompoints) :black_small_square: [FromVolume](macro-geono-mesh.md#fromvolume)
- **G** : [Grid](macro-geono-mesh.md#grid)
- **I** : [IcoSphere](macro-geono-mesh.md#icosphere) :black_small_square: [intersect](macro-geono-mesh.md#intersect) :black_small_square: [island](macro-geono-mesh.md#island)
- **L** : [Line](macro-geono-mesh.md#line) :black_small_square: [LineOffset](macro-geono-mesh.md#lineoffset) :black_small_square: [LineTo](macro-geono-mesh.md#lineto)
- **P** : [pack_uv_islands](macro-geono-mesh.md#pack_uv_islands) :black_small_square: [Plane](macro-geono-mesh.md#plane) :black_small_square: [points](macro-geono-mesh.md#points)
- **S** : [sample_nearest_surface](macro-geono-mesh.md#sample_nearest_surface) :black_small_square: [sample_uv_surface](macro-geono-mesh.md#sample_uv_surface) :black_small_square: [subdivide](macro-geono-mesh.md#subdivide) :black_small_square: [subdivision_surface](macro-geono-mesh.md#subdivision_surface)
- **T** : [to_curve](macro-geono-mesh.md#to_curve) :black_small_square: [to_volume](macro-geono-mesh.md#to_volume) :black_small_square: [triangulate](macro-geono-mesh.md#triangulate)
- **U** : [union](macro-geono-mesh.md#union) :black_small_square: [UVSphere](macro-geono-mesh.md#uvsphere) :black_small_square: [uv_unwrap](macro-geono-mesh.md#uv_unwrap)

## Properties



### corners

> _type_: **Corner**
>

CORNER domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Properties](macro-geono-mesh.md#properties)</sub>

### domain_size

> _type_: **Node**
>

> Node ERROR: Node 'Size' not found, component = 'MESH'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Properties](macro-geono-mesh.md#properties)</sub>

### edges

> _type_: **Edge**
>

EDGE domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Properties](macro-geono-mesh.md#properties)</sub>

### faces

> _type_: **Face**
>

FACE domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Properties](macro-geono-mesh.md#properties)</sub>

### island

> _type_: **Node**
>

> Node [Mesh Island](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/mesh_island.html)

``` python
mesh = Mesh.Cube()
index = mesh.island.index
count = mesh.island.count
```

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Properties](macro-geono-mesh.md#properties)</sub>

### points

> _type_: **Vertex**
>

POINT domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Properties](macro-geono-mesh.md#properties)</sub>

## Methods



----------
### boolean()

> method

``` python
boolean(*meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT', operation='DIFFERENCE')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

#### Arguments:
- **meshes** (_Mesh_) : socket 'Mesh 2' (Mesh 2)
- **self_intersection** (_Boolean_ = None) : socket 'Self Intersection' (Self Intersection)
- **hole_tolerant** (_Boolean_ = None) : socket 'Hole Tolerant' (Hole Tolerant)
- **solver** (_str_ = FLOAT) : Node.solver in ('EXACT', 'FLOAT')
- **operation** (_str_ = DIFFERENCE) : Node.operation in ('INTERSECT', 'UNION', 'DIFFERENCE')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### Circle()

> classmethod

``` python
Circle(vertices=32, radius=1.0, fill_type='NONE')
```

> Constructor node [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_circle.html)

#### Arguments:
- **vertices** (_Integer_ = 32) : socket 'Vertices' (Vertices)
- **radius** (_Float_ = 1.0) : socket 'Radius' (Radius)
- **fill_type** (_str_ = NONE) : Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### Cone()

> classmethod

``` python
Cone(vertices=32, side_segments=1, fill_segments=1, radius_top=0.0, radius_bottom=1.0, depth=2.0, fill_type='NGON')
```

> Constructor node [Cone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cone.html)

#### Arguments:
- **vertices** (_Integer_ = 32) : socket 'Vertices' (Vertices)
- **side_segments** (_Integer_ = 1) : socket 'Side Segments' (Side Segments)
- **fill_segments** (_Integer_ = 1) : socket 'Fill Segments' (Fill Segments)
- **radius_top** (_Float_ = 0.0) : socket 'Radius Top' (Radius Top)
- **radius_bottom** (_Float_ = 1.0) : socket 'Radius Bottom' (Radius Bottom)
- **depth** (_Float_ = 2.0) : socket 'Depth' (Depth)
- **fill_type** (_str_ = NGON) : Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### Cube()

> classmethod

``` python
Cube(size=(1, 1, 1), vertices_x=2, vertices_y=2, vertices_z=2)
```

> Constructor node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cube.html)

#### Arguments:
- **size** (_Vector_ = (1, 1, 1)) : socket 'Size' (Size)
- **vertices_x** (_Integer_ = 2) : socket 'Vertices X' (Vertices X)
- **vertices_y** (_Integer_ = 2) : socket 'Vertices Y' (Vertices Y)
- **vertices_z** (_Integer_ = 2) : socket 'Vertices Z' (Vertices Z)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### Cylinder()

> classmethod

``` python
Cylinder(vertices=32, side_segments=1, fill_segments=1, radius=1.0, depth=2.0, fill_type='NGON')
```

> Constructor node [Cylinder](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cylinder.html)

#### Arguments:
- **vertices** (_Integer_ = 32) : socket 'Vertices' (Vertices)
- **side_segments** (_Integer_ = 1) : socket 'Side Segments' (Side Segments)
- **fill_segments** (_Integer_ = 1) : socket 'Fill Segments' (Fill Segments)
- **radius** (_Float_ = 1.0) : socket 'Radius' (Radius)
- **depth** (_Float_ = 2.0) : socket 'Depth' (Depth)
- **fill_type** (_str_ = NGON) : Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### difference()

> method

``` python
difference(*meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

#### Arguments:
- **meshes** (_Mesh_) : socket 'Mesh 2' (Mesh 2)
- **self_intersection** (_Boolean_ = None) : socket 'Self Intersection' (Self Intersection)
- **hole_tolerant** (_Boolean_ = None) : socket 'Hole Tolerant' (Hole Tolerant)
- **solver** (_str_ = FLOAT) : Node.solver in ('EXACT', 'FLOAT')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### Disk()

> classmethod

``` python
Disk(vertices=32, radius=1.0, fill_type='NGON')
```

> Constructor node [Mesh Circle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_circle.html)

#### Arguments:
- **vertices** (_Integer_ = 32) : socket 'Vertices' (Vertices)
- **radius** (_Float_ = 1.0) : socket 'Radius' (Radius)
- **fill_type** (_str_ = NGON) : Node.fill_type in ('NONE', 'NGON', 'TRIANGLE_FAN')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### distribute_points_on_faces()

> method

``` python
distribute_points_on_faces(density=None, distance_min=None, density_max=None, density_factor=None, seed=None)
```

> Node ERROR: Node 'Distribute Points on Faces' not found

if 'density' argument is not None, 'RANDOM' method is applied, 'POISSON' otherwise

- distribute_method (str): Node.distribute_method in ('RANDOM', 'POISSON')
- use_legacy_normal (bool): Node.use_legacy_normal

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)n 'RANDOM' method if not None 'POISSON' otherwise
- **distance_min** (_Float_ = None) : socket 'Distance Min'
- **density_max** (_Float_ = None) : socket 'Density Max'
- **density_factor** (_Float_ = None) : socket 'Density Factor'
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### dual()

> method

``` python
dual(keep_boundaries=None)
```

> Node [Dual Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/dual_mesh.html)

#### Arguments:
- **keep_boundaries** (_Boolean_ = None) : socket 'Keep Boundaries' (Keep Boundaries)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### FromCurve()

> classmethod

``` python
FromCurve(curve=None, profile_curve=None, fill_caps=None)
```

> Constructor node [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html)

#### Arguments:
- **curve** (_Geometry_ = None) : socket 'Curve' (Curve)
- **profile_curve** (_Geometry_ = None) : socket 'Profile Curve' (Profile Curve)
- **fill_caps** (_Boolean_ = None) : socket 'Fill Caps' (Fill Caps)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### FromPoints()

> classmethod

``` python
FromPoints(points)
```

> Constructor node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)

#### Arguments:
- **points** (_Geometry_) : socket 'Points' (Points)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### FromVolume()

> classmethod

``` python
FromVolume(volume, voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID')
```

> Constructor node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Arguments:
- **volume** (_Geometry_) : socket 'Volume' (Volume)
- **voxel_size** (_Float_ = None) : socket 'Voxel Size'
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount'
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)
- **resolution_mode** (_str_ = GRID) : Node.resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### Grid()

> classmethod

``` python
Grid(size_x=1.0, size_y=1.0, vertices_x=3, vertices_y=3)
```

> Constructor node [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/grid.html)

#### Arguments:
- **size_x** (_Float_ = 1.0) : socket 'Size X' (Size X)
- **size_y** (_Float_ = 1.0) : socket 'Size Y' (Size Y)
- **vertices_x** (_Integer_ = 3) : socket 'Vertices X' (Vertices X)
- **vertices_y** (_Integer_ = 3) : socket 'Vertices Y' (Vertices Y)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### IcoSphere()

> classmethod

``` python
IcoSphere(radius=1.0, subdivisions=1)
```

> Constructor node ERROR: Node 'Ico Sphere' not found

#### Arguments:
- **radius** (_Float_ = 1.0) : socket 'Radius' (Radius)
- **subdivisions** (_Integer_ = 1) : socket 'Subdivisions' (Subdivisions)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### intersect()

> method

``` python
intersect(*meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

#### Arguments:
- **meshes** (_Mesh_) : socket 'Mesh 2' (Mesh 2)
- **self_intersection** (_Boolean_ = None) : socket 'Self Intersection' (Self Intersection)
- **hole_tolerant** (_Boolean_ = None) : socket 'Hole Tolerant' (Hole Tolerant)
- **solver** (_str_ = FLOAT) : Node.solver in ('EXACT', 'FLOAT')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### Line()

> classmethod

``` python
Line(count=None, start_location=None, offset=None, end_location=None, resolution=None)
```

> Constructor node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_line.html)

- count_mode (str): Node.count_mode in ('TOTAL', 'RESOLUTION')
- mode (str): Node.mode in ('OFFSET', 'END_POINTS')

If end_location is not None or resolution is not None, mode is set to 'END_POINTS',
otherwise it iset to 'OFFSET'.
If resolution is None, count_mode is set to 'TOTAL' else to 'RESOLUTION'

#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **start_location** (_Vector_ = None) : socket 'Start Location' (Start Location)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)
- **end_location** (_Vector_ = None) : socket 'End Location' (End Location)
- **resolution** (_Float_ = None) : socket 'Resolution' (Resolution)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### LineOffset()

> classmethod

``` python
LineOffset(start_location=None, offset=None, count=None)
```

> Constructor node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_line.html)

Line from start to end point

#### Arguments:
- **start_location** (_Vector_ = None) : socket 'Start Location' (Start Location)
- **offset** (_Vector_ = None) : socket 'Offset' (Offset)
- **count** (_Integer_ = None) : socket 'Count' (Count)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### LineTo()

> classmethod

``` python
LineTo(start_location=None, end_location=None, count=None, resolution=None)
```

> Constructor node [Mesh Line](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_line.html)

Line from start to end point

#### Arguments:
- **start_location** (_Vector_ = None) : socket 'Start Location' (Start Location)
- **end_location** (_Vector_ = None) : socket 'End Location' (End Location)
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **resolution** (_Float_ = None) : socket 'Resolution' (Resolution)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### pack_uv_islands()

> method

``` python
pack_uv_islands(uv=None, margin=None, rotate=None)
```

> Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/pack_uv_islands.html)

#### Arguments:
- **uv** (_Vector_ = None) : socket 'UV' (UV)
- **margin** (_Float_ = None) : socket 'Margin' (Margin)
- **rotate** (_Boolean_ = None) : socket 'Rotate' (Rotate)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### Plane()

> classmethod

``` python
Plane(size_x=1.0, size_y=1.0)
```

> Constructor node [Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/grid.html)

#### Arguments:
- **size_x** (_Float_ = 1.0) : socket 'Size X' (Size X)
- **size_y** (_Float_ = 1.0) : socket 'Size Y' (Size Y)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### sample_nearest_surface()

> method

``` python
sample_nearest_surface(value=None, group_id=None, sample_position=None, sample_group_id=None)
```

> Node [Sample Nearest Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_nearest_surface.html)

- data_type (str): Node.data_type in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (Sample Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (Sample Group ID)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### sample_uv_surface()

> method

``` python
sample_uv_surface(value=None, uv_map=None, sample_uv=None)
```

> Node [Sample UV Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_uv_surface.html)

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (Value)
- **uv_map** (_Vector_ = None) : socket 'UV Map' (Source UV Map)
- **sample_uv** (_Vector_ = None) : socket 'Sample UV' (Sample UV)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### subdivide()

> method

``` python
subdivide(level=None)
```

> Node [Subdivide Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivide_mesh.html)

#### Arguments:
- **level** (_Integer_ = None) : socket 'Level' (Level)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### subdivision_surface()

> method

``` python
subdivision_surface(level=None, edge_crease=None, vertex_crease=None, uv_smooth='PRESERVE_BOUNDARIES', boundary_smooth='ALL')
```

> Node [Subdivision Surface](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivision_surface.html)

#### Arguments:
- **level** (_Integer_ = None) : socket 'Level' (Level)
- **edge_crease** (_Float_ = None) : socket 'Edge Crease' (Edge Crease)
- **vertex_crease** (_Float_ = None) : socket 'Vertex Crease' (Vertex Crease)
- **uv_smooth** (_str_ = PRESERVE_BOUNDARIES) : Node.uv_smooth in ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')
- **boundary_smooth** (_str_ = ALL) : Node.boundary_smooth in ('PRESERVE_CORNERS', 'ALL')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### to_curve()

> method

``` python
to_curve()
```

> Node [Mesh to Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_curve.html)

#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### to_volume()

> method

``` python
to_volume(density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, amount=True)
```

> Node [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_volume.html)

- resolution_mode (str): Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (Voxel Amount)
- **interior_band_width** (_Float_ = None) : socket 'Interior Band Width' (Interior Band Width)
- **voxel_size** (_Float_ = None) : socket 'Voxel Size'
- **amount** (_bool_ = True) : resolution_mode is set to 'VOXEL_AMOUNT' (True) or 'VOXEL_SIZE' (False)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### triangulate()

> method

``` python
triangulate(minimum_vertices=None, quad_method='SHORTEST_DIAGONAL', ngon_method='BEAUTY')
```

> Node [Triangulate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/triangulate.html)

#### Arguments:
- **minimum_vertices** (_Integer_ = None) : socket 'Minimum Vertices' (Minimum Vertices)
- **quad_method** (_str_ = SHORTEST_DIAGONAL) : Node.quad_method in ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
- **ngon_method** (_str_ = BEAUTY) : Node.ngon_method in ('BEAUTY', 'CLIP')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### union()

> method

``` python
union(*meshes, self_intersection=None, hole_tolerant=None, solver='FLOAT')
```

> Node [Mesh Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html)

#### Arguments:
- **meshes** (_Mesh_) : socket 'Mesh 2' (Mesh 2)
- **self_intersection** (_Boolean_ = None) : socket 'Self Intersection' (Self Intersection)
- **hole_tolerant** (_Boolean_ = None) : socket 'Hole Tolerant' (Hole Tolerant)
- **solver** (_str_ = FLOAT) : Node.solver in ('EXACT', 'FLOAT')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### UVSphere()

> classmethod

``` python
UVSphere(segments=32, rings=16, radius=1.0)
```

> Constructor node [UV Sphere](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/uv_sphere.html)

#### Arguments:
- **segments** (_Integer_ = 32) : socket 'Segments' (Segments)
- **rings** (_Integer_ = 16) : socket 'Rings' (Rings)
- **radius** (_Float_ = 1.0) : socket 'Radius' (Radius)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>

----------
### uv_unwrap()

> method

``` python
uv_unwrap(seam=None, margin=None, fill_holes=False, method='ANGLE_BASED')
```

> Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_unwrap.html)

#### Arguments:
- **seam** (_Boolean_ = None) : socket 'Seam' (Seam)
- **margin** (_Float_ = None) : socket 'Margin' (Margin)
- **fill_holes** (_Boolean_ = False) : socket 'Fill Holes' (Fill Holes)
- **method** (_str_ = ANGLE_BASED) : Node.method in ('ANGLE_BASED', 'CONFORMAL')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Mesh](macro-geono-mesh.md#mesh) :black_small_square: [Content](macro-geono-mesh.md#content) :black_small_square: [Methods](macro-geono-mesh.md#methods)</sub>
