# Color

``` python
Color(value=(0.0, 0.0, 0.0, 1.0), name=None, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

Socket of type COLOR (RGBA)

> Nodes [RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../render/shader_nodes/input/rgb.html) [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html) [Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/color.html)

#### Arguments:
- **value** (_tuple or Socket_ = (0.0, 0.0, 0.0, 1.0)) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree panel if exists)
- **default_attribute** (_str_ = ) : default attribute name
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **A** : [alpha](color.md#alpha) :black_small_square: [ambient_occlusion](color.md#ambient_occlusion) :black_small_square: [aov_output](color.md#aov_output) :black_small_square: [Attribute](color.md#attribute)
- **B** : [background](color.md#background) :black_small_square: [Blackbody](color.md#blackbody) :black_small_square: [blue](color.md#blue) :black_small_square: [blur](color.md#blur) :black_small_square: [Brick](color.md#brick) :black_small_square: [brighter](color.md#brighter) :black_small_square: [brightness_contrast](color.md#brightness_contrast)
- **C** : [Checker](color.md#checker) :black_small_square: [ColorAttribute](color.md#colorattribute) :black_small_square: [ColorRamp](color.md#colorramp) :black_small_square: [Combine](color.md#combine) :black_small_square: [CombineHSL](color.md#combinehsl) :black_small_square: [CombineHSV](color.md#combinehsv) :black_small_square: [CombineRGB](color.md#combinergb)
- **D** : [darker](color.md#darker)
- **E** : [equal](color.md#equal)
- **F** : [FromShader](color.md#fromshader)
- **G** : [gamma](color.md#gamma) :black_small_square: [Gradient](color.md#gradient) :black_small_square: [green](color.md#green)
- **H** : [hash_value](color.md#hash_value) :black_small_square: [hsv](color.md#hsv) :black_small_square: [hue](color.md#hue) :black_small_square: [hue_saturation_value](color.md#hue_saturation_value)
- **I** : [ImageTexture](color.md#imagetexture) :black_small_square: [\_\_init__](color.md#__init__) :black_small_square: [invert](color.md#invert) :black_small_square: [invert_color](color.md#invert_color)
- **L** : [lightness](color.md#lightness) :black_small_square: [line_style_output](color.md#line_style_output)
- **M** : [Magic](color.md#magic) :black_small_square: [mix](color.md#mix) :black_small_square: [mix_add](color.md#mix_add) :black_small_square: [mix_burn](color.md#mix_burn) :black_small_square: [mix_color](color.md#mix_color) :black_small_square: [mix_darken](color.md#mix_darken) :black_small_square: [mix_difference](color.md#mix_difference) :black_small_square: [mix_divide](color.md#mix_divide) :black_small_square: [mix_dodge](color.md#mix_dodge) :black_small_square: [mix_exclusion](color.md#mix_exclusion) :black_small_square: [mix_hue](color.md#mix_hue) :black_small_square: [mix_lighten](color.md#mix_lighten) :black_small_square: [mix_linear_light](color.md#mix_linear_light) :black_small_square: [mix_mix](color.md#mix_mix) :black_small_square: [mix_multiply](color.md#mix_multiply) :black_small_square: [mix_overlay](color.md#mix_overlay) :black_small_square: [mix_saturation](color.md#mix_saturation) :black_small_square: [mix_screen](color.md#mix_screen) :black_small_square: [mix_soft_light](color.md#mix_soft_light) :black_small_square: [mix_subtract](color.md#mix_subtract) :black_small_square: [mix_value](color.md#mix_value)
- **N** : [Named](color.md#named) :black_small_square: [NamedAttribute](color.md#namedattribute) :black_small_square: [normal_map](color.md#normal_map) :black_small_square: [not_equal](color.md#not_equal)
- **O** : [out](color.md#out)
- **R** : [red](color.md#red) :black_small_square: [rgb](color.md#rgb) :black_small_square: [RGB](color.md#rgb) :black_small_square: [rgb_curves](color.md#rgb_curves) :black_small_square: [rgb_to_bw](color.md#rgb_to_bw)
- **S** : [saturation](color.md#saturation) :black_small_square: [separate](color.md#separate) :black_small_square: [separate_col](color.md#separate_col) :black_small_square: [separate_col_HSL](color.md#separate_col_hsl) :black_small_square: [separate_col_HSV](color.md#separate_col_hsv) :black_small_square: [separate_color](color.md#separate_color) :black_small_square: [separate_col_RGB](color.md#separate_col_rgb) :black_small_square: [separate_HSL](color.md#separate_hsl) :black_small_square: [separate_HSV](color.md#separate_hsv) :black_small_square: [separate_RGB](color.md#separate_rgb) :black_small_square: [SkyTexture](color.md#skytexture)
- **T** : [to_bw](color.md#to_bw)
- **V** : [value](color.md#value) :black_small_square: [vector_displacement](color.md#vector_displacement)
- **W** : [Wave](color.md#wave) :black_small_square: [Wavelength](color.md#wavelength)

## Properties



### alpha

> _type_: **alpha**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### blue

> _type_: **blue**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### green

> _type_: **green**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### hsv

> _type_: **tuple**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### hue

> _type_: **hue**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### lightness

> _type_: **lightness**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### red

> _type_: **red**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### rgb

> _type_: **tuple**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### saturation

> _type_: **saturation**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### to_bw

> _type_: **Float**
>

Conversion to black and white.

:sunrise: **ShaderNodes** only

> Node [RGB to BW](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/converter/rgb_to_bw.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

### value

> _type_: **value**
>

> Property Get [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Properties](color.md#properties)</sub>

## Methods



----------
### ambient_occlusion()

> method

``` python
ambient_occlusion(distance=None, normal=None, inside=False, only_local=False, samples=16)
```

Shader node Ambient Occlusion.

:sunrise: **ShaderNodes** only

> Node [Color Attribute](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/vertex_color.html)

#### Arguments:
- **distance** (_Float_ = None) : socket
- **normal** ( = None)
- **inside** (_Vector_ = False) : socket
- **only_local** (_bool_ = False) : parameter
- **samples** (_int_ = 16) : parameter



#### Returns:
- **Color** : 'Color' socket, [ao_]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### aov_output()

> method

``` python
aov_output(value=None, aov_name='')
```

> Method [AOV Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/aov.html)

#### Information:
- **Socket** : self



#### Arguments:
- **value** (_Float_ = None) : socket 'Value' (id: Value)
- **aov_name** (_str_ = ) : parameter 'aov_name'



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Attribute()

> classmethod

``` python
Attribute(name)
```

Shader node Color Attribute.

:sunrise: **ShaderNodes** only

> Node [Color Attribute](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/vertex_color.html)

#### Arguments:
- **name** (_str_)



#### Returns:
- **Color** : 'Color' socket, [alpha_]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### background()

> method

``` python
background(strength=None)
```

> Method ERROR: Node 'Background' not found

#### Information:
- **Socket** : self



#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (id: Strength)



#### Returns:
- **Shader** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Blackbody()

> classmethod

``` python
Blackbody(temperature=None)
```

Constructor : Black body.

:sunrise: **ShaderNodes** only

> Node [Blackbody](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../modeling/geometry_nodes/utilities/color/blackbody.html)

#### Arguments:
- **temperature** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### blur()

> method

``` python
blur(iterations=None, weight=None)
```

> Method [Blur Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT_COLOR'



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)
- **weight** (_Float_ = None) : socket 'Weight' (id: Weight)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Brick()

> classmethod

``` python
Brick(vector=None, color1=None, color2=None, mortar=None, scale=None, mortar_size=None, mortar_smooth=None, bias=None, brick_width=None, row_height=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2)
```

> Constructor [Brick Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **color1** (_Color_ = None) : socket 'Color1' (id: Color1)
- **color2** (_Color_ = None) : socket 'Color2' (id: Color2)
- **mortar** (_Color_ = None) : socket 'Mortar' (id: Mortar)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **mortar_size** (_Float_ = None) : socket 'Mortar Size' (id: Mortar Size)
- **mortar_smooth** (_Float_ = None) : socket 'Mortar Smooth' (id: Mortar Smooth)
- **bias** (_Float_ = None) : socket 'Bias' (id: Bias)
- **brick_width** (_Float_ = None) : socket 'Brick Width' (id: Brick Width)
- **row_height** (_Float_ = None) : socket 'Row Height' (id: Row Height)
- **offset** (_float_ = 0.5) : parameter 'offset'
- **offset_frequency** (_int_ = 2) : parameter 'offset_frequency'
- **squash** (_float_ = 1.0) : parameter 'squash'
- **squash_frequency** (_int_ = 2) : parameter 'squash_frequency'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### brighter()

> method

``` python
brighter(b=None)
```

> Method [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RGBA'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'BRIGHTER'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_COL)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### brightness_contrast()

> method

``` python
brightness_contrast(bright=None, contrast=None)
```

Brightness and contrast.

:sunrise: **ShaderNodes** only

> Node [Brightness/Contrast](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/bright_contrast.html)

#### Arguments:
- **bright** (_Float_ = None) : socket
- **contrast** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Checker()

> classmethod

``` python
Checker(vector=None, color1=None, color2=None, scale=None)
```

> Constructor [Checker Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **color1** (_Color_ = None) : socket 'Color1' (id: Color1)
- **color2** (_Color_ = None) : socket 'Color2' (id: Color2)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### ColorAttribute()

> classmethod

``` python
ColorAttribute(layer_name='')
```

> Constructor [Color Attribute](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/vertex_color.html)

#### Arguments:
- **layer_name** (_str_ = ) : parameter 'layer_name'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### ColorRamp()

> classmethod

``` python
ColorRamp(fac=None, stops=None)
```

Constructor : Color Ramp

> Node [Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

#### Arguments:
- **fac** (_Float_ = None)
- **stops** (_list of tuple(float, tuple)_ = None) : stops made of (float, color as tuple of floats)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Combine()

> classmethod

``` python
Combine(red=None, green=None, blue=None, alpha=None, mode='RGB')
```

> Constructor [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Arguments:
- **red** (_Float_ = None) : socket 'Red' (id: Red)
- **green** (_Float_ = None) : socket 'Green' (id: Green)
- **blue** (_Float_ = None) : socket 'Blue' (id: Blue)
- **alpha** (_Float_ = None) : socket 'Alpha' (id: Alpha)
- **mode** (_str_ = RGB) : parameter 'mode' in ('RGB', 'HSV', 'HSL')



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### CombineHSL()

> classmethod

``` python
CombineHSL(hue=None, saturation=None, lightness=None, alpha=None)
```

> Constructor [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Information:
- **Parameter** : 'HSL'



#### Arguments:
- **hue** (_Float_ = None) : socket 'Hue' (id: Red)
- **saturation** (_Float_ = None) : socket 'Saturation' (id: Green)
- **lightness** (_Float_ = None) : socket 'Lightness' (id: Blue)
- **alpha** (_Float_ = None) : socket 'Alpha' (id: Alpha)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### CombineHSV()

> classmethod

``` python
CombineHSV(hue=None, saturation=None, value=None, alpha=None)
```

> Constructor [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Information:
- **Parameter** : 'HSV'



#### Arguments:
- **hue** (_Float_ = None) : socket 'Hue' (id: Red)
- **saturation** (_Float_ = None) : socket 'Saturation' (id: Green)
- **value** (_Float_ = None) : socket 'Value' (id: Blue)
- **alpha** (_Float_ = None) : socket 'Alpha' (id: Alpha)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### CombineRGB()

> classmethod

``` python
CombineRGB(red=None, green=None, blue=None, alpha=None)
```

> Constructor [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Information:
- **Parameter** : 'RGB'



#### Arguments:
- **red** (_Float_ = None) : socket 'Red' (id: Red)
- **green** (_Float_ = None) : socket 'Green' (id: Green)
- **blue** (_Float_ = None) : socket 'Blue' (id: Blue)
- **alpha** (_Float_ = None) : socket 'Alpha' (id: Alpha)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### darker()

> method

``` python
darker(b=None)
```

> Method [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RGBA'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'DARKER'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_COL)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b=None, epsilon=None)
```

