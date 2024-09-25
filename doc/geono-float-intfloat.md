# IntFloat

> Bases classes: [ValueSocket](geono-socke-valuesocket.md)

``` python
IntFloat(socket)
```



#### Arguments:
- **socket**

### Inherited

[blur](geono-socke-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [Named](geono-socke-valuesocket.md#named) :black_small_square: [NamedAttribute](geono-socke-valuesocket.md#namedattribute) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [\_reset](geono-socke-socket.md#_reset) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square: [to_output](geono-socke-socket.md#to_output) :black_small_square:

## Content

- [clamp](geono-float-intfloat.md#clamp)
- [color_ramp](geono-float-intfloat.md#color_ramp)
- [curve](geono-float-intfloat.md#curve)
- [map_range](geono-float-intfloat.md#map_range)
- [map_range_linear](geono-float-intfloat.md#map_range_linear)
- [map_range_smooth](geono-float-intfloat.md#map_range_smooth)
- [map_range_smoother](geono-float-intfloat.md#map_range_smoother)
- [map_range_stepped](geono-float-intfloat.md#map_range_stepped)
- [mix](geono-float-intfloat.md#mix)
- [to_string](geono-float-intfloat.md#to_string)

## Methods



----------
### clamp()

> method

``` python
clamp(min=None, max=None, clamp_type='MINMAX')
```

Node 'Clamp' (ShaderNodeClamp)

[!Node] Clamp

#### Arguments:
- **min** (_Float_ = None) : socket 'Min' (Min)
- **max** (_Float_ = None) : socket 'Max' (Max)
- **clamp_type** (_str_ = MINMAX) : Node.clamp_type in ('MINMAX', 'RANGE')



#### Returns:
- **Float** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

----------
### color_ramp()

> method

``` python
color_ramp(keep=None)
```

Node 'Color Ramp' (ShaderNodeValToRGB)

[!Node] Color Ramp

#### Arguments:
- **keep** ( = None)



#### Returns:
- **Color** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

----------
### curve()

> method

``` python
curve(factor=None, keep=None)
```

Node 'Float Curve' (ShaderNodeFloatCurve)

[!Node] Float Curve

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **keep** ( = None)



#### Returns:
- **Float** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

----------
### map_range()

> method

``` python
map_range(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None, interpolation_type='LINEAR')
```

Node 'Map Range' (ShaderNodeMapRange)

[!Node] Map Range

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp
- **interpolation_type** (_str_ = LINEAR) : Node.interpolation_type in ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')



#### Returns:
- **Float** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

----------
### map_range_linear()

> method

``` python
map_range_linear(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

Node 'Map Range' (ShaderNodeMapRange)

[!Node] Map Range

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

----------
### map_range_smooth()

> method

``` python
map_range_smooth(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

Node 'Map Range' (ShaderNodeMapRange)

[!Node] Map Range

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

----------
### map_range_smoother()

> method

``` python
map_range_smoother(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

Node 'Map Range' (ShaderNodeMapRange)

[!Node] Map Range

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

----------
### map_range_stepped()

> method

``` python
map_range_stepped(from_min=None, from_max=None, to_min=None, to_max=None, clamp=None)
```

Node 'Map Range' (ShaderNodeMapRange)

[!Node] Map Range

#### Arguments:
- **from_min** (_Float_ = None) : socket 'From Min' (From Min)
- **from_max** (_Float_ = None) : socket 'From Max' (From Max)
- **to_min** (_Float_ = None) : socket 'To Min' (To Min)
- **to_max** (_Float_ = None) : socket 'To Max' (To Max)
- **clamp** (_bool_ = None) : Node.clamp



#### Returns:
- **Float** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

----------
### mix()

> method

``` python
mix(factor=None, other=None, clamp_factor=None)
```

Node 'Mix' (ShaderNodeMix)

[!Node] Mix

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor_Float)
- **other** (_Socket_ = None) : socket 'B' (B_Float)
- **clamp_factor** (_bool_ = None) : Node.clamp_factor



#### Returns:
- **Socket** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

----------
### to_string()

> method

``` python
to_string(decimals=None)
```

Node 'Value to String' (FunctionNodeValueToString)

[!Node] Value to String

#### Arguments:
- **decimals** (_Integer_ = None) : socket 'Decimals' (Decimals)



#### Returns:
- **String** :

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [Methods](geono-float-intfloat.md#methods)</sub>

<sub>:arrow_right: [index](index.md) :black_small_square: [top](#intfloat) :black_small_square: [Content](#content) :black_small_square: [IntFloat](geono-float-intfloat.md)</sub>