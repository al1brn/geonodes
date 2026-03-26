# Integer

``` python
Integer(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
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

- **A** : [abs](core-gener-integ-integer.md#abs) :black_small_square: [add](core-gener-integ-integer.md#add) :black_small_square: [advect_grid](core-gener-integ-integer.md#advect_grid)
- **B** : [blur](core-gener-integ-integer.md#blur) :black_small_square: [bw_and](core-gener-integ-integer.md#bw_and) :black_small_square: [bw_not](core-gener-integ-integer.md#bw_not) :black_small_square: [bw_or](core-gener-integ-integer.md#bw_or) :black_small_square: [bw_rotate](core-gener-integ-integer.md#bw_rotate) :black_small_square: [bw_shift](core-gener-integ-integer.md#bw_shift) :black_small_square: [bw_xor](core-gener-integ-integer.md#bw_xor)
- **C** : [clip_grid](core-gener-integ-integer.md#clip_grid) :black_small_square: [\_create_input_socket](core-gener-integ-integer.md#_create_input_socket)
- **D** : [divide](core-gener-integ-integer.md#divide) :black_small_square: [divide_ceil](core-gener-integ-integer.md#divide_ceil) :black_small_square: [divide_floor](core-gener-integ-integer.md#divide_floor) :black_small_square: [divide_round](core-gener-integ-integer.md#divide_round)
- **E** : [enable_output](core-gener-integ-integer.md#enable_output) :black_small_square: [equal](core-gener-integ-integer.md#equal)
- **F** : [Factor](core-gener-integ-integer.md#factor) :black_small_square: [field_to_grid](core-gener-integ-integer.md#field_to_grid) :black_small_square: [floored_modulo](core-gener-integ-integer.md#floored_modulo)
- **G** : [gcd](core-gener-integ-integer.md#gcd) :black_small_square: [greater_equal](core-gener-integ-integer.md#greater_equal) :black_small_square: [greater_than](core-gener-integ-integer.md#greater_than) :black_small_square: [grid_dilate_erode](core-gener-integ-integer.md#grid_dilate_erode) :black_small_square: [grid_info](core-gener-integ-integer.md#grid_info) :black_small_square: [grid_mean](core-gener-integ-integer.md#grid_mean) :black_small_square: [grid_median](core-gener-integ-integer.md#grid_median) :black_small_square: [grid_to_points](core-gener-integ-integer.md#grid_to_points)
- **H** : [hash_value](core-gener-integ-integer.md#hash_value)
- **L** : [lcm](core-gener-integ-integer.md#lcm) :black_small_square: [less_equal](core-gener-integ-integer.md#less_equal) :black_small_square: [less_than](core-gener-integ-integer.md#less_than)
- **M** : [max](core-gener-integ-integer.md#max) :black_small_square: [min](core-gener-integ-integer.md#min) :black_small_square: [modulo](core-gener-integ-integer.md#modulo) :black_small_square: [multiply](core-gener-integ-integer.md#multiply) :black_small_square: [multiply_add](core-gener-integ-integer.md#multiply_add)
- **N** : [Named](core-gener-integ-integer.md#named) :black_small_square: [NamedAttribute](core-gener-integ-integer.md#namedattribute) :black_small_square: [negate](core-gener-integ-integer.md#negate) :black_small_square: [not_equal](core-gener-integ-integer.md#not_equal)
- **P** : [Percentage](core-gener-integ-integer.md#percentage) :black_small_square: [power](core-gener-integ-integer.md#power) :black_small_square: [prune_grid](core-gener-integ-integer.md#prune_grid)
- **R** : [Random](core-gener-integ-integer.md#random)
- **S** : [sample_grid](core-gener-integ-integer.md#sample_grid) :black_small_square: [sample_grid_index](core-gener-integ-integer.md#sample_grid_index) :black_small_square: [set_grid_background](core-gener-integ-integer.md#set_grid_background) :black_small_square: [set_grid_transform](core-gener-integ-integer.md#set_grid_transform) :black_small_square: [sign](core-gener-integ-integer.md#sign) :black_small_square: [subtract](core-gener-integ-integer.md#subtract)
- **T** : [to_string](core-gener-integ-integer.md#to_string)
- **V** : [voxel_index](core-gener-integ-integer.md#voxel_index) :black_small_square: [voxelize_grid](core-gener-integ-integer.md#voxelize_grid)

## Methods



----------
### abs()

> method

``` python
abs()
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ABSOLUTE'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### add()

> method

