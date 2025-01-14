# Geometry

``` python
Geometry(value=None, name=None, tip=None, panel=None, hide_value=False, hide_in_modifier=False)
```

Socket of type 'GEOMETRY'.

If value is None, a Group Input socket of type Geometry is created.
When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

``` python
geometry = Geometry() # Default group input geometry
geometry = Geometry(name="Mesh") # Input group geometry
```

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](geobase.md#_sel) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **B** : [bake](geometry.md#bake) :black_small_square: [bounding_box](geometry.md#bounding_box)
- **C** : [convex_hull](geometry.md#convex_hull) :black_small_square: [curve](geometry.md#curve)
- **G** : [grease_pencil](geometry.md#grease_pencil)
- **I** : [id](geometry.md#id) :black_small_square: [index_of_nearest](geometry.md#index_of_nearest) :black_small_square: [\_\_init__](geometry.md#__init__) :black_small_square: [instance_on_points](geometry.md#instance_on_points) :black_small_square: [instances](geometry.md#instances)
- **J** : [Join](geometry.md#join) :black_small_square: [join](geometry.md#join)
- **M** : [material](geometry.md#material) :black_small_square: [material_index](geometry.md#material_index) :black_small_square: [merge](geometry.md#merge) :black_small_square: [merge_all](geometry.md#merge_all) :black_small_square: [merge_by_distance](geometry.md#merge_by_distance) :black_small_square: [merge_connected](geometry.md#merge_connected) :black_small_square: [mesh](geometry.md#mesh)
- **N** : [name](geometry.md#name)
- **O** : [offset](geometry.md#offset)
- **P** : [point_cloud](geometry.md#point_cloud) :black_small_square: [position](geometry.md#position) :black_small_square: [proximity](geometry.md#proximity) :black_small_square: [proximity_edges](geometry.md#proximity_edges) :black_small_square: [proximity_faces](geometry.md#proximity_faces) :black_small_square: [proximity_points](geometry.md#proximity_points)
- **R** : [raycast](geometry.md#raycast) :black_small_square: [raycast_interpolated](geometry.md#raycast_interpolated) :black_small_square: [raycast_nearest](geometry.md#raycast_nearest) :black_small_square: [realize](geometry.md#realize) :black_small_square: [remove_named_attribute](geometry.md#remove_named_attribute) :black_small_square: [remove_names](geometry.md#remove_names) :black_small_square: [replace_material](geometry.md#replace_material)
- **S** : [separate_components](geometry.md#separate_components) :black_small_square: [set_id](geometry.md#set_id) :black_small_square: [set_material](geometry.md#set_material) :black_small_square: [set_material_index](geometry.md#set_material_index) :black_small_square: [set_name](geometry.md#set_name) :black_small_square: [set_position](geometry.md#set_position) :black_small_square: [set_spline_cyclic](geometry.md#set_spline_cyclic) :black_small_square: [set_spline_resolution](geometry.md#set_spline_resolution)
- **T** : [to_instance](geometry.md#to_instance) :black_small_square: [transform](geometry.md#transform) :black_small_square: [transform_components](geometry.md#transform_components) :black_small_square: [transform_matrix](geometry.md#transform_matrix)
- **V** : [viewer](geometry.md#viewer) :black_small_square: [volume](geometry.md#volume)

## Properties



### curve

> _type_: **curve**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### grease_pencil

> _type_: **grease_pencil**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### id

> _type_: **?**
>

Property get node <Node Set ID>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### instances

> _type_: **instances**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### material

> _type_: **?**
>

Write only property for node <Node Set Material>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### material_index

> _type_: **?**
>

Property get node <Node Set Material Index>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### mesh

> _type_: **mesh**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### name

> _type_: **?**
>

Write only property for node <Node Set Geometry Name>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### offset

> _type_: **?**
>

Write only property for node <Node Set Position>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### point_cloud

> _type_: **point_cloud**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### position

> _type_: **?**
>

Property get node <Node Set Position>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

### volume

> _type_: **volume**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Properties](geometry.md#properties)</sub>

## Methods



----------
### bake()

> method

``` python
bake(**kwargs)
```

Node [Bake](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/bake.html)



#### Arguments:
- **kwargs**



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### bounding_box()

> method

``` python
bounding_box()
```

> Node [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/bounding_box.html)

#### Information:
- **Socket** : self



#### Returns:
- **Mesh** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### convex_hull()

> method

``` python
convex_hull()
```

> Node [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/convex_hull.html)

#### Information:
- **Socket** : self



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### index_of_nearest()

> classmethod

``` python
index_of_nearest(position=None, group_id=None)
```

> Node ERROR: Node 'Index of Nearest' not found

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)



#### Returns:
- **Integer** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=None, name=None, tip=None, panel=None, hide_value=False, hide_in_modifier=False)
```

Socket of type 'GEOMETRY'.

If value is None, a Group Input socket of type Geometry is created.
When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

``` python
geometry = Geometry() # Default group input geometry
geometry = Geometry(name="Mesh") # Input group geometry
```

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### instance_on_points()

> method

``` python
instance_on_points(instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### Join()

> classmethod

``` python
Join(*geometry)
```

> Node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)

#### Arguments:
- **geometry** (_Geometry_) : socket 'Geometry' (id: Geometry)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### join()

> method

``` python
join(*geometry)
```

> Node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Arguments:
- **geometry** (_Geometry_) : socket 'Geometry' (id: Geometry)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### merge()

> method

``` python
merge(distance=None, mode='ALL')
```

> Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (id: Distance)
- **mode** (_str_ = ALL) : parameter 'mode' in ('ALL', 'CONNECTED')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### merge_all()

> method

``` python
merge_all(distance=None)
```

> Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'ALL'



#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (id: Distance)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### merge_by_distance()

> method

``` python
merge_by_distance(distance=None, mode='ALL')
```

> Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (id: Distance)
- **mode** (_str_ = ALL) : parameter 'mode' in ('ALL', 'CONNECTED')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### merge_connected()

> method

``` python
merge_connected(distance=None)
```

> Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'CONNECTED'



#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (id: Distance)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### proximity()

> method

``` python
proximity(group_id=None, sample_position=None, sample_group_id=None, target_element='FACES')
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Information:
- **Socket** : self



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (id: Sample Group ID)
- **target_element** (_str_ = FACES) : parameter 'target_element' in ('POINTS', 'EDGES', 'FACES')



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### proximity_edges()

> method

``` python
proximity_edges(group_id=None, sample_position=None, sample_group_id=None)
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EDGES'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (id: Sample Group ID)



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### proximity_faces()

> method

``` python
proximity_faces(group_id=None, sample_position=None, sample_group_id=None)
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FACES'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (id: Sample Group ID)



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### proximity_points()

> method

``` python
proximity_points(group_id=None, sample_position=None, sample_group_id=None)
```

> Node [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html)

#### Information:
- **Socket** : self
- **Parameter** : 'POINTS'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Source Position)
- **sample_group_id** (_Integer_ = None) : socket 'Sample Group ID' (id: Sample Group ID)



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### raycast()

> method

``` python
raycast(attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED')
```

> Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'attribute' type



#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (id: Attribute)
- **source_position** (_Vector_ = None) : socket 'Source Position' (id: Source Position)
- **ray_direction** (_Vector_ = None) : socket 'Ray Direction' (id: Ray Direction)
- **ray_length** (_Float_ = None) : socket 'Ray Length' (id: Ray Length)
- **mapping** (_str_ = INTERPOLATED) : parameter 'mapping' in ('INTERPOLATED', 'NEAREST')



#### Returns:
- **node** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### raycast_interpolated()

> method

``` python
raycast_interpolated(attribute=None, source_position=None, ray_direction=None, ray_length=None)
```

> Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'attribute' type
- **Parameter** : 'INTERPOLATED'



#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (id: Attribute)
- **source_position** (_Vector_ = None) : socket 'Source Position' (id: Source Position)
- **ray_direction** (_Vector_ = None) : socket 'Ray Direction' (id: Ray Direction)
- **ray_length** (_Float_ = None) : socket 'Ray Length' (id: Ray Length)



#### Returns:
- **node** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### raycast_nearest()

> method

``` python
raycast_nearest(attribute=None, source_position=None, ray_direction=None, ray_length=None)
```

> Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'attribute' type
- **Parameter** : 'NEAREST'



#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (id: Attribute)
- **source_position** (_Vector_ = None) : socket 'Source Position' (id: Source Position)
- **ray_direction** (_Vector_ = None) : socket 'Ray Direction' (id: Ray Direction)
- **ray_length** (_Float_ = None) : socket 'Ray Length' (id: Ray Length)



#### Returns:
- **node** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### realize()

> method

``` python
realize(realize_all=None, depth=None)
```

> Node [Realize Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **realize_all** (_Boolean_ = None) : socket 'Realize All' (id: Realize All)
- **depth** (_Integer_ = None) : socket 'Depth' (id: Depth)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### remove_named_attribute()

> method

``` python
remove_named_attribute(name=None, pattern_mode='EXACT')
```

> Node [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **pattern_mode** (_str_ = EXACT) : parameter 'pattern_mode' in ('EXACT', 'WILDCARD')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### remove_names()

> method

``` python
remove_names(name=None)
```

> Node [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'WILDCARD'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### replace_material()

> method

``` python
replace_material(old=None, new=None)
```

> Node [Replace Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **old** (_Material_ = None) : socket 'Old' (id: Old)
- **new** (_Material_ = None) : socket 'New' (id: New)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### separate_components()

> method

``` python
separate_components()
```

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

#### Information:
- **Socket** : self



#### Returns:
- **node** (_Mesh_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_id()

> method

``` python
set_id(id=None)
```

> Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **id** (_Integer_ = None) : socket 'ID' (id: ID)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_material()

> method

``` python
set_material(material=None)
```

> Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **material** (_Material_ = None) : socket 'Material' (id: Material)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_material_index()

> method

``` python
set_material_index(material_index=None)
```

> Node [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **material_index** (_Integer_ = None) : socket 'Material Index' (id: Material Index)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_name()

> method

``` python
set_name(name=None)
```

> Node [Set Geometry Name](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_geometry_name.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_position()

> method

``` python
set_position(position=None, offset=None)
```

> Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_spline_cyclic()

> method

``` python
set_spline_cyclic(cyclic=None)
```

> Node [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_cyclic.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **cyclic** (_Boolean_ = None) : socket 'Cyclic' (id: Cyclic)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### set_spline_resolution()

> method

``` python
set_spline_resolution(resolution=None)
```

> Node [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_resolution.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **resolution** (_Integer_ = None) : socket 'Resolution' (id: Resolution)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### to_instance()

> method

``` python
to_instance(*geometry)
```

> Node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)

#### Arguments:
- **geometry** (_Geometry_) : socket 'Geometry' (id: Geometry)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### transform()

> method

``` python
transform(translation=None, rotation=None, scale=None, transform=None, mode='COMPONENTS')
```

> Node [Transform Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/transform_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (id: Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)
- **mode** (_str_ = COMPONENTS) : parameter 'mode' in ('COMPONENTS', 'MATRIX')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### transform_components()

> method

``` python
transform_components(translation=None, rotation=None, scale=None, transform=None)
```

> Node [Transform Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/transform_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'COMPONENTS'



#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (id: Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### transform_matrix()

> method

``` python
transform_matrix(translation=None, rotation=None, scale=None, transform=None)
```

> Node [Transform Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/transform_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : 'MATRIX'



#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (id: Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>

----------
### viewer()

> method

``` python
viewer(value=None)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'AUTO'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geometry.md#geometry) :black_small_square: [Content](geometry.md#content) :black_small_square: [Methods](geometry.md#methods)</sub>