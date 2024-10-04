# Integer

> Bases classes: [IntFloat](geono-intfloat.md#intfloat)

``` python
Integer(value=0, name=None, min=None, max=None, tip=None, subtype='NONE')
```

> Socket of type INTEGER

> Node [Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/value.html)

If **value** argument is None:
- if **name** argument is None, a node 'Integer' is added
- otherwise a new group input is created using **min**, **max**, **tip** and **subtype**
  arguments

If **value** argument is not None, a new **Integer** is created from the value, either
by transtyping or creating a 'Value' node.

``` python
i = Integer()      # 'Integer' node with default initial vlaue
i = Integer(123). # 'Integer' node with 123 initial value
i = Integer(123, name="User input", subtype='PERCENTAGE') # Create a new integer group input
```

#### Arguments:
- **value** (_integer or Socket_ = 0) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **min** (_float_ = None) : minimum value
- **max** (_float_ = None) : maximum value
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **subtype** (_str_ = NONE) : sub type for group input

### Inherited

[\_\_abs__](geono-intfloat.md#__abs__) :black_small_square: [\_\_add__](geono-intfloat.md#__add__) :black_small_square: [blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [\_\_ceil__](geono-intfloat.md#__ceil__) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [clamp](geono-intfloat.md#clamp) :black_small_square: [color_ramp](geono-intfloat.md#color_ramp) :black_small_square: [curve](geono-intfloat.md#curve) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_\_eq__](geono-intfloat.md#__eq__) :black_small_square: [\_\_floor__](geono-intfloat.md#__floor__) :black_small_square: [\_\_ge__](geono-intfloat.md#__ge__) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [\_\_gt__](geono-intfloat.md#__gt__) :black_small_square: [\_\_iadd__](geono-intfloat.md#__iadd__) :black_small_square: [\_\_imod__](geono-intfloat.md#__imod__) :black_small_square: [\_\_imul__](geono-intfloat.md#__imul__) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_\_ipow__](geono-intfloat.md#__ipow__) :black_small_square: [\_\_isub__](geono-intfloat.md#__isub__) :black_small_square: [\_\_itruediv__](geono-intfloat.md#__itruediv__) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [\_\_le__](geono-intfloat.md#__le__) :black_small_square: [\_\_lt__](geono-intfloat.md#__lt__) :black_small_square: [map_range](geono-intfloat.md#map_range) :black_small_square: [map_range_linear](geono-intfloat.md#map_range_linear) :black_small_square: [map_range_smooth](geono-intfloat.md#map_range_smooth) :black_small_square: [map_range_smoother](geono-intfloat.md#map_range_smoother) :black_small_square: [map_range_stepped](geono-intfloat.md#map_range_stepped) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [mix](geono-intfloat.md#mix) :black_small_square: [\_\_mod__](geono-intfloat.md#__mod__) :black_small_square: [\_\_mul__](geono-intfloat.md#__mul__) :black_small_square: [Named](geono-attribute.md#named) :black_small_square: [NamedAttribute](geono-attribute.md#namedattribute) :black_small_square: [\_\_ne__](geono-intfloat.md#__ne__) :black_small_square: [\_\_neg__](geono-intfloat.md#__neg__) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_\_pow__](geono-intfloat.md#__pow__) :black_small_square: [\_\_radd__](geono-intfloat.md#__radd__) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [\_\_rmod__](geono-intfloat.md#__rmod__) :black_small_square: [\_\_rmul__](geono-intfloat.md#__rmul__) :black_small_square: [\_\_round__](geono-intfloat.md#__round__) :black_small_square: [\_\_rpow__](geono-intfloat.md#__rpow__) :black_small_square: [\_\_rsub__](geono-intfloat.md#__rsub__) :black_small_square: [\_\_rtruediv__](geono-intfloat.md#__rtruediv__) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [\_\_sub__](geono-intfloat.md#__sub__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_string](geono-intfloat.md#to_string) :black_small_square: [\_\_truediv__](geono-intfloat.md#__truediv__) :black_small_square: [\_\_trunc__](geono-intfloat.md#__trunc__) :black_small_square:

## Content

- [equal](macro-geono-integer.md#equal)
- [Factor](macro-geono-integer.md#factor)
- [greater_equal](macro-geono-integer.md#greater_equal)
- [greater_than](macro-geono-integer.md#greater_than)
- [less_equal](macro-geono-integer.md#less_equal)
- [less_than](macro-geono-integer.md#less_than)
- [not_equal](macro-geono-integer.md#not_equal)
- [Percentage](macro-geono-integer.md#percentage)

## Methods



----------
### equal()

> method

``` python
equal(other)
```

Node 'Compare' (FunctionNodeCompare)

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](macro-geono-integer.md#integer) :black_small_square: [Content](macro-geono-integer.md#content) :black_small_square: [Methods](macro-geono-integer.md#methods)</sub>

----------
### Factor()

> classmethod

``` python
Factor(value=0, name='Factor', min=100, max=100, tip=None)
```

> Integer factor group input

#### Arguments:
- **value** ( = 0)
- **name** ( = Factor)
- **min** ( = 100)
- **max** ( = 100)
- **tip** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](macro-geono-integer.md#integer) :black_small_square: [Content](macro-geono-integer.md#content) :black_small_square: [Methods](macro-geono-integer.md#methods)</sub>

----------
### greater_equal()

> method

``` python
greater_equal(other)
```

Node 'Compare' (FunctionNodeCompare)

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](macro-geono-integer.md#integer) :black_small_square: [Content](macro-geono-integer.md#content) :black_small_square: [Methods](macro-geono-integer.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(other)
```

Node 'Compare' (FunctionNodeCompare)

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](macro-geono-integer.md#integer) :black_small_square: [Content](macro-geono-integer.md#content) :black_small_square: [Methods](macro-geono-integer.md#methods)</sub>

----------
### less_equal()

> method

``` python
less_equal(other)
```

Node 'Compare' (FunctionNodeCompare)

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](macro-geono-integer.md#integer) :black_small_square: [Content](macro-geono-integer.md#content) :black_small_square: [Methods](macro-geono-integer.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(other)
```

Node 'Compare' (FunctionNodeCompare)

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](macro-geono-integer.md#integer) :black_small_square: [Content](macro-geono-integer.md#content) :black_small_square: [Methods](macro-geono-integer.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(other)
```

Node 'Compare' (FunctionNodeCompare)

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Arguments:
- **other** (_Float_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](macro-geono-integer.md#integer) :black_small_square: [Content](macro-geono-integer.md#content) :black_small_square: [Methods](macro-geono-integer.md#methods)</sub>

----------
### Percentage()

> classmethod

``` python
Percentage(value=0, name='Percentage', min=0, max=100, tip=None)
```

> Integer percentage group input

#### Arguments:
- **value** ( = 0)
- **name** ( = Percentage)
- **min** ( = 0)
- **max** ( = 100)
- **tip** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](macro-geono-integer.md#integer) :black_small_square: [Content](macro-geono-integer.md#content) :black_small_square: [Methods](macro-geono-integer.md#methods)</sub>