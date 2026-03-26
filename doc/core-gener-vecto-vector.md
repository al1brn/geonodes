# Vector

``` python
Vector(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
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

> [!IMPORTANT]
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

[add_method](group.md#add_method) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](core-boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [menu](core-gener-menu---menu.md#menu) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-gener-menu-menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](core-color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](core-closure.md#_pop) :black_small_square: [\_push](core-closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](core-cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [\_test_socket_to_data_type](core-socket.md#_test_socket_to_data_type) :black_small_square: ['_tree' not found]() :black_small_square: [\_ul](core-socket.md#_ul) :black_small_square: ['_use_layout' not found]() :black_small_square: [user_label](core-socket.md#user_label) :black_small_square:

## Content

- **A** : [abs](core-gener-vecto-vector.md#abs) :black_small_square: [Acceleration](core-gener-vecto-vector.md#acceleration) :black_small_square: [add](core-gener-vecto-vector.md#add) :black_small_square: [advect_grid](core-gener-vecto-vector.md#advect_grid)
- **B** : [blur](core-gener-vecto-vector.md#blur)
- **C** : [ceil](core-gener-vecto-vector.md#ceil) :black_small_square: [clip_grid](core-gener-vecto-vector.md#clip_grid) :black_small_square: [CombineXYZ](core-gener-vecto-vector.md#combinexyz) :black_small_square: [cos](core-gener-vecto-vector.md#cos) :black_small_square: [\_create_input_socket](core-gener-vecto-vector.md#_create_input_socket) :black_small_square: [cross](core-gener-vecto-vector.md#cross)
- **D** : [Direction](core-gener-vecto-vector.md#direction) :black_small_square: [distance](core-gener-vecto-vector.md#distance) :black_small_square: [divide](core-gener-vecto-vector.md#divide) :black_small_square: [dot](core-gener-vecto-vector.md#dot)
- **E** : [enable_output](core-gener-vecto-vector.md#enable_output) :black_small_square: [environment_texture](core-gener-vecto-vector.md#environment_texture) :black_small_square: [equal](core-gener-vecto-vector.md#equal) :black_small_square: [Euler](core-gener-vecto-vector.md#euler)
- **F** : [faceforward](core-gener-vecto-vector.md#faceforward) :black_small_square: [Factor](core-gener-vecto-vector.md#factor) :black_small_square: [field_to_grid](core-gener-vecto-vector.md#field_to_grid) :black_small_square: [floor](core-gener-vecto-vector.md#floor) :black_small_square: [fraction](core-gener-vecto-vector.md#fraction)
- **G** : [greater_equal](core-gener-vecto-vector.md#greater_equal) :black_small_square: [greater_than](core-gener-vecto-vector.md#greater_than) :black_small_square: [grid_curl](core-gener-vecto-vector.md#grid_curl) :black_small_square: [grid_dilate_erode](core-gener-vecto-vector.md#grid_dilate_erode) :black_small_square: [grid_divergence](core-gener-vecto-vector.md#grid_divergence) :black_small_square: [grid_info](core-gener-vecto-vector.md#grid_info) :black_small_square: [grid_mean](core-gener-vecto-vector.md#grid_mean) :black_small_square: [grid_median](core-gener-vecto-vector.md#grid_median) :black_small_square: [grid_to_points](core-gener-vecto-vector.md#grid_to_points)
- **H** : [hash_value](core-gener-vecto-vector.md#hash_value)
- **I** : [ies_texture](core-gener-vecto-vector.md#ies_texture) :black_small_square: [ies_texture_external](core-gener-vecto-vector.md#ies_texture_external) :black_small_square: [ies_texture_internal](core-gener-vecto-vector.md#ies_texture_internal) :black_small_square: [image_texture](core-gener-vecto-vector.md#image_texture)
- **L** : [length](core-gener-vecto-vector.md#length) :black_small_square: [less_equal](core-gener-vecto-vector.md#less_equal) :black_small_square: [less_than](core-gener-vecto-vector.md#less_than)
- **M** : [mapping](core-gener-vecto-vector.md#mapping) :black_small_square: [map_range](core-gener-vecto-vector.md#map_range) :black_small_square: [max](core-gener-vecto-vector.md#max) :black_small_square: [min](core-gener-vecto-vector.md#min) :black_small_square: [mix_non_uniform](core-gener-vecto-vector.md#mix_non_uniform) :black_small_square: [mix_uniform](core-gener-vecto-vector.md#mix_uniform) :black_small_square: [modulo](core-gener-vecto-vector.md#modulo) :black_small_square: [multiply](core-gener-vecto-vector.md#multiply) :black_small_square: [multiply_add](core-gener-vecto-vector.md#multiply_add)
- **N** : [Named](core-gener-vecto-vector.md#named) :black_small_square: [NamedAttribute](core-gener-vecto-vector.md#namedattribute) :black_small_square: [normal](core-gener-vecto-vector.md#normal) :black_small_square: [normalize](core-gener-vecto-vector.md#normalize) :black_small_square: [not_equal](core-gener-vecto-vector.md#not_equal)
- **P** : [pack_uv_islands](core-gener-vecto-vector.md#pack_uv_islands) :black_small_square: [Percentage](core-gener-vecto-vector.md#percentage) :black_small_square: [power](core-gener-vecto-vector.md#power) :black_small_square: [project](core-gener-vecto-vector.md#project) :black_small_square: [prune_grid](core-gener-vecto-vector.md#prune_grid)
- **R** : [radial_tiling](core-gener-vecto-vector.md#radial_tiling) :black_small_square: [Random](core-gener-vecto-vector.md#random) :black_small_square: [raycast](core-gener-vecto-vector.md#raycast) :black_small_square: [reflect](core-gener-vecto-vector.md#reflect) :black_small_square: [refract](core-gener-vecto-vector.md#refract) :black_small_square: [rotate](core-gener-vecto-vector.md#rotate) :black_small_square: [rotate_axis_angle](core-gener-vecto-vector.md#rotate_axis_angle) :black_small_square: [rotate_euler_xyz](core-gener-vecto-vector.md#rotate_euler_xyz) :black_small_square: [rotate_x_axis](core-gener-vecto-vector.md#rotate_x_axis) :black_small_square: [rotate_y_axis](core-gener-vecto-vector.md#rotate_y_axis) :black_small_square: [rotate_z_axis](core-gener-vecto-vector.md#rotate_z_axis) :black_small_square: [round](core-gener-vecto-vector.md#round)
- **S** : [sample_grid](core-gener-vecto-vector.md#sample_grid) :black_small_square: [sample_grid_index](core-gener-vecto-vector.md#sample_grid_index) :black_small_square: [scale](core-gener-vecto-vector.md#scale) :black_small_square: [separate_xyz](core-gener-vecto-vector.md#separate_xyz) :black_small_square: [set_grid_background](core-gener-vecto-vector.md#set_grid_background) :black_small_square: [set_grid_transform](core-gener-vecto-vector.md#set_grid_transform) :black_small_square: [sign](core-gener-vecto-vector.md#sign) :black_small_square: [sin](core-gener-vecto-vector.md#sin) :black_small_square: [snap](core-gener-vecto-vector.md#snap) :black_small_square: [subtract](core-gener-vecto-vector.md#subtract)
- **T** : [tan](core-gener-vecto-vector.md#tan) :black_small_square: [Tangent](core-gener-vecto-vector.md#tangent) :black_small_square: [to_rotation](core-gener-vecto-vector.md#to_rotation) :black_small_square: [Translation](core-gener-vecto-vector.md#translation)
- **U** : [UvMap](core-gener-vecto-vector.md#uvmap) :black_small_square: [uv_tangent](core-gener-vecto-vector.md#uv_tangent)
- **V** : [vector_transform](core-gener-vecto-vector.md#vector_transform) :black_small_square: [Velocity](core-gener-vecto-vector.md#velocity) :black_small_square: [voxel_index](core-gener-vecto-vector.md#voxel_index) :black_small_square: [voxelize_grid](core-gener-vecto-vector.md#voxelize_grid)
- **W** : [wrap](core-gener-vecto-vector.md#wrap)
- **X** : [x](core-gener-vecto-vector.md#x) :black_small_square: [xyz](core-gener-vecto-vector.md#xyz) :black_small_square: [Xyz](core-gener-vecto-vector.md#xyz)
- **Y** : [y](core-gener-vecto-vector.md#y)
- **Z** : [z](core-gener-vecto-vector.md#z)

## Properties



### x

> _type_: **x**
>

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Properties](core-gener-vecto-vector.md#properties)</sub>

### xyz

> _type_: **tuple**
>

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Properties](core-gener-vecto-vector.md#properties)</sub>

### y

> _type_: **y**
>

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Properties](core-gener-vecto-vector.md#properties)</sub>

### z

> _type_: **z**
>

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Properties](core-gener-vecto-vector.md#properties)</sub>

## Methods



----------
### abs()

> method

``` python
abs()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ABSOLUTE'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Acceleration()

