# Cloud

> Bases classes: [Geometry](geometry.md#geometry)

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

Nodes requiring a domain parameter, are implemented in the domain [points](cloud.md#points).

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geometry.md#__add__) :black_small_square: [bake](geometry.md#bake) :black_small_square: [blur](socket.md#blur) :black_small_square: [bounding_box](geometry.md#bounding_box) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [convex_hull](geometry.md#convex_hull) :black_small_square: [curve](geometry.md#curve) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geo](geometry.md#_geo) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_geo_type](geobase.md#_geo_type) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [\_\_getitem__](geobase.md#__getitem__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [id](geobase.md#id) :black_small_square: [index_of_nearest](geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](geometry.md#__init__) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [instances](geometry.md#instances) :black_small_square: [Join](geometry.md#join) :black_small_square: [join](geometry.md#join) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [material](geobase.md#material) :black_small_square: [material_index](geobase.md#material_index) :black_small_square: [material_selection](geobase.md#material_selection) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [merge_by_distance](geometry.md#merge_by_distance) :black_small_square: [mesh](geometry.md#mesh) :black_small_square: [\_node](geometry.md#_node) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [offset](geobase.md#offset) :black_small_square: [out](socket.md#out) :black_small_square: [point_cloud](geometry.md#point_cloud) :black_small_square: [position](geobase.md#position) :black_small_square: [\_raw_sel](geobase.md#_raw_sel) :black_small_square: [raycast](geometry.md#raycast) :black_small_square: [remove_named_attribute](geometry.md#remove_named_attribute) :black_small_square: [replace_material](geobase.md#replace_material) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_sel](geobase.md#_sel) :black_small_square: [separate_components](geometry.md#separate_components) :black_small_square: [set_id](geometry.md#set_id) :black_small_square: [set_material](geometry.md#set_material) :black_small_square: [set_position](geometry.md#set_position) :black_small_square: [set_shade_smooth](geometry.md#set_shade_smooth) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [to_instance](geometry.md#to_instance) :black_small_square: [transform](geometry.md#transform) :black_small_square: [viewer](geometry.md#viewer) :black_small_square: [volume](geometry.md#volume) :black_small_square:

## Content

- **D** : [domain_size](cloud.md#domain_size)
- **F** : [FromCorners](cloud.md#fromcorners) :black_small_square: [FromCurve](cloud.md#fromcurve) :black_small_square: [FromEdges](cloud.md#fromedges) :black_small_square: [FromFaces](cloud.md#fromfaces) :black_small_square: [FromInstances](cloud.md#frominstances) :black_small_square: [FromMesh](cloud.md#frommesh) :black_small_square: [FromVertices](cloud.md#fromvertices)
- **P** : [points](cloud.md#points) :black_small_square: [Points](cloud.md#points)
- **T** : [to_curves](cloud.md#to_curves) :black_small_square: [to_vertices](cloud.md#to_vertices) :black_small_square: [to_volume](cloud.md#to_volume)

## Properties



### domain_size

> _type_: **Node**
>

> Node ERROR: Node 'Size' not found, component = 'POINTCLOUD'

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Properties](cloud.md#properties)</sub>

### points

> _type_: **CloudPoint**
>

POINT domain

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Properties](cloud.md#properties)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

----------
### to_vertices()

> method

``` python
to_vertices()
```

> Node [Points to Vertices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](cloud.md#cloud) :black_small_square: [Content](cloud.md#content) :black_small_square: [Methods](cloud.md#methods)</sub>