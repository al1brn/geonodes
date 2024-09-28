# Float

> Bases classes: [Socket](geono-socket.md#socket)

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
float = Float(3.14, name="User input", subtype='ANGLE') # Create a new float group input
```

#### Arguments:
- **value** (_float or Socket_ = 0.0) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **min** (_float_ = None) : minimum value
- **max** (_float_ = None) : maximum value
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **subtype** (_str_ = NONE) : sub type for group input

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square:

## Content

- **A** : [Angle](geono-float.md#angle)
- **C** : [ceiling](geono-float.md#ceiling) :black_small_square: [clamp](geono-float.md#clamp) :black_small_square: [color_ramp](geono-float.md#color_ramp) :black_small_square: [curve](geono-float.md#curve)
- **D** : [Distance](geono-float.md#distance)
- **E** : [equal](geono-float.md#equal)
- **F** : [Factor](geono-float.md#factor) :black_small_square: [floor](geono-float.md#floor)
- **G** : [greater_equal](geono-float.md#greater_equal) :black_small_square: [greater_than](geono-float.md#greater_than)
- **L** : [less_equal](geono-float.md#less_equal) :black_small_square: [less_than](geono-float.md#less_than)
- **M** : [map_range](geono-float.md#map_range) :black_small_square: [map_range_linear](geono-float.md#map_range_linear) :black_small_square: [map_range_smooth](geono-float.md#map_range_smooth) :black_small_square: [map_range_smoother](geono-float.md#map_range_smoother) :black_small_square: [map_range_stepped](geono-float.md#map_range_stepped) :black_small_square: [mix](geono-float.md#mix)
- **N** : [Named](geono-float.md#named) :black_small_square: [NamedAttribute](geono-float.md#namedattribute) :black_small_square: [not_equal](geono-float.md#not_equal)
- **P** : [Percentage](geono-float.md#percentage)
- **R** : [Random](geono-float.md#random) :black_small_square: [round](geono-float.md#round)
- **T** : [Time](geono-float.md#time) :black_small_square: [TimeAbsolute](geono-float.md#timeabsolute) :black_small_square: [to_integer](geono-float.md#to_integer) :black_small_square: [to_output](geono-float.md#to_output) :black_small_square: [to_string](geono-float.md#to_string) :black_small_square: [truncate](geono-float.md#truncate)
- **W** : [WaveLength](geono-float.md#wavelength)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### ceiling()

> method

``` python
ceiling()
```

> Ceiling

[!MIX]

> [!IMPORTANT]
> - **GeoNodes** : [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### equal()

> method

``` python
equal(other, epsilon=None)
```

> Equal to another value

[!MIX]

> [!IMPORTANT]
> - **GeoNodes** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### floor()

> method

``` python
floor()
```

> Floor

[!MIX]

> [!IMPORTANT]
> - **GeoNodes** : [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(other)
```

> Greater than another value

[!MIX]

> [!IMPORTANT]
> - **GeoNodes** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(other)
```

> Less than another value

[!MIX]

> [!IMPORTANT]
> - **GeoNodes** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

'Named' is a synonym of 'NamedAttribute'

``` python
with GeoNodes("Named Attributes"):

    cube = Mesh.Cube()

    # Create a named attribute
    cube.points.store("Some Value", Float.Random(0, 1, seed=0))

    # Read the random value to offset along z
    cube.points.offset = (0, 0, Float.Named("Some Value"))

    # Remove the named attribute
    cube.remove_named_attribute("Some*", exact=False)

    cube.out()
```

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

'Named' is a synonym of 'NamedAttribute'

``` python
with GeoNodes("Named Attributes"):

    cube = Mesh.Cube()

    # Create a named attribute
    cube.points.store("Some Value", Float.Random(0, 1, seed=0))

    # Read the random value to offset along z
    cube.points.offset = (0, 0, Float.NamedAttribute("Some Value"))

    # Remove the named attribute
    cube.remove_named_attribute("Some*", exact=False)

    cube.out()
```

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### round()

> method

``` python
round()
```

> Rounding

[!MIX]

> [!IMPORTANT]
> - **GeoNodes** : [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### to_output()

> method

``` python
to_output(name=None)
```

> Connect to output

[!MIX]

> [!IMPORTANT]
> - Geometry Nodes : create a group output socket with the provided name
> - Shader : create a node [AOV Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/aov.html)

#### Arguments:
- **name** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

----------
### truncate()

> method

``` python
truncate()
```

> Truncate

[!MIX]

> [!IMPORTANT]
> - **GeoNodes** : [Float to Integer](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html)
> - **ShaderNodes** : [Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/math.html)

#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Float](geono-float.md#float) :black_small_square: [Content](geono-float.md#content) :black_small_square: [Methods](geono-float.md#methods)</sub>