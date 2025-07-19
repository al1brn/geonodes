# Corner

``` python
Corner(geometry: geonodes.core.geometry_class.Geometry)
```

> Corner domain of a [Mesh](mesh.md#mesh)

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](domain.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **A** : [accumulate_field](corner.md#accumulate_field) :black_small_square: [attribute_statistic](corner.md#attribute_statistic)
- **C** : [count](corner.md#count)
- **E** : [edges](corner.md#edges) :black_small_square: [evaluate_at_index](corner.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](corner.md#evaluate_on_domain)
- **F** : [face](corner.md#face) :black_small_square: [face_index](corner.md#face_index) :black_small_square: [field_average](corner.md#field_average) :black_small_square: [field_min_max](corner.md#field_min_max) :black_small_square: [field_variance](corner.md#field_variance)
- **I** : [index_in_face](corner.md#index_in_face)
- **N** : [next_edge_index](corner.md#next_edge_index) :black_small_square: [normal](corner.md#normal)
- **O** : [offset_in_face](corner.md#offset_in_face)
- **P** : [pack_uv_islands](corner.md#pack_uv_islands) :black_small_square: [previous_edge_index](corner.md#previous_edge_index)
- **S** : [sample_index](corner.md#sample_index) :black_small_square: [sample_nearest](corner.md#sample_nearest) :black_small_square: [store](corner.md#store) :black_small_square: [store_named_attribute](corner.md#store_named_attribute) :black_small_square: [store_uv](corner.md#store_uv)
- **T** : [to_points](corner.md#to_points)
- **U** : [uv_unwrap](corner.md#uv_unwrap)
- **V** : [vertex_index](corner.md#vertex_index) :black_small_square: [viewer](corner.md#viewer)

## Properties



### count

> _type_: **Integer**
>

> Socket 'Corner Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Properties](corner.md#properties)</sub>

### normal

> _type_: **?**
>

Write only property for node <Node Set Mesh Normal>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Properties](corner.md#properties)</sub>

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
- **Parameter** : 'CORNER'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

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
- **Parameter** : 'CORNER'



#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (id: Attribute)



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### edges()

> classmethod

``` python
edges(corner_index=None)
```

> Node [Edges of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### evaluate_at_index()

> classmethod

``` python
evaluate_at_index(value=None, index=None)
```

> Node [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'CORNER'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### evaluate_on_domain()

> classmethod

``` python
evaluate_on_domain(value=None)
```

> Node [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'CORNER'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### face()

> classmethod

``` python
face(corner_index=None)
```

> Node [Face of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/face_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **node** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### face_index()

> classmethod

``` python
face_index(corner_index=None)
```

> Node [Face of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/face_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **face_index** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### field_average()

> classmethod

``` python
field_average(value=None, group_id=None, domain='POINT')
```

> Node [Field Average](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/field_average.html)

#### Information:
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)
- **domain** (_str_ = POINT) : parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### field_min_max()

> classmethod

``` python
field_min_max(value=None, group_id=None, domain='POINT')
```

> Node ERROR: Node 'Field Min & Max' not found

#### Information:
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)
- **domain** (_str_ = POINT) : parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### field_variance()

> classmethod

``` python
field_variance(value=None, group_id=None, domain='POINT')
```

> Node [Field Variance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/field_variance.html)

#### Information:
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)
- **domain** (_str_ = POINT) : parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### index_in_face()

> classmethod

``` python
index_in_face(corner_index=None)
```

> Node [Face of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/face_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **index_in_face** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### next_edge_index()

> classmethod

``` python
next_edge_index(corner_index=None)
```

> Node [Edges of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **next_edge_index** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### offset_in_face()

> classmethod

``` python
offset_in_face(corner_index=None, offset=None)
```

> Node [Offset Corner in Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/offset_corner_in_face.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)
- **offset** (_Integer_ = None) : socket 'Offset' (id: Offset)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### pack_uv_islands()

> classmethod

``` python
pack_uv_islands(uv=None, margin=None, rotate=None)
```

> Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/pack_uv_islands.html)

#### Information:
- **Socket** : self[selection]



#### Arguments:
- **uv** (_Vector_ = None) : socket 'UV' (id: UV)
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **rotate** (_Boolean_ = None) : socket 'Rotate' (id: Rotate)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### previous_edge_index()

> classmethod

``` python
previous_edge_index(corner_index=None)
```

> Node [Edges of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **previous_edge_index** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

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
- **Parameter** : 'CORNER'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **clamp** (_bool_ = False) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### sample_nearest()

> method

``` python
sample_nearest(sample_position=None)
```

> Node [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_nearest.html)

#### Information:
- **Socket** : self
- **Parameter** : 'CORNER'



#### Arguments:
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Sample Position)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

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
- **Parameter** : 'CORNER'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

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
- **Parameter** : 'CORNER'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### store_uv()

> method

``` python
store_uv(name=None, value=None)
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FLOAT2'
- **Parameter** : 'CORNER'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Vector_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

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
- **Parameter** : 'CORNERS'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### uv_unwrap()

> classmethod

``` python
uv_unwrap(seam=None, margin=None, fill_holes=None, method='ANGLE_BASED')
```

> Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_unwrap.html)

#### Information:
- **Socket** : self[selection]



#### Arguments:
- **seam** (_Boolean_ = None) : socket 'Seam' (id: Seam)
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **fill_holes** (_Boolean_ = None) : socket 'Fill Holes' (id: Fill Holes)
- **method** (_str_ = ANGLE_BASED) : parameter 'method' in ['ANGLE_BASED', 'CONFORMAL']



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### vertex_index()

> classmethod

``` python
vertex_index(corner_index=None)
```

> Node [Vertex of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/vertex_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### viewer()

> method

``` python
viewer(value=None, ui_shortcut=0)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'CORNER'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **ui_shortcut** (_int_ = 0) : parameter 'ui_shortcut'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>