# Vertex

``` python
Vertex(geometry: geonodes.core.geometry_class.Geometry)
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

[accumulate_field](core-gener-point-point.md#accumulate_field) :black_small_square: [active_element](core-gener-point-point.md#active_element) :black_small_square: [attribute_statistic](core-gener-point-point.md#attribute_statistic) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [count](corner.md#count) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [delete](core-gener-point-point.md#delete) :black_small_square: [delete_all](core-gener-point-point.md#delete_all) :black_small_square: [delete_edge_face](core-gener-point-point.md#delete_edge_face) :black_small_square: [delete_geometry](core-gener-point-point.md#delete_geometry) :black_small_square: [delete_geometry_all](core-gener-point-point.md#delete_geometry_all) :black_small_square: [delete_geometry_edge_face](core-gener-point-point.md#delete_geometry_edge_face) :black_small_square: [delete_geometry_only_face](core-gener-point-point.md#delete_geometry_only_face) :black_small_square: [delete_only_face](core-gener-point-point.md#delete_only_face) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [duplicate](core-gener-point-point.md#duplicate) :black_small_square: [evaluate_at_index](core-gener-point-point.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](core-gener-point-point.md#evaluate_on_domain) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](domain.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instance_on](core-gener-point-point.md#instance_on) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [offset](core-gener-point-point.md#offset) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [position](core-gener-point-point.md#position) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [sample_index](core-gener-point-point.md#sample_index) :black_small_square: [sample_nearest](core-gener-point-point.md#sample_nearest) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [separate](core-gener-point-point.md#separate) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [set_radius](core-gener-point-point.md#set_radius) :black_small_square: [set_selection](core-gener-point-point.md#set_selection) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [sort](core-gener-point-point.md#sort) :black_small_square: [split_to_instances](core-gener-point-point.md#split_to_instances) :black_small_square: [store](core-gener-point-point.md#store) :black_small_square: [store_named_attribute](core-gener-point-point.md#store_named_attribute) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square: [viewer](core-gener-point-point.md#viewer) :black_small_square:

## Content

- [corner_index](vertex.md#corner_index)
- [corners](vertex.md#corners)
- [corners_total](vertex.md#corners_total)
- [edge_index](vertex.md#edge_index)
- [edges](vertex.md#edges)
- [edges_total](vertex.md#edges_total)
- [neighbors](vertex.md#neighbors)
- [to_points](vertex.md#to_points)

## Methods



----------
### corner_index()

> classmethod

``` python
corner_index(vertex_index=None, weights=None, sort_index=None)
```

> Class Method [Corners of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (id: Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **corner_index** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

----------
### corners()

> classmethod

``` python
corners(vertex_index=None, weights=None, sort_index=None)
```

> Class Method [Corners of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (id: Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

----------
### corners_total()

> classmethod

``` python
corners_total(vertex_index=None, weights=None, sort_index=None)
```

> Class Method [Corners of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (id: Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **total** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

----------
### edge_index()

> classmethod

``` python
edge_index(vertex_index=None, weights=None, sort_index=None)
```

> Class Method [Edges of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (id: Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **edge_index** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

----------
### edges()

> classmethod

``` python
edges(vertex_index=None, weights=None, sort_index=None)
```

> Class Method [Edges of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (id: Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

----------
### edges_total()

> classmethod

``` python
edges_total(vertex_index=None, weights=None, sort_index=None)
```

> Class Method [Edges of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (id: Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **total** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

----------
### neighbors()

> classmethod

``` python
neighbors()
```

> Class Method [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position=None, radius=None)
```

> Method [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

Information
-----------
- Socket 'Mesh' : self
- Socket 'Selection' : self[selection]
- Parameter 'mode' : 'VERTICES'

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>