``` python
add(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ADD'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### advect_grid()

> method

``` python
advect_grid(velocity: 'Vector' = None, time_step: 'Float' = None, integration_scheme: "Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC']" = None, limiter: "Literal['None', 'Clamp', 'Revert']" = None)
```

> Node [Advect Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/advect_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **velocity** (_Vector_ = None) : socket 'Velocity' (id: Velocity)
- **time_step** (_Float_ = None) : socket 'Time Step' (id: Time Step)
- **integration_scheme** (_Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC']_ = None) : ('Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC')
- **limiter** (_Literal['None', 'Clamp', 'Revert']_ = None) : ('None', 'Clamp', 'Revert')



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### blur()

> method

``` python
blur(iterations: 'Integer' = None, weight: 'Float' = None)
```

> Node [Blur Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)
- **weight** (_Float_ = None) : socket 'Weight' (id: Weight)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### bw_and()

> method

``` python
bw_and(b: 'Integer' = None)
```

> Node [Bit Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/bit_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'AND'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### bw_not()

> method

``` python
bw_not()
```

> Node [Bit Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/bit_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NOT'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### bw_or()

> method

``` python
bw_or(b: 'Integer' = None)
```

> Node [Bit Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/bit_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'OR'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### bw_rotate()

> method

``` python
bw_rotate(shift: 'Integer' = None)
```

> Node [Bit Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/bit_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ROTATE'



#### Arguments:
- **shift** (_Integer_ = None) : socket 'Shift' (id: Shift)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### bw_shift()

> method

``` python
bw_shift(shift: 'Integer' = None)
```

> Node [Bit Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/bit_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SHIFT'



#### Arguments:
- **shift** (_Integer_ = None) : socket 'Shift' (id: Shift)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### bw_xor()

> method

``` python
bw_xor(b: 'Integer' = None)
```

> Node [Bit Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/bit_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'XOR'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### clip_grid()

> method

``` python
clip_grid(min_x: 'Integer' = None, min_y: 'Integer' = None, min_z: 'Integer' = None, max_x: 'Integer' = None, max_y: 'Integer' = None, max_z: 'Integer' = None)
```

> Node [Clip Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/clip_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **min_x** (_Integer_ = None) : socket 'Min X' (id: Min X)
- **min_y** (_Integer_ = None) : socket 'Min Y' (id: Min Y)
- **min_z** (_Integer_ = None) : socket 'Min Z' (id: Min Z)
- **max_x** (_Integer_ = None) : socket 'Max X' (id: Max X)
- **max_y** (_Integer_ = None) : socket 'Max Y' (id: Max Y)
- **max_z** (_Integer_ = None) : socket 'Max Z' (id: Max Z)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = 0, name: 'str' = 'Integer', min: 'int' = -2147483648, max: 'int' = 2147483647, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'INDEX', 'ID_OR_INDEX']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO', subtype: 'str' = 'NONE')
```

> Integer Input

New [Integer](core-gener-integ-integer.md#integer) input with subtype 'NONE'.

Aguments
--------
- value  (object = 0) : Default value
- name  (str = 'Integer') : Input socket name
- min  (int = -2147483648) : Property min_value
- max  (int = 2147483647) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'INDEX', 'ID_OR_INDEX')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')
- subtype (str = 'NONE') : Socket sub type in ('NONE', 'PERCENTAGE', 'FACTOR')

#### Arguments:
- **value** (_object_ = 0)
- **name** (_str_ = Integer)
- **min** (_int_ = -2147483648)
- **max** (_int_ = 2147483647)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'INDEX', 'ID_OR_INDEX']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)
- **subtype** (_str_ = NONE)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### divide()

> method

