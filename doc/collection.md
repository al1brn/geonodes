# Collection

> Bases classes: [Socket](socket.md#socket)

``` python
Collection(value=None, name=None, tip=None)
```

Class Collection data socket

#### Arguments:
- **value** (_bpy.types.Object or str_ = None) : collection or collection name in bpy.data.collections
- **name** (_str_ = None) : create a group input socket of type Collection if not None
- **tip** (_str_ = None) : user tip for group input socket

### Inherited

[blur](socket.md#blur) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square:

## Content

- [Info](collection.md#info)
- [info](collection.md#info)
- [\_\_init__](collection.md#__init__)

## Methods



----------
### Info()

> classmethod

``` python
Info(collection=None, separate_children=None, reset_children=None, original=True)
```

> Node [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/collection_info.html)

#### Arguments:
- **collection** (_Collection_ = None) : socket 'Collection' (Collection)
- **separate_children** (_Boolean_ = None) : socket 'Separate Children' (Separate Children)
- **reset_children** (_Boolean_ = None) : socket 'Reset Children' (Reset Children)
- **original** (_bool_ = True) : Node.transform_space = 'ORIGINAL' if True else 'RELATIVE'



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Collection](collection.md#collection) :black_small_square: [Content](collection.md#content) :black_small_square: [Methods](collection.md#methods)</sub>

----------
### info()

> method

``` python
info(separate_children=None, reset_children=None, original=True)
```

> Node [Collection Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/collection_info.html)

#### Arguments:
- **separate_children** (_Boolean_ = None) : socket 'Separate Children' (Separate Children)
- **reset_children** (_Boolean_ = None) : socket 'Reset Children' (Reset Children)
- **original** (_bool_ = True) : Node.transform_space = 'ORIGINAL' if True else 'RELATIVE'



#### Returns:
- **Instances** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Collection](collection.md#collection) :black_small_square: [Content](collection.md#content) :black_small_square: [Methods](collection.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=None, name=None, tip=None)
```

Class Collection data socket

#### Arguments:
- **value** (_bpy.types.Object or str_ = None) : collection or collection name in bpy.data.collections
- **name** (_str_ = None) : create a group input socket of type Collection if not None
- **tip** (_str_ = None) : user tip for group input socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Collection](collection.md#collection) :black_small_square: [Content](collection.md#content) :black_small_square: [Methods](collection.md#methods)</sub>