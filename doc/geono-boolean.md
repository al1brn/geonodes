# Boolean

> Bases classes: [Socket](geono-socket.md#socket)

``` python
Boolean(value=False, name=None, tip=None, subtype='NONE')
```

Socket of type BOOLEAN

[Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../modifiers/generate/booleans.html)

#### Arguments:
- **value** (_bool or Socket_ = False) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **subtype** (_str_ = NONE) : socket subtype

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_output](geono-socket.md#to_output) :black_small_square:

## Content

- [Named](geono-boolean.md#named)
- [NamedAttribute](geono-boolean.md#namedattribute)
- [Random](geono-boolean.md#random)

## Methods



----------
### Named()

> classmethod

``` python
Named(name)
```

> **node** : [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)



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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](geono-boolean.md#boolean) :black_small_square: [Content](geono-boolean.md#content) :black_small_square: [Methods](geono-boolean.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name)
```

> **node** : [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)



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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](geono-boolean.md#boolean) :black_small_square: [Content](geono-boolean.md#content) :black_small_square: [Methods](geono-boolean.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(probability=None, id=None, seed=None)
```

Constructor : random Boolean.

[Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Arguments:
- **probability** (_Float_ = None)
- **id** (_Integer_ = None)
- **seed** (_Integer_ = None)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](geono-boolean.md#boolean) :black_small_square: [Content](geono-boolean.md#content) :black_small_square: [Methods](geono-boolean.md#methods)</sub>