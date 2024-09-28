# Color

> Bases classes: [ValueSocket](geono-socke-valuesocket.md#valuesocket)

``` python
Color(value=(0.0, 0.0, 0.0, 1.0), name=None, tip=None)
```

Socket of type COLOR (RGBA)

[RGB](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../render/shader_nodes/input/rgb.html), [Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html), [Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/color.html)

#### Arguments:
- **value** (_tuple or Socket_ = (0.0, 0.0, 0.0, 1.0)) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [Named](geono-socke-valuesocket.md#named) :black_small_square: [NamedAttribute](geono-socke-valuesocket.md#namedattribute) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square:

## Content

- **A** : [add](geono-color.md#add) :black_small_square: [alpha](geono-color.md#alpha) :black_small_square: [ambient_occlusion](geono-color.md#ambient_occlusion) :black_small_square: [Attribute](geono-color.md#attribute)
- **B** : [Blackbody](geono-color.md#blackbody) :black_small_square: [blue](geono-color.md#blue) :black_small_square: [brighter](geono-color.md#brighter) :black_small_square: [brightness_contrast](geono-color.md#brightness_contrast) :black_small_square: [burn](geono-color.md#burn)
- **C** : [ColorRamp](geono-color.md#colorramp) :black_small_square: [Combine](geono-color.md#combine) :black_small_square: [CombineHSL](geono-color.md#combinehsl) :black_small_square: [CombineHSV](geono-color.md#combinehsv) :black_small_square: [CombineRGB](geono-color.md#combinergb) :black_small_square: [curves](geono-color.md#curves)
- **D** : [darken](geono-color.md#darken) :black_small_square: [darker](geono-color.md#darker) :black_small_square: [difference](geono-color.md#difference) :black_small_square: [divide](geono-color.md#divide) :black_small_square: [dodge](geono-color.md#dodge)
- **E** : [equal](geono-color.md#equal) :black_small_square: [exclusion](geono-color.md#exclusion)
- **F** : [FromShader](geono-color.md#fromshader)
- **G** : [gamma](geono-color.md#gamma) :black_small_square: [green](geono-color.md#green)
- **H** : [HSL](geono-color.md#hsl) :black_small_square: [HSV](geono-color.md#hsv) :black_small_square: [hue](geono-color.md#hue) :black_small_square: [hue_saturation_value](geono-color.md#hue_saturation_value)
- **I** : [invert](geono-color.md#invert)
- **L** : [lighten](geono-color.md#lighten) :black_small_square: [lightness](geono-color.md#lightness) :black_small_square: [linear_light](geono-color.md#linear_light)
- **M** : [mix](geono-color.md#mix) :black_small_square: [mix_color](geono-color.md#mix_color) :black_small_square: [mix_hue](geono-color.md#mix_hue) :black_small_square: [mix_saturation](geono-color.md#mix_saturation) :black_small_square: [mix_value](geono-color.md#mix_value) :black_small_square: [multiply](geono-color.md#multiply)
- **N** : [normal_map](geono-color.md#normal_map) :black_small_square: [not_equal](geono-color.md#not_equal)
- **O** : [overlay](geono-color.md#overlay)
- **R** : [red](geono-color.md#red) :black_small_square: [RGB](geono-color.md#rgb)
- **S** : [saturation](geono-color.md#saturation) :black_small_square: [screen](geono-color.md#screen) :black_small_square: [soft_light](geono-color.md#soft_light) :black_small_square: [subtract](geono-color.md#subtract)
- **T** : [to_bw](geono-color.md#to_bw) :black_small_square: [to_output](geono-color.md#to_output)
- **V** : [value](geono-color.md#value) :black_small_square: [vector_displacement](geono-color.md#vector_displacement)
- **W** : [Wavelength](geono-color.md#wavelength)

## Properties



### alpha

> _type_: **Float**
>

Alpha component

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### blue

> _type_: **Float**
>

Blue component

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### green

> _type_: **Float**
>

Green component

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### HSL

> _type_: **Node**
>

Separate HSL Node

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### HSV

> _type_: **Node**
>

Separate HSV Node

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### hue

> _type_: **Float**
>

Hue component

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### lightness

> _type_: **Float**
>

Lightness component

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### red

> _type_: **Float**
>

Red component

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### RGB

> _type_: **Node**
>

Separate RGB Node

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### saturation

> _type_: **Float**
>

Saturation component

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### to_bw

> _type_: **Float**
>

Conversion to black and white.

> ShaderNodes only

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

### value

> _type_: **Float**
>

Value component

[Separate Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/separate_color.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Properties](geono-color.md#properties)</sub>

## Methods



----------
### add()

> method

``` python
add(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : ADD

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### ambient_occlusion()

> method

``` python
ambient_occlusion(distance=None, normal=None, inside=False, only_local=False, samples=16)
```

Shader node Ambient Occlusion.

> ShaderNodes only



#### Arguments:
- **distance** (_Float_ = None) : socket
- **normal** ( = None)
- **inside** (_Vector_ = False) : socket
- **only_local** (_bool_ = False) : parameter
- **samples** (_int_ = 16) : parameter



#### Returns:
- **Color** : 'Color' socket, [ao_]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### Attribute()

> classmethod

``` python
Attribute(name)
```

Shader node Color Attribute.

> ShaderNodes only



#### Arguments:
- **name** (_str_)



#### Returns:
- **Color** : 'Color' socket, [alpha_]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### Blackbody()

> classmethod

``` python
Blackbody(temperature=None)
```

Constructor : Black body.

> ShaderNodes only



#### Arguments:
- **temperature** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### brighter()

> method

``` python
brighter(other)
```

Compare with another Color : BRIGHTER

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Color_) : socket



#### Returns:
- **Boolean** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### brightness_contrast()

> method

``` python
brightness_contrast(bright=None, contrast=None)
```

Brightness and contrast.

> ShaderNodes only



#### Arguments:
- **bright** (_Float_ = None) : socket
- **contrast** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### burn()

> method

``` python
burn(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : BURN

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### ColorRamp()

> classmethod

``` python
ColorRamp(fac=None, keep=None)
```

Constructor : Color Ramp

[Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

#### Arguments:
- **fac** (_Float_ = None)
- **keep** ( = None)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### Combine()

> classmethod

``` python
Combine(a=0, b=0, c=0, alpha=1, mode='RGB')
```

Constructor : Combine Color

[Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Arguments:
- **a** (_Float_ = 0) : depending on mode
- **b** (_Float_ = 0) : depending on mode
- **c** (_Float_ = 0) : depending on mode
- **alpha** (_Float_ = 1) : alpha component
- **mode** (_str_ = RGB)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### CombineHSL()

> classmethod

``` python
CombineHSL(hue=0, saturation=0, lightness=0, alpha=1)
```

Constructor : Combine Color from HSL

[Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Arguments:
- **hue** (_Float_ = 0)
- **saturation** (_Float_ = 0)
- **lightness** (_Float_ = 0)
- **alpha** (_Float_ = 1)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### CombineHSV()

> classmethod

``` python
CombineHSV(hue=0, saturation=0, value=0, alpha=1)
```

Constructor : Combine Color from HSV

[Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Arguments:
- **hue** (_Float_ = 0)
- **saturation** (_Float_ = 0)
- **value** (_Float_ = 0)
- **alpha** (_Float_ = 1)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### CombineRGB()

> classmethod

``` python
CombineRGB(red=0, green=0, blue=0, alpha=1)
```

Constructor : Combine Color from RGB

[Combine Color](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/combine_color.html)

#### Arguments:
- **red** (_Float_ = 0)
- **green** (_Float_ = 0)
- **blue** (_Float_ = 0)
- **alpha** (_Float_ = 1)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### curves()

> method

``` python
curves(fac=None, keep=None)
```

Color curves.

[RGB Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/rgb_curves.html)

#### Arguments:
- **fac** (_Float_ = None) : socket
- **keep** ( = None)



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### darken()

> method

``` python
darken(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : DARKEN

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### darker()

> method

``` python
darker(other)
```

Compare with another Color : DARKER

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Color_) : socket



#### Returns:
- **Boolean** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### difference()

> method

``` python
difference(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : DIFFERENCE

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### divide()

> method

``` python
divide(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : DIVIDE

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### dodge()

> method

``` python
dodge(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : DODGE

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### equal()

> method

``` python
equal(other, epsilon=None)
```

Compare with another Color : EQUAL

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Color_) : socket
- **epsilon** (_Float_ = None) : socket



#### Returns:
- **Boolean** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### exclusion()

> method

``` python
exclusion(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : EXCLUSION

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### FromShader()

> classmethod

``` python
FromShader(shader)
```

Constructor : Shader to RGB.

> ShaderNodes only



#### Arguments:
- **shader** (_Shader_) : socket



#### Returns:
- **Color** : 'Color' socket, [alpha_]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### gamma()

> method

``` python
gamma(gamma=None)
```

Gamma.

> ShaderNodes only



#### Arguments:
- **gamma** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Gamma' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### hue_saturation_value()

> method

``` python
hue_saturation_value(hue=None, saturation=None, value=None, fac=None)
```

Hue / saturation / value.

> ShaderNodes only



#### Arguments:
- **hue** (_Float_ = None) : socket
- **saturation** (_Float_ = None) : socket
- **value** (_Float_ = None) : socket
- **fac** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### invert()

> method

``` python
invert(fac=None)
```

Invert.

> ShaderNodes only



#### Arguments:
- **fac** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### lighten()

> method

``` python
lighten(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : LIGHTEN

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### linear_light()

> method

``` python
linear_light(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : LINEAR LIGHT

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### mix()

> method

``` python
mix(factor=None, other=None, clamp_result=False, clamp_factor=True, blend_type='MIX')
```

Mix with another color

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag
- **blend_type** (_str_ = MIX)



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### mix_color()

> method

``` python
mix_color(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : COLOR

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### mix_hue()

> method

``` python
mix_hue(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : HUE

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### mix_saturation()

> method

``` python
mix_saturation(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : SATURATION

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### mix_value()

> method

``` python
mix_value(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : VALUE

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : MULTIPLY

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### normal_map()

> method

``` python
normal_map(strength=None, space='TANGENT', uv_map='')
```

Normal map.

> ShaderNodes only



#### Arguments:
- **strength** (_Float_ = None) : socket
- **space** (_str_ = TANGENT) : str in ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')
- **uv_map** ( = )



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(other, epsilon=None)
```

Compare with another Color : NOT EQUAL

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Color_) : socket
- **epsilon** (_Float_ = None) : socket



#### Returns:
- **Boolean** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### overlay()

> method

``` python
overlay(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : OVERLAY

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### screen()

> method

``` python
screen(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : SCREEN

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### soft_light()

> method

``` python
soft_light(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : SOFT LIGHT

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### subtract()

> method

``` python
subtract(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : SUBTRACT

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** : 'Result' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### to_output()

> method

``` python
to_output(name=None)
```

> Connect to the output node

> [!IMPORTANT]
> Behaves differently in GeoNodes and ShaderNodes



> 
> - Geometry Nodes : create a group output socket with the provided name
> - Shader : create a node 'AOV Ouput'

#### Arguments:
- **name** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### vector_displacement()

> method

``` python
vector_displacement(midlevel=None, scale=None, space='TANGENT')
```

Vector displacement

> ShaderNodes only



#### Arguments:
- **midlevel** (_Float_ = None) : socket
- **scale** (_Float_ = None) : socket
- **space** (_str_ = TANGENT) : str in ('TANGENT', 'OBJECT', 'WORLD')



#### Returns:
- **Vector** : 'Displacement' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>

----------
### Wavelength()

> classmethod

``` python
Wavelength(wavelength=None)
```

Constructor : Wave Length.

> ShaderNodes only



#### Arguments:
- **wavelength** (_Float_ = None) : socket



#### Returns:
- **Color** : 'Color' socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color.md#color) :black_small_square: [Content](geono-color.md#content) :black_small_square: [Methods](geono-color.md#methods)</sub>