``` python
divide(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### divide_ceil()

> method

``` python
divide_ceil(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE_CEIL'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### divide_floor()

> method

``` python
divide_floor(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE_FLOOR'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### divide_round()

> method

``` python
divide_round(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE_ROUND'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b: 'Integer' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'EQUAL'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### Factor()

> classmethod

``` python
Factor(value: 'object' = 0, name: 'str' = 'Factor', min: 'int' = -2147483648, max: 'int' = 2147483647, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'INDEX', 'ID_OR_INDEX']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Factor Input

New [Integer](core-gener-integ-integer.md#integer) input with subtype 'FACTOR'.

Aguments
--------
- value  (object = 0) : Default value
- name  (str = 'Factor') : Input socket name
- min  (int = -2147483648) : Property min_value
- max  (int = 2147483647) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'INDEX', 'ID_OR_INDEX')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0)
- **name** (_str_ = Factor)
- **min** (_int_ = -2147483648)
- **max** (_int_ = 2147483647)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'INDEX', 'ID_OR_INDEX']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### field_to_grid()

> method

``` python
field_to_grid(named_sockets: 'dict' = {}, **sockets)
```

> Node [Field to Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/field_to_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **sockets**



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### floored_modulo()

> method

``` python
floored_modulo(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOORED_MODULO'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### gcd()

> method

``` python
gcd(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'GCD'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### greater_equal()

> method

``` python
greater_equal(b: 'Integer' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_EQUAL'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(b: 'Integer' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_THAN'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### grid_dilate_erode()

> method

``` python
grid_dilate_erode(connectivity: "Literal['Face', 'Edge', 'Vertex']" = None, tiles: "Literal['Ignore', 'Expand', 'Preserve']" = None, steps: 'Integer' = None)
```

> Node ERROR: Node 'Grid Dilate & Erode' not found

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **connectivity** (_Literal['Face', 'Edge', 'Vertex']_ = None) : ('Face', 'Edge', 'Vertex')
- **tiles** (_Literal['Ignore', 'Expand', 'Preserve']_ = None) : ('Ignore', 'Expand', 'Preserve')
- **steps** (_Integer_ = None) : socket 'Steps' (id: Steps)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### grid_info()

> method

``` python
grid_info()
```

> Node [Grid Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/grid_info.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Returns:
- **Matrix** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### grid_mean()

> method

``` python
grid_mean(width: 'Integer' = None, iterations: 'Integer' = None)
```

> Node [Grid Mean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_mean.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **width** (_Integer_ = None) : socket 'Width' (id: Width)
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### grid_median()

> method

``` python
grid_median(width: 'Integer' = None, iterations: 'Integer' = None)
```

> Node [Grid Median](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_median.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **width** (_Integer_ = None) : socket 'Width' (id: Width)
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### grid_to_points()

> method

``` python
grid_to_points()
```

> Node [Grid to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Returns:
- **Cloud** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed: 'Integer' = None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### lcm()

> method

``` python
lcm(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LCM'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### less_equal()

> method

``` python
less_equal(b: 'Integer' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_EQUAL'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(b: 'Integer' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_THAN'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### max()

> method

``` python
max(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MAXIMUM'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### min()

> method

``` python
min(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MINIMUM'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### modulo()

> method

``` python
modulo(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MODULO'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### multiply_add()

> method

``` python
multiply_add(multiplier: 'Integer' = None, addend: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY_ADD'



#### Arguments:
- **multiplier** (_Integer_ = None) : socket 'Multiplier' (id: Value_001)
- **addend** (_Integer_ = None) : socket 'Addend' (id: Value_002)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'INT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'INT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### negate()

> method

``` python
negate()
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NEGATE'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(b: 'Integer' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'NOT_EQUAL'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### Percentage()

> classmethod

``` python
Percentage(value: 'object' = 0, name: 'str' = 'Percentage', min: 'int' = -2147483648, max: 'int' = 2147483647, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'INDEX', 'ID_OR_INDEX']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Percentage Input

New [Integer](core-gener-integ-integer.md#integer) input with subtype 'PERCENTAGE'.

Aguments
--------
- value  (object = 0) : Default value
- name  (str = 'Percentage') : Input socket name
- min  (int = -2147483648) : Property min_value
- max  (int = 2147483647) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'INDEX', 'ID_OR_INDEX')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0)
- **name** (_str_ = Percentage)
- **min** (_int_ = -2147483648)
- **max** (_int_ = 2147483647)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'INDEX', 'ID_OR_INDEX']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### power()

> method

``` python
power(exponent: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'POWER'



#### Arguments:
- **exponent** (_Integer_ = None) : socket 'Exponent' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### prune_grid()

> method

``` python
prune_grid(mode: "Literal['Inactive', 'Threshold', 'SDF']" = None, threshold: 'Integer' = None)
```

> Node [Prune Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/prune_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **mode** (_Literal['Inactive', 'Threshold', 'SDF']_ = None) : ('Inactive', 'Threshold', 'SDF')
- **threshold** (_Integer_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(min: 'Integer' = None, max: 'Integer' = None, id: 'Integer' = None, seed: 'Integer' = None)
```

> Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Information:
- **Parameter** : 'INT'



#### Arguments:
- **min** (_Integer_ = None) : socket 'Min' (id: Min_002)
- **max** (_Integer_ = None) : socket 'Max' (id: Max_002)
- **id** (_Integer_ = None) : socket 'ID' (id: ID)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### sample_grid()

> method

``` python
sample_grid(position: 'Vector' = None, interpolation: "Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']" = None)
```

> Node [Sample Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation** (_Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']_ = None) : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x: 'Integer' = None, y: 'Integer' = None, z: 'Integer' = None)
```

> Node [Sample Grid Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid_index.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **x** (_Integer_ = None) : socket 'X' (id: X)
- **y** (_Integer_ = None) : socket 'Y' (id: Y)
- **z** (_Integer_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### set_grid_background()

> method

``` python
set_grid_background(background: 'Integer' = None, update_inactive: 'Boolean' = None)
```

> Node [Set Grid Background](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_background.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **background** (_Integer_ = None) : socket 'Background' (id: Background)
- **update_inactive** (_Boolean_ = None) : socket 'Update Inactive' (id: Update Inactive)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### set_grid_transform()

> method

``` python
set_grid_transform(transform: 'Matrix' = None)
```

> Node [Set Grid Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_transform.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Boolean** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### sign()

> method

``` python
sign()
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SIGN'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### subtract()

> method

``` python
subtract(value: 'Integer' = None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SUBTRACT'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### to_string()

> method

``` python
to_string()
```

> Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### voxel_index()

> classmethod

``` python
voxel_index()
```

> Node [Voxel Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/voxel_index.html)

#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>

----------
### voxelize_grid()

> method

``` python
voxelize_grid()
```

> Node [Voxelize Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/voxelize_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](core-gener-integ-integer.md#integer) :black_small_square: [Content](core-gener-integ-integer.md#content) :black_small_square: [Methods](core-gener-integ-integer.md#methods)</sub>