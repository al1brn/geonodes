# Volume

``` python
Volume(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', **props)
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
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **props** (_dict_) : input properties

### Inherited

[\_\_add__](boolean.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [bounding_box](core-gener-geome-geometry.md#bounding_box) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_class_test](core-socke-socket.md#_class_test) :black_small_square: [Constant](core-socke-socket.md#constant) :black_small_square: [convex_hull](core-gener-geome-geometry.md#convex_hull) :black_small_square: [\_create_input_socket](core-gener-geome-geometry.md#_create_input_socket) :black_small_square: [curve](core-gener-geome-geometry.md#curve) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [Empty](core-socke-socket.md#empty) :black_small_square: [enable_output](core-gener-geome-geometry.md#enable_output) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_geo](cloudpoint.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socke-socket.md#_get_bsocket_from_input) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](geom.md#get_selection) :black_small_square: [grease_pencil](core-gener-geome-geometry.md#grease_pencil) :black_small_square: [\_\_iadd__](float.md#__iadd__) :black_small_square: [id](core-gener-geome-geometry.md#id) :black_small_square: [index_of_nearest](core-gener-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [instance_on_points](core-gener-geome-geometry.md#instance_on_points) :black_small_square: [instances](core-gener-geome-geometry.md#instances) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socke-socket.md#_is_empty) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [Join](core-gener-geome-geometry.md#join) :black_small_square: [join](core-gener-geome-geometry.md#join) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_inputs](core-socke-socket.md#link_inputs) :black_small_square: [material](core-gener-geome-geometry.md#material) :black_small_square: [material_index](core-gener-geome-geometry.md#material_index) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [merge](core-gener-geome-geometry.md#merge) :black_small_square: [merge_by_distance](core-gener-geome-geometry.md#merge_by_distance) :black_small_square: [mesh](core-gener-geome-geometry.md#mesh) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [name](core-gener-geome-geometry.md#name) :black_small_square: [Named](core-socke-socket.md#named) :black_small_square: [NewInput](core-socke-socket.md#newinput) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [offset](core-gener-geome-geometry.md#offset) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [out_OLD](geometry.md#out_old) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [point_cloud](core-gener-geome-geometry.md#point_cloud) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [position](core-gener-geome-geometry.md#position) :black_small_square: [proximity](core-gener-geome-geometry.md#proximity) :black_small_square: [proximity_edges](core-gener-geome-geometry.md#proximity_edges) :black_small_square: [proximity_faces](core-gener-geome-geometry.md#proximity_faces) :black_small_square: [proximity_points](core-gener-geome-geometry.md#proximity_points) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [raycast](core-gener-geome-geometry.md#raycast) :black_small_square: [realize](core-gener-geome-geometry.md#realize) :black_small_square: [remove_named_attribute](core-gener-geome-geometry.md#remove_named_attribute) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [replace_material](core-gener-geome-geometry.md#replace_material) :black_small_square: ['_selection' not found]() :black_small_square: [separate_components](core-gener-geome-geometry.md#separate_components) :black_small_square: [set_id](core-gener-geome-geometry.md#set_id) :black_small_square: [set_material](core-gener-geome-geometry.md#set_material) :black_small_square: [set_material_index](core-gener-geome-geometry.md#set_material_index) :black_small_square: [set_name](core-gener-geome-geometry.md#set_name) :black_small_square: [set_position](core-gener-geome-geometry.md#set_position) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: [\_socket_type](core-socke-socket.md#_socket_type) :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: [to_instance](core-gener-geome-geometry.md#to_instance) :black_small_square: [transform](core-gener-geome-geometry.md#transform) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square: [viewer](core-gener-geome-geometry.md#viewer) :black_small_square: [volume](core-gener-geome-geometry.md#volume) :black_small_square:

## Content

- [Cube](volume.md#cube)
- [distribute_points](volume.md#distribute_points)
- [get_named_grid](volume.md#get_named_grid)
- [ImportVDB](volume.md#importvdb)
- [store_named_grid](volume.md#store_named_grid)
- [to_mesh](volume.md#to_mesh)

## Methods



----------
### Cube()

> classmethod

``` python
Cube(density: 'Float' = None, background: 'Float' = None, min: 'Vector' = None, max: 'Vector' = None, resolution_x: 'Integer' = None, resolution_y: 'Integer' = None, resolution_z: 'Integer' = None)
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
distribute_points(mode: "Literal['Random', 'Grid']" = None, density: 'Float' = None, seed: 'Integer' = None, spacing: 'Vector' = None, threshold: 'Float' = None)
```

> Node ERROR: Node 'Distribute Points in Volume' not found

#### Information:
- **Socket** : self



#### Arguments:
- **mode** (_Literal['Random', 'Grid']_ = None) : ('Random', 'Grid')
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)
- **spacing** (_Vector_ = None) : socket 'Spacing' (id: Spacing)
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### get_named_grid()

> method

``` python
get_named_grid(name: 'String' = None, remove: 'Boolean' = None, data_type: "Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']" = 'FLOAT')
```

> Node [Get Named Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/get_named_grid.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **remove** (_Boolean_ = None) : socket 'Remove' (id: Remove)
- **data_type** (_Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']_ = FLOAT) : parameter 'data_type' in ['FLOAT', 'INT', 'BOOLEAN', 'VECTOR']



#### Returns:
- **grid** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### ImportVDB()

> classmethod

``` python
ImportVDB(path: 'String' = None)
```

> Node ERROR: Node 'Import VDB' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### store_named_grid()

> method

``` python
store_named_grid(name: 'String' = None, grid: 'Boolean | Float | Integer | Vector' = None)
```

> Node [Store Named Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/store_named_grid.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : depending on 'grid' type



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **grid** (_Boolean | Float | Integer | Vector_ = None) : socket 'Grid' (id: Grid)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>

----------
### to_mesh()

> method

``` python
to_mesh(resolution_mode: "Literal['Grid', 'Amount', 'Size']" = None, voxel_size: 'Float' = None, voxel_amount: 'Float' = None, threshold: 'Float' = None, adaptivity: 'Float' = None)
```

> Node [Volume to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/volume_to_mesh.html)

#### Information:
- **Socket** : self



#### Arguments:
- **resolution_mode** (_Literal['Grid', 'Amount', 'Size']_ = None) : ('Grid', 'Amount', 'Size')
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (id: Voxel Size)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (id: Voxel Amount)
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (id: Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](volume.md#volume) :black_small_square: [Content](volume.md#content) :black_small_square: [Methods](volume.md#methods)</sub>