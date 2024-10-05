# Boolean

> Bases classes: [Attribute](attribute.md#attribute)

``` python
Boolean(value=False, name=None, tip=None, subtype='NONE')
```

Socket of type BOOLEAN

> Node [Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/boolean.html)

#### Arguments:
- **value** (_bool or Socket_ = False) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **subtype** (_str_ = NONE) : socket subtype

### Inherited

[blur](socket.md#blur) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [Named](attribute.md#named) :black_small_square: [NamedAttribute](attribute.md#namedattribute) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square:

## Content

- [\_\_init__](boolean.md#__init__)
- [Random](boolean.md#random)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(value=False, name=None, tip=None, subtype='NONE')
```

Socket of type BOOLEAN

> Node [Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/boolean.html)

#### Arguments:
- **value** (_bool or Socket_ = False) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **subtype** (_str_ = NONE) : socket subtype

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(probability=None, id=None, seed=None)
```

Constructor : random Boolean.

> Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Arguments:
- **probability** (_Float_ = None)
- **id** (_Integer_ = None)
- **seed** (_Integer_ = None)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>