# Cloud

``` python
Cloud(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', **props)
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
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **props** (_dict_) : input properties

### Inherited

[\_\_add__](boolean.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [bounding_box](core-gener-geome-geometry.md#bounding_box) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_class_test](core-socke-socket.md#_class_test) :black_small_square: [Constant](core-socke-socket.md#constant) :black_small_square: [convex_hull](core-gener-geome-geometry.md#convex_hull) :black_small_square: [\_create_input_socket](core-gener-geome-geometry.md#_create_input_socket) :black_small_square: [curve](core-gener-geome-geometry.md#curve) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [Empty](core-socke-socket.md#empty) :black_small_square: [enable_output](core-gener-geome-geometry.md#enable_output) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_geo](cloudpoint.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socke-socket.md#_get_bsocket_from_input) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](geom.md#get_selection) :black_small_square: [grease_pencil](core-gener-geome-geometry.md#grease_pencil) :black_small_square: [\_\_iadd__](float.md#__iadd__) :black_small_square: [id](core-gener-geome-geometry.md#id) :black_small_square: [index_of_nearest](core-gener-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [instance_on_points](core-gener-geome-geometry.md#instance_on_points) :black_small_square: [instances](core-gener-geome-geometry.md#instances) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socke-socket.md#_is_empty) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [Join](core-gener-geome-geometry.md#join) :black_small_square: [join](core-gener-geome-geometry.md#join) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_inputs](core-socke-socket.md#link_inputs) :black_small_square: [material](core-gener-geome-geometry.md#material) :black_small_square: [material_index](core-gener-geome-geometry.md#material_index) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [merge](core-gener-geome-geometry.md#merge) :black_small_square: [merge_by_distance](core-gener-geome-geometry.md#merge_by_distance) :black_small_square: [mesh](core-gener-geome-geometry.md#mesh) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [name](core-gener-geome-geometry.md#name) :black_small_square: [Named](core-socke-socket.md#named) :black_small_square: [NewInput](core-socke-socket.md#newinput) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [offset](core-gener-geome-geometry.md#offset) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [out_OLD](geometry.md#out_old) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [point_cloud](core-gener-geome-geometry.md#point_cloud) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [position](core-gener-geome-geometry.md#position) :black_small_square: [proximity](core-gener-geome-geometry.md#proximity) :black_small_square: [proximity_edges](core-gener-geome-geometry.md#proximity_edges) :black_small_square: [proximity_faces](core-gener-geome-geometry.md#proximity_faces) :black_small_square: [proximity_points](core-gener-geome-geometry.md#proximity_points) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [raycast](core-gener-geome-geometry.md#raycast) :black_small_square: [realize](core-gener-geome-geometry.md#realize) :black_small_square: [remove_named_attribute](core-gener-geome-geometry.md#remove_named_attribute) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [replace_material](core-gener-geome-geometry.md#replace_material) :black_small_square: ['_selection' not found]() :black_small_square: [separate_components](core-gener-geome-geometry.md#separate_components) :black_small_square: [set_id](core-gener-geome-geometry.md#set_id) :black_small_square: [set_material](core-gener-geome-geometry.md#set_material) :black_small_square: [set_material_index](core-gener-geome-geometry.md#set_material_index) :black_small_square: [set_name](core-gener-geome-geometry.md#set_name) :black_small_square: [set_position](core-gener-geome-geometry.md#set_position) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: [\_socket_type](core-socke-socket.md#_socket_type) :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: [to_instance](core-gener-geome-geometry.md#to_instance) :black_small_square: [transform](core-gener-geome-geometry.md#transform) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square: [viewer](core-gener-geome-geometry.md#viewer) :black_small_square: [volume](core-gener-geome-geometry.md#volume) :black_small_square:

## Content

- **D** : [domain_size](cloud.md#domain_size)
- **I** : [ImportCSV](cloud.md#importcsv) :black_small_square: [instance_on](cloud.md#instance_on) :black_small_square: [interpolate_curves](cloud.md#interpolate_curves)
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
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### ImportCSV()

> classmethod

``` python
ImportCSV(path: 'String' = None, delimiter: 'String' = None)
```

> Node ERROR: Node 'Import CSV' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)
- **delimiter** (_String_ = None) : socket 'Delimiter' (id: Delimiter)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### instance_on()

> method

``` python
instance_on(instance: 'Instances' = None, pick_instance: 'Boolean' = None, instance_index: 'Integer' = None, rotation: 'Rotation' = None, scale: 'Vector' = None)
```

> Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **instance** (_Instances_ = None) : socket 'Instance' (id: Instance)
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
interpolate_curves(guide_curves: 'Curve' = None, guide_up: 'Vector' = None, guide_group_id: 'Integer' = None, point_up: 'Vector' = None, point_group_id: 'Integer' = None, max_neighbors: 'Integer' = None)
```

> Node [Interpolate Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **guide_curves** (_Curve_ = None) : socket 'Guide Curves' (id: Guide Curves)
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
Points(count: 'Integer' = None, position: 'Vector' = None, radius: 'Float' = None)
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
to_curves(curve_group_id: 'Integer' = None, weight: 'Float' = None)
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
to_sdf_grid(radius: 'Float' = None, voxel_size: 'Float' = None)
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
to_volume(density: 'Float' = None, resolution_mode: "Literal['Amount', 'Size']" = None, voxel_size: 'Float' = None, voxel_amount: 'Float' = None, radius: 'Float' = None)
```

> Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)

#### Information:
- **Socket** : self



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **resolution_mode** (_Literal['Amount', 'Size']_ = None) : ('Amount', 'Size')
- **voxel_size** (_Float_ = None) : socket 'Voxel Size' (id: Voxel Size)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (id: Voxel Amount)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>