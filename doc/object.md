# Object

``` python
Object(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

> The output socket of a [Node](node.md#node)

**Socket** is the base class for data classes such as [Float](float.md#float), [Image](image.md#image) or [Geometry](geometry.md#geometry).

It refers to an **output** socket of a [Node](node.md#node). A socket can be set to the **input** socket
of another [Node](node.md#node) to create a link between the two nodes:

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Node("Cube").mesh

# cube is set the to socket 'geometry' of node 'Set Position'
node = Node("Set Position")
node.geometry = cube
```

> [!IMPORTANT]
> You can access to the other output sockets of the node in two different ways:
> - using ['#node' not found]() attribute
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
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [Constant](core-socke-socket.md#constant) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [Empty](core-socke-socket.md#empty) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socke-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](core-socke-socket.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socke-socket.md#_is_empty) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_inputs](core-socke-socket.md#link_inputs) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [Named](core-socke-socket.md#named) :black_small_square: [NewInput](core-socke-socket.md#newinput) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: [\_socket_type](core-socke-socket.md#_socket_type) :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- [ActiveCamera](object.md#activecamera)
- [camera_info](object.md#camera_info)
- [\_create_input_socket](object.md#_create_input_socket)
- [enable_output](object.md#enable_output)
- [info](object.md#info)
- [Self](object.md#self)

## Methods



----------
### ActiveCamera()

> classmethod

``` python
ActiveCamera()
```

> Node [Active Camera](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/active_camera.html)

#### Returns:
- **Object** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>

----------
### camera_info()

> method

``` python
camera_info()
```

> Node [Camera Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/camera_info.html)

#### Information:
- **Socket** : self



#### Returns:
- **Matrix** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = None, name: 'str' = 'Object', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> Object Input

New [Object](object.md#object) input with subtype 'NONE'.

Aguments
--------
- value  (object = None) : Default value
- name  (str = 'Object') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier

#### Arguments:
- **value** (_object_ = None)
- **name** (_str_ = Object)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)



#### Returns:
- **Object** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'OBJECT'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Object** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>

----------
### info()

> method

``` python
info(as_instance: 'Boolean' = None, transform_space: "Literal['ORIGINAL', 'RELATIVE']" = 'ORIGINAL')
```

> Node [Object Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/object_info.html)

#### Information:
- **Socket** : self



#### Arguments:
- **as_instance** (_Boolean_ = None) : socket 'As Instance' (id: As Instance)
- **transform_space** (_Literal['ORIGINAL', 'RELATIVE']_ = ORIGINAL) : parameter 'transform_space' in ['ORIGINAL', 'RELATIVE']



#### Returns:
- **Matrix** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>

----------
### Self()

> classmethod

``` python
Self()
```

> Node [Self Object](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/self_object.html)

#### Returns:
- **Object** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Object](object.md#object) :black_small_square: [Content](object.md#content) :black_small_square: [Methods](object.md#methods)</sub>