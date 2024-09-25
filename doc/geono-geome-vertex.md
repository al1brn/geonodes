# Vertex

> Bases classes: [Point](geono-geome-point.md)

``` python
Vertex(geometry)
```



#### Arguments:
- **geometry**

### Inherited

[accumulate_field](geono-geome-domain.md#accumulate_field) :black_small_square: [attribute_statistic](geono-geome-domain.md#attribute_statistic) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [capture](geono-geome-domain.md#capture) :black_small_square: [capture_attribute](geono-geome-domain.md#capture_attribute) :black_small_square: [count](geono-geome-point.md#count) :black_small_square: [delete](geono-geome-domain.md#delete) :black_small_square: [delete_all](geono-geome-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](geono-geome-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](geono-geome-domain.md#delete_faces) :black_small_square: [delete_geometry](geono-geome-domain.md#delete_geometry) :black_small_square: [domain_name](geono-geome-domain.md#domain_name) :black_small_square: [duplicate_elements](geono-geome-domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](geono-geome-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](geono-geome-domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](geono-geome-domain.md#exclude_corner) :black_small_square: [extrude](geono-geome-domain.md#extrude) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [instance_on](geono-geome-point.md#instance_on) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [\_node](geono-geome-domain.md#_node) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [plural_domain](geono-geome-domain.md#plural_domain) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [proximity](geono-geome-domain.md#proximity) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [restrict_domain](geono-geome-domain.md#restrict_domain) :black_small_square: [sample_index](geono-geome-domain.md#sample_index) :black_small_square: [sample_nearest](geono-geome-domain.md#sample_nearest) :black_small_square: [\_sel](geono-geome-domain.md#_sel) :black_small_square: [separate](geono-geome-domain.md#separate) :black_small_square: [set_id](geono-geome-geobase.md#set_id) :black_small_square: [set_position](geono-geome-geobase.md#set_position) :black_small_square: [sort_elements](geono-geome-domain.md#sort_elements) :black_small_square: [split_to_instances](geono-geome-domain.md#split_to_instances) :black_small_square: [store](geono-geome-domain.md#store) :black_small_square: [store_named_attribute](geono-geome-domain.md#store_named_attribute) :black_small_square: [\_\_str__](geono-geome-domain.md#__str__) :black_small_square: [to_points](geono-geome-domain.md#to_points) :black_small_square: [viewer](geono-geome-domain.md#viewer) :black_small_square:

## Content

- [corner_index](geono-geome-vertex.md#corner_index)
- [edge_index](geono-geome-vertex.md#edge_index)
- [edge_paths_to_curves](geono-geome-vertex.md#edge_paths_to_curves)
- [neighbors](geono-geome-vertex.md#neighbors)
- [neighbors_face_count](geono-geome-vertex.md#neighbors_face_count)
- [neighbors_vertex_count](geono-geome-vertex.md#neighbors_vertex_count)
- [paths_to_selection](geono-geome-vertex.md#paths_to_selection)

## Properties



### neighbors

> _type_: **Node**
>

Node 'Vertex Neighbors' (GeometryNodeInputMeshVertexNeighbors)

[!Node] Vertex Neighbors

### neighbors_face_count

> _type_: **Integer**
>

Node 'Vertex Neighbors' (GeometryNodeInputMeshVertexNeighbors)

[!Node] Vertex Neighbors

### neighbors_vertex_count

> _type_: **Integer**
>

Node 'Vertex Neighbors' (GeometryNodeInputMeshVertexNeighbors)

[!Node] Vertex Neighbors

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#vertex) :black_small_square: [Content](#content) :black_small_square: [Vertex](geono-geome-vertex.md)</sub>

## Methods



----------
### corner_index()

> classmethod

``` python
corner_index(vertex_index=None, weights=None, sort_index=None)
```

Node 'Corners of Vertex' (GeometryNodeCornersOfVertex)

[!Node] Corners of Vertex

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#vertex) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-vertex.md#methods)</sub>

----------
### edge_index()

> classmethod

``` python
edge_index(vertex_index=None, weights=None, sort_index=None)
```

Node 'Edges of Vertex' (GeometryNodeEdgesOfVertex)

[!Node] Edges of Vertex

#### Arguments:
- **vertex_index** (_Integer_ = None) : socket 'Vertex Index' (Vertex Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#vertex) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-vertex.md#methods)</sub>

----------
### edge_paths_to_curves()

> method

``` python
edge_paths_to_curves(next_vertex_index=None)
```

Node 'Edge Paths to Curves' (GeometryNodeEdgePathsToCurves)

[!Node] Edge Paths to Curves

#### Arguments:
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Curve** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#vertex) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-vertex.md#methods)</sub>

----------
### paths_to_selection()

> method

``` python
paths_to_selection(next_vertex_index)
```

Node 'Edge Paths to Selection' (GeometryNodeEdgePathsToSelection)

[!Node] Edge Paths to Selection

#### Arguments:
- **next_vertex_index** (_Integer_) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Boolean** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#vertex) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-vertex.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#vertex) :black_small_square: [Content](#content) :black_small_square: [Vertex](geono-geome-vertex.md)</sub>