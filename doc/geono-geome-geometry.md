# Geometry

> Bases classes: [Socket](geono-socke-socket.md#socket) :black_small_square: [GeoBase](geono-geome-geobase.md#geobase)

``` python
Geometry(value=None, name=None, tip=None)
```

Geometry Class

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[blur](geono-socke-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_geo_type](geono-geome-geobase.md#_geo_type) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [\_\_getitem__](geono-geome-geobase.md#__getitem__) :black_small_square: [id](geono-geome-geobase.md#id) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [material](geono-geome-geobase.md#material) :black_small_square: [material_index](geono-geome-geobase.md#material_index) :black_small_square: [material_selection](geono-geome-geobase.md#material_selection) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [offset](geono-geome-geobase.md#offset) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [position](geono-geome-geobase.md#position) :black_small_square: [\_raw_sel](geono-geome-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geome-geobase.md#replace_material) :black_small_square: [\_reset](geono-socke-socket.md#_reset) :black_small_square: [\_sel](geono-geome-geobase.md#_sel) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square: [to_output](geono-socke-socket.md#to_output) :black_small_square:

## Content

- **B** : [bounding_box](geono-geome-geometry.md#bounding_box)
- **C** : [convex_hull](geono-geome-geometry.md#convex_hull) :black_small_square: [curve](geono-geome-geometry.md#curve)
- **I** : [index_of_nearest](geono-geome-geometry.md#index_of_nearest) :black_small_square: [instances](geono-geome-geometry.md#instances)
- **J** : [join](geono-geome-geometry.md#join)
- **M** : [merge_by_distance](geono-geome-geometry.md#merge_by_distance) :black_small_square: [mesh](geono-geome-geometry.md#mesh)
- **P** : [point_cloud](geono-geome-geometry.md#point_cloud)
- **R** : [raycast](geono-geome-geometry.md#raycast) :black_small_square: [remove_named_attribute](geono-geome-geometry.md#remove_named_attribute)
- **S** : [separate_components](geono-geome-geometry.md#separate_components) :black_small_square: [set_id](geono-geome-geometry.md#set_id) :black_small_square: [set_material](geono-geome-geometry.md#set_material) :black_small_square: [set_position](geono-geome-geometry.md#set_position) :black_small_square: [set_shade_smooth](geono-geome-geometry.md#set_shade_smooth)
- **T** : [to_instance](geono-geome-geometry.md#to_instance) :black_small_square: [transform](geono-geome-geometry.md#transform)
- **V** : [viewer](geono-geome-geometry.md#viewer) :black_small_square: [volume](geono-geome-geometry.md#volume)

## Properties



### bounding_box

> _type_: **Mesh**
>

Property node 'Bounding Box' (GeometryNodeBoundBox)

[!Node] Bounding Box

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Properties](geono-geome-geometry.md#properties)</sub>

### convex_hull

> _type_: **convex_hull**
>

Property node 'Convex Hull' (GeometryNodeConvexHull)

[!Node] Convex Hull

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Properties](geono-geome-geometry.md#properties)</sub>

### curve

> _type_: **Curve**
>

Property curve component

[!Node] Separate Components

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Properties](geono-geome-geometry.md#properties)</sub>

### instances

> _type_: **Instances**
>

Property instances component

[!Node] Separate Components

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Properties](geono-geome-geometry.md#properties)</sub>

### mesh

> _type_: **Mesh**
>

Property mesh component

[!Node] Separate Components

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Properties](geono-geome-geometry.md#properties)</sub>

### point_cloud

> _type_: **Cloud**
>

Property cloud component

[!Node] Separate Components

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Properties](geono-geome-geometry.md#properties)</sub>

### separate_components

> _type_: **Node**
>

Property node 'Separate Components' (GeometryNodeSeparateComponents)

[!Node] Separate Components

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Properties](geono-geome-geometry.md#properties)</sub>

### volume

> _type_: **Volume**
>

Property volume component

[!Node] Separate Components

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Properties](geono-geome-geometry.md#properties)</sub>

## Methods



----------
### index_of_nearest()

> staticmethod

``` python
index_of_nearest(position=None, group_id=None)
```

Node 'Index of Nearest' (GeometryNodeIndexOfNearest)

[!Node] Index of Nearest

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### join()

> method

``` python
join(*geometries)
```

Node 'Join Geometry' (GeometryNodeJoinGeometry)

[!Node] Join Geometry

Operator + can be used : ``` geo + other_geo ``` is equivalent to ``` geo.join(other) ```
If all the geometries are of the same type, the returned geometry uses this type.

``` python
cube = Mesh.Cube()
cone = Mesh.Cone()
circle = Curve.Circle()

# Returns Mesh
mesh = cube.join(cone)
assert(isinstance(mesh, Mesh))

# Returns Geometry
geo = mesh + circle
assert(isinstance(geo, Geometry))
```

#### Arguments:
- **geometries**



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### merge_by_distance()

> method

``` python
merge_by_distance(distance=None, mode='ALL')
```

Node 'Merge by Distance' (GeometryNodeMergeByDistance)

[!Node] Merge by Distance

#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (Distance)
- **mode** (_str_ = ALL) : str in ('ALL', 'CONNECTED')



#### Returns:
- **geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### raycast()

> method

``` python
raycast(attribute=None, source_position=None, ray_direction=None, ray_length=None, interpolated=True)
```

Node 'Raycast' (GeometryNodeRaycast)

[!Node] Raycast

mapping in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (Attribute)
- **source_position** (_Vector_ = None) : socket 'Source Position' (Source Position)
- **ray_direction** (_Vector_ = None) : socket 'Ray Direction' (Ray Direction)
- **ray_length** (_Float_ = None) : socket 'Ray Length' (Ray Length)
- **interpolated** (_bool_ = True) : mapping = 'INTERPOLATED' if True, 'NEAREST' otherwise



#### Returns:
- **Node** : [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### remove_named_attribute()

> method

``` python
remove_named_attribute(name, exact=True)
```

Remove named attribute

[!Node] Remove Named Attribute

#### Arguments:
- **name** (_String_) : socket
- **exact** (_Boolean_ = True) : pattern_mode = 'EXACT' if True else 'WILDCARD'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### set_id()

> method

``` python
set_id(id=None)
```

Set ID.

[!Node] Set ID

#### Arguments:
- **id** (_Integer_ = None) : socket



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### set_material()

> method

``` python
set_material(material=None)
```

Set Material.

[!Node] Set Material

#### Arguments:
- **material** (_Material_ = None) : socket



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### set_position()

> method

``` python
set_position(position=None, offset=None)
```

Set Position.

[!Node] Set Position

#### Arguments:
- **position** (_Vector_ = None) : socket
- **offset** ( = None)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### set_shade_smooth()

> method

``` python
set_shade_smooth(shade_smooth=True, edge=False)
```

Set Shade Smooth.

[!Node] Set Shade Smooth

#### Arguments:
- **shade_smooth** (_Boolean_ = True) : socket
- **edge** ( = False)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### to_instance()

> method

``` python
to_instance(*geometries)
```

Node 'Geometry to Instance' (GeometryNodeGeometryToInstance)

[!Node] Geometry to Instance

#### Arguments:
- **geometries** (_Geometry_) : socket 'Geometry' (Geometry)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### transform()

> method

``` python
transform(translation=None, rotation=None, scale=None, matrix=None)
```

Node 'Transform Geometry' (GeometryNodeTransform)

[!Node] Transform Geometry

If 'matrix' argument is None, the mode 'COMPONENTS' is set.
If 'matrix' argument is not NOne, the mode 'MATRIX' is set and the other arguments are ignored.

#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)
- **matrix** (_Matrix_ = None) : socket 'Transform' (Transform)



#### Returns:
- **geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>

----------
### viewer()

> method

``` python
viewer(value=None)
```

Create a viewer node.

[!Node] Viewer

#### Arguments:
- **value** (_Socket_ = None) : socket



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geome-geometry.md#geometry) :black_small_square: [Content](geono-geome-geometry.md#content) :black_small_square: [Methods](geono-geome-geometry.md#methods)</sub>