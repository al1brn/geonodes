# Image

> Bases classes: [Socket](geono-socket.md#socket)

``` python
Image(value=None, name=None, tip=None)
```

Class Image data socket

Node [Image](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/input/image.html)

#### Arguments:
- **value** (_bpy.types.Image or str_ = None) : image or image name in bpy.data.images
- **name** (_str_ = None) : create a group input socket of type Image if not None
- **tip** (_str_ = None) : user tip for group input socket

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square:

## Content

- [fps](macro-geono-image.md#fps)
- [frame_count](macro-geono-image.md#frame_count)
- [has_alpha](macro-geono-image.md#has_alpha)
- [height](macro-geono-image.md#height)
- [Info](macro-geono-image.md#info)
- [info](macro-geono-image.md#info)
- [width](macro-geono-image.md#width)

## Properties



### fps

> _type_: **Float**
>

Socket 'FPS' of node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](macro-geono-image.md#image) :black_small_square: [Content](macro-geono-image.md#content) :black_small_square: [Properties](macro-geono-image.md#properties)</sub>

### frame_count

> _type_: **Integer**
>

Socket 'Frame Count' of node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](macro-geono-image.md#image) :black_small_square: [Content](macro-geono-image.md#content) :black_small_square: [Properties](macro-geono-image.md#properties)</sub>

### has_alpha

> _type_: **Boolean**
>

Socket 'Has Alpha' of node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](macro-geono-image.md#image) :black_small_square: [Content](macro-geono-image.md#content) :black_small_square: [Properties](macro-geono-image.md#properties)</sub>

### height

> _type_: **Integer**
>

Socket 'Height' of node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](macro-geono-image.md#image) :black_small_square: [Content](macro-geono-image.md#content) :black_small_square: [Properties](macro-geono-image.md#properties)</sub>

### width

> _type_: **Integer**
>

Socket 'Width' of node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](macro-geono-image.md#image) :black_small_square: [Content](macro-geono-image.md#content) :black_small_square: [Properties](macro-geono-image.md#properties)</sub>

## Methods



----------
### Info()

> classmethod

``` python
Info(image=None, frame=None)
```

> Node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

#### Arguments:
- **image** (_Image_ = None) : socket 'Image' (Image)
- **frame** (_Integer_ = None) : socket 'Frame' (Frame)



#### Returns:
- **Node** : 'Image Info' node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](macro-geono-image.md#image) :black_small_square: [Content](macro-geono-image.md#content) :black_small_square: [Methods](macro-geono-image.md#methods)</sub>

----------
### info()

> method

``` python
info(frame=None)
```

> Node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

#### Arguments:
- **frame** (_Integer_ = None) : socket 'Frame' (Frame)



#### Returns:
- **Node** : 'Image Info' node

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](macro-geono-image.md#image) :black_small_square: [Content](macro-geono-image.md#content) :black_small_square: [Methods](macro-geono-image.md#methods)</sub>