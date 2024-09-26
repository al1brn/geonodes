# Volume

> Bases classes: [Geometry](geono-geome-geometry.md#geometry)

``` python
Volume(value=None, name=None, tip=None)
```

Socket of type 'GEOMETRY'.

If value is None, a Group Input socket of type Geometry is created.
When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geono-geome-geometry.md#__add__) :black_small_square: [bake](geono-geome-geometry.md#bake) :black_small_square: [blur](geono-socke-socket.md#blur) :black_small_square: [bounding_box](geono-geome-geometry.md#bounding_box) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [convex_hull](geono-geome-geometry.md#convex_hull) :black_small_square: [curve](geono-geome-geometry.md#curve) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_geo](geono-geome-geometry.md#_geo) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [index_of_nearest](geono-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [instances](geono-geome-geometry.md#instances) :black_small_square: [join](geono-geome-geometry.md#join) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [merge_by_distance](geono-geome-geometry.md#merge_by_distance) :black_small_square: [mesh](geono-geome-geometry.md#mesh) :black_small_square: [\_node](geono-geome-geometry.md#_node) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [point_cloud](geono-geome-geometry.md#point_cloud) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [raycast](geono-geome-geometry.md#raycast) :black_small_square: [remove_named_attribute](geono-geome-geometry.md#remove_named_attribute) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [\_sel](geono-geome-geobase.md#_sel) :black_small_square: [separate_components](geono-geome-geometry.md#separate_components) :black_small_square: [set_id](geono-geome-geometry.md#set_id) :black_small_square: [set_material](geono-geome-geometry.md#set_material) :black_small_square: [set_position](geono-geome-geometry.md#set_position) :black_small_square: [set_shade_smooth](geono-geome-geometry.md#set_shade_smooth) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square: [to_instance](geono-geome-geometry.md#to_instance) :black_small_square: [to_output](geono-socke-socket.md#to_output) :black_small_square: [transform](geono-geome-geometry.md#transform) :black_small_square: [viewer](geono-geome-geometry.md#viewer) :black_small_square: [volume](geono-geome-geometry.md#volume) :black_small_square:

## Content

- [Cube](geono-geome-volume.md#cube)
- [distribute_grid](geono-geome-volume.md#distribute_grid)
- [distribute_points](geono-geome-volume.md#distribute_points)
- [distribute_random](geono-geome-volume.md#distribute_random)
- [FromMesh](geono-geome-volume.md#frommesh)
- [FromPoints](geono-geome-volume.md#frompoints)
- [to_mesh](geono-geome-volume.md#to_mesh)
- [to_mesh_amount](geono-geome-volume.md#to_mesh_amount)
- [to_mesh_grid](geono-geome-volume.md#to_mesh_grid)
- [to_mesh_size](geono-geome-volume.md#to_mesh_size)

## Methods



----------
### Cube()

> classmethod

``` python
Cube(density=None, background=None, min=None, max=None, resolution_x=None, resolution_y=None, resolution_z=None)
```

Node 'Volume Cube' (GeometryNodeVolumeCube)

[!Node] Volume Cube

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>

----------
### distribute_grid()

> method

``` python
distribute_grid(spacing=None, threshold=None)
```

Node 'Distribute Points in Volume' (GeometryNodeDistributePointsInVolume)

[!Node] Distribute Points in Volume

#### Arguments:
- **spacing** (_Vector_ = None) : socket 'Spacing' (Spacing)
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>

----------
### distribute_points()

> method

``` python
distribute_points(density=None, seed=None, spacing=None, threshold=None, mode='DENSITY_RANDOM')
```

Node 'Distribute Points in Volume' (GeometryNodeDistributePointsInVolume)

[!Node] Distribute Points in Volume

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)
- **spacing** (_Vector_ = None) : socket 'Spacing' (Spacing)
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **mode** (_str_ = DENSITY_RANDOM) : Node.mode in ('DENSITY_RANDOM', 'DENSITY_GRID')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>

----------
### distribute_random()

> method

``` python
distribute_random(density=None, seed=None)
```

Node 'Distribute Points in Volume' (GeometryNodeDistributePointsInVolume)

[!Node] Distribute Points in Volume

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>

----------
### FromMesh()

> classmethod

``` python
FromMesh(mesh, density=None, voxel_amount=None, interior_band_width=None, voxel_size=None, amount=True)
```

Node 'Mesh to Volume' (GeometryNodeMeshToVolume)

[!Node] Mesh to Volume

#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (Mesh)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (Voxel Amount)
- **interior_band_width** (_Float_ = None) : socket 'Interior Band Width' (Interior Band Width)
- **voxel_size** ( = None)
- **amount** ( = True)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>

----------
### FromPoints()

> classmethod

``` python
FromPoints(points, density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

Node 'Points to Volume' (GeometryNodePointsToVolume)

[!Node] Points to Volume

#### Arguments:
- **points** (_Geometry_) : socket 'Points' (Points)
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_size** ( = None)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (Voxel Amount)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **resolution_mode** (_str_ = VOXEL_AMOUNT) : Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>

----------
### to_mesh()

> method

``` python
to_mesh(voxel_size=None, voxel_amount=None, threshold=None, adaptivity=None, resolution_mode='GRID')
```

Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

[!Node] Volume to Mesh

#### Arguments:
- **voxel_size** (_Float_ = None) : socket 'Voxel Size'
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount'
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)
- **resolution_mode** (_str_ = GRID) : Node.resolution_mode in ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>

----------
### to_mesh_amount()

> method

``` python
to_mesh_amount(voxel_amount=None, threshold=None, adaptivity=None)
```

Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

[!Node] Volume to Mesh

#### Arguments:
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount'
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>

----------
### to_mesh_grid()

> method

``` python
to_mesh_grid(threshold=None, adaptivity=None)
```

Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

[!Node] Volume to Mesh

#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>

----------
### to_mesh_size()

> method

``` python
to_mesh_size(voxel_size=None, threshold=None, adaptivity=None)
```

Node 'Volume to Mesh' (GeometryNodeVolumeToMesh)

[!Node] Volume to Mesh

#### Arguments:
- **voxel_size** (_Float_ = None) : socket 'Voxel Size'
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Volume](geono-geome-volume.md#volume) :black_small_square: [Content](geono-geome-volume.md#content) :black_small_square: [Methods](geono-geome-volume.md#methods)</sub>