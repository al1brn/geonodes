# Point

``` python
Point(geometry: geonodes.core.geometry_class.Geometry)
```

> Base class for geometry domains

A domain stores the default value to be set in node needing a **domain** parameter
such as 'Store Named Attibute.

All nodes requiring a domain parameter are implemented as domain method

``` python
cube = Mesh.Cube()
cube.faces.store_named_attribute() # doamin = 'FACE'
```

> [!IMPORTANT]
> Domains are never instantiated directly but created by geometries.

> See: [Vertex](vertex.md#vertex), [Face](face.md#face), [Edge](edge.md#edge), [Corner](corner.md#corner), [SplinePoint](splinepoint.md#splinepoint), [Spline](spline.md#spline), [CloudPoint](cloudpoint.md#cloudpoint), [Instance](instance.md#instance)

Properties:
- _geo (Geometry) : the geometry the domain belongs to

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](domain.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **A** : [accumulate_field](point.md#accumulate_field) :black_small_square: [active_element](point.md#active_element) :black_small_square: [attribute_statistic](point.md#attribute_statistic)
- **C** : [count](point.md#count)
- **D** : [delete](point.md#delete) :black_small_square: [delete_all](point.md#delete_all) :black_small_square: [delete_edge_face](point.md#delete_edge_face) :black_small_square: [delete_geometry](point.md#delete_geometry) :black_small_square: [delete_geometry_all](point.md#delete_geometry_all) :black_small_square: [delete_geometry_edge_face](point.md#delete_geometry_edge_face) :black_small_square: [delete_geometry_only_face](point.md#delete_geometry_only_face) :black_small_square: [delete_only_face](point.md#delete_only_face) :black_small_square: [duplicate](point.md#duplicate)
- **E** : [evaluate_at_index](point.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](point.md#evaluate_on_domain)
- **I** : [instance_on](point.md#instance_on)
- **O** : [offset](point.md#offset)
- **P** : [position](point.md#position)
- **S** : [sample_index](point.md#sample_index) :black_small_square: [sample_nearest](point.md#sample_nearest) :black_small_square: [separate](point.md#separate) :black_small_square: [set_radius](point.md#set_radius) :black_small_square: [set_selection](point.md#set_selection) :black_small_square: [sort](point.md#sort) :black_small_square: [split_to_instances](point.md#split_to_instances) :black_small_square: [store](point.md#store) :black_small_square: [store_named_attribute](point.md#store_named_attribute)
- **V** : [viewer](point.md#viewer)

## Properties



### count

> _type_: **Integer**
>

> Socket 'Point Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Properties](point.md#properties)</sub>

### offset

> _type_: **?**
>

Write only property for node <Node Set Position>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Properties](point.md#properties)</sub>

### position

> _type_: **?**
>

Property get node <Node Set Position>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Properties](point.md#properties)</sub>

## Methods



----------
### accumulate_field()

> classmethod

``` python
accumulate_field(value=None, group_id=None)
```

> Class Method [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'POINT'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### active_element()

> classmethod

``` python
active_element()
```

> Class Method [Active Element](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/active_element.html)

#### Information:
- **Parameter** : 'POINT'



#### Returns:
- **Integer** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### attribute_statistic()

> method

``` python
attribute_statistic(attribute=None)
```

> Method [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'attribute' type
- **Parameter** : 'POINT'



#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (id: Attribute)



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### delete()

> method

``` python
delete(mode='ALL')
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'



#### Arguments:
- **mode** (_str_ = ALL) : parameter 'mode' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### delete_all()

> method

``` python
delete_all()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'
- **Parameter** : 'ALL'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### delete_edge_face()

> method

``` python
delete_edge_face()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'
- **Parameter** : 'EDGE_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### delete_geometry()

> method

``` python
delete_geometry(mode='ALL')
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'



#### Arguments:
- **mode** (_str_ = ALL) : parameter 'mode' in ('ALL', 'EDGE_FACE', 'ONLY_FACE')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### delete_geometry_all()

> method

``` python
delete_geometry_all()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'
- **Parameter** : 'ALL'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### delete_geometry_edge_face()

> method

``` python
delete_geometry_edge_face()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'
- **Parameter** : 'EDGE_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### delete_geometry_only_face()

> method

``` python
delete_geometry_only_face()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'
- **Parameter** : 'ONLY_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### delete_only_face()

> method

``` python
delete_only_face()
```

> Jump Method [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'
- **Parameter** : 'ONLY_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### duplicate()

> method

``` python
duplicate(amount=None)
```

> Jump Method [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/duplicate_elements.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'



#### Arguments:
- **amount** (_Integer_ = None) : socket 'Amount' (id: Amount)



#### Returns:
- **Geometry** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### evaluate_at_index()

> classmethod

``` python
evaluate_at_index(index=None, value=None)
```

> Class Method [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'POINT'



#### Arguments:
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### evaluate_on_domain()

> classmethod

``` python
evaluate_on_domain(value=None)
```

> Class Method [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'POINT'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### instance_on()

> method

``` python
instance_on(instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

> Method [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### sample_index()

> method

``` python
sample_index(value=None, index=None, clamp=False)
```

> Method [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'POINT'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **clamp** (_bool_ = False) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### sample_nearest()

> method

``` python
sample_nearest(sample_position=None)
```

> Method [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_nearest.html)

#### Information:
- **Socket** : self
- **Parameter** : 'POINT'



#### Arguments:
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Sample Position)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### separate()

> method

``` python
separate()
```

> Jump Method [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'



#### Returns:
- **Geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### set_radius()

> method

``` python
set_radius(radius=None)
```

> Jump Method [Set Point Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### set_selection()

> method

``` python
set_selection()
```

> Jump Method [Set Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_selection.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'
- **Parameter** : depending on 'selection' type



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### sort()

> method

``` python
sort(group_id=None, sort_weight=None)
```

> Jump Method [Sort Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/sort_elements.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sort_weight** (_Float_ = None) : socket 'Sort Weight' (id: Sort Weight)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### split_to_instances()

> method

``` python
split_to_instances(group_id=None)
```

> Method [Split to Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/split_to_instances.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'POINT'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)



#### Returns:
- **Instances** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### store()

> method

``` python
store(name=None, value=None)
```

> Jump Method [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'value' type
- **Parameter** : 'POINT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### store_named_attribute()

> method

``` python
store_named_attribute(name=None, value=None)
```

> Jump Method [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'value' type
- **Parameter** : 'POINT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>

----------
### viewer()

> method

``` python
viewer(value=None)
```

> Method [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'POINT'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Point](point.md#point) :black_small_square: [Content](point.md#content) :black_small_square: [Methods](point.md#methods)</sub>