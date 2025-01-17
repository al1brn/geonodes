# SplinePoint

``` python
SplinePoint(geometry: geonodes.core.geometry_class.Geometry)
```

> Base class for geometry domains

A domain stores the default value to be set in node needing a **domain** parameter
such as 'Store Named Attibute.

All nodes requiring a domain parameter are implemented as domain method

``` python
cube = Mesh.Cube()
cube.faces.store_named_attribute() # doamin = 'FACE'
```

When a node as a ***Selection*** socket, the value can be set using the get item syntax:

``` python
    # Plug the value of 'my_selection` into Selection socket
    Mesh().points[my_selection].store_named_attribute("Name", value)
```

> [!IMPORTANT]
> Domains are never instantiated directly but created by geometries.

The domain specific to geometries are the followings:
    - Mesh:
        - points (class [Vertex](vertex.md#vertex))
        - faces (class [Face](face.md#face))
        - edges (class [Edge](edge.md#edge))
        - corners (clas [Corner](corner.md#corner))
    - Curve:
        - points (class [SplinePoint](splinepoint.md#splinepoint))
        - splines (class [Spline](spline.md#spline))
    - GreasePencil:
        - layers (class [Layer](layer.md#layer))
    - Instances
        - insts (class [Instance](instance.md#instance))
    - Cloud
        - points (class [CloudPoint](cloudpoint.md#cloudpoint))
    - Volume

All the domain classes are a subclass of [Domain](domain.md#domain).
[Vertex](vertex.md#vertex), [SplinePoint](splinepoint.md#splinepoint) and [SplinePoint](splinepoint.md#splinepoint) classes are subclasses of [Point](point.md#point).

> See: [Vertex](vertex.md#vertex), [Face](face.md#face), [Edge](edge.md#edge), [Corner](corner.md#corner), [SplinePoint](splinepoint.md#splinepoint), [Spline](spline.md#spline), [CloudPoint](cloudpoint.md#cloudpoint), [Instance](instance.md#instance)

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[accumulate_field](core-gener-point-point.md#accumulate_field) :black_small_square: [active_element](core-gener-point-point.md#active_element) :black_small_square: [attribute_statistic](core-gener-point-point.md#attribute_statistic) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [count](corner.md#count) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [delete](core-gener-point-point.md#delete) :black_small_square: [delete_all](core-gener-point-point.md#delete_all) :black_small_square: [delete_edge_face](core-gener-point-point.md#delete_edge_face) :black_small_square: [delete_geometry](core-gener-point-point.md#delete_geometry) :black_small_square: [delete_geometry_all](core-gener-point-point.md#delete_geometry_all) :black_small_square: [delete_geometry_edge_face](core-gener-point-point.md#delete_geometry_edge_face) :black_small_square: [delete_geometry_only_face](core-gener-point-point.md#delete_geometry_only_face) :black_small_square: [delete_only_face](core-gener-point-point.md#delete_only_face) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [duplicate](core-gener-point-point.md#duplicate) :black_small_square: [evaluate_at_index](core-gener-point-point.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](core-gener-point-point.md#evaluate_on_domain) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](domain.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instance_on](core-gener-point-point.md#instance_on) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [offset](core-gener-point-point.md#offset) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [position](core-gener-point-point.md#position) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [sample_index](core-gener-point-point.md#sample_index) :black_small_square: [sample_nearest](core-gener-point-point.md#sample_nearest) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [separate](core-gener-point-point.md#separate) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [set_radius](core-gener-point-point.md#set_radius) :black_small_square: [set_selection](core-gener-point-point.md#set_selection) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [sort](core-gener-point-point.md#sort) :black_small_square: [split_to_instances](core-gener-point-point.md#split_to_instances) :black_small_square: [store](core-gener-point-point.md#store) :black_small_square: [store_named_attribute](core-gener-point-point.md#store_named_attribute) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square: [viewer](core-gener-point-point.md#viewer) :black_small_square:

## Content

- [curve_index](splinepoint.md#curve_index)
- [curve_of_point](splinepoint.md#curve_of_point)
- [\_geo](splinepoint.md#_geo)
- [index_in_curve](splinepoint.md#index_in_curve)
- [offset_in_curve](splinepoint.md#offset_in_curve)
- [radius](splinepoint.md#radius)
- [to_points](splinepoint.md#to_points)
- [to_points_count](splinepoint.md#to_points_count)
- [to_points_evaluated](splinepoint.md#to_points_evaluated)
- [to_points_length](splinepoint.md#to_points_length)

## Properties



### \_geo

> _type_: **Geometry**
>

the geometry the domain belongs to

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Properties](splinepoint.md#properties)</sub>

### radius

> _type_: **?**
>

Property get node <Node Set Curve Radius>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Properties](splinepoint.md#properties)</sub>

## Methods



----------
### curve_index()

> classmethod

``` python
curve_index(point_index=None)
```

> Node [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/curve_of_point.html)

#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (id: Point Index)



#### Returns:
- **curve_index** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Methods](splinepoint.md#methods)</sub>

----------
### curve_of_point()

> classmethod

``` python
curve_of_point(point_index=None)
```

> Node [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/curve_of_point.html)

#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (id: Point Index)



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Methods](splinepoint.md#methods)</sub>

----------
### index_in_curve()

> classmethod

``` python
index_in_curve(point_index=None)
```

> Node [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/curve_of_point.html)

#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (id: Point Index)



#### Returns:
- **index_in_curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Methods](splinepoint.md#methods)</sub>

----------
### offset_in_curve()

> classmethod

``` python
offset_in_curve(point_index=None, offset=None)
```

> Node [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/offset_point_in_curve.html)

#### Arguments:
- **point_index** (_Integer_ = None) : socket 'Point Index' (id: Point Index)
- **offset** (_Integer_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Boolean** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Methods](splinepoint.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(count=None, mode='COUNT')
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Information:
- **Socket** : self



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)
- **mode** (_str_ = COUNT) : parameter 'mode' in ['EVALUATED', 'COUNT', 'LENGTH']



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Methods](splinepoint.md#methods)</sub>

----------
### to_points_count()

> method

``` python
to_points_count(count=None)
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'COUNT'



#### Arguments:
- **count** (_Integer_ = None) : socket 'Count' (id: Count)



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Methods](splinepoint.md#methods)</sub>

----------
### to_points_evaluated()

> method

``` python
to_points_evaluated()
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EVALUATED'



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Methods](splinepoint.md#methods)</sub>

----------
### to_points_length()

> method

``` python
to_points_length(length=None)
```

> Node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LENGTH'



#### Arguments:
- **length** (_Float_ = None) : socket 'Length' (id: Length)



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [SplinePoint](splinepoint.md#splinepoint) :black_small_square: [Content](splinepoint.md#content) :black_small_square: [Methods](splinepoint.md#methods)</sub>