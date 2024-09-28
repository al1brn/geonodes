# Instance

> Bases classes: [Domain](geono-domain.md#domain)

``` python
Instance(geometry)
```

> Instant domain of [Instances](geono-instances.md#instances)

> [!NOTE]
> The geometry has only one domain sharing the same:
> - [Instances](geono-instances.md#instances) : name of geometry class
> - **Instance** : name of domain class
> - [impossible to find the section 'insts' in page 'Instances'](geono-instances.md#instances) : name of the domain property of class [Instances](geono-instances.md#instances)

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](geono-domain.md#accumulate_field) :black_small_square: [attribute_statistic](geono-domain.md#attribute_statistic) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [capture](geono-domain.md#capture) :black_small_square: [capture_attribute](geono-domain.md#capture_attribute) :black_small_square: [delete](geono-domain.md#delete) :black_small_square: [delete_all](geono-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](geono-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](geono-domain.md#delete_faces) :black_small_square: [delete_geometry](geono-domain.md#delete_geometry) :black_small_square: [domain_name](geono-domain.md#domain_name) :black_small_square: [duplicate_elements](geono-domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](geono-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](geono-domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](geono-domain.md#exclude_corner) :black_small_square: [extrude](geono-domain.md#extrude) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [\_node](geono-domain.md#_node) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [plural_domain](geono-domain.md#plural_domain) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [proximity](geono-domain.md#proximity) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [restrict_domain](geono-domain.md#restrict_domain) :black_small_square: [sample_index](geono-domain.md#sample_index) :black_small_square: [sample_nearest](geono-domain.md#sample_nearest) :black_small_square: [\_sel](geono-domain.md#_sel) :black_small_square: [separate](geono-domain.md#separate) :black_small_square: [set_id](geono-geome-geobase.md#set_id) :black_small_square: [set_position](geono-geome-geobase.md#set_position) :black_small_square: [sort_elements](geono-domain.md#sort_elements) :black_small_square: [split_to_instances](geono-domain.md#split_to_instances) :black_small_square: [store](geono-domain.md#store) :black_small_square: [store_named_attribute](geono-domain.md#store_named_attribute) :black_small_square: [\_\_str__](geono-domain.md#__str__) :black_small_square: [to_points](geono-domain.md#to_points) :black_small_square: [viewer](geono-domain.md#viewer) :black_small_square:

## Content

- [rotation](geono-instance.md#rotation)
- [scale](geono-instance.md#scale)
- [transform](geono-instance.md#transform)
- [translate](geono-instance.md#translate)

## Properties



### rotation

> _type_: **Rotation**
>

> **node** : [Instance Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](geono-instance.md#instance) :black_small_square: [Content](geono-instance.md#content) :black_small_square: [Properties](geono-instance.md#properties)</sub>

### scale

> _type_: **Vector**
>

> **node** : [Instance Scale](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](geono-instance.md#instance) :black_small_square: [Content](geono-instance.md#content) :black_small_square: [Properties](geono-instance.md#properties)</sub>

### transform

> _type_: **Matrix**
>

> **node** : [Instance Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](geono-instance.md#instance) :black_small_square: [Content](geono-instance.md#content) :black_small_square: [Properties](geono-instance.md#properties)</sub>

## Methods



----------
### translate()

> method

``` python
translate(translation=None, local_space=None)
```

> **node** : [Translate Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html)



#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **local_space** (_Boolean_ = None) : socket 'Local Space' (Local Space)



#### Returns:
- **self** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Instance](geono-instance.md#instance) :black_small_square: [Content](geono-instance.md#content) :black_small_square: [Methods](geono-instance.md#methods)</sub>