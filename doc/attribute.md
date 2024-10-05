# Attribute

> Bases classes: [Socket](socket.md#socket)

``` python
Attribute(socket)
```

Attribute Socket

Attribute socket is class root for sockets which can be used in nodes managing attributes
such as [Named Attribute](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../modeling/geometry_nodes/geometry/read/named_attribute.html) :
- [Boolean](boolean.md#boolean)
- [Integer](integer.md#integer)
- [Float](float.md#float)
- [Vector](vector.md#vector)
- [Color](color.md#color)
- [Matrix](matrix.md#matrix)
- [Rotation](rotation.md#rotation)

#### Arguments:
- **socket** (_NodeSocket_) : the output socket to wrap

### Inherited

[blur](socket.md#blur) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [\_\_init__](socket.md#__init__) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square:

## Content

- [Named](attribute.md#named)
- [NamedAttribute](attribute.md#namedattribute)

## Methods



----------
### Named()

> classmethod

``` python
Named(name)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

'Named' is a synonym of 'NamedAttribute'

``` python
with GeoNodes("Named Attributes"):

    cube = Mesh.Cube()

    # Create a named attribute
    cube.points.store("Some Value", Float.Random(0, 1, seed=0))

    # Read the random value to offset along z
    cube.points.offset = (0, 0, Float.Named("Some Value"))

    # Remove the named attribute
    cube.remove_named_attribute("Some*", exact=False)

    cube.out()
```

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Attribute](attribute.md#attribute) :black_small_square: [Content](attribute.md#content) :black_small_square: [Methods](attribute.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

'Named' is a synonym of 'NamedAttribute'

``` python
with GeoNodes("Named Attributes"):

    cube = Mesh.Cube()

    # Create a named attribute
    cube.points.store("Some Value", Float.Random(0, 1, seed=0))

    # Read the random value to offset along z
    cube.points.offset = (0, 0, Float.NamedAttribute("Some Value"))

    # Remove the named attribute
    cube.remove_named_attribute("Some*", exact=False)

    cube.out()
```

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Attribute](attribute.md#attribute) :black_small_square: [Content](attribute.md#content) :black_small_square: [Methods](attribute.md#methods)</sub>