# Geometry

> Bases classes: [Socket](geono-socket.md#socket) :black_small_square: [GeoBase](geono-geobase.md#geobase)

``` python
Geometry(value=None, name=None, tip=None)
```

Socket of type 'GEOMETRY'.

If value is None, a Group Input socket of type Geometry is created.
When a Group Input socket is created, default name 'Geometry' is used if name argument is None.

``` python
geometry = Geometry() # Default group input geometry
geometry = Geometry(name="Mesh") # Input group geometry
```

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_geo_type](geono-geobase.md#_geo_type) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [\_\_getitem__](geono-geobase.md#__getitem__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [id](geono-geobase.md#id) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [material](geono-geobase.md#material) :black_small_square: [material_index](geono-geobase.md#material_index) :black_small_square: [material_selection](geono-geobase.md#material_selection) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [offset](geono-geobase.md#offset) :black_small_square: [out](geono-socket.md#out) :black_small_square: [position](geono-geobase.md#position) :black_small_square: [\_raw_sel](geono-geobase.md#_raw_sel) :black_small_square: [replace_material](geono-geobase.md#replace_material) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [\_sel](geono-geobase.md#_sel) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square:

## Content

- **B** : [bake](macro-geono-geometry.md#bake) :black_small_square: [bounding_box](macro-geono-geometry.md#bounding_box)
- **C** : [convex_hull](macro-geono-geometry.md#convex_hull) :black_small_square: [curve](macro-geono-geometry.md#curve)
- **I** : [index_of_nearest](macro-geono-geometry.md#index_of_nearest) :black_small_square: [instances](macro-geono-geometry.md#instances)
- **J** : [Join](macro-geono-geometry.md#join) :black_small_square: [join](macro-geono-geometry.md#join)
- **M** : [merge_by_distance](macro-geono-geometry.md#merge_by_distance) :black_small_square: [mesh](macro-geono-geometry.md#mesh)
- **P** : [point_cloud](macro-geono-geometry.md#point_cloud)
- **R** : [raycast](macro-geono-geometry.md#raycast) :black_small_square: [remove_named_attribute](macro-geono-geometry.md#remove_named_attribute)
- **S** : [separate_components](macro-geono-geometry.md#separate_components) :black_small_square: [set_id](macro-geono-geometry.md#set_id) :black_small_square: [set_material](macro-geono-geometry.md#set_material) :black_small_square: [set_position](macro-geono-geometry.md#set_position) :black_small_square: [set_shade_smooth](macro-geono-geometry.md#set_shade_smooth)
- **T** : [to_instance](macro-geono-geometry.md#to_instance) :black_small_square: [transform](macro-geono-geometry.md#transform)
- **V** : [viewer](macro-geono-geometry.md#viewer) :black_small_square: [volume](macro-geono-geometry.md#volume)

## Properties



### bounding_box

> _type_: **Mesh**
>

> Bounding box read only property

- getter : [Bounding Box](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/bounding_box.html)
- setter : None

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Properties](macro-geono-geometry.md#properties)</sub>

### convex_hull

> _type_: **Mesh**
>

> Convex hull read only property

- getter : [Convex Hull](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/convex_hull.html)
- setter : None

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Properties](macro-geono-geometry.md#properties)</sub>

### curve

> _type_: **Curve**
>

> Socket 'Curve' of node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Properties](macro-geono-geometry.md#properties)</sub>

### instances

> _type_: **Instances**
>

> Socket Instances of node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Properties](macro-geono-geometry.md#properties)</sub>

### mesh

> _type_: **Mesh**
>

> Socket 'Mesh' of node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Properties](macro-geono-geometry.md#properties)</sub>

### point_cloud

> _type_: **Cloud**
>

> Socket 'Point Cloud' of node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Properties](macro-geono-geometry.md#properties)</sub>

### separate_components

> _type_: **Node**
>

> Node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

> See [mesh](macro-geono-geometry.md#mesh), [curve](macro-geono-geometry.md#curve), [point_cloud](macro-geono-geometry.md#point_cloud), [instances](macro-geono-geometry.md#instances) and [volume](macro-geono-geometry.md#volume) properties

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Properties](macro-geono-geometry.md#properties)</sub>

### volume

> _type_: **Volume**
>

> Socket 'Volume' of node [Separate Components](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Properties](macro-geono-geometry.md#properties)</sub>

## Methods



----------
### bake()

> method

``` python
bake(**kwargs)
```

Node [Bake](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/bake.html)



#### Arguments:
- **kwargs**



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### index_of_nearest()

> staticmethod

``` python
index_of_nearest(position=None, group_id=None)
```

> Node ERROR: Node 'Index of Nearest' not found

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### Join()

> classmethod

``` python
Join(*geometries)
```

> Constructor node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)

Create a new geometry by joining the arguments geometry:

``` python
geo = Geometry.Join(Mesh.Cube(), Curve.Circle())
```

> See also [join](macro-geono-geometry.md#join) method

#### Arguments:
- **geometries**



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### join()

> method

``` python
join(*geometries)
```

> Node [Join Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html)



> [!IMPORTANT]
> 3 possibilities exist to join geometries
> - Constructur [Join](macro-geono-geometry.md#join) : create an new geometry from the input geometries
> - Operator '+' : create a new geometry from the operands
> - Method 'join' : join the input geometry to the calling geometry

``` python
a = Mesh.Cube()
b = Mesh.UVSphere()

# Constructor Join
c = Mesh.Join(a, b)

# Equivalent to
c = a + b

# Method join
# After the call, a is not anymore the cube but the result of the join operation
a.join(b)

# Equivalent to
a += b
```

#### Arguments:
- **geometries**



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### merge_by_distance()

> method

``` python
merge_by_distance(distance=None, mode='ALL')
```

> Node [Merge by Distance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html)



#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (Distance)
- **mode** (_str_ = ALL) : str in ('ALL', 'CONNECTED')



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### raycast()

> method

``` python
raycast(attribute=None, source_position=None, ray_direction=None, ray_length=None, interpolated=True)
```

> Node [Raycast](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html)

:warning: returns the **node**, not a socket

#### Arguments:
- **attribute** (_Float_ = None) : socket 'Attribute' (Attribute)
- **source_position** (_Vector_ = None) : socket 'Source Position' (Source Position)
- **ray_direction** (_Vector_ = None) : socket 'Ray Direction' (Ray Direction)
- **ray_length** (_Float_ = None) : socket 'Ray Length' (Ray Length)
- **interpolated** (_bool_ = True) : mapping = 'INTERPOLATED' if True, 'NEAREST' otherwise



#### Returns:
- **Node** : 'RayCast' node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### remove_named_attribute()

> method

``` python
remove_named_attribute(name, exact=True)
```

> Node [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)



#### Arguments:
- **name** (_String_) : socket
- **exact** (_Boolean_ = True) : pattern_mode = 'EXACT' if True else 'WILDCARD'



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### set_id()

> method

``` python
set_id(id=None)
```

> Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html)



#### Arguments:
- **id** (_Integer_ = None) : socket



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### set_material()

> method

``` python
set_material(material=None)
```

> Node [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)



#### Arguments:
- **material** (_Material_ = None) : socket



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### set_position()

> method

``` python
set_position(position=None, offset=None)
```

> Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html)



#### Arguments:
- **position** (_Vector_ = None) : socket
- **offset** ( = None)



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### set_shade_smooth()

> method

``` python
set_shade_smooth(shade_smooth=True, edge=False)
```

> Node [Set Shade Smooth](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_shade_smooth.html)



#### Arguments:
- **shade_smooth** (_Boolean_ = True) : socket
- **edge** ( = False)



#### Returns:
- **Geometry** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### to_instance()

> method

``` python
to_instance(*geometries)
```

> Node [Geometry to Instance](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)



#### Arguments:
- **geometries** (_Geometry_) : socket 'Geometry' (Geometry)



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### transform()

> method

``` python
transform(translation=None, rotation=None, scale=None, matrix=None)
```

> Node [Transform Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/transform_geometry.html)



> [!NOTE]
> - If **matrix** argument is None, the mode 'COMPONENTS' is set.
> - If **matrix** argument is not NOne, the mode 'MATRIX' is set and the other arguments are ignored.

#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)
- **matrix** (_Matrix_ = None) : socket 'Transform' (Transform)



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>

----------
### viewer()

> method

``` python
viewer(value=None)
```

> Node [Viewer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/output/viewer.html)

#### Arguments:
- **value** (_Socket_ = None) : socket



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Geometry](macro-geono-geometry.md#geometry) :black_small_square: [Content](macro-geono-geometry.md#content) :black_small_square: [Methods](macro-geono-geometry.md#methods)</sub>