> Method [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RGBA'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'EQUAL'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_COL)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### FromShader()

> classmethod

``` python
FromShader(shader)
```

Constructor : Shader to RGB.

:sunrise: **ShaderNodes** only

> Node ERROR: Node 'Shader to RGB' not found

#### Arguments:
- **shader** (_Shader_) : socket



#### Returns:
- **Color** : 'Color' socket, [alpha_]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### gamma()

> method

``` python
gamma(gamma=None)
```

Gamma.

:sunrise: **ShaderNodes** only

> Node [Gamma](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/gamma.html)

#### Arguments:
- **gamma** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Gamma' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Gradient()

> classmethod

``` python
Gradient(vector=None, gradient_type='LINEAR')
```

> Constructor [Gradient Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **gradient_type** (_str_ = LINEAR) : parameter 'gradient_type' in ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed=None)
```

> Method [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RGBA'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### hue_saturation_value()

> method

``` python
hue_saturation_value(hue=None, saturation=None, value=None, fac=None)
```

Hue / saturation / value.

:sunrise: **ShaderNodes** only

> Node [Hue/Saturation/Value](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/hue_saturation.html)

#### Arguments:
- **hue** (_Float_ = None) : socket
- **saturation** (_Float_ = None) : socket
- **value** (_Float_ = None) : socket
- **fac** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### ImageTexture()

> classmethod

``` python
ImageTexture(image=None, vector=None, frame=None, extension='REPEAT', interpolation='Linear')
```

> Constructor [Image Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html)

#### Arguments:
- **image** (_Image_ = None) : socket 'Image' (id: Image)
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **frame** (_Integer_ = None) : socket 'Frame' (id: Frame)
- **extension** (_str_ = REPEAT) : parameter 'extension' in ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR')
- **interpolation** (_str_ = Linear) : parameter 'interpolation' in ('Linear', 'Closest', 'Cubic')



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=(0.0, 0.0, 0.0, 1.0), name=None, tip=None, panel=None, default_attribute='', hide_value=False, hide_in_modifier=False, single_value=False)
```

Socket of type COLOR (RGBA)

> Nodes [RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../render/shader_nodes/input/rgb.html) [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html) [Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/color.html)

#### Arguments:
- **value** (_tuple or Socket_ = (0.0, 0.0, 0.0, 1.0)) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree panel if exists)
- **default_attribute** (_str_ = ) : default attribute name
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### invert()

