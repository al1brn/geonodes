# Vertex

> Bases classes: [Domain](domain.md#domain)

``` python
Vertex(geometry)
```

> Point domain of a [Mesh](mesh.md#mesh)

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](domain.md#accumulate_field) :black_small_square: [attribute_statistic](domain.md#attribute_statistic) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [captures](domain.md#captures) :black_small_square: [delete](domain.md#delete) :black_small_square: [delete_all](domain.md#delete_all) :black_small_square: [delete_edges_and_faces](domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](domain.md#delete_faces) :black_small_square: [delete_geometry](domain.md#delete_geometry) :black_small_square: [domain_name](domain.md#domain_name) :black_small_square: [duplicate_elements](domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](domain.md#exclude_corner) :black_small_square: [extrude](domain.md#extrude) :black_small_square: [for_each](domain.md#for_each) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [id](geobase.md#id) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [material](geobase.md#material) :black_small_square: [material_index](geobase.md#material_index) :black_small_square: [material_selection](geobase.md#material_selection) :black_small_square: [\_node](domain.md#_node) :black_small_square: [offset](geobase.md#offset) :black_small_square: [plural_domain](domain.md#plural_domain) :black_small_square: [position](geobase.md#position) :black_small_square: [proximity](domain.md#proximity) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [replace_material](geobase.md#replace_material) :black_small_square: [restrict_domain](domain.md#restrict_domain) :black_small_square: [sample_index](domain.md#sample_index) :black_small_square: [sample_nearest](domain.md#sample_nearest) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [separate](domain.md#separate) :black_small_square: [set_id](geobase.md#set_id) :black_small_square: [set_position](geobase.md#set_position) :black_small_square: [sort_elements](domain.md#sort_elements) :black_small_square: [split_to_instances](domain.md#split_to_instances) :black_small_square: [store](domain.md#store) :black_small_square: [store_named_attribute](domain.md#store_named_attribute) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [to_points](domain.md#to_points) :black_small_square: [viewer](domain.md#viewer) :black_small_square:

## Content

- [corner_index](vertex.md#corner_index)
- [count](vertex.md#count)
- [edge_index](vertex.md#edge_index)
- [edge_paths_to_curves](vertex.md#edge_paths_to_curves)
- [instance_on](vertex.md#instance_on)
- [neighbors](vertex.md#neighbors)
- [neighbors_face_count](vertex.md#neighbors_face_count)
- [neighbors_vertex_count](vertex.md#neighbors_vertex_count)
- [paths_to_selection](vertex.md#paths_to_selection)

## Properties



### count

> _type_: **Integer**
>

> Socket 'Point Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Properties](vertex.md#properties)</sub>

### neighbors

> _type_: **Node**
>

> Node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Properties](vertex.md#properties)</sub>

### neighbors_face_count

> _type_: **Integer**
>

> Socket 'Face Count' of node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Properties](vertex.md#properties)</sub>

### neighbors_vertex_count

> _type_: **Integer**
>

> Socket 'Vertex Count' of node [Vertex Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Properties](vertex.md#properties)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

----------
### instance_on()

> method

``` python
instance_on(instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

> Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)



#### Arguments:
- **instance** (_Geometry_ = None) : socket 'Instance' (Instance)
- **pick_instance** (_Boolean_ = None) : socket 'Pick Instance' (Pick Instance)
- **instance_index** (_Integer_ = None) : socket 'Instance Index' (Instance Index)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vertex](vertex.md#vertex) :black_small_square: [Content](vertex.md#content) :black_small_square: [Methods](vertex.md#methods)</sub>