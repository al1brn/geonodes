# Corner

``` python
Corner(geometry: geonodes.core.geometry_class.Geometry)
```

> Corner domain of a [Mesh](mesh.md#mesh)

#### Arguments:
- **geometry** (_Geometry_)

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [\_\_call__](domain.md#__call__) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [foreach](domain.md#foreach) :black_small_square: [for_each_element](domain.md#for_each_element) :black_small_square: [\_geo](domain.md#_geo) :black_small_square: [\_geo_type](geom.md#_geo_type) :black_small_square: [\_\_getitem__](geom.md#__getitem__) :black_small_square: [get_selection](domain.md#get_selection) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_selection' not found]() :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square:

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
accumulate_field(value: 'Float | Integer | Vector | Matrix' = None, group_id: 'Integer' = None)
```

> Node [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'CORNER'



#### Arguments:
- **value** (_Float | Integer | Vector | Matrix_ = None) : socket 'Value' (id: Value)
- **group_id** (_Integer_ = None) : socket 'Group ID' (id: Group Index)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

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
- **Parameter** : 'CORNER'



#### Arguments:
- **attribute** (_Float | Vector_ = None) : socket 'Attribute' (id: Attribute)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### edges()

> classmethod

``` python
edges(corner_index: 'Integer' = None)
```

> Node [Edges of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### evaluate_at_index()

> classmethod

``` python
evaluate_at_index(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, index: 'Integer' = None)
```

> Node [Evaluate at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'CORNER'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### evaluate_on_domain()

> classmethod

``` python
evaluate_on_domain(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None)
```

> Node [Evaluate on Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html)

#### Information:
- **Parameter** : depending on 'value' type
- **Parameter** : 'CORNER'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### face()

> classmethod

``` python
face(corner_index: 'Integer' = None)
```

> Node [Face of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/face_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### face_index()

> classmethod

``` python
face_index(corner_index: 'Integer' = None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### index_in_face()

> classmethod

``` python
index_in_face(corner_index: 'Integer' = None)
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
next_edge_index(corner_index: 'Integer' = None)
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
offset_in_face(corner_index: 'Integer' = None, offset: 'Integer' = None)
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
pack_uv_islands(uv: 'Vector' = None, margin: 'Float' = None, rotate: 'Boolean' = None, method: "Literal['Bounding Box', 'Convex Hull', 'Exact Shape']" = None)
```

> Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/pack_uv_islands.html)

#### Information:
- **Socket** : self[selection]



#### Arguments:
- **uv** (_Vector_ = None) : socket 'UV' (id: UV)
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **rotate** (_Boolean_ = None) : socket 'Rotate' (id: Rotate)
- **method** (_Literal['Bounding Box', 'Convex Hull', 'Exact Shape']_ = None) : ('Bounding Box', 'Convex Hull', 'Exact Shape')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### previous_edge_index()

> classmethod

``` python
previous_edge_index(corner_index: 'Integer' = None)
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
sample_index(value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix' = None, index: 'Integer' = None, clamp=False)
```

> Node [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'value' type
- **Parameter** : 'CORNER'



#### Arguments:
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix_ = None) : socket 'Value' (id: Value)
- **index** (_Integer_ = None) : socket 'Index' (id: Index)
- **clamp** (_bool_ = False) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### sample_nearest()

> method

``` python
sample_nearest(sample_position: 'Vector' = None)
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
store(name: 'String' = None, value: 'Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color' = None)
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
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

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
- **Parameter** : 'CORNER'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)
- **value** (_Float | Integer | Boolean | Vector | Color | Rotation | Matrix | Integer | Vector | Color_ = None) : socket 'Value' (id: Value)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### store_uv()

> method

``` python
store_uv(name: 'String' = None, value: 'Vector' = None)
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
to_points(position: 'Vector' = None, radius: 'Float' = None)
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
uv_unwrap(seam: 'Boolean' = None, margin: 'Float' = None, fill_holes: 'Boolean' = None, method: "Literal['Angle Based', 'Conformal']" = None)
```

> Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_unwrap.html)

#### Information:
- **Socket** : self[selection]



#### Arguments:
- **seam** (_Boolean_ = None) : socket 'Seam' (id: Seam)
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **fill_holes** (_Boolean_ = None) : socket 'Fill Holes' (id: Fill Holes)
- **method** (_Literal['Angle Based', 'Conformal']_ = None) : ('Angle Based', 'Conformal')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### vertex_index()

> classmethod

``` python
vertex_index(corner_index: 'Integer' = None)
```

> Node [Vertex of Corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/vertex_of_corner.html)

#### Arguments:
- **corner_index** (_Integer_ = None) : socket 'Corner Index' (id: Corner Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>

----------
### viewer()

> classmethod

``` python
viewer(named_sockets: 'dict' = {}, ui_shortcut=0, **sockets)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Information:
- **Parameter** : 'CORNER'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **ui_shortcut** (_int_ = 0) : parameter 'ui_shortcut'
- **sockets**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Corner](corner.md#corner) :black_small_square: [Content](corner.md#content) :black_small_square: [Methods](corner.md#methods)</sub>