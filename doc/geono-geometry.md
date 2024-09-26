# Geometry

> Bases classes: [Socket](geono-socket.md#socket)

``` python
Geometry(value=None, name=None, tip=None)
```

Geometry Class

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_output](geono-socket.md#to_output) :black_small_square:

## Content

- **B** : [bounding_box](geono-geometry.md#bounding_box)
- **C** : [convex_hull](geono-geometry.md#convex_hull) :black_small_square: [curve](geono-geometry.md#curve)
- **I** : [id](geono-geometry.md#id) :black_small_square: [index_of_nearest](geono-geometry.md#index_of_nearest) :black_small_square: [instances](geono-geometry.md#instances)
- **J** : [join](geono-geometry.md#join)
- **M** : [material_index](geono-geometry.md#material_index) :black_small_square: [merge_by_distance](geono-geometry.md#merge_by_distance) :black_small_square: [mesh](geono-geometry.md#mesh)
- **P** : [point_cloud](geono-geometry.md#point_cloud) :black_small_square: [position](geono-geometry.md#position)
- **R** : [raycast](geono-geometry.md#raycast) :black_small_square: [remove_named_attribute](geono-geometry.md#remove_named_attribute) :black_small_square: [replace_material](geono-geometry.md#replace_material)
- **S** : [separate_components](geono-geometry.md#separate_components) :black_small_square: [set_id](geono-geometry.md#set_id) :black_small_square: [set_material](geono-geometry.md#set_material) :black_small_square: [set_position](geono-geometry.md#set_position) :black_small_square: [set_shade_smooth](geono-geometry.md#set_shade_smooth)
- **T** : [to_instance](geono-geometry.md#to_instance) :black_small_square: [transform](geono-geometry.md#transform)
- **V** : [viewer](geono-geometry.md#viewer) :black_small_square: [volume](geono-geometry.md#volume)

## Properties



### bounding_box

> _type_: **Mesh**
>

Property node 'Bounding Box' (GeometryNodeBoundBox)

ERROR: Node 'Bounding Box' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### convex_hull

> _type_: **convex_hull**
>

Property node 'Convex Hull' (GeometryNodeConvexHull)

[Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../meshes/editing/mesh/convex_hull.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### curve

> _type_: **Curve**
>

Property curve component

ERROR: Node 'Separate Components' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### id

> _type_: **Integer**
>

ERROR: Node 'ID' not found

ERROR: Node 'ID' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### instances

> _type_: **Instances**
>

Property instances component

ERROR: Node 'Separate Components' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### material_index

> _type_: **Integer**
>

ERROR: Node 'Material Index' not found

ERROR: Node 'Material Index' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### mesh

> _type_: **Mesh**
>

Property mesh component

ERROR: Node 'Separate Components' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### point_cloud

> _type_: **Cloud**
>

Property cloud component

ERROR: Node 'Separate Components' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### position

> _type_: **Vector**
>

ERROR: Node 'Position' not found

ERROR: Node 'Position' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### separate_components

> _type_: **Node**
>

Property node 'Separate Components' (GeometryNodeSeparateComponents)

ERROR: Node 'Separate Components' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

### volume

> _type_: **Volume**
>

Property volume component

ERROR: Node 'Separate Components' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Properties](geono-geometry.md#properties)</sub>

## Methods



----------
### index_of_nearest()

> staticmethod

``` python
index_of_nearest(position=None, group_id=None)
```

[Index of Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/index_of_nearest.html)

[Index of Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/index_of_nearest.html)

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### join()

> method

``` python
join(*geometries)
```

ERROR: Node 'Join Geometry' not found

ERROR: Node 'Join Geometry' not found

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### merge_by_distance()

> method

``` python
merge_by_distance(distance=None, mode='ALL')
```

ERROR: Node 'Merge by Distance' not found

ERROR: Node 'Merge by Distance' not found

#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (Distance)
- **mode** (_str_ = ALL) : str in ('ALL', 'CONNECTED')



#### Returns:
- **geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### raycast()

> method

``` python
raycast(attribute=None, source_position=None, ray_direction=None, ray_length=None, interpolated=True)
```

ERROR: Node 'Raycast' not found

ERROR: Node 'Raycast' not found

mapping in ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN', 'QUATERNION', 'FLOAT4X4')

#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (Attribute)
- **source_position** (_Vector_ = None) : socket 'Source Position' (Source Position)
- **ray_direction** (_Vector_ = None) : socket 'Ray Direction' (Ray Direction)
- **ray_length** (_Float_ = None) : socket 'Ray Length' (Ray Length)
- **interpolated** (_bool_ = True) : mapping = 'INTERPOLATED' if True, 'NEAREST' otherwise



#### Returns:
- **Node** : [is_hit (Boolean), hit_position (Vector), hit_normal (Vector), hit_distance (Float), attribute (Float)]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### remove_named_attribute()

> method

``` python
remove_named_attribute(name, exact=True)
```

Remove named attribute

ERROR: Node 'Remove Named Attribute' not found

#### Arguments:
- **name** (_String_) : socket
- **exact** (_Boolean_ = True) : pattern_mode = 'EXACT' if True else 'WILDCARD'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### replace_material()

> method

``` python
replace_material(old=None, new=None)
```

ERROR: Node 'Replace Material' not found

ERROR: Node 'Replace Material' not found

#### Arguments:
- **old** (_Material_ = None) : socket 'Old' (Old)
- **new** (_Material_ = None) : socket 'New' (New)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### set_id()

> method

``` python
set_id(id=None)
```

Set ID.

ERROR: Node 'Set ID' not found

#### Arguments:
- **id** (_Integer_ = None) : socket



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### set_material()

> method

``` python
set_material(material=None)
```

Set Material.

ERROR: Node 'Set Material' not found

#### Arguments:
- **material** (_Material_ = None) : socket



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### set_position()

> method

``` python
set_position(position=None, offset=None)
```

Set Position.

ERROR: Node 'Set Position' not found

#### Arguments:
- **position** (_Vector_ = None) : socket
- **offset** ( = None)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### set_shade_smooth()

> method

``` python
set_shade_smooth(shade_smooth=True, edge=False)
```

Set Shade Smooth.

ERROR: Node 'Set Shade Smooth' not found

#### Arguments:
- **shade_smooth** (_Boolean_ = True) : socket
- **edge** ( = False)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### to_instance()

> method

``` python
to_instance(*geometries)
```

ERROR: Node 'Geometry to Instance' not found

ERROR: Node 'Geometry to Instance' not found

#### Arguments:
- **geometries** (_Geometry_) : socket 'Geometry' (Geometry)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### transform()

> method

``` python
transform(translation=None, rotation=None, scale=None, matrix=None)
```

ERROR: Node 'Transform Geometry' not found

ERROR: Node 'Transform Geometry' not found

If 'matrix' argument is None, the mode 'COMPONENTS' is set.
If 'matrix' argument is not NOne, the mode 'MATRIX' is set and the other arguments are ignored.

#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)
- **matrix** (_Matrix_ = None) : socket 'Transform' (Transform)



#### Returns:
- **geometry** (_Geometry_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>

----------
### viewer()

> method

``` python
viewer(value=None)
```

Create a viewer node.

ERROR: Node 'Viewer' not found

#### Arguments:
- **value** (_Socket_ = None) : socket



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](geono-geometry.md#geometry) :black_small_square: [Content](geono-geometry.md#content) :black_small_square: [Methods](geono-geometry.md#methods)</sub>