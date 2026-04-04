# Image

``` python
Image(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
```

> The output socket of a [Node](node.md#node)

**Socket** is the base class for data classes such as [Float](core-gener-float-float.md#float), [Image](core-gener-image-image.md#image) or [Geometry](core-gener-geome-geometry.md#geometry).

It refers to an **output** socket of a [Node](node.md#node). A socket can be set to the **input** socket
of another [Node](node.md#node) to create a link between the two nodes:

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Node("Cube").mesh

# cube is set the to socket 'geometry' of node 'Set Position'
node = Node("Set Position")
node.geometry = cube
```

!!! important
> You can access to the other output sockets of the node in two different ways:
> - using [node](core-socket.md#node) attribute
> - using ***peer socket** naming convention where the **snake_case** name of
>.  the other sockets is suffixed by '_'

The example below shows how to access the to 'UV Map' socket of node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cube.html):

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Mesh.Cube()

# Getting 'UV Map' through the node
uv_map = cube.node.uv_map

# Or using the 'peer socket' naming convention
uv_map = cuve.uv_map_
```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None) : input name if not None
- **tip** (_str_ = ) : description
- **panel** (_str_ = ) : panel name
- **user_label** (_str_ = None) : user label
- **props**

### Inherited

[add_method](group.md#add_method) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](core-boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [menu](core-gener-menu---menu.md#menu) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-gener-menu-menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [Named](core-gener-boole-boolean.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](core-color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](core-closure.md#_pop) :black_small_square: [\_push](core-closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](core-cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [\_test_socket_to_data_type](core-socket.md#_test_socket_to_data_type) :black_small_square: ['_tree' not found]() :black_small_square: [\_ul](core-socket.md#_ul) :black_small_square: ['_use_layout' not found]() :black_small_square: [user_label](core-socket.md#user_label) :black_small_square:

## Content

- [\_create_input_socket](core-gener-image-image.md#_create_input_socket)
- [enable_output](core-gener-image-image.md#enable_output)
- [fps](core-gener-image-image.md#fps)
- [frame_count](core-gener-image-image.md#frame_count)
- [has_alpha](core-gener-image-image.md#has_alpha)
- [height](core-gener-image-image.md#height)
- [image_texture](core-gener-image-image.md#image_texture)
- [info](core-gener-image-image.md#info)
- [width](core-gener-image-image.md#width)

## Methods



----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = None, name: 'str' = 'Image', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> Image Input

New [Image](core-gener-image-image.md#image) input with subtype 'NONE'.

Aguments
--------
- value  (object = None) : Default value
- name  (str = 'Image') : Input socket name
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](core-gener-image-image.md#image) :black_small_square: [Content](core-gener-image-image.md#content) :black_small_square: [Methods](core-gener-image-image.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](core-gener-image-image.md#image) :black_small_square: [Content](core-gener-image-image.md#content) :black_small_square: [Methods](core-gener-image-image.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](core-gener-image-image.md#image) :black_small_square: [Content](core-gener-image-image.md#content) :black_small_square: [Methods](core-gener-image-image.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](core-gener-image-image.md#image) :black_small_square: [Content](core-gener-image-image.md#content) :black_small_square: [Methods](core-gener-image-image.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](core-gener-image-image.md#image) :black_small_square: [Content](core-gener-image-image.md#content) :black_small_square: [Methods](core-gener-image-image.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](core-gener-image-image.md#image) :black_small_square: [Content](core-gener-image-image.md#content) :black_small_square: [Methods](core-gener-image-image.md#methods)</sub>

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
- **extension** (_Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']_ = REPEAT) : parameter 'extension' in ('Repeat', 'Extend', 'Clip', 'Mirror')
- **interpolation** (_Literal['Linear', 'Closest', 'Cubic']_ = Linear) : parameter 'interpolation' in ('Linear', 'Closest', 'Cubic')



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](core-gener-image-image.md#image) :black_small_square: [Content](core-gener-image-image.md#content) :black_small_square: [Methods](core-gener-image-image.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](core-gener-image-image.md#image) :black_small_square: [Content](core-gener-image-image.md#content) :black_small_square: [Methods](core-gener-image-image.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Image](core-gener-image-image.md#image) :black_small_square: [Content](core-gener-image-image.md#content) :black_small_square: [Methods](core-gener-image-image.md#methods)</sub>