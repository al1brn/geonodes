# Edge

> Bases classes: [Domain](domain.md#domain)

``` python
Edge(geometry)
```

> Edge domain of a [Mesh](mesh.md#mesh)

#### Arguments:
- **geometry**

### Inherited

[accumulate_field](domain.md#accumulate_field) :black_small_square: [attribute_statistic](domain.md#attribute_statistic) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [capture](domain.md#capture) :black_small_square: [capture_attribute](domain.md#capture_attribute) :black_small_square: [captures](domain.md#captures) :black_small_square: [delete](domain.md#delete) :black_small_square: [delete_all](domain.md#delete_all) :black_small_square: [delete_edges_and_faces](domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](domain.md#delete_faces) :black_small_square: [delete_geometry](domain.md#delete_geometry) :black_small_square: [domain_name](domain.md#domain_name) :black_small_square: [duplicate_elements](domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](domain.md#exclude_corner) :black_small_square: [extrude](domain.md#extrude) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [id](geobase.md#id) :black_small_square: [\_\_init__](domain.md#__init__) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: [material](geobase.md#material) :black_small_square: [material_index](geobase.md#material_index) :black_small_square: [material_selection](geobase.md#material_selection) :black_small_square: [\_node](domain.md#_node) :black_small_square: [offset](geobase.md#offset) :black_small_square: [plural_domain](domain.md#plural_domain) :black_small_square: [position](geobase.md#position) :black_small_square: [proximity](domain.md#proximity) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [replace_material](geobase.md#replace_material) :black_small_square: [restrict_domain](domain.md#restrict_domain) :black_small_square: [sample_index](domain.md#sample_index) :black_small_square: [sample_nearest](domain.md#sample_nearest) :black_small_square: [\_sel](domain.md#_sel) :black_small_square: [separate](domain.md#separate) :black_small_square: [set_id](geobase.md#set_id) :black_small_square: [set_position](geobase.md#set_position) :black_small_square: [sort_elements](domain.md#sort_elements) :black_small_square: [split_to_instances](domain.md#split_to_instances) :black_small_square: [store](domain.md#store) :black_small_square: [store_named_attribute](domain.md#store_named_attribute) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [to_points](domain.md#to_points) :black_small_square: [viewer](domain.md#viewer) :black_small_square:

## Content

- **A** : [angle](edge.md#angle)
- **C** : [corner_index](edge.md#corner_index) :black_small_square: [count](edge.md#count)
- **N** : [neighbors](edge.md#neighbors)
- **P** : [paths_to_curves](edge.md#paths_to_curves) :black_small_square: [position_1](edge.md#position_1) :black_small_square: [position_2](edge.md#position_2)
- **S** : [scale](edge.md#scale) :black_small_square: [shortest_paths](edge.md#shortest_paths) :black_small_square: [signed_angle](edge.md#signed_angle) :black_small_square: [smooth](edge.md#smooth) :black_small_square: [split](edge.md#split)
- **T** : [to_face_groups](edge.md#to_face_groups)
- **U** : [unsigned_angle](edge.md#unsigned_angle)
- **V** : [vertex_index_1](edge.md#vertex_index_1) :black_small_square: [vertex_index_2](edge.md#vertex_index_2) :black_small_square: [vertices](edge.md#vertices)

## Properties



### angle

> _type_: **Node**
>

> Node [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_angle.html)

> [!IMPORTANT]
> This method return the node, use [unsigned_angle](edge.md#unsigned_angle) and [signed_angle](edge.md#signed_angle) to
> get directly the sockets

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### count

> _type_: **Integer**
>

> Socket 'Edge Count' of node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### neighbors

> _type_: **Integer**
>

> Neighbors read only property

- getter : [Edge Neighbors](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_neighbors.html)
- setter : None

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### position_1

> _type_: **Vector**
>

> Socket 'Position 1' of node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_vertices.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### position_2

> _type_: **Vector**
>

> Socket 'Position 2' of node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_vertices.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### signed_angle

> _type_: **Float**
>

> Socket 'Signed Angle' of node [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_angle.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### smooth

> _type_: **Boolean**
>

> Smooth property

- getter : node [Is Edge Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/is_edge_smooth.html)
- setter : node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_shade_smooth.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### to_face_groups

> _type_: **Integer**
>

> Node [Edges to Face Groups](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edges_to_face_groups.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### unsigned_angle

> _type_: **Float**
>

> Socket 'Unsigned Angle' of node [Edge Angle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_angle.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### vertex_index_1

> _type_: **Integer**
>

> Socket 'Vertex Index 1' of node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_vertices.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### vertex_index_2

> _type_: **Integer**
>

> Socket 'Vertex Index 2' of node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_vertices.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

### vertices

> _type_: **Node**
>

> Node [Edge Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_vertices.html)

:warning: returns the **node**, not a socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Properties](edge.md#properties)</sub>

## Methods



----------
### corner_index()

> classmethod

``` python
corner_index(edge_index=None, weights=None, sort_index=None)
```

> Node [Corners of Edge](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_edge.html)

#### Arguments:
- **edge_index** (_Integer_ = None) : socket 'Edge Index' (Edge Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### paths_to_curves()

> method

``` python
paths_to_curves(start_vertices=None, next_vertex_index=None)
```

> Node [Edge Paths to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_curves.html)



#### Arguments:
- **start_vertices** (_Boolean_ = None) : socket 'Start Vertices' (Start Vertices)
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### shortest_paths()

> method

``` python
shortest_paths(edge_cost=None)
```

> Node [Shortest Edge Paths](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/shortest_edge_paths.html)

#### Arguments:
- **edge_cost** (_Float_ = None) : socket 'Edge Cost' (Edge Cost)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>

----------
### split()

> method

``` python
split()
```

> Node [Split Edges](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/split_edges.html)



#### Returns:
- **Mesh** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Edge](edge.md#edge) :black_small_square: [Content](edge.md#content) :black_small_square: [Methods](edge.md#methods)</sub>