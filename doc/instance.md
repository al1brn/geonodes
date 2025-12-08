# Instance

``` python
Instance(geometry: geonodes.core.geometry_class.Geometry)
```

> Instance domain of [Instances](instances.md#instances)

> [!NOTE]
> The geometry has only one domain sharing the same name:
> - [Instances](instances.md#instances) : name of geometry class
> - **Instance** : name of domain class
> - [insts](instances.md#insts) : name of the domain property of class [Instances](instances.md#instances)

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [foreach](domain.md#foreach) :black_small_square: [for_each_element](domain.md#for_each_element) :black_small_square: [\_geo](domain.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](domain.md#get_selection) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_selection' not found]() :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square:

## Content

- **A** : [accumulate_field](instance.md#accumulate_field) :black_small_square: [attribute_statistic](instance.md#attribute_statistic)
- **C** : [count](instance.md#count)
- **D** : [delete](instance.md#delete) :black_small_square: [delete_all](instance.md#delete_all) :black_small_square: [delete_edge_face](instance.md#delete_edge_face) :black_small_square: [delete_geometry](instance.md#delete_geometry) :black_small_square: [delete_geometry_all](instance.md#delete_geometry_all) :black_small_square: [delete_geometry_edge_face](instance.md#delete_geometry_edge_face) :black_small_square: [delete_geometry_only_face](instance.md#delete_geometry_only_face) :black_small_square: [delete_only_face](instance.md#delete_only_face) :black_small_square: [duplicate](instance.md#duplicate)
- **E** : [evaluate_at_index](instance.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](instance.md#evaluate_on_domain)
- **F** : [field_average](instance.md#field_average) :black_small_square: [field_min_max](instance.md#field_min_max) :black_small_square: [field_variance](instance.md#field_variance)
- **R** : [rotation](instance.md#rotation)
- **S** : [sample_index](instance.md#sample_index) :black_small_square: [scale](instance.md#scale) :black_small_square: [separate](instance.md#separate) :black_small_square: [sort](instance.md#sort) :black_small_square: [split_to_instances](instance.md#split_to_instances) :black_small_square: [store](instance.md#store) :black_small_square: [store_named_attribute](instance.md#store_named_attribute)
- **V** : [viewer](instance.md#viewer)

## Properties



### count

> _type_: **Integer**
>

> Socket 'Instance Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Properties](instance.md#properties)</sub>

### rotation

> _type_: **?**
>

> Rotation property

- getter : [Instance Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html)
- setter : [Rotate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html)

 Rotation can be set either by a [Rotation](rotation.md#rotation) argument or by a dict with keys
 in ('Rotation', 'Pivot Point', 'Local Space')

 ``` python
 instances = Instances()
 instances.insts.rotation = (1, 2, 3)
 instances.insts.rotation = {'Rotation': (1, 2, 3), 'Pivot Point': (10, 11, 12), 'Local Space': True}
 ```

 Returns
 -------
 - Rotation

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Properties](instance.md#properties)</sub>

### scale

> _type_: **Vector**
>

> Scale property

- getter : [Instance Scale](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html)
- setter : [Scale Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html)

Scale can be set either by a [Vector](vector.md#vector) argument or by a dict with keys
in ('Scale', 'Center', 'Local Space')

``` python
instances = Instances()
instances.insts.scale = (1, 2, 3)
instances.insts.scale = {'Scale': (1, 2, 3), 'Center': (10, 11, 12), 'Local Space': True}
```

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Properties](instance.md#properties)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **value** (_Float | Integer | Vector | Matrix_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **attribute** (_Float | Vector_ = None) : socket 'Attribute' (id: Attribute)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **mode** (_Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']_ = ALL) : parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'
- **Parameter** : 'ALL'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'
- **Parameter** : 'EDGE_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **mode** (_Literal['ALL', 'EDGE_FACE', 'ONLY_FACE']_ = ALL) : parameter 'mode' in ['ALL', 'EDGE_FACE', 'ONLY_FACE']



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'
- **Parameter** : 'ALL'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'
- **Parameter** : 'EDGE_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'
- **Parameter** : 'ONLY_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'
- **Parameter** : 'ONLY_FACE'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **amount** (_Integer_ = None) : socket 'Amount' (id: Amount)



#### Returns:
- **Geometry** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

----------
### evaluate_at_index()

> classmethod

``` python
evaluate_at_index(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, index: 'Integer' = None)
```

> Node [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'INSTANCE'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

----------
### evaluate_on_domain()

> classmethod

``` python
evaluate_on_domain(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None)
```

> Node [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'INSTANCE'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **clamp** (_bool_ = False) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Returns:
- **Geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)
- **sort_weight** (_Float_ = None) : socket 'Sort Weight' (id: Sort Weight)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group ID)



#### Returns:
- **Instances** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

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
- **Parameter** : 'INSTANCE'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>

----------
### viewer()

> classmethod

``` python
viewer(named_sockets: 'dict' = {}, ui_shortcut=0, **sockets)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Information:
- **Parameter** : 'INSTANCE'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **ui_shortcut** (_int_ = 0) : parameter 'ui_shortcut'
- **sockets**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>