> method

``` python
invert(fac=None)
```

Invert.

:sunrise: **ShaderNodes** only

> Node [Invert Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/invert_color.html)

#### Arguments:
- **fac** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### invert_color()

> method

``` python
invert_color(fac=None)
```

> Method [Invert Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/invert_color.html)

#### Information:
- **Socket** : self



#### Arguments:
- **fac** (_Float_ = None) : socket 'Fac' (id: Fac)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### line_style_output()

> method

``` python
line_style_output(color_fac=None, alpha=None, alpha_fac=None, blend_type='MIX', is_active_output=True, target='ALL', use_alpha=False, use_clamp=False)
```

> Method ERROR: Node 'Line Style Output' not found

#### Information:
- **Socket** : self



#### Arguments:
- **color_fac** (_Float_ = None) : socket 'Color Fac' (id: Color Fac)
- **alpha** (_Float_ = None) : socket 'Alpha' (id: Alpha)
- **alpha_fac** (_Float_ = None) : socket 'Alpha Fac' (id: Alpha Fac)
- **blend_type** (_str_ = MIX) : parameter 'blend_type' in ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
- **is_active_output** (_bool_ = True) : parameter 'is_active_output'
- **target** (_str_ = ALL) : parameter 'target' in ('ALL', 'EEVEE', 'CYCLES')
- **use_alpha** (_bool_ = False) : parameter 'use_alpha'
- **use_clamp** (_bool_ = False) : parameter 'use_clamp'



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Magic()

