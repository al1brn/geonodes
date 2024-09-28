# Integer

> Bases classes: [Socket](geono-socket.md#socket)

``` python
Integer(value=0, name=None, min=None, max=None, tip=None, subtype='NONE')
```



#### Arguments:
- **value** ( = 0)
- **name** ( = None)
- **min** ( = None)
- **max** ( = None)
- **tip** ( = None)
- **subtype** ( = NONE)

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_output](geono-socket.md#to_output) :black_small_square:

## Content

- **C** : [clamp](geono-integer.md#clamp) :black_small_square: [color_ramp](geono-integer.md#color_ramp) :black_small_square: [curve](geono-integer.md#curve)
- **E** : [equal](geono-integer.md#equal)
- **G** : [greater_equal](geono-integer.md#greater_equal) :black_small_square: [greater_than](geono-integer.md#greater_than)
- **L** : [less_equal](geono-integer.md#less_equal) :black_small_square: [less_than](geono-integer.md#less_than)
- **M** : [map_range](geono-integer.md#map_range) :black_small_square: [map_range_linear](geono-integer.md#map_range_linear) :black_small_square: [map_range_smooth](geono-integer.md#map_range_smooth) :black_small_square: [map_range_smoother](geono-integer.md#map_range_smoother) :black_small_square: [map_range_stepped](geono-integer.md#map_range_stepped) :black_small_square: [mix](geono-integer.md#mix)
- **N** : [Named](geono-integer.md#named) :black_small_square: [NamedAttribute](geono-integer.md#namedattribute) :black_small_square: [not_equal](geono-integer.md#not_equal)
- **T** : [to_string](geono-integer.md#to_string)

## Methods



----------
### clamp()

> method

``` python
clamp(min=None, max=None, clamp_type='MINMAX')
```

> Clamp

[Clamp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/clamp.html)

#### Arguments:
- **min** (_Float_ = None) : socket 'Min' (Min)
- **max** (_Float_ = None) : socket 'Max' (Max)
- **clamp_type** (_str_ = MINMAX) : Node.clamp_type in ('MINMAX', 'RANGE')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### color_ramp()

> method

``` python
color_ramp(keep=None)
```

> Color Ramp

[Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

#### Arguments:
- **keep** ( = None)



#### Returns:
- **Color** : [alpha_]

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### curve()

> method

``` python
curve(factor=None, keep=None)
```

> Float Curve

ERROR: Node 'Float Curve' not found

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **keep** ( = None)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### equal()

> method

``` python
equal(other)
```

> **node** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### greater_equal()

> method

``` python
greater_equal(other)
```

> **node** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(other)
```

> **node** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### less_equal()

> method

``` python
less_equal(other)
```

> **node** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(other)
```

> **node** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### map_range()

> method

``` python
map_range(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None, interpolation_type='LINEAR')
```

> Map range

[Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp
- **interpolation_type** (_str_ = LINEAR) : Node.interpolation_type in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### map_range_linear()

> method

``` python
map_range_linear(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

> Map Range, LINEAR interpolation

[Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### map_range_smooth()

> method

``` python
map_range_smooth(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

> Map Range, SMOOTH interpolation

[Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### map_range_smoother()

> method

``` python
map_range_smoother(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

> Map Range, SMOOTHER interpolation

[Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### map_range_stepped()

> method

``` python
map_range_stepped(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

> Map Range, STEPPED interpolation

[Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### mix()

> method

``` python
mix(factor=None, other=None, clamp_factor=None)
```

> Mix

[Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor_Float)
- **other** (_Socket_ = None) : socket 'B' (B_Float)
- **clamp_factor** (_bool_ = None) : Node.clamp_factor



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name)
```

> **node** : [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

[Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name)
```

> **node** : [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

[Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(other)
```

> **node** : [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

[Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>

----------
### to_string()

> method

``` python
to_string(decimals=None)
```

> To String

[Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html)

#### Arguments:
- **decimals** (_Integer_ = None) : socket 'Decimals' (Decimals)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](geono-integer.md#integer) :black_small_square: [Content](geono-integer.md#content) :black_small_square: [Methods](geono-integer.md#methods)</sub>