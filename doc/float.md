# Float

> Bases classes: [Attribute](attribute.md#attribute)

``` python
Float(value=0.0, name=None, min=None, max=None, tip=None, subtype='NONE')
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
- **value** (_float or Socket_ = 0.0) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **min** (_float_ = None) : minimum value
- **max** (_float_ = None) : maximum value
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **subtype** (_str_ = NONE) : sub type for group input

### Inherited

[blur](socket.md#blur) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [hash_value](socket.md#hash_value) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [Named](attribute.md#named) :black_small_square: [NamedAttribute](attribute.md#namedattribute) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square:

## Content

- **A** : [Angle](float.md#angle)
- **C** : [ceiling](float.md#ceiling) :black_small_square: [clamp](float.md#clamp) :black_small_square: [color_ramp](float.md#color_ramp) :black_small_square: [curve](float.md#curve)
- **D** : [dial_gizmo](float.md#dial_gizmo) :black_small_square: [Distance](float.md#distance)
- **E** : [equal](float.md#equal)
- **F** : [Factor](float.md#factor) :black_small_square: [floor](float.md#floor)
- **G** : [greater_equal](float.md#greater_equal) :black_small_square: [greater_than](float.md#greater_than)
- **I** : [\_\_init__](float.md#__init__)
- **L** : [less_equal](float.md#less_equal) :black_small_square: [less_than](float.md#less_than) :black_small_square: [linear_gizmo](float.md#linear_gizmo)
- **M** : [map_range](float.md#map_range) :black_small_square: [map_range_linear](float.md#map_range_linear) :black_small_square: [map_range_smooth](float.md#map_range_smooth) :black_small_square: [map_range_smoother](float.md#map_range_smoother) :black_small_square: [map_range_stepped](float.md#map_range_stepped) :black_small_square: [mix](float.md#mix)
- **N** : [not_equal](float.md#not_equal)
- **O** : [out](float.md#out)
- **P** : [Percentage](float.md#percentage)
- **R** : [Random](float.md#random) :black_small_square: [round](float.md#round)
- **T** : [Time](float.md#time) :black_small_square: [TimeAbsolute](float.md#timeabsolute) :black_small_square: [to_integer](float.md#to_integer) :black_small_square: [to_string](float.md#to_string) :black_small_square: [truncate](float.md#truncate)
- **W** : [WaveLength](float.md#wavelength)

## Methods



----------
### Angle()

> classmethod

``` python
Angle(value=0.0, name='Angle', min=None, max=None, tip=None)
```

> Angle group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Angle)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### ceiling()

> method

``` python
ceiling()
```

> Ceiling

:sunrise: **ShaderNodes** only


> [!IMPORTANT]
> - **GeoNodes** : [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### clamp()

> method

``` python
clamp(min=None, max=None, clamp_type='MINMAX')
```

> Clamp

> Node [Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/clamp.html)

#### Arguments:
- **min** (_Float_ = None) : socket 'Min' (Min)
- **max** (_Float_ = None) : socket 'Max' (Max)
- **clamp_type** (_str_ = MINMAX) : Node.clamp_type in ('MINMAX', 'RANGE')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### color_ramp()

> method

``` python
color_ramp(keep=None)
```

> Color Ramp

> Node [Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

#### Arguments:
- **keep** ( = None)



#### Returns:
- **Color** : [alpha_]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### curve()

> method

``` python
curve(factor=None, keep=None)
```

> Float Curve

> Node ERROR: Node 'Float Curve' not found

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **keep** ( = None)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### dial_gizmo()

> method

``` python
dial_gizmo(position=None, up=None, screen_space=None, radius=None, color_id='PRIMARY')
```

> Node ERROR: Node 'Dial Gizmo' not found

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **up** (_Vector_ = None) : socket 'Up' (Up)
- **screen_space** (_Boolean_ = None) : socket 'Screen Space' (Screen Space)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **color_id** (_str_ = PRIMARY) : Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')



#### Returns:
- **Gizmo** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Distance()

> classmethod

``` python
Distance(value=0.0, name='Distance', min=None, max=None, tip=None)
```

> Distance group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Distance)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### equal()

> method

``` python
equal(other, epsilon=None)
```

> Equal to another value

:sunrise: **ShaderNodes** only


> [!IMPORTANT]
> - **GeoNodes** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Factor()

> classmethod

``` python
Factor(value=0.0, name='Factor', min=0, max=1, tip=None)
```

> Factor group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Factor)
- **min** ( = 0)
- **max** ( = 1)
- **tip** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### floor()

> method

``` python
floor()
```

> Floor

:sunrise: **ShaderNodes** only


> [!IMPORTANT]
> - **GeoNodes** : [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### greater_equal()

> method

``` python
greater_equal(other)
```

> Greater than another value

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(other)
```

> Greater than another value

:sunrise: **ShaderNodes** only


> [!IMPORTANT]
> - **GeoNodes** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=0.0, name=None, min=None, max=None, tip=None, subtype='NONE')
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
- **value** (_float or Socket_ = 0.0) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **min** (_float_ = None) : minimum value
- **max** (_float_ = None) : maximum value
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **subtype** (_str_ = NONE) : sub type for group input

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### less_equal()

