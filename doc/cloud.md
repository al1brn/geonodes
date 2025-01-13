# Cloud

``` python
Cloud(value=None, name=None, tip=None, panel=None, hide_value=False, hide_in_modifier=False)
```

> Cloud of Points Geometry

> [!NOTE]
> In Blender, the name can vary between **Point Cloud** and **Points**.
> In GeoNodes, the geometry is named **Cloud**.

The **Cloud** exposes all methods specific to points cloud.
Since there is no ambiguity, the word **points** is omitted in the name of
the methods:

``` python
curves = cloud.to_curves() # Node 'Points to Curves'
```

Nodes requiring a domain parameter, are implemented in the domain [points](cloud.md#points).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

### Inherited

[\_\_add__](boolean.md#__add__) :black_small_square: [bake](nd.md#bake) :black_small_square: [bounding_box](core-gener-geome-geometry.md#bounding_box) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [convex_hull](core-gener-geome-geometry.md#convex_hull) :black_small_square: [curve](core-gener-geome-geometry.md#curve) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geo](cloudpoint.md#_geo) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [grease_pencil](core-gener-geome-geometry.md#grease_pencil) :black_small_square: [id](core-gener-geome-geometry.md#id) :black_small_square: [index_of_nearest](core-gener-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](boolean.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instance_on_points](core-gener-geome-geometry.md#instance_on_points) :black_small_square: [instances](core-gener-geome-geometry.md#instances) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [Join](core-gener-geome-geometry.md#join) :black_small_square: [join](core-gener-geome-geometry.md#join) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [material](core-gener-geome-geometry.md#material) :black_small_square: [material_index](core-gener-geome-geometry.md#material_index) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [merge](core-gener-geome-geometry.md#merge) :black_small_square: [merge_all](core-gener-geome-geometry.md#merge_all) :black_small_square: [merge_by_distance](core-gener-geome-geometry.md#merge_by_distance) :black_small_square: [merge_connected](core-gener-geome-geometry.md#merge_connected) :black_small_square: [mesh](core-gener-geome-geometry.md#mesh) :black_small_square: [name](core-gener-geome-geometry.md#name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [offset](core-gener-geome-geometry.md#offset) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [point_cloud](core-gener-geome-geometry.md#point_cloud) :black_small_square: [position](core-gener-geome-geometry.md#position) :black_small_square: [proximity](core-gener-geome-geometry.md#proximity) :black_small_square: [proximity_edges](core-gener-geome-geometry.md#proximity_edges) :black_small_square: [proximity_faces](core-gener-geome-geometry.md#proximity_faces) :black_small_square: [proximity_points](core-gener-geome-geometry.md#proximity_points) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [raycast](core-gener-geome-geometry.md#raycast) :black_small_square: [raycast_interpolated](core-gener-geome-geometry.md#raycast_interpolated) :black_small_square: [raycast_nearest](core-gener-geome-geometry.md#raycast_nearest) :black_small_square: [realize](core-gener-geome-geometry.md#realize) :black_small_square: [remove_named_attribute](core-gener-geome-geometry.md#remove_named_attribute) :black_small_square: [remove_names](core-gener-geome-geometry.md#remove_names) :black_small_square: [replace_material](core-gener-geome-geometry.md#replace_material) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](geobase.md#_sel) :black_small_square: [separate_components](core-gener-geome-geometry.md#separate_components) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [set_id](core-gener-geome-geometry.md#set_id) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [set_material](core-gener-geome-geometry.md#set_material) :black_small_square: [set_material_index](core-gener-geome-geometry.md#set_material_index) :black_small_square: [set_name](core-gener-geome-geometry.md#set_name) :black_small_square: [set_position](core-gener-geome-geometry.md#set_position) :black_small_square: [set_spline_cyclic](core-gener-geome-geometry.md#set_spline_cyclic) :black_small_square: [set_spline_resolution](core-gener-geome-geometry.md#set_spline_resolution) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [to_instance](core-gener-geome-geometry.md#to_instance) :black_small_square: [transform](core-gener-geome-geometry.md#transform) :black_small_square: [transform_components](core-gener-geome-geometry.md#transform_components) :black_small_square: [transform_matrix](core-gener-geome-geometry.md#transform_matrix) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square: [viewer](core-gener-geome-geometry.md#viewer) :black_small_square: [volume](core-gener-geome-geometry.md#volume) :black_small_square:

## Content

- **D** : [DistributeInGrid](cloud.md#distributeingrid) :black_small_square: [DistributeingridDensityGrid](cloud.md#distributeingriddensitygrid) :black_small_square: [DistributeingridDensityRandom](cloud.md#distributeingriddensityrandom) :black_small_square: [domain_size](cloud.md#domain_size)
- **I** : [instance_on](cloud.md#instance_on) :black_small_square: [interpolate_curves](cloud.md#interpolate_curves)
- **P** : [points](cloud.md#points) :black_small_square: [Points](cloud.md#points)
- **R** : [radius](cloud.md#radius)
- **T** : [to_curves](cloud.md#to_curves) :black_small_square: [to_sdf_grid](cloud.md#to_sdf_grid) :black_small_square: [to_vertices](cloud.md#to_vertices) :black_small_square: [to_volume](cloud.md#to_volume)

## Properties



### points

> _type_: **CloudPoint**
>

POINT domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Properties](cloud.md#properties)</sub>

### radius

> _type_: **?**
>

Property get node <Node Set Point Radius>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Properties](cloud.md#properties)</sub>

## Methods



----------
### DistributeInGrid()

> classmethod

``` python
DistributeInGrid(grid=None, density=None, seed=None, mode='DENSITY_RANDOM')
```

> Node ERROR: Node 'Distribute Points in Grid' not found

#### Arguments:
- **grid** (_Float_ = None) : socket 'Grid' (id: Grid)
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)
- **mode** (_str_ = DENSITY_RANDOM) : parameter 'mode' in ('DENSITY_RANDOM', 'DENSITY_GRID')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### DistributeingridDensityGrid()

> classmethod

``` python
DistributeingridDensityGrid(grid=None, spacing=None, threshold=None)
```

> Node ERROR: Node 'Distribute Points in Grid' not found

#### Information:
- **Parameter** : 'DENSITY_GRID'



#### Arguments:
- **grid** (_Float_ = None) : socket 'Grid' (id: Grid)
- **spacing** (_Vector_ = None) : socket 'Spacing' (id: Spacing)
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### DistributeingridDensityRandom()

> classmethod

``` python
DistributeingridDensityRandom(grid=None, density=None, seed=None)
```

> Node ERROR: Node 'Distribute Points in Grid' not found

#### Information:
- **Parameter** : 'DENSITY_RANDOM'



#### Arguments:
- **grid** (_Float_ = None) : socket 'Grid' (id: Grid)
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### domain_size()

> method

``` python
domain_size()
```

> Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

#### Information:
- **Socket** : self
- **Parameter** : 'POINTCLOUD'



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### instance_on()

> method

``` python
instance_on(instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

> Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **instance** (_Geometry_ = None) : socket 'Instance' (id: Instance)
- **pick_instance** (_Boolean_ = None) : socket 'Pick Instance' (id: Pick Instance)
- **instance_index** (_Integer_ = None) : socket 'Instance Index' (id: Instance Index)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### interpolate_curves()

> method

``` python
interpolate_curves(guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None)
```

> Node [Interpolate Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **guide_curves** (_Geometry_ = None) : socket 'Guide Curves' (id: Guide Curves)
- **guide_up** (_Vector_ = None) : socket 'Guide Up' (id: Guide Up)
- **guide_group_id** (_Integer_ = None) : socket 'Guide Group ID' (id: Guide Group ID)
- **point_up** (_Vector_ = None) : socket 'Point Up' (id: Point Up)
- **point_group_id** (_Integer_ = None) : socket 'Point Group ID' (id: Point Group ID)
- **max_neighbors** (_Integer_ = None) : socket 'Max Neighbors' (id: Max Neighbors)



#### Returns:
- **Curve** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### Points()

> classmethod

``` python
Points(count=None, position=None, radius=None)
```

> Node [Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html)

#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(curve_group_id=None, weight=None)
```

> Node [Points to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **curve_group_id** (_Integer_ = None) : socket 'Curve Group ID' (id: Curve Group ID)
- **weight** (_Float_ = None) : socket 'Weight' (id: Weight)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### to_sdf_grid()

> method

``` python
to_sdf_grid(radius=None, voxel_size=None)
```

> Node ERROR: Node 'Points to SDF Grid' not found

#### Information:
- **Socket** : self



#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (id: Voxel Size)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### to_vertices()

> method

``` python
to_vertices()
```

> Node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### to_volume()

> method

``` python
to_volume(density=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

> Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)

#### Information:
- **Socket** : self



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (id: Voxel Amount)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **resolution_mode** (_str_ = VOXEL_AMOUNT) : parameter 'resolution_mode' in ('VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>