# Cloud

> Bases classes: [Geometry](geono-geometry.md#geometry)

``` python
Cloud(value=None, name=None, tip=None)
```

> Cloud of Points Geometry

> [!NOTE]
> In Blender, the name can vary between **Point Cloud** and **Points**.
> In GeoNodes, the geometry is named **Cloud**.

The **Cloud** exposes all methods specific to points cloud.
Since there is no ambiguity, the word **points** is omitted in the name of
the methods:

``` python
curves = cloud.to_curves() # Node 'Points to Curves'
```

Nodes requiring a domain parameter, are implemented in the domain [points](macro-geono-cloud.md#points).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geono-geometry.md#__add__) :black_small_square: [bake](geono-geometry.md#bake) :black_small_square: [blur](geono-socket.md#blur) :black_small_square: [bounding_box](geono-geometry.md#bounding_box) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [convex_hull](geono-geometry.md#convex_hull) :black_small_square: [curve](geono-geometry.md#curve) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geo](geono-geometry.md#_geo) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_geo_type](geono-geobase.md#_geo_type) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [\_\_getitem__](geono-geobase.md#__getitem__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [id](geono-geobase.md#id) :black_small_square: [index_of_nearest](geono-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [instances](geono-geometry.md#instances) :black_small_square: [Join](geono-geometry.md#join) :black_small_square: [join](geono-geometry.md#join) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [material](geono-geobase.md#material) :black_small_square: [material_index](geono-geobase.md#material_index) :black_small_square: [material_selection](geono-geobase.md#material_selection) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [merge_by_distance](geono-geometry.md#merge_by_distance) :black_small_square: [mesh](geono-geometry.md#mesh) :black_small_square: [\_node](geono-geometry.md#_node) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [offset](geono-geobase.md#offset) :black_small_square: [out](geono-socket.md#out) :black_small_square: [point_cloud](geono-geometry.md#point_cloud) :black_small_square: [position](geono-geobase.md#position) :black_small_square: [\_raw_sel](geono-geobase.md#_raw_sel) :black_small_square: [raycast](geono-geometry.md#raycast) :black_small_square: [remove_named_attribute](geono-geometry.md#remove_named_attribute) :black_small_square: [replace_material](geono-geobase.md#replace_material) :black_small_square: [\_sel](geono-geobase.md#_sel) :black_small_square: [separate_components](geono-geometry.md#separate_components) :black_small_square: [set_id](geono-geometry.md#set_id) :black_small_square: [set_material](geono-geometry.md#set_material) :black_small_square: [set_position](geono-geometry.md#set_position) :black_small_square: [set_shade_smooth](geono-geometry.md#set_shade_smooth) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_instance](geono-geometry.md#to_instance) :black_small_square: [transform](geono-geometry.md#transform) :black_small_square: [viewer](geono-geometry.md#viewer) :black_small_square: [volume](geono-geometry.md#volume) :black_small_square:

## Content

- **D** : [domain_size](macro-geono-cloud.md#domain_size)
- **F** : [FromCorners](macro-geono-cloud.md#fromcorners) :black_small_square: [FromCurve](macro-geono-cloud.md#fromcurve) :black_small_square: [FromEdges](macro-geono-cloud.md#fromedges) :black_small_square: [FromFaces](macro-geono-cloud.md#fromfaces) :black_small_square: [FromInstances](macro-geono-cloud.md#frominstances) :black_small_square: [FromMesh](macro-geono-cloud.md#frommesh) :black_small_square: [FromVertices](macro-geono-cloud.md#fromvertices)
- **P** : [points](macro-geono-cloud.md#points) :black_small_square: [Points](macro-geono-cloud.md#points)
- **T** : [to_curves](macro-geono-cloud.md#to_curves) :black_small_square: [to_vertices](macro-geono-cloud.md#to_vertices) :black_small_square: [to_volume](macro-geono-cloud.md#to_volume)

## Properties



### domain_size

> _type_: **Node**
>

> Node ERROR: Node 'Size' not found, component = 'POINTCLOUD'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Properties](macro-geono-cloud.md#properties)</sub>

### points

> _type_: **CloudPoint**
>

POINT domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Properties](macro-geono-cloud.md#properties)</sub>

## Methods



----------
### FromCorners()

> classmethod

``` python
FromCorners(mesh, position=None, radius=None)
```

> Constructor node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html), mode CORNERS

#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (Mesh)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### FromCurve()

> classmethod

``` python
FromCurve(curve, count=None, length=None, mode='COUNT')
```

> Constructor node [Curve to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html)

#### Arguments:
- **curve** (_Geometry_) : socket 'Curve' (Curve)
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **length** ( = None)
- **mode** (_str_ = COUNT) : Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### FromEdges()

> classmethod

``` python
FromEdges(mesh, position=None, radius=None)
```

> Constructor node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html), mode EDGES

#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (Mesh)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### FromFaces()

> classmethod

``` python
FromFaces(mesh, position=None, radius=None)
```

> Constructor node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html), mode FACES

#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (Mesh)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### FromInstances()

> classmethod

``` python
FromInstances(instances, position=None, radius=None)
```

> Constructor node [Instances to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html)

#### Arguments:
- **instances** (_Geometry_) : socket 'Instances' (Instances)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### FromMesh()

> classmethod

``` python
FromMesh(mesh, position=None, radius=None, mode='POINTS')
```

> Constructor node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html)

#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (Mesh)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **mode** (_str_ = POINTS) : Node.mode in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### FromVertices()

> classmethod

``` python
FromVertices(mesh, position=None, radius=None)
```

> Constructor node [Mesh to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html), mode VERTICES

#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (Mesh)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### Points()

> classmethod

``` python
Points(count=1, position=None, radius=None)
```

> Constructor node [Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html)

#### Arguments:
- **count** (_Integer_ = 1) : socket 'Count' (Count)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(curve_group_id=None, weight=None)
```

> Node [Points to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_curves.html)



#### Arguments:
- **curve_group_id** (_Integer_ = None) : socket 'Curve Group ID' (Curve Group ID)
- **weight** (_Float_ = None) : socket 'Weight' (Weight)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### to_vertices()

> method

``` python
to_vertices()
```

> Node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>

----------
### to_volume()

> method

``` python
to_volume(density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

> Node [Points to Volume](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html)



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_size** ( = None)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (Voxel Amount)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **resolution_mode** (_str_ = VOXEL_AMOUNT) : Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](macro-geono-cloud.md#cloud) :black_small_square: [Content](macro-geono-cloud.md#content) :black_small_square: [Methods](macro-geono-cloud.md#methods)</sub>