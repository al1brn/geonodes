# Face

> Bases classes: [Domain](geono-geome-domain.md#domain)

``` python
Face(geometry)
```



#### Arguments:
- **geometry**

### Inherited

[accumulate_field](geono-geome-domain.md#accumulate_field) :black_small_square: [attribute_statistic](geono-geome-domain.md#attribute_statistic) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [capture](geono-geome-domain.md#capture) :black_small_square: [capture_attribute](geono-geome-domain.md#capture_attribute) :black_small_square: [delete](geono-geome-domain.md#delete) :black_small_square: [delete_all](geono-geome-domain.md#delete_all) :black_small_square: [delete_edges_and_faces](geono-geome-domain.md#delete_edges_and_faces) :black_small_square: [delete_faces](geono-geome-domain.md#delete_faces) :black_small_square: [delete_geometry](geono-geome-domain.md#delete_geometry) :black_small_square: [domain_name](geono-geome-domain.md#domain_name) :black_small_square: [duplicate_elements](geono-geome-domain.md#duplicate_elements) :black_small_square: [evaluate_at_index](geono-geome-domain.md#evaluate_at_index) :black_small_square: [evaluate_on_domain](geono-geome-domain.md#evaluate_on_domain) :black_small_square: [exclude_corner](geono-geome-domain.md#exclude_corner) :black_small_square: [extrude](geono-geome-domain.md#extrude) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [\_node](geono-geome-domain.md#_node) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [plural_domain](geono-geome-domain.md#plural_domain) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [proximity](geono-geome-domain.md#proximity) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [restrict_domain](geono-geome-domain.md#restrict_domain) :black_small_square: [sample_index](geono-geome-domain.md#sample_index) :black_small_square: [sample_nearest](geono-geome-domain.md#sample_nearest) :black_small_square: [\_sel](geono-geome-domain.md#_sel) :black_small_square: [separate](geono-geome-domain.md#separate) :black_small_square: [set_id](geono-geome-geobase.md#set_id) :black_small_square: [set_position](geono-geome-geobase.md#set_position) :black_small_square: [sort_elements](geono-geome-domain.md#sort_elements) :black_small_square: [split_to_instances](geono-geome-domain.md#split_to_instances) :black_small_square: [store](geono-geome-domain.md#store) :black_small_square: [store_named_attribute](geono-geome-domain.md#store_named_attribute) :black_small_square: [\_\_str__](geono-geome-domain.md#__str__) :black_small_square: [to_points](geono-geome-domain.md#to_points) :black_small_square: [viewer](geono-geome-domain.md#viewer) :black_small_square:

## Content

- **A** : [area](geono-geome-face.md#area)
- **C** : [corner_index](geono-geome-face.md#corner_index) :black_small_square: [count](geono-geome-face.md#count)
- **D** : [distribute_points](geono-geome-face.md#distribute_points)
- **F** : [flip](geono-geome-face.md#flip)
- **G** : [group_boundaries](geono-geome-face.md#group_boundaries)
- **I** : [is_planar](geono-geome-face.md#is_planar)
- **N** : [neighbors](geono-geome-face.md#neighbors) :black_small_square: [neighbors_face_count](geono-geome-face.md#neighbors_face_count) :black_small_square: [neighbors_vertex_count](geono-geome-face.md#neighbors_vertex_count)
- **S** : [scale](geono-geome-face.md#scale) :black_small_square: [smooth](geono-geome-face.md#smooth)

## Properties



### area

> _type_: **Float**
>

Node 'Face Area' (GeometryNodeInputMeshFaceArea)

[!Node] Face Area

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Properties](geono-geome-face.md#properties)</sub>

### count

> _type_: **Integer**
>

Node 'Domain Size' (GeometryNodeAttributeDomainSize)

[!Node] Domain Size

Socket 'Face Count' of node 'Domain Size'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Properties](geono-geome-face.md#properties)</sub>

### neighbors

> _type_: **Node**
>

Node 'Face Neighbors' (GeometryNodeInputMeshFaceNeighbors)

[!Node] Face Neighbors

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Properties](geono-geome-face.md#properties)</sub>

### neighbors_face_count

> _type_: **Integer**
>

Node 'Face Neighbors' (GeometryNodeInputMeshVertexNeighbors)

[!Node] Face Neighbors

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Properties](geono-geome-face.md#properties)</sub>

### neighbors_vertex_count

> _type_: **Integer**
>

Node 'Face Neighbors' (GeometryNodeInputMeshVertexNeighbors)

[!Node] Face Neighbors

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Properties](geono-geome-face.md#properties)</sub>

### smooth

> _type_: **Boolean**
>

Node 'Is Face Smooth' (GeometryNodeInputShadeSmooth)

[!Node] Is Face Smooth

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Properties](geono-geome-face.md#properties)</sub>

## Methods



----------
### corner_index()

> classmethod

``` python
corner_index(face_index=None, weights=None, sort_index=None)
```

Node 'Corners of Face' (GeometryNodeCornersOfFace)

[!Node] Corners of Face

#### Arguments:
- **face_index** (_Integer_ = None) : socket 'Face Index' (Face Index)
- **weights** (_Float_ = None) : socket 'Weights' (Weights)
- **sort_index** (_Integer_ = None) : socket 'Sort Index' (Sort Index)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Methods](geono-geome-face.md#methods)</sub>

----------
### distribute_points()

> method

``` python
distribute_points(density=None, distance_min=None, density_max=None, density_factor=None, seed=None)
```

Node 'Distribute Points on Faces' (GeometryNodeDistributePointsOnFaces)

[!Node] Distribute Points on Faces

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
- **Points** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Methods](geono-geome-face.md#methods)</sub>

----------
### flip()

> method

``` python
flip()
```

Node 'Flip Faces' (GeometryNodeFlipFaces)

[!Node] Flip Faces

#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Methods](geono-geome-face.md#methods)</sub>

----------
### group_boundaries()

> method

``` python
group_boundaries(face_group_id=None)
```

Node 'Face Group Boundaries' (GeometryNodeMeshFaceSetBoundaries)

[!Node] Face Group Boundaries

#### Arguments:
- **face_group_id** (_Integer_ = None) : socket 'Face Group ID' (Face Set)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Methods](geono-geome-face.md#methods)</sub>

----------
### is_planar()

> method

``` python
is_planar(threshold=None)
```

Node 'Is Face Planar' (GeometryNodeInputMeshFaceIsPlanar)

[!Node] Is Face Planar

#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (Threshold)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Methods](geono-geome-face.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Face](geono-geome-face.md#face) :black_small_square: [Content](geono-geome-face.md#content) :black_small_square: [Methods](geono-geome-face.md#methods)</sub>