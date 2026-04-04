# Float

``` python
Float(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
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

[add_method](group.md#add_method) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](core-boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [menu](core-gener-menu---menu.md#menu) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-gener-menu-menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](core-color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](core-closure.md#_pop) :black_small_square: [\_push](core-closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](core-cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [\_test_socket_to_data_type](core-socket.md#_test_socket_to_data_type) :black_small_square: ['_tree' not found]() :black_small_square: [\_ul](core-socket.md#_ul) :black_small_square: ['_use_layout' not found]() :black_small_square: [user_label](core-socket.md#user_label) :black_small_square:

## Content

- **A** : [abs](core-gener-float-float.md#abs) :black_small_square: [acos](core-gener-float-float.md#acos) :black_small_square: [add](core-gener-float-float.md#add) :black_small_square: [advect_grid](core-gener-float-float.md#advect_grid) :black_small_square: [Angle](core-gener-float-float.md#angle) :black_small_square: [arctangent](core-gener-float-float.md#arctangent) :black_small_square: [asin](core-gener-float-float.md#asin) :black_small_square: [atan2](core-gener-float-float.md#atan2)
- **B** : [bevel](core-gener-float-float.md#bevel) :black_small_square: [blur](core-gener-float-float.md#blur) :black_small_square: [bump](core-gener-float-float.md#bump)
- **C** : [ceil](core-gener-float-float.md#ceil) :black_small_square: [clamp](core-gener-float-float.md#clamp) :black_small_square: [clamp_minmax](core-gener-float-float.md#clamp_minmax) :black_small_square: [clamp_range](core-gener-float-float.md#clamp_range) :black_small_square: [clip_grid](core-gener-float-float.md#clip_grid) :black_small_square: [ColorTemperature](core-gener-float-float.md#colortemperature) :black_small_square: [combine_color](core-gener-float-float.md#combine_color) :black_small_square: [combine_color_HSL](core-gener-float-float.md#combine_color_hsl) :black_small_square: [combine_color_HSV](core-gener-float-float.md#combine_color_hsv) :black_small_square: [combine_color_RGB](core-gener-float-float.md#combine_color_rgb) :black_small_square: [compare](core-gener-float-float.md#compare) :black_small_square: [cos](core-gener-float-float.md#cos) :black_small_square: [cosh](core-gener-float-float.md#cosh) :black_small_square: [\_create_input_socket](core-gener-float-float.md#_create_input_socket)
- **D** : [degrees](core-gener-float-float.md#degrees) :black_small_square: [dial_gizmo](core-gener-float-float.md#dial_gizmo) :black_small_square: [displacement](core-gener-float-float.md#displacement) :black_small_square: [Distance](core-gener-float-float.md#distance) :black_small_square: [distribute_points_in_grid](core-gener-float-float.md#distribute_points_in_grid) :black_small_square: [distribute_points_in_grid_density_grid](core-gener-float-float.md#distribute_points_in_grid_density_grid) :black_small_square: [distribute_points_in_grid_density_random](core-gener-float-float.md#distribute_points_in_grid_density_random) :black_small_square: [divide](core-gener-float-float.md#divide)
- **E** : [enable_output](core-gener-float-float.md#enable_output) :black_small_square: [equal](core-gener-float-float.md#equal) :black_small_square: [exp](core-gener-float-float.md#exp)
- **F** : [Factor](core-gener-float-float.md#factor) :black_small_square: [field_to_grid](core-gener-float-float.md#field_to_grid) :black_small_square: [floor](core-gener-float-float.md#floor) :black_small_square: [floored_modulo](core-gener-float-float.md#floored_modulo) :black_small_square: [fract](core-gener-float-float.md#fract) :black_small_square: [Frequency](core-gener-float-float.md#frequency) :black_small_square: [fresnel](core-gener-float-float.md#fresnel)
- **G** : [Gabor](core-gener-float-float.md#gabor) :black_small_square: [greater_equal](core-gener-float-float.md#greater_equal) :black_small_square: [greater_than](core-gener-float-float.md#greater_than) :black_small_square: [grid_dilate_erode](core-gener-float-float.md#grid_dilate_erode) :black_small_square: [grid_gradient](core-gener-float-float.md#grid_gradient) :black_small_square: [grid_info](core-gener-float-float.md#grid_info) :black_small_square: [grid_laplacian](core-gener-float-float.md#grid_laplacian) :black_small_square: [grid_mean](core-gener-float-float.md#grid_mean) :black_small_square: [grid_median](core-gener-float-float.md#grid_median) :black_small_square: [grid_to_mesh](core-gener-float-float.md#grid_to_mesh) :black_small_square: [grid_to_points](core-gener-float-float.md#grid_to_points)
- **H** : [hash_value](core-gener-float-float.md#hash_value) :black_small_square: [hue_saturation_value](core-gener-float-float.md#hue_saturation_value)
- **I** : [inverse_sqrt](core-gener-float-float.md#inverse_sqrt)
- **L** : [layer_weight](core-gener-float-float.md#layer_weight) :black_small_square: [less_equal](core-gener-float-float.md#less_equal) :black_small_square: [less_than](core-gener-float-float.md#less_than) :black_small_square: [light_falloff](core-gener-float-float.md#light_falloff) :black_small_square: [linear_gizmo](core-gener-float-float.md#linear_gizmo) :black_small_square: [log](core-gener-float-float.md#log)
- **M** : [map_range](core-gener-float-float.md#map_range) :black_small_square: [map_range_linear](core-gener-float-float.md#map_range_linear) :black_small_square: [map_range_smoother_step](core-gener-float-float.md#map_range_smoother_step) :black_small_square: [map_range_smooth_step](core-gener-float-float.md#map_range_smooth_step) :black_small_square: [map_range_stepped](core-gener-float-float.md#map_range_stepped) :black_small_square: [Mass](core-gener-float-float.md#mass) :black_small_square: [max](core-gener-float-float.md#max) :black_small_square: [mgreater_than](core-gener-float-float.md#mgreater_than) :black_small_square: [min](core-gener-float-float.md#min) :black_small_square: [mix](core-gener-float-float.md#mix) :black_small_square: [mless_than](core-gener-float-float.md#mless_than) :black_small_square: [modulo](core-gener-float-float.md#modulo) :black_small_square: [multiply](core-gener-float-float.md#multiply) :black_small_square: [multiply_add](core-gener-float-float.md#multiply_add)
- **N** : [Named](core-gener-float-float.md#named) :black_small_square: [NamedAttribute](core-gener-float-float.md#namedattribute) :black_small_square: [Noise](core-gener-float-float.md#noise) :black_small_square: [normal_map](core-gener-float-float.md#normal_map) :black_small_square: [not_equal](core-gener-float-float.md#not_equal)
- **P** : [Percentage](core-gener-float-float.md#percentage) :black_small_square: [pingpong](core-gener-float-float.md#pingpong) :black_small_square: [power](core-gener-float-float.md#power) :black_small_square: [prune_grid](core-gener-float-float.md#prune_grid)
- **R** : [radians](core-gener-float-float.md#radians) :black_small_square: [Random](core-gener-float-float.md#random) :black_small_square: [round](core-gener-float-float.md#round)
- **S** : [sample_grid](core-gener-float-float.md#sample_grid) :black_small_square: [sample_grid_index](core-gener-float-float.md#sample_grid_index) :black_small_square: [sdf_difference](core-gener-float-float.md#sdf_difference) :black_small_square: [sdf_grid_boolean](core-gener-float-float.md#sdf_grid_boolean) :black_small_square: [sdf_grid_fillet](core-gener-float-float.md#sdf_grid_fillet) :black_small_square: [sdf_grid_laplacian](core-gener-float-float.md#sdf_grid_laplacian) :black_small_square: [sdf_grid_mean](core-gener-float-float.md#sdf_grid_mean) :black_small_square: [sdf_grid_mean_curvature](core-gener-float-float.md#sdf_grid_mean_curvature) :black_small_square: [sdf_grid_median](core-gener-float-float.md#sdf_grid_median) :black_small_square: [sdf_grid_offset](core-gener-float-float.md#sdf_grid_offset) :black_small_square: [sdf_intersect](core-gener-float-float.md#sdf_intersect) :black_small_square: [sdf_union](core-gener-float-float.md#sdf_union) :black_small_square: [set_grid_background](core-gener-float-float.md#set_grid_background) :black_small_square: [set_grid_transform](core-gener-float-float.md#set_grid_transform) :black_small_square: [sign](core-gener-float-float.md#sign) :black_small_square: [sin](core-gener-float-float.md#sin) :black_small_square: [sinh](core-gener-float-float.md#sinh) :black_small_square: [smooth_max](core-gener-float-float.md#smooth_max) :black_small_square: [smooth_min](core-gener-float-float.md#smooth_min) :black_small_square: [snap](core-gener-float-float.md#snap) :black_small_square: [sqrt](core-gener-float-float.md#sqrt) :black_small_square: [subtract](core-gener-float-float.md#subtract)
- **T** : [tan](core-gener-float-float.md#tan) :black_small_square: [tanh](core-gener-float-float.md#tanh) :black_small_square: [Time](core-gener-float-float.md#time) :black_small_square: [TimeAbsolute](core-gener-float-float.md#timeabsolute) :black_small_square: [to_integer](core-gener-float-float.md#to_integer) :black_small_square: [to_string](core-gener-float-float.md#to_string) :black_small_square: [trunc](core-gener-float-float.md#trunc)
- **V** : [Voronoi](core-gener-float-float.md#voronoi) :black_small_square: [voxel_index](core-gener-float-float.md#voxel_index) :black_small_square: [voxelize_grid](core-gener-float-float.md#voxelize_grid)
- **W** : [Wavelength](core-gener-float-float.md#wavelength) :black_small_square: [wavelength](core-gener-float-float.md#wavelength) :black_small_square: [WhiteNoise](core-gener-float-float.md#whitenoise) :black_small_square: [wireframe](core-gener-float-float.md#wireframe) :black_small_square: [wrap](core-gener-float-float.md#wrap)

## Methods



----------
### abs()

> method

``` python
abs(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ABSOLUTE'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### acos()

> method

``` python
acos(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ARCCOSINE'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### add()

> method

``` python
add(value: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ADD'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### advect_grid()

> method

``` python
advect_grid(velocity: 'Vector' = None, time_step: 'Float' = None, integration_scheme: "Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC']" = None, limiter: "Literal['None', 'Clamp', 'Revert']" = None)
```

> Node [Advect Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/advect_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **velocity** (_Vector_ = None) : socket 'Velocity' (id: Velocity)
- **time_step** (_Float_ = None) : socket 'Time Step' (id: Time Step)
- **integration_scheme** (_Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC']_ = None) : ('Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC')
- **limiter** (_Literal['None', 'Clamp', 'Revert']_ = None) : ('None', 'Clamp', 'Revert')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Angle()

> classmethod

``` python
Angle(value: 'object' = 0.0, name: 'str' = 'Angle', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Angle Input

New [Float](core-gener-float-float.md#float) input with subtype 'ANGLE'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'Angle') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = Angle)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### arctangent()

> method

``` python
arctangent(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ARCTANGENT'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### asin()

> method

``` python
asin(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ARCSINE'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### atan2()

> method

``` python
atan2(value: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ARCTAN2'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### bevel()

> method

``` python
bevel(normal: 'Vector' = None, samples=4)
```

> Node [Bevel](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/bevel.html)

#### Information:
- **Socket** : self



#### Arguments:
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **samples** (_int_ = 4) : parameter 'samples'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### blur()

> method

``` python
blur(iterations: 'Integer' = None, weight: 'Float' = None)
```

> Node [Blur Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)
- **weight** (_Float_ = None) : socket 'Weight' (id: Weight)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### bump()

> method

``` python
bump(distance: 'Float' = None, filter_width: 'Float' = None, height: 'Float' = None, normal: 'Vector' = None, invert=False)
```

> Node [Bump](https://docs.blender.org/manual/en/latest/render/shader_nodes/displacement/bump.html)

#### Information:
- **Socket** : self



#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (id: Distance)
- **filter_width** (_Float_ = None) : socket 'Filter Width' (id: Filter Width)
- **height** (_Float_ = None) : socket 'Height' (id: Height)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### ceil()

> method

``` python
ceil(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'CEIL'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### clamp()

> method

``` python
clamp(min: 'Float' = None, max: 'Float' = None, clamp_type: "Literal['MINMAX', 'RANGE']" = 'MINMAX')
```

> Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/clamp.html)

#### Information:
- **Socket** : self



#### Arguments:
- **min** (_Float_ = None) : socket 'Min' (id: Min)
- **max** (_Float_ = None) : socket 'Max' (id: Max)
- **clamp_type** (_Literal['MINMAX', 'RANGE']_ = MINMAX) : parameter 'clamp_type' in ('Min Max', 'Range')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### clamp_minmax()

> method

``` python
clamp_minmax(min: 'Float' = None, max: 'Float' = None)
```

> Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/clamp.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MINMAX'



#### Arguments:
- **min** (_Float_ = None) : socket 'Min' (id: Min)
- **max** (_Float_ = None) : socket 'Max' (id: Max)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### clamp_range()

> method

``` python
clamp_range(min: 'Float' = None, max: 'Float' = None)
```

> Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/clamp.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RANGE'



#### Arguments:
- **min** (_Float_ = None) : socket 'Min' (id: Min)
- **max** (_Float_ = None) : socket 'Max' (id: Max)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### clip_grid()

> method

``` python
clip_grid(min_x: 'Integer' = None, min_y: 'Integer' = None, min_z: 'Integer' = None, max_x: 'Integer' = None, max_y: 'Integer' = None, max_z: 'Integer' = None)
```

> Node [Clip Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/clip_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **min_x** (_Integer_ = None) : socket 'Min X' (id: Min X)
- **min_y** (_Integer_ = None) : socket 'Min Y' (id: Min Y)
- **min_z** (_Integer_ = None) : socket 'Min Z' (id: Min Z)
- **max_x** (_Integer_ = None) : socket 'Max X' (id: Max X)
- **max_y** (_Integer_ = None) : socket 'Max Y' (id: Max Y)
- **max_z** (_Integer_ = None) : socket 'Max Z' (id: Max Z)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### ColorTemperature()

> classmethod

``` python
ColorTemperature(value: 'object' = 0.0, name: 'str' = 'ColorTemperature', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> ColorTemperature Input

New [Float](core-gener-float-float.md#float) input with subtype 'COLOR_TEMPERATURE'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'ColorTemperature') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = ColorTemperature)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### combine_color()

> method

``` python
combine_color(green: 'Float' = None, blue: 'Float' = None, mode: "Literal['RGB', 'HSV', 'HSL']" = 'RGB')
```

> Node [Combine Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Information:
- **Socket** : self



#### Arguments:
- **green** (_Float_ = None) : socket 'Green' (id: Green)
- **blue** (_Float_ = None) : socket 'Blue' (id: Blue)
- **mode** (_Literal['RGB', 'HSV', 'HSL']_ = RGB) : parameter 'mode' in ('RGB', 'HSV', 'HSL')



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### combine_color_HSL()

> method

``` python
combine_color_HSL(saturation: 'Float' = None, lightness: 'Float' = None)
```

> Node [Combine Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'HSL'



#### Arguments:
- **saturation** (_Float_ = None) : socket 'Saturation' (id: Green)
- **lightness** (_Float_ = None) : socket 'Lightness' (id: Blue)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### combine_color_HSV()

> method

``` python
combine_color_HSV(saturation: 'Float' = None, value: 'Float' = None)
```

> Node [Combine Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'HSV'



#### Arguments:
- **saturation** (_Float_ = None) : socket 'Saturation' (id: Green)
- **value** (_Float_ = None) : socket 'Value' (id: Blue)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### combine_color_RGB()

> method

``` python
combine_color_RGB(green: 'Float' = None, blue: 'Float' = None)
```

> Node [Combine Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RGB'



#### Arguments:
- **green** (_Float_ = None) : socket 'Green' (id: Green)
- **blue** (_Float_ = None) : socket 'Blue' (id: Blue)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### compare()

> method

``` python
compare(value: 'Float' = None, epsilon: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'COMPARE'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### cos()

> method

``` python
cos(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'COSINE'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### cosh()

> method

``` python
cosh(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'COSH'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = 0.0, name: 'str' = 'Float', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO', subtype: 'str' = 'NONE')
```

> Float Input

New [Float](core-gener-float-float.md#float) input with subtype 'NONE'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'Float') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')
subtype : str, optional
    Socket sub type in ('NONE', 'PERCENTAGE', 'FACTOR', 'MASS', 'ANGLE', 'TIME', 'TIME_ABSOLUTE', 'DISTANCE', 'WAVELENGTH', 'COLOR_TEMPERATURE', 'FREQUENCY') Default: 'NONE'.


#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = Float)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)
- **subtype** (_str_ = NONE)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### degrees()

> method

``` python
degrees(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DEGREES'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### dial_gizmo()

> method

``` python
dial_gizmo(*value: 'Float', position: 'Vector' = None, up: 'Vector' = None, screen_space: 'Boolean' = None, radius: 'Float' = None, color_id: "Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z']" = 'PRIMARY')
```

> Node ERROR: Node 'Dial Gizmo' not found

#### Arguments:
- **value** (_Float_) : socket 'Value' (id: Value)
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **up** (_Vector_ = None) : socket 'Up' (id: Up)
- **screen_space** (_Boolean_ = None) : socket 'Screen Space' (id: Screen Space)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **color_id** (_Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z']_ = PRIMARY) : parameter 'color_id' in ('Primary', 'Secondary', 'X', 'Y', 'Z')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### displacement()

> method

``` python
displacement(midlevel: 'Float' = None, scale: 'Float' = None, normal: 'Vector' = None, space: "Literal['OBJECT', 'WORLD']" = 'OBJECT')
```

> Node [Displacement](https://docs.blender.org/manual/en/latest/render/shader_nodes/displacement/displacement.html)

#### Information:
- **Socket** : self



#### Arguments:
- **midlevel** (_Float_ = None) : socket 'Midlevel' (id: Midlevel)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **space** (_Literal['OBJECT', 'WORLD']_ = OBJECT) : parameter 'space' in ('Object Space', 'World Space')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Distance()

> classmethod

``` python
Distance(value: 'object' = 0.0, name: 'str' = 'Distance', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Distance Input

New [Float](core-gener-float-float.md#float) input with subtype 'DISTANCE'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'Distance') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = Distance)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### distribute_points_in_grid()

> method

``` python
distribute_points_in_grid(density: 'Float' = None, seed: 'Integer' = None, mode: "Literal['DENSITY_RANDOM', 'DENSITY_GRID']" = 'DENSITY_RANDOM')
```

> Node ERROR: Node 'Distribute Points in Grid' not found

#### Information:
- **Socket** : self



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)
- **mode** (_Literal['DENSITY_RANDOM', 'DENSITY_GRID']_ = DENSITY_RANDOM) : parameter 'mode' in ('Random', 'Grid')



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### distribute_points_in_grid_density_grid()

> method

``` python
distribute_points_in_grid_density_grid(spacing: 'Vector' = None, threshold: 'Float' = None)
```

> Node ERROR: Node 'Distribute Points in Grid' not found

#### Information:
- **Socket** : self
- **Parameter** : 'DENSITY_GRID'



#### Arguments:
- **spacing** (_Vector_ = None) : socket 'Spacing' (id: Spacing)
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### distribute_points_in_grid_density_random()

> method

``` python
distribute_points_in_grid_density_random(density: 'Float' = None, seed: 'Integer' = None)
```

> Node ERROR: Node 'Distribute Points in Grid' not found

#### Information:
- **Socket** : self
- **Parameter** : 'DENSITY_RANDOM'



#### Arguments:
- **density** (_Float_ = None) : socket 'Density' (id: Density)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Cloud** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### divide()

> method

``` python
divide(value: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b: 'Float' = None, epsilon: 'Float' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'EQUAL'



#### Arguments:
- **b** (_Float_ = None) : socket 'B' (id: B)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### exp()

> method

``` python
exp(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EXPONENT'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Factor()

> classmethod

``` python
Factor(value: 'object' = 0.0, name: 'str' = 'Factor', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Factor Input

New [Float](core-gener-float-float.md#float) input with subtype 'FACTOR'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'Factor') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = Factor)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### field_to_grid()

> method

``` python
field_to_grid(named_sockets: 'dict' = {}, **sockets)
```

> Node [Field to Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/field_to_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **sockets**



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### floor()

> method

``` python
floor(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOOR'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### floored_modulo()

> method

``` python
floored_modulo(value: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOORED_MODULO'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### fract()

> method

``` python
fract(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FRACT'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Frequency()

> classmethod

``` python
Frequency(value: 'object' = 0.0, name: 'str' = 'Frequency', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Frequency Input

New [Float](core-gener-float-float.md#float) input with subtype 'FREQUENCY'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'Frequency') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = Frequency)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### fresnel()

> method

``` python
fresnel(normal: 'Vector' = None)
```

> Node [Fresnel](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/fresnel.html)

#### Information:
- **Socket** : self



#### Arguments:
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Gabor()

> classmethod

``` python
Gabor(vector: 'Vector' = None, scale: 'Float' = None, frequency: 'Float' = None, anisotropy: 'Float' = None, orientation: 'Float' = None, gabor_type: "Literal['2D', '3D']" = '2D')
```

> Node [Gabor Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gabor.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **frequency** (_Float_ = None) : socket 'Frequency' (id: Frequency)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **orientation** (_Float_ = None) : socket 'Orientation' (id: Orientation 2D)
- **gabor_type** (_Literal['2D', '3D']_ = 2D) : parameter 'gabor_type' in ('2D', '3D')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### greater_equal()

> method

``` python
greater_equal(b: 'Float' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_EQUAL'



#### Arguments:
- **b** (_Float_ = None) : socket 'B' (id: B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(b: 'Float' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_THAN'



#### Arguments:
- **b** (_Float_ = None) : socket 'B' (id: B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### grid_dilate_erode()

> method

``` python
grid_dilate_erode(connectivity: "Literal['Face', 'Edge', 'Vertex']" = None, tiles: "Literal['Ignore', 'Expand', 'Preserve']" = None, steps: 'Integer' = None)
```

> Node ERROR: Node 'Grid Dilate & Erode' not found

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **connectivity** (_Literal['Face', 'Edge', 'Vertex']_ = None) : ('Face', 'Edge', 'Vertex')
- **tiles** (_Literal['Ignore', 'Expand', 'Preserve']_ = None) : ('Ignore', 'Expand', 'Preserve')
- **steps** (_Integer_ = None) : socket 'Steps' (id: Steps)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### grid_gradient()

> method

``` python
grid_gradient()
```

> Node [Grid Gradient](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/grid_gradient.html)

#### Information:
- **Socket** : self



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### grid_info()

> method

``` python
grid_info()
```

> Node [Grid Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/grid_info.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Returns:
- **Matrix** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### grid_laplacian()

> method

``` python
grid_laplacian()
```

> Node [Grid Laplacian](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/grid_laplacian.html)

#### Information:
- **Socket** : self



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### grid_mean()

> method

``` python
grid_mean(width: 'Integer' = None, iterations: 'Integer' = None)
```

> Node [Grid Mean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_mean.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **width** (_Integer_ = None) : socket 'Width' (id: Width)
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### grid_median()

> method

``` python
grid_median(width: 'Integer' = None, iterations: 'Integer' = None)
```

> Node [Grid Median](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_median.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **width** (_Integer_ = None) : socket 'Width' (id: Width)
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### grid_to_mesh()

> method

``` python
grid_to_mesh(threshold: 'Float' = None, adaptivity: 'Float' = None)
```

> Node [Grid to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_to_mesh.html)

#### Information:
- **Socket** : self



#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (id: Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### grid_to_points()

> method

``` python
grid_to_points()
```

> Node [Grid to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Returns:
- **Cloud** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed: 'Integer' = None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### hue_saturation_value()

> method

``` python
hue_saturation_value(saturation: 'Float' = None, value: 'Float' = None, color: 'Color' = None, factor: 'Float' = None)
```

> Node [Hue/Saturation/Value](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/hue_saturation.html)

#### Information:
- **Socket** : self



#### Arguments:
- **saturation** (_Float_ = None) : socket 'Saturation' (id: Saturation)
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Fac)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### inverse_sqrt()

> method

``` python
inverse_sqrt(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INVERSE_SQRT'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### layer_weight()

> method

``` python
layer_weight(normal: 'Vector' = None)
```

> Node [Layer Weight](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/layer_weight.html)

#### Information:
- **Socket** : self



#### Arguments:
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### less_equal()

> method

``` python
less_equal(b: 'Float' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_EQUAL'



#### Arguments:
- **b** (_Float_ = None) : socket 'B' (id: B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(b: 'Float' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_THAN'



#### Arguments:
- **b** (_Float_ = None) : socket 'B' (id: B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### light_falloff()

> method

``` python
light_falloff(smooth: 'Float' = None)
```

> Node [Light Falloff](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/light_falloff.html)

#### Information:
- **Socket** : self



#### Arguments:
- **smooth** (_Float_ = None) : socket 'Smooth' (id: Smooth)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### linear_gizmo()

> method

``` python
linear_gizmo(*value: 'Float', position: 'Vector' = None, direction: 'Vector' = None, color_id: "Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z']" = 'PRIMARY', draw_style: "Literal['ARROW', 'CROSS', 'BOX']" = 'ARROW')
```

> Node ERROR: Node 'Linear Gizmo' not found

#### Arguments:
- **value** (_Float_) : socket 'Value' (id: Value)
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **direction** (_Vector_ = None) : socket 'Direction' (id: Direction)
- **color_id** (_Literal['PRIMARY', 'SECONDARY', 'X', 'Y', 'Z']_ = PRIMARY) : parameter 'color_id' in ('Primary', 'Secondary', 'X', 'Y', 'Z')
- **draw_style** (_Literal['ARROW', 'CROSS', 'BOX']_ = ARROW) : parameter 'draw_style' in ('Arrow', 'Cross', 'Box')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### log()

> method

``` python
log(base: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LOGARITHM'



#### Arguments:
- **base** (_Float_ = None) : socket 'Base' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### map_range()

> method

``` python
map_range(from_min: 'Float | Vector' = None, from_max: 'Float | Vector' = None, to_min: 'Float | Vector' = None, to_max: 'Float | Vector' = None, clamp=True, interpolation_type: "Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']" = 'LINEAR')
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type



#### Arguments:
- **from_min** (_Float | Vector_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float | Vector_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float | Vector_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float | Vector_ = None) : socket 'To Max' (id: To Max)
- **clamp** (_bool_ = True) : parameter 'clamp'
- **interpolation_type** (_Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']_ = LINEAR) : parameter 'interpolation_type' in ('Linear', 'Stepped Linear', 'Smooth Step', 'Smoother Step')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### map_range_linear()

> method

``` python
map_range_linear(from_min: 'Float | Vector' = None, from_max: 'Float | Vector' = None, to_min: 'Float | Vector' = None, to_max: 'Float | Vector' = None, clamp=True)
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type
- **Parameter** : 'LINEAR'



#### Arguments:
- **from_min** (_Float | Vector_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float | Vector_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float | Vector_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float | Vector_ = None) : socket 'To Max' (id: To Max)
- **clamp** (_bool_ = True) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### map_range_smoother_step()

> method

``` python
map_range_smoother_step(from_min: 'Float | Vector' = None, from_max: 'Float | Vector' = None, to_min: 'Float | Vector' = None, to_max: 'Float | Vector' = None, clamp=True)
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type
- **Parameter** : 'SMOOTHERSTEP'



#### Arguments:
- **from_min** (_Float | Vector_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float | Vector_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float | Vector_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float | Vector_ = None) : socket 'To Max' (id: To Max)
- **clamp** (_bool_ = True) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### map_range_smooth_step()

> method

``` python
map_range_smooth_step(from_min: 'Float | Vector' = None, from_max: 'Float | Vector' = None, to_min: 'Float | Vector' = None, to_max: 'Float | Vector' = None, clamp=True)
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type
- **Parameter** : 'SMOOTHSTEP'



#### Arguments:
- **from_min** (_Float | Vector_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float | Vector_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float | Vector_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float | Vector_ = None) : socket 'To Max' (id: To Max)
- **clamp** (_bool_ = True) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### map_range_stepped()

> method

``` python
map_range_stepped(from_min: 'Float | Vector' = None, from_max: 'Float | Vector' = None, to_min: 'Float | Vector' = None, to_max: 'Float | Vector' = None, steps: 'Float' = None, clamp=True)
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type
- **Parameter** : 'STEPPED'



#### Arguments:
- **from_min** (_Float | Vector_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float | Vector_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float | Vector_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float | Vector_ = None) : socket 'To Max' (id: To Max)
- **steps** (_Float_ = None) : socket 'Steps' (id: Steps)
- **clamp** (_bool_ = True) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Mass()

> classmethod

``` python
Mass(value: 'object' = 0.0, name: 'str' = 'Mass', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Mass Input

New [Float](core-gener-float-float.md#float) input with subtype 'MASS'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'Mass') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = Mass)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### max()

> method

``` python
max(value: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MAXIMUM'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### mgreater_than()

> method

``` python
mgreater_than(threshold: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'GREATER_THAN'



#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### min()

> method

``` python
min(value: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MINIMUM'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### mix()

> method

``` python
mix(b: 'Float' = None, factor: 'Float' = None, clamp_factor=True)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MIX'
- **Parameter** : False
- **Parameter** : 'FLOAT'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Float_ = None) : socket 'B' (id: B_Float)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### mless_than()

> method

``` python
mless_than(threshold: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LESS_THAN'



#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### modulo()

> method

``` python
modulo(value: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MODULO'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(value: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### multiply_add()

> method

``` python
multiply_add(multiplier: 'Float' = None, addend: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY_ADD'



#### Arguments:
- **multiplier** (_Float_ = None) : socket 'Multiplier' (id: Value_001)
- **addend** (_Float_ = None) : socket 'Addend' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Noise()

> classmethod

``` python
Noise(vector: 'Vector' = None, scale: 'Float' = None, detail: 'Float' = None, roughness: 'Float' = None, lacunarity: 'Float' = None, distortion: 'Float' = None, noise_dimensions: "Literal['1D', '2D', '3D', '4D']" = '3D', noise_type: "Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN']" = 'FBM', normalize=True)
```

> Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (id: Lacunarity)
- **distortion** (_Float_ = None) : socket 'Distortion' (id: Distortion)
- **noise_dimensions** (_Literal['1D', '2D', '3D', '4D']_ = 3D) : parameter 'noise_dimensions' in ('1D', '2D', '3D', '4D')
- **noise_type** (_Literal['MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN']_ = FBM) : parameter 'noise_type' in ('Multifractal', 'Ridged Multifractal', 'Hybrid Multifractal', 'fBM', 'Hetero Terrain')
- **normalize** (_bool_ = True) : parameter 'normalize'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### normal_map()

> method

``` python
normal_map(color: 'Color' = None, base: "Literal['ORIGINAL', 'DISPLACED']" = 'DISPLACED', convention: "Literal['OPENGL', 'DIRECTX']" = 'OPENGL', space: "Literal['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD']" = 'TANGENT', uv_map='')
```

> Node [Normal Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/displacement/normal_map.html)

#### Information:
- **Socket** : self



#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **base** (_Literal['ORIGINAL', 'DISPLACED']_ = DISPLACED) : parameter 'base' in ('Original Base', 'Displaced Base')
- **convention** (_Literal['OPENGL', 'DIRECTX']_ = OPENGL) : parameter 'convention' in ('OpenGL', 'DirectX')
- **space** (_Literal['TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD']_ = TANGENT) : parameter 'space' in ('Tangent Space', 'Object Space', 'World Space', 'Blender Object Space', 'Blender World Space')
- **uv_map** (_str_ = ) : parameter 'uv_map'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(b: 'Float' = None, epsilon: 'Float' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'NOT_EQUAL'



#### Arguments:
- **b** (_Float_ = None) : socket 'B' (id: B)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Percentage()

> classmethod

``` python
Percentage(value: 'object' = 0.0, name: 'str' = 'Percentage', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Percentage Input

New [Float](core-gener-float-float.md#float) input with subtype 'PERCENTAGE'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'Percentage') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = Percentage)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### pingpong()

> method

``` python
pingpong(scale: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'PINGPONG'



#### Arguments:
- **scale** (_Float_ = None) : socket 'Scale' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### power()

> method

``` python
power(exponent: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'POWER'



#### Arguments:
- **exponent** (_Float_ = None) : socket 'Exponent' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### prune_grid()

> method

``` python
prune_grid(mode: "Literal['Inactive', 'Threshold', 'SDF']" = None, threshold: 'Float' = None)
```

> Node [Prune Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/prune_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **mode** (_Literal['Inactive', 'Threshold', 'SDF']_ = None) : ('Inactive', 'Threshold', 'SDF')
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### radians()

> method

``` python
radians(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RADIANS'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(min: 'Float' = None, max: 'Float' = None, id: 'Integer' = None, seed: 'Integer' = None)
```

> Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Information:
- **Parameter** : 'FLOAT'



#### Arguments:
- **min** (_Float_ = None) : socket 'Min' (id: Min_001)
- **max** (_Float_ = None) : socket 'Max' (id: Max_001)
- **id** (_Integer_ = None) : socket 'ID' (id: ID)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### round()

> method

``` python
round(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ROUND'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sample_grid()

> method

``` python
sample_grid(position: 'Vector' = None, interpolation: "Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']" = None)
```

> Node [Sample Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation** (_Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']_ = None) : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x: 'Integer' = None, y: 'Integer' = None, z: 'Integer' = None)
```

> Node [Sample Grid Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid_index.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **x** (_Integer_ = None) : socket 'X' (id: X)
- **y** (_Integer_ = None) : socket 'Y' (id: Y)
- **z** (_Integer_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_difference()

> method

``` python
sdf_difference(*grid_2: 'Float')
```

> Node [SDF Grid Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/sdf_grid_boolean.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIFFERENCE'



#### Arguments:
- **grid_2** (_Float_) : socket 'Grid 2' (id: Grid 2)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_grid_boolean()

> method

``` python
sdf_grid_boolean(*grid_2: 'Float', operation: "Literal['INTERSECT', 'UNION', 'DIFFERENCE']" = 'DIFFERENCE')
```

> Node [SDF Grid Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/sdf_grid_boolean.html)

#### Information:
- **Socket** : self



#### Arguments:
- **grid_2** (_Float_) : socket 'Grid 2' (id: Grid 2)
- **operation** (_Literal['INTERSECT', 'UNION', 'DIFFERENCE']_ = DIFFERENCE) : parameter 'operation' in ('Intersect', 'Union', 'Difference')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_grid_fillet()

> method

``` python
sdf_grid_fillet(iterations: 'Integer' = None)
```

> Node ERROR: Node 'SDF Grid Fillet' not found

#### Information:
- **Socket** : self



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_grid_laplacian()

> method

``` python
sdf_grid_laplacian(iterations: 'Integer' = None)
```

> Node [SDF Grid Laplacian](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/sdf_grid_laplacian.html)

#### Information:
- **Socket** : self



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_grid_mean()

> method

``` python
sdf_grid_mean(width: 'Integer' = None, iterations: 'Integer' = None)
```

> Node [SDF Grid Mean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/sdf_grid_mean.html)

#### Information:
- **Socket** : self



#### Arguments:
- **width** (_Integer_ = None) : socket 'Width' (id: Width)
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_grid_mean_curvature()

> method

``` python
sdf_grid_mean_curvature(iterations: 'Integer' = None)
```

> Node [SDF Grid Mean Curvature](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/sdf_grid_mean_curvature.html)

#### Information:
- **Socket** : self



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_grid_median()

> method

``` python
sdf_grid_median(width: 'Integer' = None, iterations: 'Integer' = None)
```

> Node [SDF Grid Median](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/sdf_grid_median.html)

#### Information:
- **Socket** : self



#### Arguments:
- **width** (_Integer_ = None) : socket 'Width' (id: Width)
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_grid_offset()

> method

``` python
sdf_grid_offset(distance: 'Float' = None)
```

> Node [SDF Grid Offset](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/sdf_grid_offset.html)

#### Information:
- **Socket** : self



#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (id: Distance)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_intersect()

> method

``` python
sdf_intersect(*grid: 'Float')
```

> Node [SDF Grid Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/sdf_grid_boolean.html)

#### Information:
- **Parameter** : 'INTERSECT'



#### Arguments:
- **grid** (_Float_) : socket 'Grid' (id: Grid 2)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sdf_union()

> method

``` python
sdf_union(*grid: 'Float')
```

> Node [SDF Grid Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/sdf_grid_boolean.html)

#### Information:
- **Parameter** : 'UNION'



#### Arguments:
- **grid** (_Float_) : socket 'Grid' (id: Grid 2)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### set_grid_background()

> method

``` python
set_grid_background(background: 'Float' = None, update_inactive: 'Boolean' = None)
```

> Node [Set Grid Background](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_background.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **background** (_Float_ = None) : socket 'Background' (id: Background)
- **update_inactive** (_Boolean_ = None) : socket 'Update Inactive' (id: Update Inactive)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### set_grid_transform()

> method

``` python
set_grid_transform(transform: 'Matrix' = None)
```

> Node [Set Grid Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_transform.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Boolean** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sign()

> method

``` python
sign(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SIGN'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sin()

> method

``` python
sin(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SINE'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sinh()

> method

``` python
sinh(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SINH'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### smooth_max()

> method

``` python
smooth_max(value: 'Float' = None, distance: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SMOOTH_MAX'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **distance** (_Float_ = None) : socket 'Distance' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### smooth_min()

> method

``` python
smooth_min(value: 'Float' = None, distance: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SMOOTH_MIN'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **distance** (_Float_ = None) : socket 'Distance' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### snap()

> method

``` python
snap(increment: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SNAP'



#### Arguments:
- **increment** (_Float_ = None) : socket 'Increment' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### sqrt()

> method

``` python
sqrt(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SQRT'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### subtract()

> method

``` python
subtract(value: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SUBTRACT'



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value_001)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### tan()

> method

``` python
tan(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'TANGENT'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### tanh()

> method

``` python
tanh(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'TANH'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Time()

> classmethod

``` python
Time(value: 'object' = 0.0, name: 'str' = 'Time', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Time Input

New [Float](core-gener-float-float.md#float) input with subtype 'TIME'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'Time') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = Time)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### TimeAbsolute()

> classmethod

``` python
TimeAbsolute(value: 'object' = 0.0, name: 'str' = 'TimeAbsolute', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> TimeAbsolute Input

New [Float](core-gener-float-float.md#float) input with subtype 'TIME_ABSOLUTE'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'TimeAbsolute') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = TimeAbsolute)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### to_integer()

> method

``` python
to_integer(rounding_mode: "Literal['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE']" = 'ROUND')
```

> Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)

#### Information:
- **Socket** : self



#### Arguments:
- **rounding_mode** (_Literal['ROUND', 'FLOOR', 'CEILING', 'TRUNCATE']_ = ROUND) : parameter 'rounding_mode' in ('Round', 'Floor', 'Ceiling', 'Truncate')



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### to_string()

> method

``` python
to_string(decimals: 'Integer' = None)
```

> Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **decimals** (_Integer_ = None) : socket 'Decimals' (id: Decimals)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### trunc()

> method

``` python
trunc(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'TRUNC'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Voronoi()

> classmethod

``` python
Voronoi(vector: 'Vector' = None, scale: 'Float' = None, detail: 'Float' = None, roughness: 'Float' = None, lacunarity: 'Float' = None, randomness: 'Float' = None, distance: "Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI']" = 'EUCLIDEAN', feature: "Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS']" = 'F1', normalize=False, voronoi_dimensions: "Literal['1D', '2D', '3D', '4D']" = '3D')
```

> Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (id: Lacunarity)
- **randomness** (_Float_ = None) : socket 'Randomness' (id: Randomness)
- **distance** (_Literal['EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI']_ = EUCLIDEAN) : parameter 'distance' in ('Euclidean', 'Manhattan', 'Chebychev', 'Minkowski')
- **feature** (_Literal['F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS']_ = F1) : parameter 'feature' in ('F1', 'F2', 'Smooth F1', 'Distance to Edge', 'N-Sphere Radius')
- **normalize** (_bool_ = False) : parameter 'normalize'
- **voronoi_dimensions** (_Literal['1D', '2D', '3D', '4D']_ = 3D) : parameter 'voronoi_dimensions' in ('1D', '2D', '3D', '4D')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### voxel_index()

> classmethod

``` python
voxel_index()
```

> Node [Voxel Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/voxel_index.html)

#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### voxelize_grid()

> method

``` python
voxelize_grid()
```

> Node [Voxelize Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/voxelize_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### Wavelength()

> classmethod

``` python
Wavelength(value: 'object' = 0.0, name: 'str' = 'Wavelength', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Wavelength Input

New [Float](core-gener-float-float.md#float) input with subtype 'WAVELENGTH'.

Aguments
--------
- value  (object = 0.0) : Default value
- name  (str = 'Wavelength') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = 0.0)
- **name** (_str_ = Wavelength)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### wavelength()

> method

``` python
wavelength()
```

> Node [Wavelength](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/wavelength.html)

#### Information:
- **Socket** : self



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### WhiteNoise()

> classmethod

``` python
WhiteNoise(vector: 'Vector' = None, noise_dimensions: "Literal['1D', '2D', '3D', '4D']" = '3D')
```

> Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **noise_dimensions** (_Literal['1D', '2D', '3D', '4D']_ = 3D) : parameter 'noise_dimensions' in ('1D', '2D', '3D', '4D')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### wireframe()

> method

``` python
wireframe(use_pixel_size=False)
```

> Node [Wireframe](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/wireframe.html)

#### Information:
- **Socket** : self



#### Arguments:
- **use_pixel_size** (_bool_ = False) : parameter 'use_pixel_size'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>

----------
### wrap()

> method

``` python
wrap(max: 'Float' = None, min: 'Float' = None, use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'WRAP'



#### Arguments:
- **max** (_Float_ = None) : socket 'Max' (id: Value_001)
- **min** (_Float_ = None) : socket 'Min' (id: Value_002)
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](core-gener-float-float.md#float) :black_small_square: [Content](core-gener-float-float.md#content) :black_small_square: [Methods](core-gener-float-float.md#methods)</sub>