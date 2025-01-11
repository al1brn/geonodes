# Face

``` python
Face(geometry: geonodes.core.geometry_class.Geometry)
```

> Face domain of a [Mesh](mesh.md#mesh)

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](domain.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **A** : [accumulate_field](face.md#accumulate_field) :black_small_square: [active_element](face.md#active_element) :black_small_square: [attribute_statistic](face.md#attribute_statistic)
- **C** : [corner_index](face.md#corner_index) :black_small_square: [corners](face.md#corners) :black_small_square: [corners_total](face.md#corners_total) :black_small_square: [count](face.md#count)
- **D** : [delete](face.md#delete) :black_small_square: [delete_all](face.md#delete_all) :black_small_square: [delete_edge_face](face.md#delete_edge_face) :black_small_square: [delete_geometry](face.md#delete_geometry) :black_small_square: [delete_geometry_all](face.md#delete_geometry_all) :black_small_square: [delete_geometry_edge_face](face.md#delete_geometry_edge_face) :black_small_square: [delete_geometry_only_face](face.md#delete_geometry_only_face) :black_small_square: [delete_only_face](face.md#delete_only_face) :black_small_square: [distribute_points_poisson](face.md#distribute_points_poisson) :black_small_square: [distribute_points_random](face.md#distribute_points_random) :black_small_square: [duplicate](face.md#duplicate)
- **E** : [evaluate_at_index](face.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](face.md#evaluate_on_domain)
- **I** : [is_planar](face.md#is_planar)
- **M** : [material](face.md#material) :black_small_square: [material_index](face.md#material_index)
- **N** : [neighbors](face.md#neighbors)
- **S** : [sample_index](face.md#sample_index) :black_small_square: [sample_nearest](face.md#sample_nearest) :black_small_square: [scale](face.md#scale) :black_small_square: [scale_single_axis](face.md#scale_single_axis) :black_small_square: [scale_uniform](face.md#scale_uniform) :black_small_square: [separate](face.md#separate) :black_small_square: [set_selection](face.md#set_selection) :black_small_square: [set_shade_smooth](face.md#set_shade_smooth) :black_small_square: [shade_smooth](face.md#shade_smooth) :black_small_square: [smooth](face.md#smooth) :black_small_square: [sort](face.md#sort) :black_small_square: [split_to_instances](face.md#split_to_instances) :black_small_square: [store](face.md#store) :black_small_square: [store_named_attribute](face.md#store_named_attribute)
- **T** : [to_points](face.md#to_points)
- **V** : [viewer](face.md#viewer)

## Properties



### count

> _type_: **Integer**
>

> Socket 'Face Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

### material

> _type_: **?**
>

Write only property for node <Node Set Material>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

### material_index

> _type_: **?**
>

Property get node <Node Set Material Index>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

### shade_smooth

> _type_: **?**
>

Property get node <Node Set Shade Smooth>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

### smooth

> _type_: **?**
>

Property get node <Node Set Shade Smooth>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

## Methods



----------
### accumulate_field()

> classmethod

``` python
accumulate_field(value=None, group_id=None)
```

> Node [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACE'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### active_element()

> classmethod

``` python
active_element()
```

> Node [Active Element](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/active_element.html)

#### Information:
- **Parameter** : 'FACE'



#### Returns:
- **Integer** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### attribute_statistic()

> method

``` python
attribute_statistic(attribute=None)
```

> Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'attribute' type
- **Parameter** : 'FACE'



#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (id: Attribute)



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### corner_index()

> classmethod

``` python
corner_index(face_index=None, weights=None, sort_index=None)
```

> Node [Corners of Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_face.html)

#### Arguments:
- **face_index** (_Integer_ = None) : socket 'Face Index' (id: Face Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **corner_index** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### corners()

> classmethod

``` python
corners(face_index=None, weights=None, sort_index=None)
```

> Node [Corners of Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_face.html)

#### Arguments:
- **face_index** (_Integer_ = None) : socket 'Face Index' (id: Face Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### corners_total()

> classmethod

``` python
corners_total(face_index=None, weights=None, sort_index=None)
```

> Node [Corners of Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_face.html)

#### Arguments:
- **face_index** (_Integer_ = None) : socket 'Face Index' (id: Face Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **total** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### delete()

> method

``` python
delete(mode='ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Arguments:
- **mode** (_str_ = ALL) : parameter 'mode' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### delete_all()

> method

``` python
delete_all()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'
- **Parameter** : 'ALL'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### delete_edge_face()

> method

``` python
delete_edge_face()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'
- **Parameter** : 'EDGE_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### delete_geometry()

> method

``` python
delete_geometry(mode='ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Arguments:
- **mode** (_str_ = ALL) : parameter 'mode' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### delete_geometry_all()

> method

``` python
delete_geometry_all()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'
- **Parameter** : 'ALL'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### delete_geometry_edge_face()

> method

``` python
delete_geometry_edge_face()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'
- **Parameter** : 'EDGE_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### delete_geometry_only_face()

> method

``` python
delete_geometry_only_face()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'
- **Parameter** : 'ONLY_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### delete_only_face()

> method

``` python
delete_only_face()
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'
- **Parameter** : 'ONLY_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### distribute_points_poisson()

> method

``` python
distribute_points_poisson(distance_min=None, density_max=None, density_factor=None, seed=None, use_legacy_normal=False)
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
- **use_legacy_normal** (_bool_ = False) : parameter 'use_legacy_normal'



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### distribute_points_random()

> method

``` python
distribute_points_random(density=None, seed=None, use_legacy_normal=False)
```

> Node ERROR: Node 'Distribute Points on Faces' not found

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'RANDOM'



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)
- **use_legacy_normal** (_bool_ = False) : parameter 'use_legacy_normal'



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### duplicate()

> method

``` python
duplicate(amount=None)
```

> Node [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/duplicate_elements.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Arguments:
- **amount** (_Integer_ = None) : socket 'Amount' (id: Amount)



#### Returns:
- **Geometry** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### evaluate_at_index()

> classmethod

``` python
evaluate_at_index(index=None, value=None)
```

> Node [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACE'



#### Arguments:
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### evaluate_on_domain()

> classmethod

``` python
evaluate_on_domain(value=None)
```

> Node [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACE'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### is_planar()

> classmethod

``` python
is_planar(threshold=None)
```

> Node [Is Face Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_is_planar.html)

#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### neighbors()

> classmethod

``` python
neighbors()
```

> Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_neighbors.html)

#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### sample_index()

> method

``` python
sample_index(value=None, index=None, clamp=False)
```

> Node [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACE'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **clamp** (_bool_ = False) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### sample_nearest()

> method

``` python
sample_nearest(sample_position=None)
```

> Node [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_nearest.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FACE'



#### Arguments:
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Sample Position)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale=None, center=None, scale_mode='UNIFORM')
```

> Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/scale_elements.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Arguments:
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **scale_mode** (_str_ = UNIFORM) : parameter 'scale_mode' in ('UNIFORM', 'SINGLE_AXIS')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### scale_single_axis()

> method

``` python
scale_single_axis(scale=None, center=None, axis=None)
```

> Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/scale_elements.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'
- **Parameter** : 'SINGLE_AXIS'



#### Arguments:
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **axis** (_Vector_ = None) : socket 'Axis' (id: Axis)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### scale_uniform()

> method

``` python
scale_uniform(scale=None, center=None)
```

> Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/scale_elements.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **center** (_Vector_ = None) : socket 'Center' (id: Center)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### separate()

> method

``` python
separate()
```

> Node [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Returns:
- **Geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### set_selection()

> method

``` python
set_selection()
```

> Node [Set Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_selection.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'
- **Parameter** : depending on 'selection' type



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### set_shade_smooth()

> method

``` python
set_shade_smooth(shade_smooth=None)
```

> Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_shade_smooth.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Arguments:
- **shade_smooth** (_Boolean_ = None) : socket 'Shade Smooth' (id: Shade Smooth)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### sort()

> method

``` python
sort(group_id=None, sort_weight=None)
```

> Node [Sort Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/sort_elements.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sort_weight** (_Float_ = None) : socket 'Sort Weight' (id: Sort Weight)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### split_to_instances()

> method

``` python
split_to_instances(group_id=None)
```

> Node [Split to Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/split_to_instances.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)



#### Returns:
- **Instances** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### store()

> method

``` python
store(name=None, value=None)
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACE'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### store_named_attribute()

> method

``` python
store_named_attribute(name=None, value=None)
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACE'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position=None, radius=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

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
- **Parameter** : 'FACE'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>