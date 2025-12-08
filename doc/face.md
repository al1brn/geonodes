# Face

``` python
Face(geometry: geonodes.core.geometry_class.Geometry)
```

> Face domain of a [Mesh](mesh.md#mesh)

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [foreach](domain.md#foreach) :black_small_square: [for_each_element](domain.md#for_each_element) :black_small_square: [\_geo](domain.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](domain.md#get_selection) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_selection' not found]() :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square:

## Content

- **A** : [accumulate_field](face.md#accumulate_field) :black_small_square: [active_element](face.md#active_element) :black_small_square: [attribute_statistic](face.md#attribute_statistic)
- **C** : [corner_index](face.md#corner_index) :black_small_square: [corners](face.md#corners) :black_small_square: [corners_total](face.md#corners_total) :black_small_square: [count](face.md#count)
- **D** : [delete](face.md#delete) :black_small_square: [delete_all](face.md#delete_all) :black_small_square: [delete_edge_face](face.md#delete_edge_face) :black_small_square: [delete_geometry](face.md#delete_geometry) :black_small_square: [delete_geometry_all](face.md#delete_geometry_all) :black_small_square: [delete_geometry_edge_face](face.md#delete_geometry_edge_face) :black_small_square: [delete_geometry_only_face](face.md#delete_geometry_only_face) :black_small_square: [delete_only_face](face.md#delete_only_face) :black_small_square: [distribute_points](face.md#distribute_points) :black_small_square: [distribute_points_poisson](face.md#distribute_points_poisson) :black_small_square: [distribute_points_random](face.md#distribute_points_random) :black_small_square: [duplicate](face.md#duplicate)
- **E** : [evaluate_at_index](face.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](face.md#evaluate_on_domain) :black_small_square: [extrude](face.md#extrude)
- **F** : [field_average](face.md#field_average) :black_small_square: [field_min_max](face.md#field_min_max) :black_small_square: [field_variance](face.md#field_variance)
- **I** : [is_planar](face.md#is_planar)
- **M** : [material](face.md#material) :black_small_square: [material_index](face.md#material_index)
- **N** : [normal](face.md#normal)
- **S** : [sample_index](face.md#sample_index) :black_small_square: [sample_nearest](face.md#sample_nearest) :black_small_square: [scale](face.md#scale) :black_small_square: [separate](face.md#separate) :black_small_square: [set_selection](face.md#set_selection) :black_small_square: [set_shade_smooth](face.md#set_shade_smooth) :black_small_square: [shade_smooth](face.md#shade_smooth) :black_small_square: [smooth](face.md#smooth) :black_small_square: [sort](face.md#sort) :black_small_square: [split_to_instances](face.md#split_to_instances) :black_small_square: [store](face.md#store) :black_small_square: [store_named_attribute](face.md#store_named_attribute)
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

### normal

> _type_: **?**
>

Write only property for node <Node Set Mesh Normal>

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
accumulate_field(value: 'Float | Integer | Vector | Matrix' = None, group_id: 'Integer' = None)
```

> Node [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACE'



#### Arguments:
- **value** (_Float | Integer | Vector | Matrix_ = None) : socket 'Value' (id: Value)
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
attribute_statistic(attribute: 'Float | Vector' = None)
```

> Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : depending on 'attribute' type
- **Parameter** : 'FACE'



#### Arguments:
- **attribute** (_Float | Vector_ = None) : socket 'Attribute' (id: Attribute)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### corner_index()

> classmethod

``` python
corner_index(face_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
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
corners(face_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
```

> Node [Corners of Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_face.html)

#### Arguments:
- **face_index** (_Integer_ = None) : socket 'Face Index' (id: Face Index)
- **weights** (_Float_ = None) : socket 'Weights' (id: Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (id: Sort Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### corners_total()

> classmethod

``` python
corners_total(face_index: 'Integer' = None, weights: 'Float' = None, sort_index: 'Integer' = None)
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
delete(mode: "Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']" = 'ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Arguments:
- **mode** (_Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']_ = ALL) : parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']



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
delete_geometry(mode: "Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']" = 'ALL')
```

> Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACE'



#### Arguments:
- **mode** (_Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']_ = ALL) : parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']



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
### distribute_points()

> method

``` python
distribute_points(density: 'Float' = None, seed: 'Integer' = None, distribute_method: "Literal['RANDOM', 'POISSON']" = 'RANDOM')
```

> Node ERROR: Node 'Distribute Points on Faces' not found

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)
- **distribute_method** (_Literal['RANDOM', 'POISSON']_ = RANDOM) : parameter 'distribute_method' in ['RANDOM', 'POISSON']



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### distribute_points_poisson()

> method

``` python
distribute_points_poisson(distance_min: 'Float' = None, density_max: 'Float' = None, density_factor: 'Float' = None, seed: 'Integer' = None)
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



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### distribute_points_random()

> method

``` python
distribute_points_random(density: 'Float' = None, seed: 'Integer' = None)
```

> Node ERROR: Node 'Distribute Points on Faces' not found

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'RANDOM'



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

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
evaluate_at_index(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, index: 'Integer' = None)
```

> Node [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACE'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### evaluate_on_domain()

> classmethod

``` python
evaluate_on_domain(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None)
```

> Node [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'FACE'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### extrude()

> method

``` python
extrude(offset: 'Vector' = None, offset_scale: 'Float' = None, individual: 'Boolean' = None)
```

> Node [Extrude Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Socket** : self[selection]
- **Parameter** : 'FACES'



#### Arguments:
- **offset** (_Vector_ = None) : socket 'Offset' (id: Offset)
- **offset_scale** (_Float_ = None) : socket 'Offset Scale' (id: Offset Scale)
- **individual** (_Boolean_ = None) : socket 'Individual' (id: Individual)



#### Returns:
- **Mesh** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### is_planar()

> classmethod

``` python
is_planar(threshold: 'Float' = None)
```

> Node [Is Face Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_is_planar.html)

#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

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
- **Parameter** : 'FACE'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **clamp** (_bool_ = False) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### sample_nearest()

> method

``` python
sample_nearest(sample_position: 'Vector' = None)
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
scale(scale: 'Float' = None, center: 'Vector' = None, scale_mode: "Literal['Uniform', 'Single Axis']" = None, axis: 'Vector' = None)
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
- **scale_mode** (_Literal['Uniform', 'Single Axis']_ = None) : ('Uniform', 'Single Axis')
- **axis** (_Vector_ = None) : socket 'Axis' (id: Axis)



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
set_shade_smooth(shade_smooth: 'Boolean' = None)
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
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

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
split_to_instances(group_id: 'Integer' = None)
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
store(name: 'String' = None, value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color' = None)
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
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

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
- **Parameter** : 'FACE'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

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
- **Parameter** : 'FACES'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### viewer()

> classmethod

``` python
viewer(named_sockets: 'dict' = {}, ui_shortcut=0, **sockets)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Information:
- **Parameter** : 'FACE'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **ui_shortcut** (_int_ = 0) : parameter 'ui_shortcut'
- **sockets**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>