> classmethod

``` python
Acceleration(value: 'object' = (0, 0, 0), name: 'str' = 'Acceleration', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Acceleration Input

New [Vector](core-gener-vecto-vector.md#vector) input with subtype 'ACCELERATION'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Acceleration') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Acceleration)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### add()

> method

``` python
add(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ADD'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### advect_grid()

> method

``` python
advect_grid(velocity: 'Vector' = None, time_step: 'Float' = None, integration_scheme: "Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC']" = None, limiter: "Literal['None', 'Clamp', 'Revert']" = None)
```

> Node [Advect Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/advect_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **velocity** (_Vector_ = None) : socket 'Velocity' (id: Velocity)
- **time_step** (_Float_ = None) : socket 'Time Step' (id: Time Step)
- **integration_scheme** (_Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC']_ = None) : ('Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC')
- **limiter** (_Literal['None', 'Clamp', 'Revert']_ = None) : ('None', 'Clamp', 'Revert')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### blur()

> method

``` python
blur(iterations: 'Integer' = None, weight: 'Float' = None)
```

> Node [Blur Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)
- **weight** (_Float_ = None) : socket 'Weight' (id: Weight)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### ceil()

> method

``` python
ceil()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'CEIL'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### clip_grid()

> method

``` python
clip_grid(min_x: 'Integer' = None, min_y: 'Integer' = None, min_z: 'Integer' = None, max_x: 'Integer' = None, max_y: 'Integer' = None, max_z: 'Integer' = None)
```

> Node [Clip Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/clip_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **min_x** (_Integer_ = None) : socket 'Min X' (id: Min X)
- **min_y** (_Integer_ = None) : socket 'Min Y' (id: Min Y)
- **min_z** (_Integer_ = None) : socket 'Min Z' (id: Min Z)
- **max_x** (_Integer_ = None) : socket 'Max X' (id: Max X)
- **max_y** (_Integer_ = None) : socket 'Max Y' (id: Max Y)
- **max_z** (_Integer_ = None) : socket 'Max Z' (id: Max Z)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### CombineXYZ()

> classmethod

``` python
CombineXYZ(x: 'Float' = None, y: 'Float' = None, z: 'Float' = None)
```

> Node [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/combine_xyz.html)

#### Arguments:
- **x** (_Float_ = None) : socket 'X' (id: X)
- **y** (_Float_ = None) : socket 'Y' (id: Y)
- **z** (_Float_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### cos()

> method

``` python
cos()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'COSINE'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = (0, 0, 0), name: 'str' = 'Vector', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO', subtype: 'str' = 'NONE')
```

> Vector Input

New [Vector](core-gener-vecto-vector.md#vector) input with subtype 'NONE'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Vector') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')
- subtype (str = 'NONE') : Socket sub type in ('NONE', 'PERCENTAGE', 'FACTOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'EULER', 'XYZ')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Vector)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)
- **subtype** (_str_ = NONE)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### cross()

> method

``` python
cross(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'CROSS_PRODUCT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Direction()

> classmethod

``` python
Direction(value: 'object' = (0, 0, 0), name: 'str' = 'Direction', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Direction Input

New [Vector](core-gener-vecto-vector.md#vector) input with subtype 'DIRECTION'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Direction') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Direction)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### distance()

> method

``` python
distance(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DISTANCE'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### divide()

> method

``` python
divide(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### dot()

> method

``` python
dot(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DOT_PRODUCT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### environment_texture()

> method

``` python
environment_texture(image=None, interpolation: "Literal['Linear', 'Closest', 'Cubic', 'Smart']" = 'Linear', projection: "Literal['EQUIRECTANGULAR', 'MIRROR_BALL']" = 'EQUIRECTANGULAR')
```

> Node [Environment Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/environment.html)

#### Information:
- **Socket** : self



#### Arguments:
- **image** (_NoneType_ = None) : parameter 'image'
- **interpolation** (_Literal['Linear', 'Closest', 'Cubic', 'Smart']_ = Linear) : parameter 'interpolation' in ('Linear', 'Closest', 'Cubic', 'Smart')
- **projection** (_Literal['EQUIRECTANGULAR', 'MIRROR_BALL']_ = EQUIRECTANGULAR) : parameter 'projection' in ('Equirectangular', 'Mirror Ball')



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b: 'Vector' = None, epsilon: 'Float' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'EQUAL'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Euler()

> classmethod

``` python
Euler(value: 'object' = (0, 0, 0), name: 'str' = 'Euler', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Euler Input

New [Vector](core-gener-vecto-vector.md#vector) input with subtype 'EULER'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Euler') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Euler)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### faceforward()

> method

``` python
faceforward(incident: 'Vector' = None, reference: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FACEFORWARD'



#### Arguments:
- **incident** (_Vector_ = None) : socket 'Incident' (id: Vector_001)
- **reference** (_Vector_ = None) : socket 'Reference' (id: Vector_002)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Factor()

> classmethod

``` python
Factor(value: 'object' = (0, 0, 0), name: 'str' = 'Factor', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Factor Input

New [Vector](core-gener-vecto-vector.md#vector) input with subtype 'FACTOR'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Factor') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Factor)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### field_to_grid()

> method

``` python
field_to_grid(named_sockets: 'dict' = {}, **sockets)
```

> Node [Field to Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/field_to_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **sockets**



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### floor()

> method

``` python
floor()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOOR'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### fraction()

> method

``` python
fraction()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FRACTION'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### greater_equal()

> method

``` python
greater_equal(b: 'Vector' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_EQUAL'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(b: 'Vector' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_THAN'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### grid_curl()

> method

``` python
grid_curl()
```

> Node [Grid Curl](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/grid_curl.html)

#### Information:
- **Socket** : self



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### grid_dilate_erode()

> method

``` python
grid_dilate_erode(connectivity: "Literal['Face', 'Edge', 'Vertex']" = None, tiles: "Literal['Ignore', 'Expand', 'Preserve']" = None, steps: 'Integer' = None)
```

> Node ERROR: Node 'Grid Dilate & Erode' not found

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **connectivity** (_Literal['Face', 'Edge', 'Vertex']_ = None) : ('Face', 'Edge', 'Vertex')
- **tiles** (_Literal['Ignore', 'Expand', 'Preserve']_ = None) : ('Ignore', 'Expand', 'Preserve')
- **steps** (_Integer_ = None) : socket 'Steps' (id: Steps)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### grid_divergence()

> method

``` python
grid_divergence()
```

> Node [Grid Divergence](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/grid_divergence.html)

#### Information:
- **Socket** : self



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### grid_info()

> method

``` python
grid_info()
```

> Node [Grid Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/grid_info.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Returns:
- **Matrix** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### grid_mean()

> method

``` python
grid_mean(width: 'Integer' = None, iterations: 'Integer' = None)
```

> Node [Grid Mean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_mean.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **width** (_Integer_ = None) : socket 'Width' (id: Width)
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### grid_median()

> method

``` python
grid_median(width: 'Integer' = None, iterations: 'Integer' = None)
```

> Node [Grid Median](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_median.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **width** (_Integer_ = None) : socket 'Width' (id: Width)
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### grid_to_points()

> method

``` python
grid_to_points()
```

> Node [Grid to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Returns:
- **Cloud** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed: 'Integer' = None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### ies_texture()

> method

``` python
ies_texture(strength: 'Float' = None, filepath='', ies=None, mode: "Literal['INTERNAL', 'EXTERNAL']" = 'INTERNAL')
```

> Node [IES Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/ies.html)

#### Information:
- **Socket** : self



#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (id: Strength)
- **filepath** (_str_ = ) : parameter 'filepath'
- **ies** (_NoneType_ = None) : parameter 'ies'
- **mode** (_Literal['INTERNAL', 'EXTERNAL']_ = INTERNAL) : parameter 'mode' in ('Internal', 'External')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### ies_texture_external()

> method

``` python
ies_texture_external(strength: 'Float' = None, filepath='', ies=None)
```

> Node [IES Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/ies.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EXTERNAL'



#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (id: Strength)
- **filepath** (_str_ = ) : parameter 'filepath'
- **ies** (_NoneType_ = None) : parameter 'ies'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### ies_texture_internal()

> method

``` python
ies_texture_internal(strength: 'Float' = None, filepath='', ies=None)
```

> Node [IES Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/ies.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INTERNAL'



#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (id: Strength)
- **filepath** (_str_ = ) : parameter 'filepath'
- **ies** (_NoneType_ = None) : parameter 'ies'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### image_texture()

> method

``` python
image_texture(extension: "Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']" = 'REPEAT', image=None, interpolation: "Literal['Linear', 'Closest', 'Cubic', 'Smart']" = 'Linear', projection: "Literal['FLAT', 'BOX', 'SPHERE', 'TUBE']" = 'FLAT', projection_blend=0.0)
```

> Node [Image Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../modeling/geometry_nodes/texture/image.html)

#### Information:
- **Socket** : self



#### Arguments:
- **extension** (_Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']_ = REPEAT) : parameter 'extension' in ('Repeat', 'Extend', 'Clip', 'Mirror')
- **image** (_NoneType_ = None) : parameter 'image'
- **interpolation** (_Literal['Linear', 'Closest', 'Cubic', 'Smart']_ = Linear) : parameter 'interpolation' in ('Linear', 'Closest', 'Cubic', 'Smart')
- **projection** (_Literal['FLAT', 'BOX', 'SPHERE', 'TUBE']_ = FLAT) : parameter 'projection' in ('Flat', 'Box', 'Sphere', 'Tube')
- **projection_blend** (_float_ = 0.0) : parameter 'projection_blend'



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### length()

> method

``` python
length()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LENGTH'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### less_equal()

> method

``` python
less_equal(b: 'Vector' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_EQUAL'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(b: 'Vector' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_THAN'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### mapping()

> method

``` python
mapping(location: 'Vector' = None, rotation: 'Vector' = None, scale: 'Vector' = None, vector_type: "Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL']" = 'POINT')
```

> Node [Mapping](https://docs.blender.org/manual/en/latest/render/shader_nodes/utilities/vector/mapping.html)

#### Information:
- **Socket** : self



#### Arguments:
- **location** (_Vector_ = None) : socket 'Location' (id: Location)
- **rotation** (_Vector_ = None) : socket 'Rotation' (id: Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)
- **vector_type** (_Literal['POINT', 'TEXTURE', 'VECTOR', 'NORMAL']_ = POINT) : parameter 'vector_type' in ('Point', 'Texture', 'Vector', 'Normal')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### map_range()

> method

``` python
map_range(from_min: 'Vector' = None, from_max: 'Vector' = None, to_min: 'Vector' = None, to_max: 'Vector' = None, clamp=True, interpolation_type: "Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']" = 'LINEAR')
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **from_min** (_Vector_ = None) : socket 'From Min' (id: From_Min_FLOAT3)
- **from_max** (_Vector_ = None) : socket 'From Max' (id: From_Max_FLOAT3)
- **to_min** (_Vector_ = None) : socket 'To Min' (id: To_Min_FLOAT3)
- **to_max** (_Vector_ = None) : socket 'To Max' (id: To_Max_FLOAT3)
- **clamp** (_bool_ = True) : parameter 'clamp'
- **interpolation_type** (_Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']_ = LINEAR) : parameter 'interpolation_type' in ('Linear', 'Stepped Linear', 'Smooth Step', 'Smoother Step')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### max()

> method

``` python
max(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MAXIMUM'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### min()

> method

``` python
min(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MINIMUM'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### mix_non_uniform()

> method

``` python
mix_non_uniform(b: 'Vector' = None, factor: 'Vector' = None, clamp_factor=True)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MIX'
- **Parameter** : False
- **Parameter** : 'VECTOR'
- **Parameter** : 'NON_UNIFORM'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_Vector)
- **factor** (_Vector_ = None) : socket 'Factor' (id: Factor_Vector)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### mix_uniform()

> method

``` python
mix_uniform(b: 'Vector' = None, factor: 'Float' = None, clamp_factor=True)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MIX'
- **Parameter** : False
- **Parameter** : 'VECTOR'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### modulo()

> method

``` python
modulo(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MODULO'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### multiply_add()

> method

``` python
multiply_add(multiplier: 'Vector' = None, addend: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY_ADD'



#### Arguments:
- **multiplier** (_Vector_ = None) : socket 'Multiplier' (id: Vector_001)
- **addend** (_Vector_ = None) : socket 'Addend' (id: Vector_002)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### normal()

> method

``` python
normal()
```

> Node [Normal](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../modeling/geometry_nodes/geometry/read/normal.html)

#### Information:
- **Socket** : self



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### normalize()

> method

``` python
normalize()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NORMALIZE'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(b: 'Vector' = None, epsilon: 'Float' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'NOT_EQUAL'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### pack_uv_islands()

> method

``` python
pack_uv_islands(margin: 'Float' = None, rotate: 'Boolean' = None, method: "Literal['Bounding Box', 'Convex Hull', 'Exact Shape']" = None, bottom_left: 'Vector' = None, top_right: 'Vector' = None)
```

> Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/pack_uv_islands.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **rotate** (_Boolean_ = None) : socket 'Rotate' (id: Rotate)
- **method** (_Literal['Bounding Box', 'Convex Hull', 'Exact Shape']_ = None) : ('Bounding Box', 'Convex Hull', 'Exact Shape')
- **bottom_left** (_Vector_ = None) : socket 'Bottom Left' (id: Bottom Left)
- **top_right** (_Vector_ = None) : socket 'Top Right' (id: Top Right)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Percentage()

> classmethod

``` python
Percentage(value: 'object' = (0, 0, 0), name: 'str' = 'Percentage', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Percentage Input

New [Vector](core-gener-vecto-vector.md#vector) input with subtype 'PERCENTAGE'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Percentage') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Percentage)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### power()

> method

``` python
power(exponent: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'POWER'



#### Arguments:
- **exponent** (_Vector_ = None) : socket 'Exponent' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### project()

> method

``` python
project(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'PROJECT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### prune_grid()

> method

``` python
prune_grid(mode: "Literal['Inactive', 'Threshold', 'SDF']" = None, threshold: 'Vector' = None)
```

> Node [Prune Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/prune_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **mode** (_Literal['Inactive', 'Threshold', 'SDF']_ = None) : ('Inactive', 'Threshold', 'SDF')
- **threshold** (_Vector_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### radial_tiling()

> method

``` python
radial_tiling(sides: 'Float' = None, roundness: 'Float' = None, normalize=False)
```

> Node [Radial Tiling](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/radial_tiling.html)

#### Information:
- **Socket** : self



#### Arguments:
- **sides** (_Float_ = None) : socket 'Sides' (id: Sides)
- **roundness** (_Float_ = None) : socket 'Roundness' (id: Roundness)
- **normalize** (_bool_ = False) : parameter 'normalize'



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(min: 'Vector' = None, max: 'Vector' = None, id: 'Integer' = None, seed: 'Integer' = None)
```

> Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Information:
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **min** (_Vector_ = None) : socket 'Min' (id: Min)
- **max** (_Vector_ = None) : socket 'Max' (id: Max)
- **id** (_Integer_ = None) : socket 'ID' (id: ID)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### raycast()

> method

``` python
raycast(direction: 'Vector' = None, length: 'Float' = None, only_local=False)
```

> Node [Raycast](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../modeling/geometry_nodes/geometry/sample/raycast.html)

#### Information:
- **Socket** : self



#### Arguments:
- **direction** (_Vector_ = None) : socket 'Direction' (id: Direction)
- **length** (_Float_ = None) : socket 'Length' (id: Length)
- **only_local** (_bool_ = False) : parameter 'only_local'



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### reflect()

> method

``` python
reflect(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'REFLECT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### refract()

> method

``` python
refract(vector: 'Vector' = None, ior: 'Float' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'REFRACT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)
- **ior** (_Float_ = None) : socket 'IOR' (id: Scale)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(center: 'Vector' = None, axis: 'Vector' = None, angle: 'Float' = None, invert=False, rotation_type: "Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']" = 'AXIS_ANGLE')
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **axis** (_Vector_ = None) : socket 'Axis' (id: Axis)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'
- **rotation_type** (_Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']_ = AXIS_ANGLE) : parameter 'rotation_type' in ('Axis Angle', 'X Axis', 'Y Axis', 'Z Axis', 'Euler')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### rotate_axis_angle()

> method

``` python
rotate_axis_angle(center: 'Vector' = None, axis: 'Vector' = None, angle: 'Float' = None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'AXIS_ANGLE'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **axis** (_Vector_ = None) : socket 'Axis' (id: Axis)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### rotate_euler_xyz()

> method

``` python
rotate_euler_xyz(center: 'Vector' = None, rotation: 'Vector' = None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EULER_XYZ'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **rotation** (_Vector_ = None) : socket 'Rotation' (id: Rotation)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### rotate_x_axis()

> method

``` python
rotate_x_axis(center: 'Vector' = None, angle: 'Float' = None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'X_AXIS'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### rotate_y_axis()

> method

``` python
rotate_y_axis(center: 'Vector' = None, angle: 'Float' = None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'Y_AXIS'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### rotate_z_axis()

> method

``` python
rotate_z_axis(center: 'Vector' = None, angle: 'Float' = None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'Z_AXIS'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### round()

> method

``` python
round()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ROUND'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### sample_grid()

> method

``` python
sample_grid(position: 'Vector' = None, interpolation: "Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']" = None)
```

> Node [Sample Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation** (_Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']_ = None) : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x: 'Integer' = None, y: 'Integer' = None, z: 'Integer' = None)
```

> Node [Sample Grid Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid_index.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **x** (_Integer_ = None) : socket 'X' (id: X)
- **y** (_Integer_ = None) : socket 'Y' (id: Y)
- **z** (_Integer_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale: 'Float' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SCALE'



#### Arguments:
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### separate_xyz()

> method

``` python
separate_xyz()
```

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

#### Information:
- **Socket** : self



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### set_grid_background()

> method

``` python
set_grid_background(background: 'Vector' = None, update_inactive: 'Boolean' = None)
```

> Node [Set Grid Background](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_background.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **background** (_Vector_ = None) : socket 'Background' (id: Background)
- **update_inactive** (_Boolean_ = None) : socket 'Update Inactive' (id: Update Inactive)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### set_grid_transform()

> method

``` python
set_grid_transform(transform: 'Matrix' = None)
```

> Node [Set Grid Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_transform.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Boolean** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### sign()

> method

``` python
sign()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SIGN'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### sin()

> method

``` python
sin()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SINE'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### snap()

> method

``` python
snap(increment: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SNAP'



#### Arguments:
- **increment** (_Vector_ = None) : socket 'Increment' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### subtract()

> method

``` python
subtract(vector: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SUBTRACT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### tan()

> method

``` python
tan()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'TANGENT'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Tangent()

> classmethod

``` python
Tangent(axis: "Literal['X', 'Y', 'Z']" = 'Z', direction_type: "Literal['RADIAL', 'UV_MAP']" = 'RADIAL', uv_map='')
```

> Node [Tangent](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/tangent.html)

#### Arguments:
- **axis** (_Literal['X', 'Y', 'Z']_ = Z) : parameter 'axis' in ('X', 'Y', 'Z')
- **direction_type** (_Literal['RADIAL', 'UV_MAP']_ = RADIAL) : parameter 'direction_type' in ('Radial', 'UV Map')
- **uv_map** (_str_ = ) : parameter 'uv_map'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### to_rotation()

> method

``` python
to_rotation()
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

#### Information:
- **Socket** : self



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Translation()

> classmethod

``` python
Translation(value: 'object' = (0, 0, 0), name: 'str' = 'Translation', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Translation Input

New [Vector](core-gener-vecto-vector.md#vector) input with subtype 'TRANSLATION'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Translation') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Translation)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### UvMap()

> classmethod

``` python
UvMap(from_instancer=False, uv_map='')
```

> Node [UV Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/uv_map.html)

#### Arguments:
- **from_instancer** (_bool_ = False) : parameter 'from_instancer'
- **uv_map** (_str_ = ) : parameter 'uv_map'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### uv_tangent()

> method

``` python
uv_tangent(method: "Literal['Exact', 'Fast']" = None)
```

> Node [UV Tangent](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_tangent.html)

#### Information:
- **Socket** : self



#### Arguments:
- **method** (_Literal['Exact', 'Fast']_ = None) : ('Exact', 'Fast')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### vector_transform()

> method

``` python
vector_transform(convert_from: "Literal['WORLD', 'OBJECT', 'CAMERA']" = 'WORLD', convert_to: "Literal['WORLD', 'OBJECT', 'CAMERA']" = 'OBJECT', vector_type: "Literal['POINT', 'VECTOR', 'NORMAL']" = 'VECTOR')
```

> Node [Vector Transform](https://docs.blender.org/manual/en/latest/render/shader_nodes/utilities/vector/transform.html)

#### Information:
- **Socket** : self



#### Arguments:
- **convert_from** (_Literal['WORLD', 'OBJECT', 'CAMERA']_ = WORLD) : parameter 'convert_from' in ('World', 'Object', 'Camera')
- **convert_to** (_Literal['WORLD', 'OBJECT', 'CAMERA']_ = OBJECT) : parameter 'convert_to' in ('World', 'Object', 'Camera')
- **vector_type** (_Literal['POINT', 'VECTOR', 'NORMAL']_ = VECTOR) : parameter 'vector_type' in ('Point', 'Vector', 'Normal')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Velocity()

> classmethod

``` python
Velocity(value: 'object' = (0, 0, 0), name: 'str' = 'Velocity', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Velocity Input

New [Vector](core-gener-vecto-vector.md#vector) input with subtype 'VELOCITY'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Velocity') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Velocity)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### voxel_index()

> classmethod

``` python
voxel_index()
```

> Node [Voxel Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/voxel_index.html)

#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### voxelize_grid()

> method

``` python
voxelize_grid()
```

> Node [Voxelize Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/voxelize_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### wrap()

> method

``` python
wrap(max: 'Vector' = None, min: 'Vector' = None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'WRAP'



#### Arguments:
- **max** (_Vector_ = None) : socket 'Max' (id: Vector_001)
- **min** (_Vector_ = None) : socket 'Min' (id: Vector_002)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>

----------
### Xyz()

> classmethod

``` python
Xyz(value: 'object' = (0, 0, 0), name: 'str' = 'Xyz', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Xyz Input

New [Vector](core-gener-vecto-vector.md#vector) input with subtype 'XYZ'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Xyz') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Xyz)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](core-gener-vecto-vector.md#vector) :black_small_square: [Content](core-gener-vecto-vector.md#content) :black_small_square: [Methods](core-gener-vecto-vector.md#methods)</sub>