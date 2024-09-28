# Vertex

> Bases classes: [Domain](geono-domain.md#domain)

``` python
Vertex(geometry)
```

> Point domain of a [Mesh](geono-mesh.md#mesh)

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](geono-domain.md#accumulate_field) :black_small_square: [attribute_statistic](geono-domain.md#attribute_statistic) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [capture](geono-domain.md#capture) :black_small_square: [capture_attribute](geono-domain.md#capture_attribute) :black_small_square: [delete](geono-domain.md#delete) :black_small_square: [delete_all](geono-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](geono-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](geono-domain.md#delete_faces) :black_small_square: [delete_geometry](geono-domain.md#delete_geometry) :black_small_square: [domain_name](geono-domain.md#domain_name) :black_small_square: [duplicate_elements](geono-domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](geono-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](geono-domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](geono-domain.md#exclude_corner) :black_small_square: [extrude](geono-domain.md#extrude) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [\_node](geono-domain.md#_node) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [plural_domain](geono-domain.md#plural_domain) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [proximity](geono-domain.md#proximity) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [restrict_domain](geono-domain.md#restrict_domain) :black_small_square: [sample_index](geono-domain.md#sample_index) :black_small_square: [sample_nearest](geono-domain.md#sample_nearest) :black_small_square: [\_sel](geono-domain.md#_sel) :black_small_square: [separate](geono-domain.md#separate) :black_small_square: [set_id](geono-geome-geobase.md#set_id) :black_small_square: [set_position](geono-geome-geobase.md#set_position) :black_small_square: [sort_elements](geono-domain.md#sort_elements) :black_small_square: [split_to_instances](geono-domain.md#split_to_instances) :black_small_square: [store](geono-domain.md#store) :black_small_square: [store_named_attribute](geono-domain.md#store_named_attribute) :black_small_square: [\_\_str__](geono-domain.md#__str__) :black_small_square: [to_points](geono-domain.md#to_points) :black_small_square: [viewer](geono-domain.md#viewer) :black_small_square:

## Content

- [corner_index](geono-vertex.md#corner_index)
- [count](geono-vertex.md#count)
- [edge_index](geono-vertex.md#edge_index)
- [edge_paths_to_curves](geono-vertex.md#edge_paths_to_curves)
- [instance_on](geono-vertex.md#instance_on)
- [neighbors](geono-vertex.md#neighbors)
- [neighbors_face_count](geono-vertex.md#neighbors_face_count)
- [neighbors_vertex_count](geono-vertex.md#neighbors_vertex_count)
- [paths_to_selection](geono-vertex.md#paths_to_selection)

## Properties



### count

> _type_: **Integer**
>



[Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

Socket 'Point Count' of node 'Domain Size'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](geono-vertex.md#vertex) :black_small_square: [Content](geono-vertex.md#content) :black_small_square: [Properties](geono-vertex.md#properties)</sub>

### neighbors

> _type_: **Node**
>



[Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](geono-vertex.md#vertex) :black_small_square: [Content](geono-vertex.md#content) :black_small_square: [Properties](geono-vertex.md#properties)</sub>

### neighbors_face_count

> _type_: **Integer**
>



[Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](geono-vertex.md#vertex) :black_small_square: [Content](geono-vertex.md#content) :black_small_square: [Properties](geono-vertex.md#properties)</sub>

### neighbors_vertex_count

> _type_: **Integer**
>



[Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](geono-vertex.md#vertex) :black_small_square: [Content](geono-vertex.md#content) :black_small_square: [Properties](geono-vertex.md#properties)</sub>

## Methods



----------
### corner_index()

> classmethod

``` python
corner_index(vertex_index=None, weights=None, sort_index=None)
```



[Corners of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](geono-vertex.md#vertex) :black_small_square: [Content](geono-vertex.md#content) :black_small_square: [Methods](geono-vertex.md#methods)</sub>

----------
### edge_index()

> classmethod

``` python
edge_index(vertex_index=None, weights=None, sort_index=None)
```



[Edges of Vertex](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_vertex.html)

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](geono-vertex.md#vertex) :black_small_square: [Content](geono-vertex.md#content) :black_small_square: [Methods](geono-vertex.md#methods)</sub>

----------
### edge_paths_to_curves()

> method

``` python
edge_paths_to_curves(next_vertex_index=None)
```



[Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_curves.html)

#### Arguments:
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](geono-vertex.md#vertex) :black_small_square: [Content](geono-vertex.md#content) :black_small_square: [Methods](geono-vertex.md#methods)</sub>

----------
### instance_on()

> method

``` python
instance_on(instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```



[Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)

#### Arguments:
- **instance** (_Geometry_ = None) : socket 'Instance' (Instance)
- **pick_instance** (_Boolean_ = None) : socket 'Pick Instance' (Pick Instance)
- **instance_index** (_Integer_ = None) : socket 'Instance Index' (Instance Index)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)



#### Returns:
- **instances** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](geono-vertex.md#vertex) :black_small_square: [Content](geono-vertex.md#content) :black_small_square: [Methods](geono-vertex.md#methods)</sub>

----------
### paths_to_selection()

> method

``` python
paths_to_selection(next_vertex_index)
```



[Edge Paths to Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_selection.html)

#### Arguments:
- **next_vertex_index** (_Integer_) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](geono-vertex.md#vertex) :black_small_square: [Content](geono-vertex.md#content) :black_small_square: [Methods](geono-vertex.md#methods)</sub>