# Face

> Bases classes: [Domain](geono-domain.md#domain)

``` python
Face(geometry)
```

> Face domain of a [Mesh](geono-mesh.md#mesh)

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](geono-domain.md#accumulate_field) :black_small_square: [attribute_statistic](geono-domain.md#attribute_statistic) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [capture](geono-domain.md#capture) :black_small_square: [capture_attribute](geono-domain.md#capture_attribute) :black_small_square: [captures](geono-domain.md#captures) :black_small_square: [delete](geono-domain.md#delete) :black_small_square: [delete_all](geono-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](geono-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](geono-domain.md#delete_faces) :black_small_square: [delete_geometry](geono-domain.md#delete_geometry) :black_small_square: [domain_name](geono-domain.md#domain_name) :black_small_square: [duplicate_elements](geono-domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](geono-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](geono-domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](geono-domain.md#exclude_corner) :black_small_square: [extrude](geono-domain.md#extrude) :black_small_square: [\_geo_type](geono-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geobase.md#__getitem__) :black_small_square: [id](geono-geobase.md#id) :black_small_square: [\_jump](geono-domain.md#_jump) :black_small_square: [material](geono-geobase.md#material) :black_small_square: [material_index](geono-geobase.md#material_index) :black_small_square: [material_selection](geono-geobase.md#material_selection) :black_small_square: [\_node](geono-domain.md#_node) :black_small_square: [offset](geono-geobase.md#offset) :black_small_square: [plural_domain](geono-domain.md#plural_domain) :black_small_square: [position](geono-geobase.md#position) :black_small_square: [proximity](geono-domain.md#proximity) :black_small_square: [\_raw_sel](geono-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geobase.md#replace_material) :black_small_square: [restrict_domain](geono-domain.md#restrict_domain) :black_small_square: [sample_index](geono-domain.md#sample_index) :black_small_square: [sample_nearest](geono-domain.md#sample_nearest) :black_small_square: [\_sel](geono-domain.md#_sel) :black_small_square: [separate](geono-domain.md#separate) :black_small_square: [set_id](geono-geobase.md#set_id) :black_small_square: [set_position](geono-geobase.md#set_position) :black_small_square: [sort_elements](geono-domain.md#sort_elements) :black_small_square: [split_to_instances](geono-domain.md#split_to_instances) :black_small_square: [store](geono-domain.md#store) :black_small_square: [store_named_attribute](geono-domain.md#store_named_attribute) :black_small_square: [\_\_str__](geono-domain.md#__str__) :black_small_square: [to_points](geono-domain.md#to_points) :black_small_square: [viewer](geono-domain.md#viewer) :black_small_square:

## Content

- **A** : [area](macro-geono-face.md#area)
- **C** : [corner_index](macro-geono-face.md#corner_index) :black_small_square: [count](macro-geono-face.md#count)
- **D** : [distribute_points](macro-geono-face.md#distribute_points)
- **F** : [flip](macro-geono-face.md#flip)
- **G** : [group_boundaries](macro-geono-face.md#group_boundaries)
- **I** : [is_planar](macro-geono-face.md#is_planar)
- **N** : [neighbors](macro-geono-face.md#neighbors) :black_small_square: [neighbors_face_count](macro-geono-face.md#neighbors_face_count) :black_small_square: [neighbors_vertex_count](macro-geono-face.md#neighbors_vertex_count)
- **S** : [scale](macro-geono-face.md#scale) :black_small_square: [smooth](macro-geono-face.md#smooth)

## Properties



### area

> _type_: **Float**
>

> Area read only property

- getter : [Face Area](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_area.html)
- setter : None

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Properties](macro-geono-face.md#properties)</sub>

### count

> _type_: **Integer**
>

> Socket 'Face Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Properties](macro-geono-face.md#properties)</sub>

### neighbors

> _type_: **Node**
>

> Node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Properties](macro-geono-face.md#properties)</sub>

### neighbors_face_count

> _type_: **Integer**
>

> Socket 'Face Count' of node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Properties](macro-geono-face.md#properties)</sub>

### neighbors_vertex_count

> _type_: **Integer**
>

> Socket 'Vertex Count' of node [Face Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Properties](macro-geono-face.md#properties)</sub>

### smooth

> _type_: **Boolean**
>

> Smooth property

- getter : node [Is Face Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/is_face_smooth.html)
- setter : node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_shade_smooth.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Properties](macro-geono-face.md#properties)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Methods](macro-geono-face.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Methods](macro-geono-face.md#methods)</sub>

----------
### flip()

> method

``` python
flip()
```

> Node [Flip Faces](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/flip_faces.html)



#### Returns:
- **Mesh** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Methods](macro-geono-face.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Methods](macro-geono-face.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Methods](macro-geono-face.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](macro-geono-face.md#face) :black_small_square: [Content](macro-geono-face.md#content) :black_small_square: [Methods](macro-geono-face.md#methods)</sub>