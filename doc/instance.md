# Instance

> Bases classes: [Domain](domain.md#domain)

``` python
Instance(geometry)
```

> Instant domain of [Instances](instances.md#instances)

> [!NOTE]
> The geometry has only one domain sharing the same:
> - [Instances](instances.md#instances) : name of geometry class
> - **Instance** : name of domain class
> - [insts](instances.md#insts) : name of the domain property of class [Instances](instances.md#instances)

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](domain.md#accumulate_field) :black_small_square: [attribute_statistic](domain.md#attribute_statistic) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [captures](domain.md#captures) :black_small_square: [delete](domain.md#delete) :black_small_square: [delete_all](domain.md#delete_all) :black_small_square: [delete_edges_and_faces](domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](domain.md#delete_faces) :black_small_square: [delete_geometry](domain.md#delete_geometry) :black_small_square: [domain_name](domain.md#domain_name) :black_small_square: [duplicate_elements](domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](domain.md#exclude_corner) :black_small_square: [extrude](domain.md#extrude) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [id](geobase.md#id) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [material](geobase.md#material) :black_small_square: [material_index](geobase.md#material_index) :black_small_square: [material_selection](geobase.md#material_selection) :black_small_square: [\_node](domain.md#_node) :black_small_square: [offset](geobase.md#offset) :black_small_square: [plural_domain](domain.md#plural_domain) :black_small_square: [position](geobase.md#position) :black_small_square: [proximity](domain.md#proximity) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [replace_material](geobase.md#replace_material) :black_small_square: [restrict_domain](domain.md#restrict_domain) :black_small_square: [sample_index](domain.md#sample_index) :black_small_square: [sample_nearest](domain.md#sample_nearest) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [separate](domain.md#separate) :black_small_square: [set_id](geobase.md#set_id) :black_small_square: [set_position](geobase.md#set_position) :black_small_square: [sort_elements](domain.md#sort_elements) :black_small_square: [split_to_instances](domain.md#split_to_instances) :black_small_square: [store](domain.md#store) :black_small_square: [store_named_attribute](domain.md#store_named_attribute) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [to_points](domain.md#to_points) :black_small_square: [viewer](domain.md#viewer) :black_small_square:

## Content

- [count](instance.md#count)
- [rotation](instance.md#rotation)
- [scale](instance.md#scale)
- [transform](instance.md#transform)
- [translate](instance.md#translate)

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

### transform

> _type_: **Matrix**
>

> Transform property

- getter : [Instance Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_transform.html)
- setter : <@Node Set Instance Transform>

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Properties](instance.md#properties)</sub>

## Methods



----------
### translate()

> method

``` python
translate(translation=None, local_space=None)
```

> Node [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html)



#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **Instances** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](instance.md#instance) :black_small_square: [Content](instance.md#content) :black_small_square: [Methods](instance.md#methods)</sub>