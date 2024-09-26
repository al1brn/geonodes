# Cloud

> Bases classes: [Geometry](geono-geome-geometry.md#geometry)

``` python
Cloud(value=None, name=None, tip=None)
```

Socket of type 'GEOMETRY'.

If value is None, a Group Input socket of type Geometry is created.
When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_add__](geono-geome-geometry.md#__add__) :black_small_square: [bake](geono-geome-geometry.md#bake) :black_small_square: [blur](geono-socke-socket.md#blur) :black_small_square: [bounding_box](geono-geome-geometry.md#bounding_box) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [convex_hull](geono-geome-geometry.md#convex_hull) :black_small_square: [curve](geono-geome-geometry.md#curve) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_geo](geono-geome-geometry.md#_geo) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [index_of_nearest](geono-geome-geometry.md#index_of_nearest) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [instances](geono-geome-geometry.md#instances) :black_small_square: [join](geono-geome-geometry.md#join) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [merge_by_distance](geono-geome-geometry.md#merge_by_distance) :black_small_square: [mesh](geono-geome-geometry.md#mesh) :black_small_square: [\_node](geono-geome-geometry.md#_node) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [point_cloud](geono-geome-geometry.md#point_cloud) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [raycast](geono-geome-geometry.md#raycast) :black_small_square: [remove_named_attribute](geono-geome-geometry.md#remove_named_attribute) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [\_sel](geono-geome-geobase.md#_sel) :black_small_square: [separate_components](geono-geome-geometry.md#separate_components) :black_small_square: [set_id](geono-geome-geometry.md#set_id) :black_small_square: [set_material](geono-geome-geometry.md#set_material) :black_small_square: [set_position](geono-geome-geometry.md#set_position) :black_small_square: [set_shade_smooth](geono-geome-geometry.md#set_shade_smooth) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square: [to_instance](geono-geome-geometry.md#to_instance) :black_small_square: [to_output](geono-socke-socket.md#to_output) :black_small_square: [transform](geono-geome-geometry.md#transform) :black_small_square: [viewer](geono-geome-geometry.md#viewer) :black_small_square: [volume](geono-geome-geometry.md#volume) :black_small_square:

## Content

- [FromCurve](geono-geome-cloud.md#fromcurve)
- [FromInstances](geono-geome-cloud.md#frominstances)
- [FromMesh](geono-geome-cloud.md#frommesh)
- [Points](geono-geome-cloud.md#points)
- [to_curves](geono-geome-cloud.md#to_curves)
- [to_vertices](geono-geome-cloud.md#to_vertices)
- [to_volume](geono-geome-cloud.md#to_volume)

## Methods



----------
### FromCurve()

> classmethod

``` python
FromCurve(curve, count=None, length=None, mode='COUNT')
```

Node 'Curve to Points' (GeometryNodeCurveToPoints)

[!Node] Curve to Points

#### Arguments:
- **curve** (_Geometry_) : socket 'Curve' (Curve)
- **count** (_Integer_ = None) : socket 'Count' (Count)
- **length** ( = None)
- **mode** (_str_ = COUNT) : Node.mode in ('EVALUATED', 'COUNT', 'LENGTH')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](geono-geome-cloud.md#cloud) :black_small_square: [Content](geono-geome-cloud.md#content) :black_small_square: [Methods](geono-geome-cloud.md#methods)</sub>

----------
### FromInstances()

> classmethod

``` python
FromInstances(instances, position=None, radius=None)
```

Node 'Instances to Points' (GeometryNodeInstancesToPoints)

[!Node] Instances to Points

#### Arguments:
- **instances** (_Geometry_) : socket 'Instances' (Instances)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](geono-geome-cloud.md#cloud) :black_small_square: [Content](geono-geome-cloud.md#content) :black_small_square: [Methods](geono-geome-cloud.md#methods)</sub>

----------
### FromMesh()

> classmethod

``` python
FromMesh(mesh, position=None, radius=None, mode='POINTS')
```

Node 'Mesh to Points' (GeometryNodeMeshToPoints)

[!Node] Mesh to Points

#### Arguments:
- **mesh** (_Mesh_) : socket 'Mesh' (Mesh)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **mode** (_str_ = POINTS) : Node.mode in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](geono-geome-cloud.md#cloud) :black_small_square: [Content](geono-geome-cloud.md#content) :black_small_square: [Methods](geono-geome-cloud.md#methods)</sub>

----------
### Points()

> classmethod

``` python
Points(count=1, position=None, radius=None)
```

Node 'Points' (GeometryNodePoints)

[!Node] Points

#### Arguments:
- **count** (_Integer_ = 1) : socket 'Count' (Count)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](geono-geome-cloud.md#cloud) :black_small_square: [Content](geono-geome-cloud.md#content) :black_small_square: [Methods](geono-geome-cloud.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(curve_group_id=None, weight=None)
```

Node 'Points to Curves' (GeometryNodePointsToCurves)

[!Node] Points to Curves

#### Arguments:
- **curve_group_id** (_Integer_ = None) : socket 'Curve Group ID' (Curve Group ID)
- **weight** (_Float_ = None) : socket 'Weight' (Weight)



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](geono-geome-cloud.md#cloud) :black_small_square: [Content](geono-geome-cloud.md#content) :black_small_square: [Methods](geono-geome-cloud.md#methods)</sub>

----------
### to_vertices()

> method

``` python
to_vertices()
```

Node 'Points to Vertices' (GeometryNodePointsToVertices)

[!Node] Points to Vertices

#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](geono-geome-cloud.md#cloud) :black_small_square: [Content](geono-geome-cloud.md#content) :black_small_square: [Methods](geono-geome-cloud.md#methods)</sub>

----------
### to_volume()

> method

``` python
to_volume(density=None, voxel_size=None, voxel_amount=None, radius=None, resolution_mode='VOXEL_AMOUNT')
```

Node 'Points to Volume' (GeometryNodePointsToVolume)

[!Node] Points to Volume

#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (Density)
- **voxel_size** ( = None)
- **voxel_amount** (_Float_ = None) : socket 'Voxel Amount' (Voxel Amount)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **resolution_mode** (_str_ = VOXEL_AMOUNT) : Node.resolution_mode in ('VOXEL_AMOUNT', 'VOXEL_SIZE')



#### Returns:
- **Volume** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Cloud](geono-geome-cloud.md#cloud) :black_small_square: [Content](geono-geome-cloud.md#content) :black_small_square: [Methods](geono-geome-cloud.md#methods)</sub>