> classmethod

``` python
Magic(vector=None, scale=None, distortion=None, turbulence_depth=2)
```

> Constructor [Magic Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **distortion** (_Float_ = None) : socket 'Distortion' (id: Distortion)
- **turbulence_depth** (_int_ = 2) : parameter 'turbulence_depth'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix()

> method

``` python
mix(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MIX'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_add()

> method

``` python
mix_add(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ADD'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_burn()

> method

``` python
mix_burn(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BURN'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_color()

> method

``` python
mix_color(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'COLOR'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_darken()

> method

``` python
mix_darken(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DARKEN'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_difference()

> method

``` python
mix_difference(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIFFERENCE'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_divide()

> method

``` python
mix_divide(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_dodge()

> method

``` python
mix_dodge(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DODGE'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_exclusion()

> method

``` python
mix_exclusion(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EXCLUSION'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_hue()

> method

``` python
mix_hue(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'HUE'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_lighten()

> method

``` python
mix_lighten(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LIGHTEN'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_linear_light()

> method

``` python
mix_linear_light(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LINEAR_LIGHT'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_mix()

> method

``` python
mix_mix(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MIX'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_multiply()

> method

``` python
mix_multiply(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_overlay()

> method

``` python
mix_overlay(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'OVERLAY'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_saturation()

> method

``` python
mix_saturation(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SATURATION'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_screen()

> method

``` python
mix_screen(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SCREEN'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_soft_light()

> method

``` python
mix_soft_light(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SOFT_LIGHT'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_subtract()

> method

``` python
mix_subtract(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SUBTRACT'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### mix_value()

> method

``` python
mix_value(b=None, factor=None, clamp_factor=True, clamp_result=False)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VALUE'
- **Parameter** : 'RGBA'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_Color)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'
- **clamp_result** (_bool_ = False) : parameter 'clamp_result'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name=None)
```

> Constructor [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT_COLOR'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name=None)
```

> Constructor [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT_COLOR'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### normal_map()

> method

``` python
normal_map(strength=None, space='TANGENT', uv_map='')
```

Normal map.

:sunrise: **ShaderNodes** only

> Node [Normal Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/normal_map.html)

#### Arguments:
- **strength** (_Float_ = None) : socket
- **space** (_str_ = TANGENT) : str in ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')
- **uv_map** ( = )



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(b=None, epsilon=None)
```

> Method [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RGBA'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'NOT_EQUAL'



#### Arguments:
- **b** (_Color_ = None) : socket 'B' (id: B_COL)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### out()

> method

``` python
out(name=None)
```

> Connect to output

:sunrise: **ShaderNodes** only


> [!IMPORTANT]
> - Geometry Nodes : create a group output socket with the provided name
> - Shader : create a node [AOV Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/aov.html)

#### Arguments:
- **name** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### RGB()

> classmethod

``` python
RGB()
```

> Constructor [RGB](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/rgb.html)

#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### rgb_curves()

> method

``` python
rgb_curves(fac=None)
```

> Method [RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/rgb_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **fac** (_Float_ = None) : socket 'Fac' (id: Fac)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### rgb_to_bw()

> method

``` python
rgb_to_bw()
```

> Method [RGB to BW](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/converter/rgb_to_bw.html)

#### Information:
- **Socket** : self



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### separate()

> method

``` python
separate(mode='RGB')
```

> Method [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Information:
- **Socket** : self



#### Arguments:
- **mode** (_str_ = RGB) : parameter 'mode' in ('RGB', 'HSV', 'HSL')



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### separate_col()

> method

``` python
separate_col(mode='RGB')
```

> Method [Separate Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Information:
- **Socket** : self



#### Arguments:
- **mode** (_str_ = RGB) : parameter 'mode' in ('RGB', 'HSV', 'HSL')



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### separate_col_HSL()

> method

``` python
separate_col_HSL()
```

> Method [Separate Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'HSL'



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### separate_col_HSV()

> method

``` python
separate_col_HSV()
```

> Method [Separate Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'HSV'



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### separate_color()

> method

``` python
separate_color()
```

> Method [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RGB'



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### separate_col_RGB()

> method

``` python
separate_col_RGB()
```

> Method [Separate Color](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RGB'



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### separate_HSL()

> method

``` python
separate_HSL()
```

> Method [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'HSL'



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### separate_HSV()

> method

``` python
separate_HSV()
```

> Method [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'HSV'



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### separate_RGB()

> method

``` python
separate_RGB()
```

> Method [Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

#### Information:
- **Socket** : self
- **Parameter** : 'RGB'



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### SkyTexture()

> classmethod

``` python
SkyTexture(air_density=1.0, altitude=0.0, dust_density=1.0, ground_albedo=0.30000001192092896, ozone_density=1.0, sky_type='NISHITA', sun_disc=True, sun_elevation=0.2617993950843811, sun_intensity=1.0, sun_rotation=0.0, sun_size=0.009512044489383698, turbidity=2.200000047683716)
```

> Constructor [Sky Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/sky.html)

#### Arguments:
- **air_density** (_float_ = 1.0) : parameter 'air_density'
- **altitude** (_float_ = 0.0) : parameter 'altitude'
- **dust_density** (_float_ = 1.0) : parameter 'dust_density'
- **ground_albedo** (_float_ = 0.30000001192092896) : parameter 'ground_albedo'
- **ozone_density** (_float_ = 1.0) : parameter 'ozone_density'
- **sky_type** (_str_ = NISHITA) : parameter 'sky_type' in ('PREETHAM', 'HOSEK_WILKIE', 'NISHITA')
- **sun_disc** (_bool_ = True) : parameter 'sun_disc'
- **sun_elevation** (_float_ = 0.2617993950843811) : parameter 'sun_elevation'
- **sun_intensity** (_float_ = 1.0) : parameter 'sun_intensity'
- **sun_rotation** (_float_ = 0.0) : parameter 'sun_rotation'
- **sun_size** (_float_ = 0.009512044489383698) : parameter 'sun_size'
- **turbidity** (_float_ = 2.200000047683716) : parameter 'turbidity'



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### vector_displacement()

> method

``` python
vector_displacement(midlevel=None, scale=None, space='TANGENT')
```

Vector displacement

:sunrise: **ShaderNodes** only

> Node [Vector Displacement](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/vector_displacement.html)

#### Arguments:
- **midlevel** (_Float_ = None) : socket
- **scale** (_Float_ = None) : socket
- **space** (_str_ = TANGENT) : str in ('TANGENT', 'OBJECT', 'WORLD')



#### Returns:
- **Vector** : 'Displacement' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Wave()

> classmethod

``` python
Wave(vector=None, scale=None, distortion=None, detail=None, detail_scale=None, detail_roughness=None, phase_offset=None, bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS')
```

> Constructor [Wave Texture](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)
- **distortion** (_Float_ = None) : socket 'Distortion' (id: Distortion)
- **detail** (_Float_ = None) : socket 'Detail' (id: Detail)
- **detail_scale** (_Float_ = None) : socket 'Detail Scale' (id: Detail Scale)
- **detail_roughness** (_Float_ = None) : socket 'Detail Roughness' (id: Detail Roughness)
- **phase_offset** (_Float_ = None) : socket 'Phase Offset' (id: Phase Offset)
- **bands_direction** (_str_ = X) : parameter 'bands_direction' in ('X', 'Y', 'Z', 'DIAGONAL')
- **rings_direction** (_str_ = X) : parameter 'rings_direction' in ('X', 'Y', 'Z', 'SPHERICAL')
- **wave_profile** (_str_ = SIN) : parameter 'wave_profile' in ('SIN', 'SAW', 'TRI')
- **wave_type** (_str_ = BANDS) : parameter 'wave_type' in ('BANDS', 'RINGS')



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>

----------
### Wavelength()

> classmethod

``` python
Wavelength(wavelength=None)
```

Constructor : Wave Length.

:sunrise: **ShaderNodes** only

> Node [Wavelength](https://docs.blender.org/manual/en/latest/render/shader_nodes/converter/wavelength.html)

#### Arguments:
- **wavelength** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](color.md#color) :black_small_square: [Content](color.md#content) :black_small_square: [Methods](color.md#methods)</sub>