# Volume

> Bases classes: [Geometry](geometry.md#geometry)

``` python
Volume(value=None, name=None, tip=None)
```

> Volume Geometry

The **Volume** class exposes all methods specific to volume.
Since there is no ambiguity, the word **volume** is omitted in the name of
the methods:

``` python
cube = Volume.Cube() # Node 'Volume Cube'
```

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geometry.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [blur](socket.md#blur) :black_small_square: [bounding_box](geometry.md#bounding_box) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [convex_hull](geometry.md#convex_hull) :black_small_square: [curve](geometry.md#curve) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geo](geometry.md#_geo) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [id](geobase.md#id) :black_small_square: [index_of_nearest](geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](geometry.md#__init__) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instances](geometry.md#instances) :black_small_square: [Join](geometry.md#join) :black_small_square: [join](geometry.md#join) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [material](geobase.md#material) :black_small_square: [material_index](geobase.md#material_index) :black_small_square: [material_selection](geobase.md#material_selection) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [merge_by_distance](geometry.md#merge_by_distance) :black_small_square: [mesh](geometry.md#mesh) :black_small_square: [\_node](geometry.md#_node) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [offset](geobase.md#offset) :black_small_square: [out](socket.md#out) :black_small_square: [point_cloud](geometry.md#point_cloud) :black_small_square: [position](geobase.md#position) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [raycast](geometry.md#raycast) :black_small_square: [remove_named_attribute](geometry.md#remove_named_attribute) :black_small_square: [replace_material](geobase.md#replace_material) :black_small_square: [\_sel](geobase.md#_sel) :black_small_square: [separate_components](geometry.md#separate_components) :black_small_square: [set_id](geometry.md#set_id) :black_small_square: [set_material](geometry.md#set_material) :black_small_square: [set_position](geometry.md#set_position) :black_small_square: [set_shade_smooth](geometry.md#set_shade_smooth) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [to_instance](geometry.md#to_instance) :black_small_square: [transform](geometry.md#transform) :black_small_square: [viewer](geometry.md#viewer) :black_small_square: [volume](geometry.md#volume) :black_small_square:

## Content

- [Cube](volume.md#cube)
- [distribute_grid](volume.md#distribute_grid)
- [distribute_points](volume.md#distribute_points)
- [distribute_random](volume.md#distribute_random)
- [FromMesh](volume.md#frommesh)
- [FromPoints](volume.md#frompoints)
- [to_mesh](volume.md#to_mesh)
- [to_mesh_amount](volume.md#to_mesh_amount)
- [to_mesh_grid](volume.md#to_mesh_grid)
- [to_mesh_size](volume.md#to_mesh_size)

## Methods



----------
### Cube()

> classmethod

``` python
Cube(density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None)
```

> Constructor node [Volume Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/primitives/volume_cube.html)

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)
- **background** (_Float_ = None) : socket 'Background' (Background)
- **min** (_Vector_ = None) : socket 'Min' (Min)
- **max** (_Vector_ = None) : socket 'Max' (Max)
- **resolution_x** (_Integer_ = None) : socket 'Resolution X' (Resolution X)
- **resolution_y** (_Integer_ = None) : socket 'Resolution Y' (Resolution Y)
- **resolution_z** (_Integer_ = None) : socket 'Resolution Z' (Resolution Z)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### distribute_grid()

> method

``` python
distribute_grid(spacing=None, threshold=None)
```

> Node ERROR: Node 'Distribute Points in Volume' not found

#### Arguments:
- **spacing** (_Vector_ = None) : socket 'Spacing' (Spacing)
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### distribute_points()

> method

``` python
distribute_points(density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM')
```

> Node ERROR: Node 'Distribute Points in Volume' not found

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)
- **spacing** (_Vector_ = None) : socket 'Spacing' (Spacing)
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **mode** (_str_ = DENSITY_RANDOM) : Node.mode in ('DENSITY_RANDOM', 'DENSITY_GRID')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### distribute_random()

> method

``` python
distribute_random(density=None, seed=None)
```

> Node ERROR: Node 'Distribute Points in Volume' not found

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### FromMesh()

> classmethod

``` python
FromMesh(mesh, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, amount=True)
```

> Constructor node [Mesh to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_volume.html)

#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (Mesh)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (Voxel Amount)
- **interior_band_width** (_Float_ = None) : socket 'Interior Band Width' (Interior Band Width)
- **voxel_size** ( = None)
- **amount** ( = True)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### FromPoints()

> classmethod

``` python
FromPoints(points, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

> Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)

#### Arguments:
- **points** (_Geometry_) : socket 'Points' (Points)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_size** ( = None)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (Voxel Amount)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **resolution_mode** (_str_ = VOXEL_AMOUNT) : Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### to_mesh()

> method

``` python
to_mesh(voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID')
```

> Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Arguments:
- **voxel_size** (_Float_ = None) : socket 'Voxel Size'
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount'
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)
- **resolution_mode** (_str_ = GRID) : Node.resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### to_mesh_amount()

> method

``` python
to_mesh_amount(voxel_amount=None, threshold=None, adaptivity=None)
```

> Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Arguments:
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount'
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### to_mesh_grid()

> method

``` python
to_mesh_grid(threshold=None, adaptivity=None)
```

> Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### to_mesh_size()

> method

``` python
to_mesh_size(voxel_size=None, threshold=None, adaptivity=None)
```

> Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Arguments:
- **voxel_size** (_Float_ = None) : socket 'Voxel Size'
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>