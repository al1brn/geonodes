# Instances

``` python
Instances(value=None, name=None, tip=None, panel=None, hide_value=False, hide_in_modifier=False)
```

> Instances Geometry

> [!NOTE]
> The name of geometry class is plural : **Instances** when the name of the
> domain is singular : [Instance](instance.md#instance). The named of the domain property is [insts](instances.md#insts).

The **Instances** class exposes all methods specific to instances.
Since there is no ambiguity, the word **instances** is omitted in the name of
the methods:

``` python
realized = instances.realize() # Node 'Realize Instances'
```
Nodes requiring a domain parameter, are implemented in the domain [insts](instances.md#insts).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

### Inherited

[\_\_add__](boolean.md#__add__) :black_small_square: [bake](nd.md#bake) :black_small_square: [bounding_box](core-gener-geome-geometry.md#bounding_box) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [convex_hull](core-gener-geome-geometry.md#convex_hull) :black_small_square: [curve](core-gener-geome-geometry.md#curve) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geo](cloudpoint.md#_geo) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [grease_pencil](core-gener-geome-geometry.md#grease_pencil) :black_small_square: [id](core-gener-geome-geometry.md#id) :black_small_square: [index_of_nearest](core-gener-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](boolean.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instance_on_points](core-gener-geome-geometry.md#instance_on_points) :black_small_square: [instances](core-gener-geome-geometry.md#instances) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [Join](core-gener-geome-geometry.md#join) :black_small_square: [join](core-gener-geome-geometry.md#join) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [material](core-gener-geome-geometry.md#material) :black_small_square: [material_index](core-gener-geome-geometry.md#material_index) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [merge](core-gener-geome-geometry.md#merge) :black_small_square: [merge_all](core-gener-geome-geometry.md#merge_all) :black_small_square: [merge_by_distance](core-gener-geome-geometry.md#merge_by_distance) :black_small_square: [merge_connected](core-gener-geome-geometry.md#merge_connected) :black_small_square: [mesh](core-gener-geome-geometry.md#mesh) :black_small_square: [\_name](socket.md#_name) :black_small_square: [name](core-gener-geome-geometry.md#name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [offset](core-gener-geome-geometry.md#offset) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [point_cloud](core-gener-geome-geometry.md#point_cloud) :black_small_square: [position](core-gener-geome-geometry.md#position) :black_small_square: [proximity](core-gener-geome-geometry.md#proximity) :black_small_square: [proximity_edges](core-gener-geome-geometry.md#proximity_edges) :black_small_square: [proximity_faces](core-gener-geome-geometry.md#proximity_faces) :black_small_square: [proximity_points](core-gener-geome-geometry.md#proximity_points) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [raycast](core-gener-geome-geometry.md#raycast) :black_small_square: [raycast_interpolated](core-gener-geome-geometry.md#raycast_interpolated) :black_small_square: [raycast_nearest](core-gener-geome-geometry.md#raycast_nearest) :black_small_square: [realize](core-gener-geome-geometry.md#realize) :black_small_square: [remove_named_attribute](core-gener-geome-geometry.md#remove_named_attribute) :black_small_square: [remove_names](core-gener-geome-geometry.md#remove_names) :black_small_square: [replace_material](core-gener-geome-geometry.md#replace_material) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](geobase.md#_sel) :black_small_square: [separate_components](core-gener-geome-geometry.md#separate_components) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [set_id](core-gener-geome-geometry.md#set_id) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [set_material](core-gener-geome-geometry.md#set_material) :black_small_square: [set_material_index](core-gener-geome-geometry.md#set_material_index) :black_small_square: [set_name](core-gener-geome-geometry.md#set_name) :black_small_square: [set_position](core-gener-geome-geometry.md#set_position) :black_small_square: [set_spline_cyclic](core-gener-geome-geometry.md#set_spline_cyclic) :black_small_square: [set_spline_resolution](core-gener-geome-geometry.md#set_spline_resolution) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [to_instance](core-gener-geome-geometry.md#to_instance) :black_small_square: [transform](core-gener-geome-geometry.md#transform) :black_small_square: [transform_components](core-gener-geome-geometry.md#transform_components) :black_small_square: [transform_matrix](core-gener-geome-geometry.md#transform_matrix) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square: [viewer](core-gener-geome-geometry.md#viewer) :black_small_square: [volume](core-gener-geome-geometry.md#volume) :black_small_square:

## Content

- [domain_size](instances.md#domain_size)
- [FromGeometry](instances.md#fromgeometry)
- [ImportOBJ](instances.md#importobj)
- [insts](instances.md#insts)
- [rotate](instances.md#rotate)
- [scale](instances.md#scale)
- [set_transform](instances.md#set_transform)
- [to_points](instances.md#to_points)
- [translate](instances.md#translate)

## Properties



### insts

> _type_: **Instance**
>

INSTANCES domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Properties](instances.md#properties)</sub>

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
- **Parameter** : 'INSTANCES'



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### FromGeometry()

> classmethod

``` python
FromGeometry(*geometry)
```

> Node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)

#### Arguments:
- **geometry** (_Geometry_) : socket 'Geometry' (id: Geometry)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### ImportOBJ()

> classmethod

``` python
ImportOBJ(path=None)
```

> Node ERROR: Node 'Import OBJ' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(rotation=None, pivot_point=None, local_space=None)
```

> Node [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **pivot_point** (_Vector_ = None) : socket 'Pivot Point' (id: Pivot Point)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (id: Local Space)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale=None, center=None, local_space=None)
```

> Node [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (id: Local Space)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### set_transform()

> method

``` python
set_transform(transform=None)
```

> Node [Set Instance Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/set_instance_transform.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position=None, radius=None)
```

> Node [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>

----------
### translate()

> method

``` python
translate(translation=None, local_space=None)
```

> Node [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (id: Translation)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (id: Local Space)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instances](instances.md#instances) :black_small_square: [Content](instances.md#content) :black_small_square: [Methods](instances.md#methods)</sub>