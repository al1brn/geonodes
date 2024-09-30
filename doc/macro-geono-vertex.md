# Vertex

> Bases classes: [Point](geono-point.md#point)

``` python
Vertex(geometry)
```

> Point domain of a [Mesh](geono-mesh.md#mesh)

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](geono-domain.md#accumulate_field) :black_small_square: [attribute_statistic](geono-domain.md#attribute_statistic) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [capture](geono-domain.md#capture) :black_small_square: [capture_attribute](geono-domain.md#capture_attribute) :black_small_square: [count](geono-point.md#count) :black_small_square: [delete](geono-domain.md#delete) :black_small_square: [delete_all](geono-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](geono-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](geono-domain.md#delete_faces) :black_small_square: [delete_geometry](geono-domain.md#delete_geometry) :black_small_square: [domain_name](geono-domain.md#domain_name) :black_small_square: [duplicate_elements](geono-domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](geono-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](geono-domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](geono-domain.md#exclude_corner) :black_small_square: [extrude](geono-domain.md#extrude) :black_small_square: [\_geo_type](geono-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geobase.md#__getitem__) :black_small_square: [id](geono-geobase.md#id) :black_small_square: [instance_on](geono-point.md#instance_on) :black_small_square: [\_jump](geono-domain.md#_jump) :black_small_square: [material](geono-geobase.md#material) :black_small_square: [material_index](geono-geobase.md#material_index) :black_small_square: [material_selection](geono-geobase.md#material_selection) :black_small_square: [\_node](geono-domain.md#_node) :black_small_square: [offset](geono-geobase.md#offset) :black_small_square: [plural_domain](geono-domain.md#plural_domain) :black_small_square: [position](geono-geobase.md#position) :black_small_square: [proximity](geono-domain.md#proximity) :black_small_square: [\_raw_sel](geono-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geobase.md#replace_material) :black_small_square: [restrict_domain](geono-domain.md#restrict_domain) :black_small_square: [sample_index](geono-domain.md#sample_index) :black_small_square: [sample_nearest](geono-domain.md#sample_nearest) :black_small_square: [\_sel](geono-domain.md#_sel) :black_small_square: [separate](geono-domain.md#separate) :black_small_square: [set_id](geono-geobase.md#set_id) :black_small_square: [set_position](geono-geobase.md#set_position) :black_small_square: [sort_elements](geono-domain.md#sort_elements) :black_small_square: [split_to_instances](geono-domain.md#split_to_instances) :black_small_square: [store](geono-domain.md#store) :black_small_square: [store_named_attribute](geono-domain.md#store_named_attribute) :black_small_square: [\_\_str__](geono-domain.md#__str__) :black_small_square: [to_points](geono-domain.md#to_points) :black_small_square: [viewer](geono-domain.md#viewer) :black_small_square:

## Content

- [corner_index](macro-geono-vertex.md#corner_index)
- [edge_index](macro-geono-vertex.md#edge_index)
- [edge_paths_to_curves](macro-geono-vertex.md#edge_paths_to_curves)
- [neighbors](macro-geono-vertex.md#neighbors)
- [neighbors_face_count](macro-geono-vertex.md#neighbors_face_count)
- [neighbors_vertex_count](macro-geono-vertex.md#neighbors_vertex_count)
- [paths_to_selection](macro-geono-vertex.md#paths_to_selection)

## Properties



### neighbors

> _type_: **Node**
>

> Node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](macro-geono-vertex.md#vertex) :black_small_square: [Content](macro-geono-vertex.md#content) :black_small_square: [Properties](macro-geono-vertex.md#properties)</sub>

### neighbors_face_count

> _type_: **Integer**
>

> Socket 'Face Count' of node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](macro-geono-vertex.md#vertex) :black_small_square: [Content](macro-geono-vertex.md#content) :black_small_square: [Properties](macro-geono-vertex.md#properties)</sub>

### neighbors_vertex_count

> _type_: **Integer**
>

> Socket 'Vertex Count' of node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](macro-geono-vertex.md#vertex) :black_small_square: [Content](macro-geono-vertex.md#content) :black_small_square: [Properties](macro-geono-vertex.md#properties)</sub>

## Methods



----------
### corner_index()

> classmethod

``` python
corner_index(vertex_index=None, weights=None, sort_index=None)
```

> Node [Corners of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](macro-geono-vertex.md#vertex) :black_small_square: [Content](macro-geono-vertex.md#content) :black_small_square: [Methods](macro-geono-vertex.md#methods)</sub>

----------
### edge_index()

> classmethod

``` python
edge_index(vertex_index=None, weights=None, sort_index=None)
```

> Node [Edges of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](macro-geono-vertex.md#vertex) :black_small_square: [Content](macro-geono-vertex.md#content) :black_small_square: [Methods](macro-geono-vertex.md#methods)</sub>

----------
### edge_paths_to_curves()

> method

``` python
edge_paths_to_curves(next_vertex_index=None)
```

> Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_curves.html)

#### Arguments:
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](macro-geono-vertex.md#vertex) :black_small_square: [Content](macro-geono-vertex.md#content) :black_small_square: [Methods](macro-geono-vertex.md#methods)</sub>

----------
### paths_to_selection()

> method

``` python
paths_to_selection(next_vertex_index)
```

> Node [Edge Paths to Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_selection.html)

#### Arguments:
- **next_vertex_index** (_Integer_) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](macro-geono-vertex.md#vertex) :black_small_square: [Content](macro-geono-vertex.md#content) :black_small_square: [Methods](macro-geono-vertex.md#methods)</sub>