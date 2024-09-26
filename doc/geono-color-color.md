# Color

> Bases classes: [VectorLike](geono-vecto-vectorlike.md#vectorlike)

``` python
Color(value=(0.0, 0.0, 0.0, 1.0), name=None, tip=None)
```

Socket of type COLOR (RGBA)

[!Node] RGB, Combine Color, Color

#### Arguments:
- **value** (_tuple or Socket_ = (0.0, 0.0, 0.0, 1.0)) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[\_\_abs__](geono-vecto-vectorlike.md#__abs__) :black_small_square: [\_\_add__](geono-vecto-vectorlike.md#__add__) :black_small_square: [blur](geono-socke-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [\_\_ceil__](geono-vecto-vectorlike.md#__ceil__) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_\_floor__](geono-vecto-vectorlike.md#__floor__) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [\_\_iadd__](geono-vecto-vectorlike.md#__iadd__) :black_small_square: [\_\_imod__](geono-vecto-vectorlike.md#__imod__) :black_small_square: [\_\_imul__](geono-vecto-vectorlike.md#__imul__) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [\_\_ipow__](geono-vecto-vectorlike.md#__ipow__) :black_small_square: [\_\_isub__](geono-vecto-vectorlike.md#__isub__) :black_small_square: [\_\_itruediv__](geono-vecto-vectorlike.md#__itruediv__) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [\_\_matmul__](geono-vecto-vectorlike.md#__matmul__) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [\_\_mod__](geono-vecto-vectorlike.md#__mod__) :black_small_square: [\_\_mul__](geono-vecto-vectorlike.md#__mul__) :black_small_square: [Named](geono-socke-valuesocket.md#named) :black_small_square: [NamedAttribute](geono-socke-valuesocket.md#namedattribute) :black_small_square: [\_\_neg__](geono-vecto-vectorlike.md#__neg__) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [\_\_pow__](geono-vecto-vectorlike.md#__pow__) :black_small_square: [\_\_radd__](geono-vecto-vectorlike.md#__radd__) :black_small_square: [\_reset](geono-socke-socket.md#_reset) :black_small_square: [\_\_rmod__](geono-vecto-vectorlike.md#__rmod__) :black_small_square: [\_\_rmul__](geono-vecto-vectorlike.md#__rmul__) :black_small_square: [\_\_rpow__](geono-vecto-vectorlike.md#__rpow__) :black_small_square: [\_\_rsub__](geono-vecto-vectorlike.md#__rsub__) :black_small_square: [\_\_rtruediv__](geono-vecto-vectorlike.md#__rtruediv__) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [\_\_sub__](geono-vecto-vectorlike.md#__sub__) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square: [\_\_truediv__](geono-vecto-vectorlike.md#__truediv__) :black_small_square:

## Content

- **A** : [add](geono-color-color.md#add) :black_small_square: [alpha](geono-color-color.md#alpha) :black_small_square: [ambient_occlusion](geono-color-color.md#ambient_occlusion) :black_small_square: [Attribute](geono-color-color.md#attribute)
- **B** : [Blackbody](geono-color-color.md#blackbody) :black_small_square: [blue](geono-color-color.md#blue) :black_small_square: [brighter](geono-color-color.md#brighter) :black_small_square: [brightness_contrast](geono-color-color.md#brightness_contrast) :black_small_square: [burn](geono-color-color.md#burn)
- **C** : [ColorRamp](geono-color-color.md#colorramp) :black_small_square: [Combine](geono-color-color.md#combine) :black_small_square: [CombineHSL](geono-color-color.md#combinehsl) :black_small_square: [CombineHSV](geono-color-color.md#combinehsv) :black_small_square: [CombineRGB](geono-color-color.md#combinergb) :black_small_square: [curves](geono-color-color.md#curves)
- **D** : [darken](geono-color-color.md#darken) :black_small_square: [darker](geono-color-color.md#darker) :black_small_square: [difference](geono-color-color.md#difference) :black_small_square: [divide](geono-color-color.md#divide) :black_small_square: [dodge](geono-color-color.md#dodge)
- **E** : [equal](geono-color-color.md#equal) :black_small_square: [exclusion](geono-color-color.md#exclusion)
- **F** : [FromShader](geono-color-color.md#fromshader)
- **G** : [gamma](geono-color-color.md#gamma) :black_small_square: [green](geono-color-color.md#green)
- **H** : [hue](geono-color-color.md#hue) :black_small_square: [hue_saturation_value](geono-color-color.md#hue_saturation_value)
- **I** : [invert](geono-color-color.md#invert)
- **L** : [lighten](geono-color-color.md#lighten) :black_small_square: [lightness](geono-color-color.md#lightness) :black_small_square: [linear_light](geono-color-color.md#linear_light)
- **M** : [mix](geono-color-color.md#mix) :black_small_square: [mix_color](geono-color-color.md#mix_color) :black_small_square: [mix_hue](geono-color-color.md#mix_hue) :black_small_square: [mix_saturation](geono-color-color.md#mix_saturation) :black_small_square: [mix_value](geono-color-color.md#mix_value) :black_small_square: [multiply](geono-color-color.md#multiply)
- **N** : [normal_map](geono-color-color.md#normal_map) :black_small_square: [not_equal](geono-color-color.md#not_equal)
- **O** : [overlay](geono-color-color.md#overlay)
- **R** : [red](geono-color-color.md#red)
- **S** : [saturation](geono-color-color.md#saturation) :black_small_square: [screen](geono-color-color.md#screen) :black_small_square: [soft_light](geono-color-color.md#soft_light) :black_small_square: [subtract](geono-color-color.md#subtract)
- **T** : [to_bw](geono-color-color.md#to_bw)
- **V** : [value](geono-color-color.md#value) :black_small_square: [vector_displacement](geono-color-color.md#vector_displacement)
- **W** : [Wavelength](geono-color-color.md#wavelength)

## Properties



### alpha

> _type_: **Float**
>

Alpha component

[!Node] Separate Color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Properties](geono-color-color.md#properties)</sub>

### blue

> _type_: **Float**
>

Blue component

[!Node] Separate Color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Properties](geono-color-color.md#properties)</sub>

### green

> _type_: **Float**
>

Green component

[!Node] Separate Color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Properties](geono-color-color.md#properties)</sub>

### hue

> _type_: **Float**
>

Hue component

[!Node] Separate Color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Properties](geono-color-color.md#properties)</sub>

### lightness

> _type_: **Float**
>

Lightness component

[!Node] Separate Color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Properties](geono-color-color.md#properties)</sub>

### red

> _type_: **Float**
>

Red component

[!Node] Separate Color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Properties](geono-color-color.md#properties)</sub>

### saturation

> _type_: **Float**
>

Saturation component

[!Node] Separate Color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Properties](geono-color-color.md#properties)</sub>

### to_bw

> _type_: **Float**
>

Conversion to black and white.

[!Node] RGG to BW

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Properties](geono-color-color.md#properties)</sub>

### value

> _type_: **Float**
>

Value component

[!Node] Separate Color

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Properties](geono-color-color.md#properties)</sub>

## Methods



----------
### add()

> method

``` python
add(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : ADD

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### ambient_occlusion()

> method

``` python
ambient_occlusion(distance=None, normal=None, inside=False, only_local=False, samples=16)
```

Shader node Ambient Occlusion.

[!Node] Color Attribute

#### Arguments:
- **distance** (_Float_ = None) : socket
- **normal** ( = None)
- **inside** (_Vector_ = False) : socket
- **only_local** (_bool_ = False) : parameter
- **samples** (_int_ = 16) : parameter



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### Attribute()

> classmethod

``` python
Attribute(name)
```

Shader node Color Attribute.

[!Node] Color Attribute

#### Arguments:
- **name** (_str_)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### Blackbody()

> classmethod

``` python
Blackbody(temperature=None)
```

Constructor : Black body.

[!Node] Blackbody

#### Arguments:
- **temperature** (_Float_ = None) : socket



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### brighter()

> method

``` python
brighter(other)
```

Compare with another Color : BRIGHTER

[!Node] Compare

#### Arguments:
- **other** (_Color_) : socket



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### brightness_contrast()

> method

``` python
brightness_contrast(bright=None, contrast=None)
```

Brightness and contrast.

[!Node] Brightness/Contrast

#### Arguments:
- **bright** (_Float_ = None) : socket
- **contrast** (_Float_ = None) : socket



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### burn()

> method

``` python
burn(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : BURN

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### ColorRamp()

> classmethod

``` python
ColorRamp(fac=None, keep=None)
```

Constructor : Color Ramp

[!Node] Color Ramp

#### Arguments:
- **fac** (_Float_ = None)
- **keep** ( = None)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### Combine()

> classmethod

``` python
Combine(a=0, b=0, c=0, alpha=1, mode='RGB')
```

Constructor : Combine Color

[!Node] Combine Color

#### Arguments:
- **a** (_Float_ = 0) : depending on mode
- **b** (_Float_ = 0) : depending on mode
- **c** (_Float_ = 0) : depending on mode
- **alpha** (_Float_ = 1) : alpha component
- **mode** (_str_ = RGB)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### CombineHSL()

> classmethod

``` python
CombineHSL(hue=0, saturation=0, lightness=0, alpha=1)
```

Constructor : Combine Color from HSL

[!Node] Combine Color

#### Arguments:
- **hue** (_Float_ = 0)
- **saturation** (_Float_ = 0)
- **lightness** (_Float_ = 0)
- **alpha** (_Float_ = 1)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### CombineHSV()

> classmethod

``` python
CombineHSV(hue=0, saturation=0, value=0, alpha=1)
```

Constructor : Combine Color from HSV

[!Node] Combine Color

#### Arguments:
- **hue** (_Float_ = 0)
- **saturation** (_Float_ = 0)
- **value** (_Float_ = 0)
- **alpha** (_Float_ = 1)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### CombineRGB()

> classmethod

``` python
CombineRGB(red=0, green=0, blue=0, alpha=1)
```

Constructor : Combine Color from RGB

[!Node] Combine Color

#### Arguments:
- **red** (_Float_ = 0)
- **green** (_Float_ = 0)
- **blue** (_Float_ = 0)
- **alpha** (_Float_ = 1)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### curves()

> method

``` python
curves(fac=None, keep=None)
```

Color curves.

[!Node] RGB Curves

#### Arguments:
- **fac** (_Float_ = None) : socket
- **keep** ( = None)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### darken()

> method

``` python
darken(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : DARKEN

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### darker()

> method

``` python
darker(other)
```

Compare with another Color : DARKER

[!Node] Compare

#### Arguments:
- **other** (_Color_) : socket



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### difference()

> method

``` python
difference(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : DIFFERENCE

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### divide()

> method

``` python
divide(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : DIVIDE

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### dodge()

> method

``` python
dodge(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : DODGE

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### equal()

> method

``` python
equal(other, epsilon=None)
```

Compare with another Color : EQUAL

[!Node] Compare

#### Arguments:
- **other** (_Color_) : socket
- **epsilon** (_Float_ = None) : socket



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### exclusion()

> method

``` python
exclusion(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : EXCLUSION

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### FromShader()

> classmethod

``` python
FromShader(shader)
```

Constructor : Shader to RGB.

[!Node] Shader to RGB

#### Arguments:
- **shader** (_Shader_) : socket



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### gamma()

> method

``` python
gamma(gamma=None)
```

Gamma.

[!Node] Gamma

#### Arguments:
- **gamma** (_Float_ = None) : socket



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### hue_saturation_value()

> method

``` python
hue_saturation_value(hue=None, saturation=None, value=None, fac=None)
```

Hue / saturation / value.

[!Node] Hue/Saturation/Value

#### Arguments:
- **hue** (_Float_ = None) : socket
- **saturation** (_Float_ = None) : socket
- **value** (_Float_ = None) : socket
- **fac** (_Float_ = None) : socket



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### invert()

> method

``` python
invert(fac=None)
```

Invert.

[!Node] Invert Color

#### Arguments:
- **fac** (_Float_ = None) : socket



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### lighten()

> method

``` python
lighten(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : LIGHTEN

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### linear_light()

> method

``` python
linear_light(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : LINEAR LIGHT

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### mix()

> method

``` python
mix(factor=None, other=None, clamp_result=False, clamp_factor=True, blend_type='MIX')
```

Mix with another color

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag
- **blend_type** (_str_ = MIX)



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### mix_color()

> method

``` python
mix_color(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : COLOR

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### mix_hue()

> method

``` python
mix_hue(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : HUE

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### mix_saturation()

> method

``` python
mix_saturation(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : SATURATION

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### mix_value()

> method

``` python
mix_value(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : VALUE

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : MULTIPLY

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### normal_map()

> method

``` python
normal_map(strength=None, space='TANGENT', uv_map='')
```

Normal map.

[!Node] Normal Map

#### Arguments:
- **strength** (_Float_ = None) : socket
- **space** (_str_ = TANGENT) : str in ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')
- **uv_map** ( = )



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(other, epsilon=None)
```

Compare with another Color : NOT EQUAL

[!Node] Compare

#### Arguments:
- **other** (_Color_) : socket
- **epsilon** (_Float_ = None) : socket



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### overlay()

> method

``` python
overlay(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : OVERLAY

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### screen()

> method

``` python
screen(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : SCREEN

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### soft_light()

> method

``` python
soft_light(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : SOFT LIGHT

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### subtract()

> method

``` python
subtract(factor=None, other=None, clamp_result=False, clamp_factor=True)
```

Mix with another color : SUBTRACT

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket
- **other** (_Color_ = None) : socket
- **clamp_result** (_bool_ = False) : clamp result flag
- **clamp_factor** (_bool_ = True) : clamp factor flag



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### vector_displacement()

> method

``` python
vector_displacement(midlevel=None, scale=None, space='TANGENT')
```

Normal map.

[!Node] Normal Map

#### Arguments:
- **midlevel** (_Float_ = None) : socket
- **scale** (_Float_ = None) : socket
- **space** (_str_ = TANGENT) : str in ('TANGENT', 'OBJECT', 'WORLD')



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>

----------
### Wavelength()

> classmethod

``` python
Wavelength(wavelength=None)
```

Constructor : Wave Length.

[!Node] Wavelength

#### Arguments:
- **wavelength** (_Float_ = None) : socket



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Color](geono-color-color.md#color) :black_small_square: [Content](geono-color-color.md#content) :black_small_square: [Methods](geono-color-color.md#methods)</sub>