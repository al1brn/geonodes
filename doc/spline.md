# Spline

> Bases classes: [Domain](domain.md#domain)

``` python
Spline(geometry)
```

> Curve, or Spline, domain of a [Curve](curve.md#curve)

Methods of **Spline** class are nodes which accept a SPLINE or CURVE domain.

In addition, the node [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/points_of_curve.html) is implemented as method [points](spline.md#points).

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](domain.md#accumulate_field) :black_small_square: [attribute_statistic](domain.md#attribute_statistic) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [captures](domain.md#captures) :black_small_square: [delete](domain.md#delete) :black_small_square: [delete_all](domain.md#delete_all) :black_small_square: [delete_edges_and_faces](domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](domain.md#delete_faces) :black_small_square: [delete_geometry](domain.md#delete_geometry) :black_small_square: [domain_name](domain.md#domain_name) :black_small_square: [duplicate_elements](domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](domain.md#exclude_corner) :black_small_square: [extrude](domain.md#extrude) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [id](geobase.md#id) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [material](geobase.md#material) :black_small_square: [material_index](geobase.md#material_index) :black_small_square: [material_selection](geobase.md#material_selection) :black_small_square: [\_node](domain.md#_node) :black_small_square: [offset](geobase.md#offset) :black_small_square: [plural_domain](domain.md#plural_domain) :black_small_square: [position](geobase.md#position) :black_small_square: [proximity](domain.md#proximity) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [replace_material](geobase.md#replace_material) :black_small_square: [restrict_domain](domain.md#restrict_domain) :black_small_square: [sample_index](domain.md#sample_index) :black_small_square: [sample_nearest](domain.md#sample_nearest) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [separate](domain.md#separate) :black_small_square: [set_id](geobase.md#set_id) :black_small_square: [set_position](geobase.md#set_position) :black_small_square: [sort_elements](domain.md#sort_elements) :black_small_square: [split_to_instances](domain.md#split_to_instances) :black_small_square: [store](domain.md#store) :black_small_square: [store_named_attribute](domain.md#store_named_attribute) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [to_points](domain.md#to_points) :black_small_square: [viewer](domain.md#viewer) :black_small_square:

## Content

- [count](spline.md#count)
- [is_cyclic](spline.md#is_cyclic)
- [parameter](spline.md#parameter)
- [points](spline.md#points)
- [resolution](spline.md#resolution)
- [type](spline.md#type)

## Properties



### count

> _type_: **Integer**
>

> Socket 'Spline Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### is_cyclic

> _type_: **Boolean**
>

> Is cyclic property

- getter : node [Is Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/is_spline_cyclic.html)
- setter : node [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_cyclic.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### parameter

> _type_: **Node**
>

> Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/spline_parameter.html)

``` python
factor = curve.parameter.factor
length = curve.parameter.length
index = curve.parameter.index
```

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### resolution

> _type_: **Integer**
>

> Resolution property

- getter : node [Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/spline_resolution.html)
- setter : node [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_resolution.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

### type

> _type_: **Error**
>

> Type wite only property

> [!Note]
> Write only property

- getter : None, write only property
- setter : node [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_type.html), value in ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Properties](spline.md#properties)</sub>

## Methods



----------
### points()

> method

``` python
points(curve_index=None, weights=None, sort_index=None)
```

> Socket 'Point Index' of node ERROR: Node 'of curve' not found

#### Arguments:
- **curve_index** (_Integer_ = None) : socket 'Curve Index'
- **weights** (_Float_ = None) : socket 'Weights'
- **sort_index** (_Integer_ = None) : socket 'Sort Index'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Spline](spline.md#spline) :black_small_square: [Content](spline.md#content) :black_small_square: [Methods](spline.md#methods)</sub>