# Image

``` python
Image(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

Image Socket.

You can create an image with its name in `bpy.data.images`.

Use the class `Texture` to create an Image from a Texture.

``` python
from geonodes import GeoNodes, Image, nd, Texture, Geometry

with GeoNodes("Image Test"):
    
    Geometry().out()
    
    img = Image(name="Image")
    img.info().out(panel="Image Info")
    
    Texture.Checker().out("Checker")
    
    img.image_texture().out("Image Texture")  
```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [Constant](core-socke-socket.md#constant) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [Empty](core-socke-socket.md#empty) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socke-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](core-socke-socket.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socke-socket.md#_is_empty) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_inputs](core-socke-socket.md#link_inputs) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [Named](core-socke-socket.md#named) :black_small_square: [NewInput](core-socke-socket.md#newinput) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: [\_socket_type](core-socke-socket.md#_socket_type) :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- [\_create_input_socket](image.md#_create_input_socket)
- [enable_output](image.md#enable_output)
- [fps](image.md#fps)
- [frame_count](image.md#frame_count)
- [has_alpha](image.md#has_alpha)
- [height](image.md#height)
- [image_texture](image.md#image_texture)
- [info](image.md#info)
- [width](image.md#width)

## Methods



----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = None, name: 'str' = 'Image', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> Image Input

New [Image](image.md#image) input with subtype 'NONE'.

Aguments
--------
- value  (object = None) : Default value
- name  (str = 'Image') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier

#### Arguments:
- **value** (_object_ = None)
- **name** (_str_ = Image)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)



#### Returns:
- **Image** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](image.md#image) :black_small_square: [Content](image.md#content) :black_small_square: [Methods](image.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'IMAGE'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Image** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](image.md#image) :black_small_square: [Content](image.md#content) :black_small_square: [Methods](image.md#methods)</sub>

----------
### fps()

> method

``` python
fps(frame: 'Integer' = None)
```

> Node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

#### Information:
- **Socket** : self



#### Arguments:
- **frame** (_Integer_ = None) : socket 'Frame' (id: Frame)



#### Returns:
- **fps** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](image.md#image) :black_small_square: [Content](image.md#content) :black_small_square: [Methods](image.md#methods)</sub>

----------
### frame_count()

> method

``` python
frame_count(frame: 'Integer' = None)
```

> Node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

#### Information:
- **Socket** : self



#### Arguments:
- **frame** (_Integer_ = None) : socket 'Frame' (id: Frame)



#### Returns:
- **frame_count** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](image.md#image) :black_small_square: [Content](image.md#content) :black_small_square: [Methods](image.md#methods)</sub>

----------
### has_alpha()

> method

``` python
has_alpha(frame: 'Integer' = None)
```

> Node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

#### Information:
- **Socket** : self



#### Arguments:
- **frame** (_Integer_ = None) : socket 'Frame' (id: Frame)



#### Returns:
- **has_alpha** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](image.md#image) :black_small_square: [Content](image.md#content) :black_small_square: [Methods](image.md#methods)</sub>

----------
### height()

> method

``` python
height(frame: 'Integer' = None)
```

> Node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

#### Information:
- **Socket** : self



#### Arguments:
- **frame** (_Integer_ = None) : socket 'Frame' (id: Frame)



#### Returns:
- **height** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](image.md#image) :black_small_square: [Content](image.md#content) :black_small_square: [Methods](image.md#methods)</sub>

----------
### image_texture()

> method

``` python
image_texture(vector: 'Vector' = None, frame: 'Integer' = None, extension: "Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']" = 'REPEAT', interpolation: "Literal['Linear', 'Closest', 'Cubic']" = 'Linear')
```

> Node [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html)

#### Information:
- **Socket** : self



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **frame** (_Integer_ = None) : socket 'Frame' (id: Frame)
- **extension** (_Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']_ = REPEAT) : parameter 'extension' in ['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']
- **interpolation** (_Literal['Linear', 'Closest', 'Cubic']_ = Linear) : parameter 'interpolation' in ['Linear', 'Closest', 'Cubic']



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](image.md#image) :black_small_square: [Content](image.md#content) :black_small_square: [Methods](image.md#methods)</sub>

----------
### info()

> method

``` python
info(frame: 'Integer' = None)
```

> Node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

#### Information:
- **Socket** : self



#### Arguments:
- **frame** (_Integer_ = None) : socket 'Frame' (id: Frame)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](image.md#image) :black_small_square: [Content](image.md#content) :black_small_square: [Methods](image.md#methods)</sub>

----------
### width()

> method

``` python
width(frame: 'Integer' = None)
```

> Node [Image Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html)

#### Information:
- **Socket** : self



#### Arguments:
- **frame** (_Integer_ = None) : socket 'Frame' (id: Frame)



#### Returns:
- **width** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](image.md#image) :black_small_square: [Content](image.md#content) :black_small_square: [Methods](image.md#methods)</sub>