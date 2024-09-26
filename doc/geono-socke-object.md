# Object

> Bases classes: [Socket](geono-socke-socket.md#socket)

``` python
Object(value=None, name=None, tip=None)
```

Class Object data socket

#### Arguments:
- **value** (_bpy.types.Object or str_ = None) : object or object name in bpy.data.objects
- **name** (_str_ = None) : create a group input socket of type Object if not None
- **tip** (_str_ = None) : user tip for group input socket

### Inherited

[blur](geono-socke-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [\_reset](geono-socke-socket.md#_reset) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square: [to_output](geono-socke-socket.md#to_output) :black_small_square:

## Content

- [Info](geono-socke-object.md#info)
- [info](geono-socke-object.md#info)

## Methods



----------
### Info()

> staticmethod

``` python
Info(object=None, as_instance=None, original=True)
```

Node 'Object Info'

Tree: Geometry Nodes

Sockets
-------
- Object (Object) : object
- As Instance (Boolean) : as_instance
- original (Boolean) : original

Parameters
----------
- transform_space = 'ORIGINAL' or 'RELATIVE'

#### Arguments:
- **object** (_Object_ = None) : 'Object' socket
- **as_instance** (_Boolean_ = None) : 'As Instance': socket
- **original** (_Boolean_ = True) : transform_space parameter



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](geono-socke-object.md#object) :black_small_square: [Content](geono-socke-object.md#content) :black_small_square: [Methods](geono-socke-object.md#methods)</sub>

----------
### info()

> method

``` python
info(as_instance=None, original=True)
```

Node 'Object Info' (GeometryNodeObjectInfo)

#### Arguments:
- **as_instance** (_Boolean_ = None) : socket 'As Instance' (As Instance)
- **original** (_bool_ = True) : Node.transform_space in = 'ORIGINAL' if True else 'RELATIVE'



#### Returns:
- **Node** : [transform (Matrix), location (Vector), rotation (Rotation), scale (Vector), geometry (GEOMETRY)]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](geono-socke-object.md#object) :black_small_square: [Content](geono-socke-object.md#content) :black_small_square: [Methods](geono-socke-object.md#methods)</sub>