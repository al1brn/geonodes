# Edge

``` python
Edge(geometry: geonodes.core.geometry_class.Geometry)
```

> Edge domain of a [Mesh](mesh.md#mesh)

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [foreach](domain.md#foreach) :black_small_square: [for_each_element](domain.md#for_each_element) :black_small_square: [\_geo](domain.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](domain.md#get_selection) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_selection' not found]() :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square:

## Content

- **A** : [accumulate_field](edge.md#accumulate_field) :black_small_square: [active_element](edge.md#active_element) :black_small_square: [attribute_statistic](edge.md#attribute_statistic)
- **C** : [corner_index](edge.md#corner_index) :black_small_square: [corners](edge.md#corners) :black_small_square: [corners_total](edge.md#corners_total) :black_small_square: [count](edge.md#count)
- **D** : [delete](edge.md#delete) :black_small_square: [delete_all](edge.md#delete_all) :black_small_square: [delete_edge_face](edge.md#delete_edge_face) :black_small_square: [delete_geometry](edge.md#delete_geometry) :black_small_square: [delete_geometry_all](edge.md#delete_geometry_all) :black_small_square: [delete_geometry_edge_face](edge.md#delete_geometry_edge_face) :black_small_square: [delete_geometry_only_face](edge.md#delete_geometry_only_face) :black_small_square: [delete_only_face](edge.md#delete_only_face) :black_small_square: [duplicate](edge.md#duplicate)
- **E** : [evaluate_at_index](edge.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](edge.md#evaluate_on_domain) :black_small_square: [extrude](edge.md#extrude)
- **F** : [field_average](edge.md#field_average) :black_small_square: [field_min_max](edge.md#field_min_max) :black_small_square: [field_variance](edge.md#field_variance)
- **M** : [material](edge.md#material)
- **P** : [paths_to_curves](edge.md#paths_to_curves) :black_small_square: [paths_to_selection](edge.md#paths_to_selection)
- **S** : [sample_index](edge.md#sample_index) :black_small_square: [sample_nearest](edge.md#sample_nearest) :black_small_square: [scale](edge.md#scale) :black_small_square: [separate](edge.md#separate) :black_small_square: [set_selection](edge.md#set_selection) :black_small_square: [set_shade_smooth](edge.md#set_shade_smooth) :black_small_square: [shade_smooth](edge.md#shade_smooth) :black_small_square: [shortest_paths](edge.md#shortest_paths) :black_small_square: [smooth](edge.md#smooth) :black_small_square: [sort](edge.md#sort) :black_small_square: [split](edge.md#split) :black_small_square: [split_to_instances](edge.md#split_to_instances) :black_small_square: [store](edge.md#store) :black_small_square: [store_named_attribute](edge.md#store_named_attribute)
- **T** : [to_face_groups](edge.md#to_face_groups) :black_small_square: [to_points](edge.md#to_points)
- **V** : [viewer](edge.md#viewer)

## Properties



### count

> _type_: **Integer**
>

> Socket 'Edge Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### material

> _type_: **?**
>

Write only property for node <Node Set Material>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### shade_smooth

> _type_: **?**
>

Property get node <Node Set Shade Smooth>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### smooth

> _type_: **?**
>

Property get node <Node Set Shade Smooth>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### to_face_groups

> _type_: **Integer**
>

> Node [Edges to Face Groups](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edges_to_face_groups.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

## Methods



----------
### accumulate_field()

> classmethod

``` python
accumulate_field(value: 'Float | Integer | Vector | Matrix' = None, group_id: 'Integer' = None)
```

> Node [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'EDGE'



#### Arguments:
- **value** (_Float | Integer | Vector | Matrix_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### active_element()

> classmethod

``` python
active_element()
```

> Node [Active Element](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/active_element.html)

#### Information:
- **Parameter** : 'EDGE'



#### Returns:
- **Integer** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### attribute_statistic()

> method

``` python
attribute_statistic(attribute: 'Float | Vector' = None)
```

> Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'attribute' type
- **Parameter** : 'EDGE'



#### Arguments:
- **attribute** (_Float | Vector_ = None) : socket 'Attribute' (id: Attribute)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### corner_index()

> classmethod

``` python
corner_index(edge_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
```

> Node [Corners of Edge](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_edge.html)

#### Arguments:
- **edge_index** (_Integer_ = None) : socket 'Edge Index' (id: Edge Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **corner_index** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### corners()

> classmethod

``` python
corners(edge_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
```

> Node [Corners of Edge](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_edge.html)

#### Arguments:
- **edge_index** (_Integer_ = None) : socket 'Edge Index' (id: Edge Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### corners_total()

> classmethod

``` python
corners_total(edge_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
```

> Node [Corners of Edge](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_edge.html)

#### Arguments:
- **edge_index** (_Integer_ = None) : socket 'Edge Index' (id: Edge Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **total** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### delete()

> method

``` python
delete(mode: "Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']" = 'ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGE'



#### Arguments:
- **mode** (_Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']_ = ALL) : parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

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
- **Parameter** : 'EDGE'
- **Parameter** : 'ALL'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

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
- **Parameter** : 'EDGE'
- **Parameter** : 'EDGE_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### delete_geometry()

> method

``` python
delete_geometry(mode: "Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']" = 'ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGE'



#### Arguments:
- **mode** (_Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']_ = ALL) : parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

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
- **Parameter** : 'EDGE'
- **Parameter** : 'ALL'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

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
- **Parameter** : 'EDGE'
- **Parameter** : 'EDGE_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

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
- **Parameter** : 'EDGE'
- **Parameter** : 'ONLY_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

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
- **Parameter** : 'EDGE'
- **Parameter** : 'ONLY_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### duplicate()

> method

``` python
duplicate(amount: 'Integer' = None)
```

> Node [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/duplicate_elements.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGE'



#### Arguments:
- **amount** (_Integer_ = None) : socket 'Amount' (id: Amount)



#### Returns:
- **Geometry** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### evaluate_at_index()

> classmethod

``` python
evaluate_at_index(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, index: 'Integer' = None)
```

> Node [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'EDGE'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### evaluate_on_domain()

> classmethod

``` python
evaluate_on_domain(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None)
```

> Node [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'EDGE'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### extrude()

> method

``` python
extrude(offset: 'Vector' = None, offset_scale: 'Float' = None)
```

> Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGES'



#### Arguments:
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **offset_scale** (_Float_ = None) : socket 'Offset Scale' (id: Offset Scale)



#### Returns:
- **Mesh** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### field_average()

> classmethod

``` python
field_average(value: 'Float | Vector' = None, group_id: 'Integer' = None, domain: "Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']" = 'POINT')
```

> Node [Field Average](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/field_average.html)

#### Information:
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float | Vector_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)
- **domain** (_Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']_ = POINT) : parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### field_min_max()

> classmethod

``` python
field_min_max(value: 'Float | Integer | Vector' = None, group_id: 'Integer' = None, domain: "Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']" = 'POINT')
```

> Node ERROR: Node 'Field Min & Max' not found

#### Information:
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float | Integer | Vector_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)
- **domain** (_Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']_ = POINT) : parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### field_variance()

> classmethod

``` python
field_variance(value: 'Float | Vector' = None, group_id: 'Integer' = None, domain: "Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']" = 'POINT')
```

> Node [Field Variance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/field_variance.html)

#### Information:
- **Parameter** : depending on 'value' type



#### Arguments:
- **value** (_Float | Vector_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)
- **domain** (_Literal['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']_ = POINT) : parameter 'domain' in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE', 'LAYER']



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### paths_to_curves()

> method

``` python
paths_to_curves(start_vertices: 'Boolean' = None, next_vertex_index: 'Integer' = None)
```

> Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **start_vertices** (_Boolean_ = None) : socket 'Start Vertices' (id: Start Vertices)
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (id: Next Vertex Index)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### paths_to_selection()

> classmethod

``` python
paths_to_selection(start_vertices: 'Boolean' = None, next_vertex_index: 'Integer' = None)
```

> Node [Edge Paths to Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_selection.html)

#### Arguments:
- **start_vertices** (_Boolean_ = None) : socket 'Start Vertices' (id: Start Vertices)
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (id: Next Vertex Index)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### sample_index()

> method

``` python
sample_index(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, index: 'Integer' = None, clamp=False)
```

> Node [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'EDGE'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **clamp** (_bool_ = False) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### sample_nearest()

> method

``` python
sample_nearest(sample_position: 'Vector' = None)
```

> Node [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_nearest.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EDGE'



#### Arguments:
- **sample_position** (_Vector_ = None) : socket 'Sample Position' (id: Sample Position)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale: 'Float' = None, center: 'Vector' = None, scale_mode: "Literal['Uniform', 'Single Axis']" = None, axis: 'Vector' = None)
```

> Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/scale_elements.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGE'



#### Arguments:
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **scale_mode** (_Literal['Uniform', 'Single Axis']_ = None) : ('Uniform', 'Single Axis')
- **axis** (_Vector_ = None) : socket 'Axis' (id: Axis)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

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
- **Parameter** : 'EDGE'



#### Returns:
- **node** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

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
- **Parameter** : 'EDGE'
- **Parameter** : depending on 'selection' type



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### set_shade_smooth()

> method

``` python
set_shade_smooth(shade_smooth: 'Boolean' = None)
```

> Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_shade_smooth.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGE'



#### Arguments:
- **shade_smooth** (_Boolean_ = None) : socket 'Shade Smooth' (id: Shade Smooth)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### shortest_paths()

> classmethod

``` python
shortest_paths(end_vertex: 'Boolean' = None, edge_cost: 'Float' = None)
```

> Node [Shortest Edge Paths](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/shortest_edge_paths.html)

#### Arguments:
- **end_vertex** (_Boolean_ = None) : socket 'End Vertex' (id: End Vertex)
- **edge_cost** (_Float_ = None) : socket 'Edge Cost' (id: Edge Cost)



#### Returns:
- **Integer** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### sort()

> method

``` python
sort(group_id: 'Integer' = None, sort_weight: 'Float' = None)
```

> Node [Sort Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/sort_elements.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGE'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sort_weight** (_Float_ = None) : socket 'Sort Weight' (id: Sort Weight)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### split()

> method

``` python
split()
```

> Node [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/split_edges.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### split_to_instances()

> method

``` python
split_to_instances(group_id: 'Integer' = None)
```

> Node [Split to Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/split_to_instances.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGE'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)



#### Returns:
- **Instances** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### store()

> method

``` python
store(name: 'String' = None, value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color' = None)
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'value' type
- **Parameter** : 'EDGE'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### store_named_attribute()

> method

``` python
store_named_attribute(name: 'String' = None, value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color' = None)
```

> Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'value' type
- **Parameter** : 'EDGE'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### to_points()

> method

``` python
to_points(position: 'Vector' = None, radius: 'Float' = None)
```

> Node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'EDGES'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### viewer()

> classmethod

``` python
viewer(named_sockets: 'dict' = {}, ui_shortcut=0, **sockets)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Information:
- **Parameter** : 'EDGE'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **ui_shortcut** (_int_ = 0) : parameter 'ui_shortcut'
- **sockets**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>