> method

``` python
less_equal(other)
```

> Less than another value

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(other)
```

> Less than another value

:sunrise: **ShaderNodes** only


> [!IMPORTANT]
> - **GeoNodes** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### linear_gizmo()

> method

``` python
linear_gizmo(position=None, direction=None, color_id='PRIMARY', draw_style='ARROW')
```

> Node ERROR: Node 'Linear Gizmo' not found

#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **direction** (_Vector_ = None) : socket 'Direction' (Direction)
- **color_id** (_str_ = PRIMARY) : Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')
- **draw_style** (_str_ = ARROW) : Node.draw_style in ('ARROW', 'CROSS', 'BOX')



#### Returns:
- **Gizmo** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range()

> method

``` python
map_range(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None, interpolation_type='LINEAR')
```

> Map range

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp
- **interpolation_type** (_str_ = LINEAR) : Node.interpolation_type in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range_linear()

> method

``` python
map_range_linear(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

> Map Range, LINEAR interpolation

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range_smooth()

> method

``` python
map_range_smooth(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

> Map Range, SMOOTH interpolation

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range_smoother()

> method

``` python
map_range_smoother(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

> Map Range, SMOOTHER interpolation

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### map_range_stepped()

> method

``` python
map_range_stepped(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

> Map Range, STEPPED interpolation

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



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
### not_equal()

> method

``` python
not_equal(other, epsilon=None)
```

> Not equal to another value

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Percentage()

> classmethod

``` python
Percentage(value=0.0, name='Percentage', min=None, max=None, tip=None)
```

> Percentage group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Percentage)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)

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
round()
```

> Rounding

:sunrise: **ShaderNodes** only


> [!IMPORTANT]
> - **GeoNodes** : [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### Time()

> classmethod

``` python
Time(value=0.0, name='Time', min=None, max=None, tip=None)
```

> Time group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = Time)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### TimeAbsolute()

> classmethod

``` python
TimeAbsolute(value=0.0, name='TimeAbsolute', min=None, max=None, tip=None)
```

> Time Absolute group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = TimeAbsolute)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### to_integer()

> method

``` python
to_integer(rounding_mode=None)
```

> Conversion to integer

> Node [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)

#### Arguments:
- **rounding_mode** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### to_string()

> method

``` python
to_string(decimals=None)
```

> To String

> Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html)

#### Arguments:
- **decimals** (_Integer_ = None) : socket 'Decimals' (Decimals)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### truncate()

> method

``` python
truncate()
```

> Truncate

:sunrise: **ShaderNodes** only


> [!IMPORTANT]
> - **GeoNodes** : [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>

----------
### WaveLength()

> classmethod

``` python
WaveLength(value=0.0, name='WaveLength', min=None, max=None, tip=None)
```

> Wave Length group input

#### Arguments:
- **value** ( = 0.0)
- **name** ( = WaveLength)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](float.md#float) :black_small_square: [Content](float.md#content) :black_small_square: [Methods](float.md#methods)</sub>