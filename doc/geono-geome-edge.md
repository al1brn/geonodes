# Edge

> Bases classes: [Domain](geono-geome-domain.md)

``` python
Edge(geometry)
```



#### Arguments:
- **geometry**

### Inherited

[accumulate_field](geono-geome-domain.md#accumulate_field) :black_small_square: [attribute_statistic](geono-geome-domain.md#attribute_statistic) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [capture](geono-geome-domain.md#capture) :black_small_square: [capture_attribute](geono-geome-domain.md#capture_attribute) :black_small_square: [delete](geono-geome-domain.md#delete) :black_small_square: [delete_all](geono-geome-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](geono-geome-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](geono-geome-domain.md#delete_faces) :black_small_square: [delete_geometry](geono-geome-domain.md#delete_geometry) :black_small_square: [domain_name](geono-geome-domain.md#domain_name) :black_small_square: [duplicate_elements](geono-geome-domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](geono-geome-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](geono-geome-domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](geono-geome-domain.md#exclude_corner) :black_small_square: [extrude](geono-geome-domain.md#extrude) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [\_node](geono-geome-domain.md#_node) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [plural_domain](geono-geome-domain.md#plural_domain) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [proximity](geono-geome-domain.md#proximity) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [restrict_domain](geono-geome-domain.md#restrict_domain) :black_small_square: [sample_index](geono-geome-domain.md#sample_index) :black_small_square: [sample_nearest](geono-geome-domain.md#sample_nearest) :black_small_square: [\_sel](geono-geome-domain.md#_sel) :black_small_square: [separate](geono-geome-domain.md#separate) :black_small_square: [set_id](geono-geome-geobase.md#set_id) :black_small_square: [set_position](geono-geome-geobase.md#set_position) :black_small_square: [sort_elements](geono-geome-domain.md#sort_elements) :black_small_square: [split_to_instances](geono-geome-domain.md#split_to_instances) :black_small_square: [store](geono-geome-domain.md#store) :black_small_square: [store_named_attribute](geono-geome-domain.md#store_named_attribute) :black_small_square: [\_\_str__](geono-geome-domain.md#__str__) :black_small_square: [to_points](geono-geome-domain.md#to_points) :black_small_square: [viewer](geono-geome-domain.md#viewer) :black_small_square:

## Content

- **A** : [angle](geono-geome-edge.md#angle)
- **C** : [corner_index](geono-geome-edge.md#corner_index) :black_small_square: [count](geono-geome-edge.md#count)
- **N** : [neighbors](geono-geome-edge.md#neighbors)
- **P** : [paths_to_curves](geono-geome-edge.md#paths_to_curves) :black_small_square: [position_1](geono-geome-edge.md#position_1) :black_small_square: [position_2](geono-geome-edge.md#position_2)
- **S** : [scale](geono-geome-edge.md#scale) :black_small_square: [shortest_paths](geono-geome-edge.md#shortest_paths) :black_small_square: [signed_angle](geono-geome-edge.md#signed_angle) :black_small_square: [smooth](geono-geome-edge.md#smooth) :black_small_square: [split](geono-geome-edge.md#split)
- **T** : [to_face_groups](geono-geome-edge.md#to_face_groups)
- **U** : [unsigned_angle](geono-geome-edge.md#unsigned_angle)
- **V** : [vertex_index_1](geono-geome-edge.md#vertex_index_1) :black_small_square: [vertex_index_2](geono-geome-edge.md#vertex_index_2) :black_small_square: [vertices](geono-geome-edge.md#vertices)

## Properties



### angle

> _type_: **Node**
>

Node 'Edge Angle' (GeometryNodeInputMeshEdgeAngle)

[!Node] Edge Angle

### count

> _type_: **Integer**
>

Node 'Domain Size' (GeometryNodeAttributeDomainSize)

[!Node] Domain Size

Socket 'Edge Count' of node 'Domain Size'

### neighbors

> _type_: **Integer**
>

Node 'Edge Neighbors' (GeometryNodeInputMeshEdgeNeighbors)

[!Node] Edge Neighbors

### position_1

> _type_: **Vector**
>

Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

[!Node] Edge Vertices

### position_2

> _type_: **Vector**
>

Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

[!Node] Edge Vertices

### signed_angle

> _type_: **Float**
>

Node 'Edge Angle' (GeometryNodeInputMeshEdgeAngle)

[!Node] Edge Angle

### smooth

> _type_: **Boolean**
>

Node 'Is Edge Smooth' (GeometryNodeInputEdgeSmooth)

[!Node] Is Edge Smooth

### to_face_groups

> _type_: **Integer**
>

Node 'Edges to Face Groups' (GeometryNodeEdgesToFaceGroups)

[!Node] Edges to Face Groups

### unsigned_angle

> _type_: **Float**
>

Node 'Edge Angle' (GeometryNodeInputMeshEdgeAngle)

[!Node] Edge Angle

### vertex_index_1

> _type_: **Integer**
>

Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

[!Node] Edge Vertices

### vertex_index_2

> _type_: **Integer**
>

Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

[!Node] Edge Vertices

### vertices

> _type_: **Node**
>

Node 'Edge Vertices' (GeometryNodeInputMeshEdgeVertices)

[!Node] Edge Vertices

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#edge) :black_small_square: [Content](#content) :black_small_square: [Edge](geono-geome-edge.md)</sub>

## Methods



----------
### corner_index()

> classmethod

``` python
corner_index(edge_index=None, weights=None, sort_index=None)
```

Node 'Corners of Edge' (GeometryNodeCornersOfEdge)

[!Node] Corners of Edge

#### Arguments:
- **edge_index** (_Integer_ = None) : socket 'Edge Index' (Edge Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#edge) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-edge.md#methods)</sub>

----------
### paths_to_curves()

> method

``` python
paths_to_curves(start_vertices=None, next_vertex_index=None)
```

Node 'Edge Paths to Curves' (GeometryNodeEdgePathsToCurves)

[!Node] Edge Paths to Curves

#### Arguments:
- **start_vertices** (_Boolean_ = None) : socket 'Start Vertices' (Start Vertices)
- **next_vertex_index** (_Integer_ = None) : socket 'Next Vertex Index' (Next Vertex Index)



#### Returns:
- **Curve** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#edge) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-edge.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale=None, center=None, uniform=True)
```

Node 'Scale Elements' (GeometryNodeScaleElements)

[!Node] Scale Elements

- domain (str): Node.domain in ('FACE', 'EDGE')
- scale_mode (str): Node.scale_mode in ('UNIFORM', 'SINGLE_AXIS')

#### Arguments:
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **uniform** ( = True)



#### Returns:
- **Mesh** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#edge) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-edge.md#methods)</sub>

----------
### shortest_paths()

> method

``` python
shortest_paths(edge_cost=None)
```

Node 'Shortest Edge Paths' (GeometryNodeInputShortestEdgePaths)

[!Node] Shortest Edge Paths

#### Arguments:
- **edge_cost** (_Float_ = None) : socket 'Edge Cost' (Edge Cost)



#### Returns:
- **Integer** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#edge) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-edge.md#methods)</sub>

----------
### split()

> method

``` python
split()
```

Node 'Split Edges' (GeometryNodeSplitEdges)

[!Node] Split Edges

#### Returns:
- **Mesh** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#edge) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-geome-edge.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#edge) :black_small_square: [Content](#content) :black_small_square: [Edge](geono-geome-edge.md)</sub>