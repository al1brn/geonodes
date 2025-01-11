# Spline

``` python
Spline(geometry: geonodes.core.geometry_class.Geometry)
```

> Curve, or Spline, domain of a [Curve](curve.md#curve)

Methods of **Spline** class are nodes which accept a SPLINE or CURVE domain.

In addition, the node [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/points_of_curve.html) is implemented as method [points](nd.md#points).

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](domain.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **A** : [accumulate_field](spline.md#accumulate_field) :black_small_square: [attribute_statistic](spline.md#attribute_statistic)
- **C** : [count](spline.md#count)
- **D** : [delete](spline.md#delete) :black_small_square: [delete_all](spline.md#delete_all) :black_small_square: [delete_edge_face](spline.md#delete_edge_face) :black_small_square: [delete_geometry](spline.md#delete_geometry) :black_small_square: [delete_geometry_all](spline.md#delete_geometry_all) :black_small_square: [delete_geometry_edge_face](spline.md#delete_geometry_edge_face) :black_small_square: [delete_geometry_only_face](spline.md#delete_geometry_only_face) :black_small_square: [delete_only_face](spline.md#delete_only_face) :black_small_square: [duplicate](spline.md#duplicate)
- **E** : [evaluate_at_index](spline.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](spline.md#evaluate_on_domain)
- **I** : [is_cyclic](spline.md#is_cyclic)
- **M** : [material_index](spline.md#material_index)
- **N** : [normal](spline.md#normal)
- **P** : [parameter](spline.md#parameter) :black_small_square: [point_index](spline.md#point_index) :black_small_square: [points_of_curve](spline.md#points_of_curve) :black_small_square: [points_total](spline.md#points_total)
- **R** : [resolution](spline.md#resolution)
- **S** : [sample_index](spline.md#sample_index) :black_small_square: [separate](spline.md#separate) :black_small_square: [set_selection](spline.md#set_selection) :black_small_square: [sort](spline.md#sort) :black_small_square: [spline_length](spline.md#spline_length) :black_small_square: [split_to_instances](spline.md#split_to_instances) :black_small_square: [store](spline.md#store) :black_small_square: [store_named_attribute](spline.md#store_named_attribute)
- **T** : [tilt](spline.md#tilt) :black_small_square: [type](spline.md#type)
- **V** : [viewer](spline.md#viewer)

## Properties



### count

> _type_: **Integer**
>

> Socket 'Spline Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### is_cyclic

> _type_: **?**
>

Property get node <Node Set Spline Cyclic>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### material_index

> _type_: **?**
>

Property get node <Node Set Material Index>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### normal

> _type_: **?**
>

Write only property for node <Node Set Curve Normal>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### resolution

> _type_: **?**
>

Property get node <Node Set Spline Resolution>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### tilt

> _type_: **?**
>

Property get node <Node Set Curve Tilt>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### type

> _type_: **?**
>

Write only property for node <Node Set Spline Type>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

## Methods



----------
### accumulate_field()

> classmethod

``` python
accumulate_field(value=None, group_id=None)
```

> Class Method [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html)

Information
-----------
- Parameter 'data_type' : depending on 'value' type
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### attribute_statistic()

> method

``` python
attribute_statistic(attribute=None)
```

> Method [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'data_type' : depending on 'attribute' type
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (id: Attribute)



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### delete()

> method

``` python
delete(mode='ALL')
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **mode** (_str_ = ALL) : parameter 'mode' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### delete_all()

> method

``` python
delete_all()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'
- Parameter 'mode' : 'ALL'

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### delete_edge_face()

> method

``` python
delete_edge_face()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'
- Parameter 'mode' : 'EDGE_FACE'

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### delete_geometry()

> method

``` python
delete_geometry(mode='ALL')
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **mode** (_str_ = ALL) : parameter 'mode' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### delete_geometry_all()

> method

``` python
delete_geometry_all()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'
- Parameter 'mode' : 'ALL'

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### delete_geometry_edge_face()

> method

``` python
delete_geometry_edge_face()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'
- Parameter 'mode' : 'EDGE_FACE'

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### delete_geometry_only_face()

> method

``` python
delete_geometry_only_face()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'
- Parameter 'mode' : 'ONLY_FACE'

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### delete_only_face()

> method

``` python
delete_only_face()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'
- Parameter 'mode' : 'ONLY_FACE'

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### duplicate()

> method

``` python
duplicate(amount=None)
```

> Jump Method [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/duplicate_elements.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'SPLINE'

#### Arguments:
- **amount** (_Integer_ = None) : socket 'Amount' (id: Amount)



#### Returns:
- **Geometry** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### evaluate_at_index()

> classmethod

``` python
evaluate_at_index(index=None, value=None)
```

> Class Method [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

Information
-----------
- Parameter 'data_type' : depending on 'value' type
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### evaluate_on_domain()

> classmethod

``` python
evaluate_on_domain(value=None)
```

> Class Method [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

Information
-----------
- Parameter 'data_type' : depending on 'value' type
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### parameter()

> classmethod

``` python
parameter()
```

> Class Method [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/spline_parameter.html)

#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### point_index()

> classmethod

``` python
point_index(curve_index=None, weights=None, sort_index=None)
```

> Class Method [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/points_of_curve.html)

#### Arguments:
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (id: Curve Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **point_index** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### points_of_curve()

> classmethod

``` python
points_of_curve(curve_index=None, weights=None, sort_index=None)
```

> Class Method [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/points_of_curve.html)

#### Arguments:
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (id: Curve Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### points_total()

> classmethod

``` python
points_total(curve_index=None, weights=None, sort_index=None)
```

> Class Method [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/points_of_curve.html)

#### Arguments:
- **curve_index** (_Integer_ = None) : socket 'Curve Index' (id: Curve Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **total** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### sample_index()

> method

``` python
sample_index(value=None, index=None, clamp=False)
```

> Method [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html)

Information
-----------
- Socket 'Geometry' : self
- Parameter 'data_type' : depending on 'value' type
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **clamp** (_bool_ = False) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### separate()

> method

``` python
separate()
```

> Jump Method [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'

#### Returns:
- **Geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### set_selection()

> method

``` python
set_selection()
```

> Jump Method [Set Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_selection.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'
- Parameter 'selection_type' : depending on 'selection' type

#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### sort()

> method

``` python
sort(group_id=None, sort_weight=None)
```

> Jump Method [Sort Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/sort_elements.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sort_weight** (_Float_ = None) : socket 'Sort Weight' (id: Sort Weight)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### spline_length()

> classmethod

``` python
spline_length()
```

> Class Method [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/spline_length.html)

#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### split_to_instances()

> method

``` python
split_to_instances(group_id=None)
```

> Method [Split to Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/split_to_instances.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)



#### Returns:
- **Instances** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### store()

> method

``` python
store(name=None, value=None)
```

> Jump Method [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'data_type' : depending on 'value' type
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### store_named_attribute()

> method

``` python
store_named_attribute(name=None, value=None)
```

> Jump Method [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

Information
-----------
- Socket 'Geometry' : self
- Socket 'Selection' : self[selection]
- Parameter 'data_type' : depending on 'value' type
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>

----------
### viewer()

> method

``` python
viewer(value=None)
```

> Method [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

Information
-----------
- Socket 'Geometry' : self
- Parameter 'data_type' : depending on 'value' type
- Parameter 'domain' : 'CURVE'

#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>