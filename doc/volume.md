# Volume

``` python
Volume(value=None, name=None, tip=None, panel=None, hide_value=False, hide_in_modifier=False)
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
- **panel** (_str_ = None) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

### Inherited

[\_\_add__](boolean.md#__add__) :black_small_square: [bake](nd.md#bake) :black_small_square: [bounding_box](core-gener-geome-geometry.md#bounding_box) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [convex_hull](core-gener-geome-geometry.md#convex_hull) :black_small_square: [curve](core-gener-geome-geometry.md#curve) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geo](geometry.md#_geo) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [grease_pencil](core-gener-geome-geometry.md#grease_pencil) :black_small_square: [id](core-gener-geome-geometry.md#id) :black_small_square: [index_of_nearest](core-gener-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](core-geono-geonodes.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instance_on_points](core-gener-geome-geometry.md#instance_on_points) :black_small_square: [instances](core-gener-geome-geometry.md#instances) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [Join](core-gener-geome-geometry.md#join) :black_small_square: [join](core-gener-geome-geometry.md#join) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [material](core-gener-geome-geometry.md#material) :black_small_square: [material_index](core-gener-geome-geometry.md#material_index) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [merge](core-gener-geome-geometry.md#merge) :black_small_square: [merge_all](core-gener-geome-geometry.md#merge_all) :black_small_square: [merge_by_distance](core-gener-geome-geometry.md#merge_by_distance) :black_small_square: [merge_connected](core-gener-geome-geometry.md#merge_connected) :black_small_square: [mesh](core-gener-geome-geometry.md#mesh) :black_small_square: [name](core-gener-geome-geometry.md#name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [\_node_OLD](geometry.md#_node_old) :black_small_square: [offset](core-gener-geome-geometry.md#offset) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [point_cloud](core-gener-geome-geometry.md#point_cloud) :black_small_square: [position](core-gener-geome-geometry.md#position) :black_small_square: [proximity](core-gener-geome-geometry.md#proximity) :black_small_square: [proximity_edges](core-gener-geome-geometry.md#proximity_edges) :black_small_square: [proximity_faces](core-gener-geome-geometry.md#proximity_faces) :black_small_square: [proximity_points](core-gener-geome-geometry.md#proximity_points) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [raycast](core-gener-geome-geometry.md#raycast) :black_small_square: [raycast_interpolated](core-gener-geome-geometry.md#raycast_interpolated) :black_small_square: [raycast_nearest](core-gener-geome-geometry.md#raycast_nearest) :black_small_square: [realize](core-gener-geome-geometry.md#realize) :black_small_square: [remove_named_attribute](core-gener-geome-geometry.md#remove_named_attribute) :black_small_square: [remove_names](core-gener-geome-geometry.md#remove_names) :black_small_square: [replace_material](core-gener-geome-geometry.md#replace_material) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](geobase.md#_sel) :black_small_square: [separate_components](core-gener-geome-geometry.md#separate_components) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [set_id](core-gener-geome-geometry.md#set_id) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [set_material](core-gener-geome-geometry.md#set_material) :black_small_square: [set_material_index](core-gener-geome-geometry.md#set_material_index) :black_small_square: [set_name](core-gener-geome-geometry.md#set_name) :black_small_square: [set_position](core-gener-geome-geometry.md#set_position) :black_small_square: [set_spline_cyclic](core-gener-geome-geometry.md#set_spline_cyclic) :black_small_square: [set_spline_resolution](core-gener-geome-geometry.md#set_spline_resolution) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [to_instance](core-gener-geome-geometry.md#to_instance) :black_small_square: [transform](core-gener-geome-geometry.md#transform) :black_small_square: [transform_components](core-gener-geome-geometry.md#transform_components) :black_small_square: [transform_geometry](core-gener-geome-geometry.md#transform_geometry) :black_small_square: [transform_matrix](core-gener-geome-geometry.md#transform_matrix) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square: [viewer](core-gener-geome-geometry.md#viewer) :black_small_square: [volume](core-gener-geome-geometry.md#volume) :black_small_square:

## Content

- **C** : [Cube](volume.md#cube)
- **D** : [distribute_points](volume.md#distribute_points) :black_small_square: [distribute_points_density_grid](volume.md#distribute_points_density_grid) :black_small_square: [distribute_points_density_random](volume.md#distribute_points_density_random)
- **G** : [get_named_grid](volume.md#get_named_grid)
- **N** : [named_float_grid](volume.md#named_float_grid) :black_small_square: [named_vector_grid](volume.md#named_vector_grid)
- **S** : [store_named_grid](volume.md#store_named_grid)
- **T** : [to_mesh](volume.md#to_mesh) :black_small_square: [to_mesh_grid](volume.md#to_mesh_grid) :black_small_square: [to_mesh_voxel_amount](volume.md#to_mesh_voxel_amount) :black_small_square: [to_mesh_voxel_size](volume.md#to_mesh_voxel_size)

## Methods



----------
### Cube()

> classmethod

``` python
Cube(density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None)
```

> Node [Volume Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/primitives/volume_cube.html)

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **background** (_Float_ = None) : socket 'Background' (id: Background)
- **min** (_Vector_ = None) : socket 'Min' (id: Min)
- **max** (_Vector_ = None) : socket 'Max' (id: Max)
- **resolution_x** (_Integer_ = None) : socket 'Resolution X' (id: Resolution X)
- **resolution_y** (_Integer_ = None) : socket 'Resolution Y' (id: Resolution Y)
- **resolution_z** (_Integer_ = None) : socket 'Resolution Z' (id: Resolution Z)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### distribute_points()

> method

``` python
distribute_points(density=None, seed=None, mode='DENSITY_RANDOM')
```

> Node ERROR: Node 'Distribute Points in Volume' not found

#### Information:
- **Socket** : self



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)
- **mode** (_str_ = DENSITY_RANDOM) : parameter 'mode' in ('DENSITY_RANDOM', 'DENSITY_GRID')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### distribute_points_density_grid()

> method

``` python
distribute_points_density_grid(spacing=None, threshold=None)
```

> Node ERROR: Node 'Distribute Points in Volume' not found

#### Information:
- **Socket** : self
- **Parameter** : 'DENSITY_GRID'



#### Arguments:
- **spacing** (_Vector_ = None) : socket 'Spacing' (id: Spacing)
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### distribute_points_density_random()

> method

``` python
distribute_points_density_random(density=None, seed=None)
```

> Node ERROR: Node 'Distribute Points in Volume' not found

#### Information:
- **Socket** : self
- **Parameter** : 'DENSITY_RANDOM'



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### get_named_grid()

> method

``` python
get_named_grid(name=None, remove=None, data_type='FLOAT')
```

> Node ERROR: Node 'Get Named Grid' not found

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **remove** (_Boolean_ = None) : socket 'Remove' (id: Remove)
- **data_type** (_str_ = FLOAT) : parameter 'data_type' in ('FLOAT', 'VECTOR')



#### Returns:
- **Volume** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### named_float_grid()

> method

``` python
named_float_grid(name=None, remove=None)
```

> Node ERROR: Node 'Get Named Grid' not found

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **remove** (_Boolean_ = None) : socket 'Remove' (id: Remove)



#### Returns:
- **Volume** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### named_vector_grid()

> method

``` python
named_vector_grid(name=None, remove=None)
```

> Node ERROR: Node 'Get Named Grid' not found

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **remove** (_Boolean_ = None) : socket 'Remove' (id: Remove)



#### Returns:
- **Volume** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### store_named_grid()

> method

``` python
store_named_grid(name=None, grid=None)
```

> Node ERROR: Node 'Store Named Grid' not found

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : depending on 'grid' type



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **grid** (_Float_ = None) : socket 'Grid' (id: Grid)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### to_mesh()

> method

``` python
to_mesh(threshold=None, adaptivity=None, resolution_mode='GRID')
```

> Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Information:
- **Socket** : self



#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (id: Adaptivity)
- **resolution_mode** (_str_ = GRID) : parameter 'resolution_mode' in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')



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

#### Information:
- **Socket** : self
- **Parameter** : 'GRID'



#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (id: Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### to_mesh_voxel_amount()

> method

``` python
to_mesh_voxel_amount(voxel_amount=None, threshold=None, adaptivity=None)
```

> Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VOXEL_AMOUNT'



#### Arguments:
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (id: Voxel Amount)
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (id: Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### to_mesh_voxel_size()

> method

``` python
to_mesh_voxel_size(voxel_size=None, threshold=None, adaptivity=None)
```

> Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VOXEL_SIZE'



#### Arguments:
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (id: Voxel Size)
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (id: Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>