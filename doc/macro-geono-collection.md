# Collection

> Bases classes: [Socket](geono-socket.md#socket)

``` python
Collection(value=None, name=None, tip=None)
```

Class Collection data socket

#### Arguments:
- **value** (_bpy.types.Object or str_ = None) : collection or collection name in bpy.data.collections
- **name** (_str_ = None) : create a group input socket of type Collection if not None
- **tip** (_str_ = None) : user tip for group input socket

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square:

## Content

- [Info](macro-geono-collection.md#info)
- [info](macro-geono-collection.md#info)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Collection](macro-geono-collection.md#collection) :black_small_square: [Content](macro-geono-collection.md#content) :black_small_square: [Methods](macro-geono-collection.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Collection](macro-geono-collection.md#collection) :black_small_square: [Content](macro-geono-collection.md#content) :black_small_square: [Methods](macro-geono-collection.md#methods)</sub>