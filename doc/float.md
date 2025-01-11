# Float

``` python
Float(value=0.0, name=None, min=None, max=None, tip=None, panel=None, subtype='NONE', default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Socket of type VALUE

> Node [Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/value.html)

If **value** argument is None:
- if **name** argument is None, a node 'Value' is added
- otherwise a new group input is created using **min**, **max**, **tip** and **subtype**
  arguments

If **value** argument is not None, a new **Float** is created from the value, either
by transtyping or creating a 'Value' node.

``` python
float = Float()      # 'Value' node with default initial vlaue
float = Float(3.14). # 'Value' node with 3.14 initial value
float = Float(3.14, name="User input", subtype='ANGLE') # Create a new Float group input
```

#### Arguments:
- **value** (_float | str | Socket_ = 0.0) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **min** (_float_ = None) : minimum value
- **max** (_float_ = None) : maximum value
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree pane if exists)
- **subtype** (_str in ('NONE', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'TIME_ABSOLUTE', 'DISTANCE', 'WAVELENGTH', 'COLOR_TEMPERATURE', 'FREQUENCY')_ = NONE) : sub type for group input
- **default_attribute** (_str_ = ) : default attribute name
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **A** : [abs](float.md#abs) :black_small_square: [add](float.md#add) :black_small_square: [Angle](float.md#angle) :black_small_square: [arccosine](float.md#arccosine) :black_small_square: [arcsine](float.md#arcsine) :black_small_square: [arctan2](float.md#arctan2) :black_small_square: [arctangent](float.md#arctangent)
- **B** : [bevel](float.md#bevel) :black_small_square: [blur](float.md#blur) :black_small_square: [bump](float.md#bump)
- **C** : [ceil](float.md#ceil) :black_small_square: [clamp](float.md#clamp) :black_small_square: [clamp_minmax](float.md#clamp_minmax) :black_small_square: [clamp_range](float.md#clamp_range) :black_small_square: [color_ramp](float.md#color_ramp) :black_small_square: [ColorTemperature](float.md#colortemperature) :black_small_square: [combine_color](float.md#combine_color) :black_small_square: [combine_color_HSL](float.md#combine_color_hsl) :black_small_square: [combine_color_HSV](float.md#combine_color_hsv) :black_small_square: [combine_color_RGB](float.md#combine_color_rgb) :black_small_square: [compare](float.md#compare) :black_small_square: [cos](float.md#cos) :black_small_square: [cosh](float.md#cosh)
- **D** : [degrees](float.md#degrees) :black_small_square: [dial_gizmo](float.md#dial_gizmo) :black_small_square: [displacement](float.md#displacement) :black_small_square: [Distance](float.md#distance) :black_small_square: [divide](float.md#divide)
- **E** : [equal](float.md#equal) :black_small_square: [exp](float.md#exp)
- **F** : [Factor](float.md#factor) :black_small_square: [float_curve](float.md#float_curve) :black_small_square: [floor](float.md#floor) :black_small_square: [floored_modulo](float.md#floored_modulo) :black_small_square: [fract](float.md#fract) :black_small_square: [Frequency](float.md#frequency) :black_small_square: [fresnel](float.md#fresnel)
- **G** : [Gabor](float.md#gabor) :black_small_square: [greater_equal](float.md#greater_equal) :black_small_square: [greater_than](float.md#greater_than) :black_small_square: [grid_boolean](float.md#grid_boolean)
- **H** : [hash_value](float.md#hash_value) :black_small_square: [hue_saturation_value](float.md#hue_saturation_value)
- **I** : [\_\_init__](float.md#__init__) :black_small_square: [inverse_sqrt](float.md#inverse_sqrt)
- **L** : [layer_weight](float.md#layer_weight) :black_small_square: [less_equal](float.md#less_equal) :black_small_square: [less_than](float.md#less_than) :black_small_square: [light_falloff](float.md#light_falloff) :black_small_square: [linear_gizmo](float.md#linear_gizmo) :black_small_square: [log](float.md#log)
- **M** : [map_range](float.md#map_range) :black_small_square: [map_range_linear](float.md#map_range_linear) :black_small_square: [map_range_smoother_step](float.md#map_range_smoother_step) :black_small_square: [map_range_smooth_step](float.md#map_range_smooth_step) :black_small_square: [map_range_stepped](float.md#map_range_stepped) :black_small_square: [max](float.md#max) :black_small_square: [mgreater_than](float.md#mgreater_than) :black_small_square: [min](float.md#min) :black_small_square: [mix](float.md#mix) :black_small_square: [mless_than](float.md#mless_than) :black_small_square: [modulo](float.md#modulo) :black_small_square: [multiply](float.md#multiply) :black_small_square: [multiply_add](float.md#multiply_add)
- **N** : [Named](float.md#named) :black_small_square: [NamedAttribute](float.md#namedattribute) :black_small_square: [Noise](float.md#noise) :black_small_square: [normal_map](float.md#normal_map) :black_small_square: [not_equal](float.md#not_equal)
- **O** : [out](float.md#out)
- **P** : [Percentage](float.md#percentage) :black_small_square: [pingpong](float.md#pingpong) :black_small_square: [power](float.md#power)
- **R** : [radians](float.md#radians) :black_small_square: [Random](float.md#random) :black_small_square: [round](float.md#round)
- **S** : [sample_grid](float.md#sample_grid) :black_small_square: [sample_grid_index](float.md#sample_grid_index) :black_small_square: [scene_time](float.md#scene_time) :black_small_square: [sdf_difference](float.md#sdf_difference) :black_small_square: [sdf_intersect](float.md#sdf_intersect) :black_small_square: [sdf_union](float.md#sdf_union) :black_small_square: [sign](float.md#sign) :black_small_square: [sin](float.md#sin) :black_small_square: [sinh](float.md#sinh) :black_small_square: [smooth_max](float.md#smooth_max) :black_small_square: [smooth_min](float.md#smooth_min) :black_small_square: [snap](float.md#snap) :black_small_square: [sqrt](float.md#sqrt) :black_small_square: [subtract](float.md#subtract)
- **T** : [tan](float.md#tan) :black_small_square: [tanh](float.md#tanh) :black_small_square: [Time](float.md#time) :black_small_square: [TimeAbsolute](float.md#timeabsolute) :black_small_square: [to_integer](float.md#to_integer) :black_small_square: [to_mesh](float.md#to_mesh) :black_small_square: [to_string](float.md#to_string) :black_small_square: [trunc](float.md#trunc)
- **V** : [Voronoi](float.md#voronoi)
- **W** : [WaveLength](float.md#wavelength) :black_small_square: [wavelength](float.md#wavelength) :black_small_square: [WhiteNoise](float.md#whitenoise) :black_small_square: [wireframe](float.md#wireframe) :black_small_square: [wrap](float.md#wrap)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### add()

> method

``` python
add(value=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Angle()

> classmethod

``` python
Angle(value=0.0, name='Angle', min=None, max=None, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Angle group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Angle)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)
- **panel** ( = None)
- **default_attribute** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### arccosine()

> method

``` python
arccosine(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ARCCOSINE'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### arcsine()

> method

``` python
arcsine(use_clamp=False)
```

> Node [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ARCSINE'



#### Arguments:
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### arctan2()

> method

``` python
arctan2(value=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### bevel()

> method

``` python
bevel(normal=None, samples=4)
```

> Node [Bevel](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/bevel.html)

#### Information:
- **Socket** : self



#### Arguments:
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **samples** (_int_ = 4) : parameter 'samples'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### blur()

> method

``` python
blur(iterations=None, weight=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### bump()

> method

``` python
bump(distance=None, height=None, normal=None, invert=False)
```

> Node [Bump](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/bump.html)

#### Information:
- **Socket** : self



#### Arguments:
- **distance** (_Float_ = None) : socket 'Distance' (id: Distance)
- **height** (_Float_ = None) : socket 'Height' (id: Height)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### clamp()

> method

``` python
clamp(min=None, max=None, clamp_type='MINMAX')
```

> Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/clamp.html)

#### Information:
- **Socket** : self



#### Arguments:
- **min** (_Float_ = None) : socket 'Min' (id: Min)
- **max** (_Float_ = None) : socket 'Max' (id: Max)
- **clamp_type** (_str_ = MINMAX) : parameter 'clamp_type' in ('MINMAX', 'RANGE')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### clamp_minmax()

> method

``` python
clamp_minmax(min=None, max=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### clamp_range()

> method

``` python
clamp_range(min=None, max=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### color_ramp()

> method

``` python
color_ramp(stops=None)
```

> Color Ramp

> Node [Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

#### Arguments:
- **stops** (_list of tuple(float, tuple)_ = None) : stops made of (float, color as tuple of floats)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### ColorTemperature()

> classmethod

``` python
ColorTemperature(value=0.0, name='Color Temperature', min=None, max=None, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Wave Length group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Color Temperature)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)
- **panel** ( = None)
- **default_attribute** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### combine_color()

> method

``` python
combine_color(green=None, blue=None, mode='RGB')
```

> Node [Combine Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Information:
- **Socket** : self



#### Arguments:
- **green** (_Float_ = None) : socket 'Green' (id: Green)
- **blue** (_Float_ = None) : socket 'Blue' (id: Blue)
- **mode** (_str_ = RGB) : parameter 'mode' in ('RGB', 'HSV', 'HSL')



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### combine_color_HSL()

> method

``` python
combine_color_HSL(saturation=None, lightness=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### combine_color_HSV()

> method

``` python
combine_color_HSV(saturation=None, value=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### combine_color_RGB()

> method

``` python
combine_color_RGB(green=None, blue=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### compare()

> method

``` python
compare(value=None, epsilon=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### dial_gizmo()

> method

``` python
dial_gizmo(*value, position=None, up=None, screen_space=None, radius=None, color_id='PRIMARY')
```

> Node ERROR: Node 'Dial Gizmo' not found

#### Arguments:
- **value** (_Float_) : socket 'Value' (id: Value)
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **up** (_Vector_ = None) : socket 'Up' (id: Up)
- **screen_space** (_Boolean_ = None) : socket 'Screen Space' (id: Screen Space)
- **radius** (_Float_ = None) : socket 'Radius' (id: Radius)
- **color_id** (_str_ = PRIMARY) : parameter 'color_id' in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### displacement()

> method

``` python
displacement(midlevel=None, scale=None, normal=None, space='OBJECT')
```

> Node [Displacement](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/displacement.html)

#### Information:
- **Socket** : self



#### Arguments:
- **midlevel** (_Float_ = None) : socket 'Midlevel' (id: Midlevel)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)
- **space** (_str_ = OBJECT) : parameter 'space' in ('OBJECT', 'WORLD')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Distance()

> classmethod

``` python
Distance(value=0.0, name='Distance', min=None, max=None, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Distance group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Distance)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)
- **panel** ( = None)
- **default_attribute** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### divide()

> method

``` python
divide(value=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b=None, epsilon=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Factor()

> classmethod

``` python
Factor(value=0.0, name='Factor', min=0, max=1, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Factor group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Factor)
- **min** ( = 0)
- **max** ( = 1)
- **tip** ( = None)
- **panel** ( = None)
- **default_attribute** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### float_curve()

> method

``` python
float_curve(factor=None)
```

> Node ERROR: Node 'Float Curve' not found

#### Information:
- **Socket** : self



#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### floored_modulo()

> method

``` python
floored_modulo(value=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Frequency()

> classmethod

``` python
Frequency(value=0.0, name='Frequency', min=None, max=None, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Wave Length group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Frequency)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)
- **panel** ( = None)
- **default_attribute** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### fresnel()

> method

``` python
fresnel(normal=None)
```

> Node [Fresnel](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/fresnel.html)

#### Information:
- **Socket** : self



#### Arguments:
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Gabor()

> classmethod

``` python
Gabor(vector=None, scale=None, frequency=None, anisotropy=None, orientation=None, gabor_type='2D')
```

> Node [Gabor Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gabor.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **frequency** (_Float_ = None) : socket 'Frequency' (id: Frequency)
- **anisotropy** (_Float_ = None) : socket 'Anisotropy' (id: Anisotropy)
- **orientation** (_Float_ = None) : socket 'Orientation' (id: Orientation 2D)
- **gabor_type** (_str_ = 2D) : parameter 'gabor_type' in ('2D', '3D')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### greater_equal()

> method

``` python
greater_equal(b=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(b=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### grid_boolean()

> method

``` python
grid_boolean(*grid_2, operation='DIFFERENCE')
```

> Node ERROR: Node 'SDF Grid Boolean' not found

#### Information:
- **Socket** : self



#### Arguments:
- **grid_2** (_Float_) : socket 'Grid 2' (id: Grid 2)
- **operation** (_str_ = DIFFERENCE) : parameter 'operation' in ('INTERSECT', 'UNION', 'DIFFERENCE')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed=None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### hue_saturation_value()

> method

``` python
hue_saturation_value(saturation=None, value=None, color=None, fac=None)
```

> Node [Hue/Saturation/Value](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/hue_saturation.html)

#### Information:
- **Socket** : self



#### Arguments:
- **saturation** (_Float_ = None) : socket 'Saturation' (id: Saturation)
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **fac** (_Float_ = None) : socket 'Fac' (id: Fac)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=0.0, name=None, min=None, max=None, tip=None, panel=None, subtype='NONE', default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Socket of type VALUE

> Node [Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/value.html)

If **value** argument is None:
- if **name** argument is None, a node 'Value' is added
- otherwise a new group input is created using **min**, **max**, **tip** and **subtype**
  arguments

If **value** argument is not None, a new **Float** is created from the value, either
by transtyping or creating a 'Value' node.

``` python
float = Float()      # 'Value' node with default initial vlaue
float = Float(3.14). # 'Value' node with 3.14 initial value
float = Float(3.14, name="User input", subtype='ANGLE') # Create a new Float group input
```

#### Arguments:
- **value** (_float | str | Socket_ = 0.0) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **min** (_float_ = None) : minimum value
- **max** (_float_ = None) : maximum value
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree pane if exists)
- **subtype** (_str in ('NONE', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'TIME_ABSOLUTE', 'DISTANCE', 'WAVELENGTH', 'COLOR_TEMPERATURE', 'FREQUENCY')_ = NONE) : sub type for group input
- **default_attribute** (_str_ = ) : default attribute name
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### layer_weight()

> method

``` python
layer_weight(normal=None)
```

> Node [Layer Weight](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/layer_weight.html)

#### Information:
- **Socket** : self



#### Arguments:
- **normal** (_Vector_ = None) : socket 'Normal' (id: Normal)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### less_equal()

> method

``` python
less_equal(b=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(b=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### light_falloff()

> method

``` python
light_falloff(smooth=None)
```

> Node [Light Falloff](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/light_falloff.html)

#### Information:
- **Socket** : self



#### Arguments:
- **smooth** (_Float_ = None) : socket 'Smooth' (id: Smooth)



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### linear_gizmo()

> method

``` python
linear_gizmo(*value, position=None, direction=None, color_id='PRIMARY', draw_style='ARROW')
```

> Node ERROR: Node 'Linear Gizmo' not found

#### Arguments:
- **value** (_Float_) : socket 'Value' (id: Value)
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **direction** (_Vector_ = None) : socket 'Direction' (id: Direction)
- **color_id** (_str_ = PRIMARY) : parameter 'color_id' in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')
- **draw_style** (_str_ = ARROW) : parameter 'draw_style' in ('ARROW', 'CROSS', 'BOX')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### log()

> method

``` python
log(base=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range()

> method

``` python
map_range(from_min=None, from_max=None, to_min=None, to_max=None, clamp=True, interpolation_type='LINEAR')
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type



#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (id: To Max)
- **clamp** (_bool_ = True) : parameter 'clamp'
- **interpolation_type** (_str_ = LINEAR) : parameter 'interpolation_type' in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range_linear()

> method

``` python
map_range_linear(from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type
- **Parameter** : 'LINEAR'



#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (id: To Max)
- **clamp** (_bool_ = True) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range_smoother_step()

> method

``` python
map_range_smoother_step(from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type
- **Parameter** : 'SMOOTHERSTEP'



#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (id: To Max)
- **clamp** (_bool_ = True) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range_smooth_step()

> method

``` python
map_range_smooth_step(from_min=None, from_max=None, to_min=None, to_max=None, clamp=True)
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type
- **Parameter** : 'SMOOTHSTEP'



#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (id: To Max)
- **clamp** (_bool_ = True) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range_stepped()

> method

``` python
map_range_stepped(from_min=None, from_max=None, to_min=None, to_max=None, steps=None, clamp=True)
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : depending on 'from_min' type
- **Parameter** : 'STEPPED'



#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (id: From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (id: From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (id: To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (id: To Max)
- **steps** (_Float_ = None) : socket 'Steps' (id: Steps)
- **clamp** (_bool_ = True) : parameter 'clamp'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### max()

> method

``` python
max(value=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### mgreater_than()

> method

``` python
mgreater_than(threshold=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### min()

> method

``` python
min(value=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### mix()

> method

``` python
mix(factor=None, other=None, clamp_factor=None)
```

> Mix

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor_Float)
- **other** (_Socket_ = None) : socket 'B' (B_Float)
- **clamp_factor** (_bool_ = None) : Node.clamp_factor



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### mless_than()

> method

``` python
mless_than(threshold=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### modulo()

> method

``` python
modulo(value=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(value=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### multiply_add()

> method

``` python
multiply_add(multiplier=None, addend=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Noise()

> classmethod

``` python
Noise(vector=None, scale=None, detail=None, roughness=None, lacunarity=None, distortion=None, noise_dimensions='3D', noise_type='FBM', normalize=True)
```

> Node [Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (id: Lacunarity)
- **distortion** (_Float_ = None) : socket 'Distortion' (id: Distortion)
- **noise_dimensions** (_str_ = 3D) : parameter 'noise_dimensions' in ('1D', '2D', '3D', '4D')
- **noise_type** (_str_ = FBM) : parameter 'noise_type' in ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
- **normalize** (_bool_ = True) : parameter 'normalize'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### normal_map()

> method

``` python
normal_map(color=None, space='TANGENT', uv_map='')
```

> Node [Normal Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/normal_map.html)

#### Information:
- **Socket** : self



#### Arguments:
- **color** (_Color_ = None) : socket 'Color' (id: Color)
- **space** (_str_ = TANGENT) : parameter 'space' in ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')
- **uv_map** (_str_ = ) : parameter 'uv_map'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(b=None, epsilon=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### out()

> method

``` python
out(name=None, **props)
```

> Connect to output

:sunrise: **ShaderNodes** only


> [!IMPORTANT]
> - Geometry Nodes : create a group output socket with the provided name
> - Shader : create a node [AOV Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/aov.html)

#### Arguments:
- **name** ( = None)
- **props**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Percentage()

> classmethod

``` python
Percentage(value=0.0, name='Percentage', min=0, max=100, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Percentage group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Percentage)
- **min** ( = 0)
- **max** ( = 100)
- **tip** ( = None)
- **panel** ( = None)
- **default_attribute** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### pingpong()

> method

``` python
pingpong(scale=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### power()

> method

``` python
power(exponent=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(min=None, max=None, id=None, seed=None)
```

> Random float

> Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Arguments:
- **min** ( = None)
- **max** ( = None)
- **id** ( = None)
- **seed** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### sample_grid()

> method

``` python
sample_grid(position=None, interpolation_mode='TRILINEAR')
```

> Node ERROR: Node 'Sample Grid' not found

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation_mode** (_str_ = TRILINEAR) : parameter 'interpolation_mode' in ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x=None, y=None, z=None)
```

> Node ERROR: Node 'Sample Grid Index' not found

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **x** (_Integer_ = None) : socket 'X' (id: X)
- **y** (_Integer_ = None) : socket 'Y' (id: Y)
- **z** (_Integer_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### scene_time()

> classmethod

``` python
scene_time()
```

> Node [Scene Time](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/scene_time.html)

#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### sdf_difference()

> method

``` python
sdf_difference(*grid_2)
```

> Node ERROR: Node 'SDF Grid Boolean' not found

#### Information:
- **Socket** : self
- **Parameter** : 'DIFFERENCE'



#### Arguments:
- **grid_2** (_Float_) : socket 'Grid 2' (id: Grid 2)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### sdf_intersect()

> method

``` python
sdf_intersect(*grid)
```

> Node ERROR: Node 'SDF Grid Boolean' not found

#### Information:
- **Parameter** : 'INTERSECT'



#### Arguments:
- **grid** (_Float_) : socket 'Grid' (id: Grid 2)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### sdf_union()

> method

``` python
sdf_union(*grid)
```

> Node ERROR: Node 'SDF Grid Boolean' not found

#### Information:
- **Parameter** : 'UNION'



#### Arguments:
- **grid** (_Float_) : socket 'Grid' (id: Grid 2)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### smooth_max()

> method

``` python
smooth_max(value=None, distance=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### smooth_min()

> method

``` python
smooth_min(value=None, distance=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### snap()

> method

``` python
snap(increment=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### subtract()

> method

``` python
subtract(value=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Time()

> classmethod

``` python
Time(value=0.0, name='Time', min=None, max=None, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Time group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Time)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)
- **panel** ( = None)
- **default_attribute** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### TimeAbsolute()

> classmethod

``` python
TimeAbsolute(value=0.0, name='Time Absolute', min=None, max=None, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Time Absolute group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Time Absolute)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)
- **panel** ( = None)
- **default_attribute** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### to_integer()

> method

``` python
to_integer(rounding_mode='ROUND')
```

> Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)

#### Information:
- **Socket** : self



#### Arguments:
- **rounding_mode** (_str_ = ROUND) : parameter 'rounding_mode' in ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### to_mesh()

> method

``` python
to_mesh(threshold=None, adaptivity=None)
```

> Node ERROR: Node 'Grid to Mesh' not found

#### Information:
- **Socket** : self



#### Arguments:
- **threshold** (_Float_ = None) : socket 'Threshold' (id: Threshold)
- **adaptivity** (_Float_ = None) : socket 'Adaptivity' (id: Adaptivity)



#### Returns:
- **Mesh** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### to_string()

> method

``` python
to_string(decimals=None)
```

> Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Arguments:
- **decimals** (_Integer_ = None) : socket 'Decimals' (id: Decimals)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Voronoi()

> classmethod

``` python
Voronoi(vector=None, scale=None, detail=None, roughness=None, lacunarity=None, randomness=None, distance='EUCLIDEAN', feature='F1', normalize=False, voronoi_dimensions='3D')
```

> Node [Voronoi Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **roughness** (_Float_ = None) : socket 'Roughness' (id: Roughness)
- **lacunarity** (_Float_ = None) : socket 'Lacunarity' (id: Lacunarity)
- **randomness** (_Float_ = None) : socket 'Randomness' (id: Randomness)
- **distance** (_str_ = EUCLIDEAN) : parameter 'distance' in ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI')
- **feature** (_str_ = F1) : parameter 'feature' in ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS')
- **normalize** (_bool_ = False) : parameter 'normalize'
- **voronoi_dimensions** (_str_ = 3D) : parameter 'voronoi_dimensions' in ('1D', '2D', '3D', '4D')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### WaveLength()

> classmethod

``` python
WaveLength(value=0.0, name='Wave Length', min=None, max=None, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Wave Length group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Wave Length)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)
- **panel** ( = None)
- **default_attribute** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### wavelength()

> method

``` python
wavelength()
```

> Node [Wavelength](https://docs.blender.org/manual/en/latest/render/shader_nodes/converter/wavelength.html)

#### Information:
- **Socket** : self



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### WhiteNoise()

> classmethod

``` python
WhiteNoise(vector=None, noise_dimensions='3D')
```

> Node [White Noise Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **noise_dimensions** (_str_ = 3D) : parameter 'noise_dimensions' in ('1D', '2D', '3D', '4D')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### wrap()

> method

``` python
wrap(max=None, min=None, use_clamp=False)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>