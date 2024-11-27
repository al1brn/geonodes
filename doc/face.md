# Face

> Bases classes: [Domain](domain.md#domain)

``` python
Face(geometry)
```

> Face domain of a [Mesh](mesh.md#mesh)

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](domain.md#accumulate_field) :black_small_square: [attribute_statistic](domain.md#attribute_statistic) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [captures](domain.md#captures) :black_small_square: [delete](domain.md#delete) :black_small_square: [delete_all](domain.md#delete_all) :black_small_square: [delete_edges_and_faces](domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](domain.md#delete_faces) :black_small_square: [delete_geometry](domain.md#delete_geometry) :black_small_square: [domain_name](domain.md#domain_name) :black_small_square: [duplicate_elements](domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](domain.md#exclude_corner) :black_small_square: [extrude](domain.md#extrude) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [id](geobase.md#id) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [material](geobase.md#material) :black_small_square: [material_index](geobase.md#material_index) :black_small_square: [material_selection](geobase.md#material_selection) :black_small_square: [\_node](domain.md#_node) :black_small_square: [offset](geobase.md#offset) :black_small_square: [plural_domain](domain.md#plural_domain) :black_small_square: [position](geobase.md#position) :black_small_square: [proximity](domain.md#proximity) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [replace_material](geobase.md#replace_material) :black_small_square: [restrict_domain](domain.md#restrict_domain) :black_small_square: [sample_index](domain.md#sample_index) :black_small_square: [sample_nearest](domain.md#sample_nearest) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [separate](domain.md#separate) :black_small_square: [set_id](geobase.md#set_id) :black_small_square: [set_position](geobase.md#set_position) :black_small_square: [sort_elements](domain.md#sort_elements) :black_small_square: [split_to_instances](domain.md#split_to_instances) :black_small_square: [store](domain.md#store) :black_small_square: [store_named_attribute](domain.md#store_named_attribute) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [to_points](domain.md#to_points) :black_small_square: [viewer](domain.md#viewer) :black_small_square:

## Content

- **A** : [area](face.md#area)
- **C** : [corner_index](face.md#corner_index) :black_small_square: [count](face.md#count)
- **D** : [distribute_points](face.md#distribute_points)
- **F** : [flip](face.md#flip)
- **G** : [group_boundaries](face.md#group_boundaries)
- **I** : [is_planar](face.md#is_planar)
- **N** : [neighbors](face.md#neighbors) :black_small_square: [neighbors_face_count](face.md#neighbors_face_count) :black_small_square: [neighbors_vertex_count](face.md#neighbors_vertex_count)
- **S** : [scale](face.md#scale) :black_small_square: [smooth](face.md#smooth)

## Properties



### area

> _type_: **Float**
>

> Area read only property

- getter : [Face Area](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_area.html)
- setter : None

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

### count

> _type_: **Integer**
>

> Socket 'Face Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

### neighbors

> _type_: **Node**
>

> Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

### neighbors_face_count

> _type_: **Integer**
>

> Socket 'Face Count' of node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

### neighbors_vertex_count

> _type_: **Integer**
>

> Socket 'Vertex Count' of node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

### smooth

> _type_: **Boolean**
>

> Smooth property

- getter : node [Is Face Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/is_face_smooth.html)
- setter : node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_shade_smooth.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Properties](face.md#properties)</sub>

## Methods



----------
### corner_index()

> classmethod

``` python
corner_index(face_index=None, weights=None, sort_index=None)
```

> Node [Corners of Face](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_face.html)

#### Arguments:
- **face_index** (_Integer_ = None) : socket 'Face Index' (Face Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### distribute_points()

> method

``` python
distribute_points(density=None, distance_min=None, density_max=None, density_factor=None, seed=None)
```

> Node ERROR: Node 'Distribute Points on Faces' not found



if 'density' argument is not None, 'RANDOM' method is applied, 'POISSON' otherwise

- distribute_method (str): Node.distribute_method in ('RANDOM', 'POISSON')
- use_legacy_normal (bool): Node.use_legacy_normal

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)n 'RANDOM' method if not None 'POISSON' otherwise
- **distance_min** (_Float_ = None) : socket 'Distance Min'
- **density_max** (_Float_ = None) : socket 'Density Max'
- **density_factor** (_Float_ = None) : socket 'Density Factor'
- **seed** (_Integer_ = None) : socket 'Seed' (Seed)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### flip()

> method

``` python
flip()
```

> Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/flip_faces.html)



#### Returns:
- **Mesh** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### group_boundaries()

> method

``` python
group_boundaries(face_group_id=None)
```

> Node [Face Group Boundaries](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_group_boundaries.html)

#### Arguments:
- **face_group_id** (_Integer_ = None) : socket 'Face Group ID' (Face Set)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### is_planar()

> method

``` python
is_planar(threshold=None)
```

> Node [Is Face Planar](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_is_planar.html)

#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale=None, center=None, uniform=True)
```

> Node [Scale Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/scale_elements.html)



- domain (str): Node.domain in ('FACE', 'EDGE')
- scale_mode (str): Node.scale_mode in ('UNIFORM', 'SINGLE_AXIS')

#### Arguments:
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **uniform** ( = True)



#### Returns:
- **Mesh** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](face.md#face) :black_small_square: [Content](face.md#content) :black_small_square: [Methods](face.md#methods)</sub>