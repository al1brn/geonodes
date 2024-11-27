# String

> Bases classes: [Socket](socket.md#socket)

``` python
String(value='', name=None, tip=None)
```

Socket of type String

Node [String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/string.html)

A group input socket of type String is created if the name is not None.

#### Arguments:
- **value** (_str or Socket_ = ) : initial value
- **name** (_str_ = None) : group input socket name if not None
- **tip** (_str_ = None) : user type for group input socket

### Inherited

[blur](socket.md#blur) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [hash_value](socket.md#hash_value) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square:

## Content

- [equal](string.md#equal)
- [FromValue](string.md#fromvalue)
- [\_\_init__](string.md#__init__)
- [Join](string.md#join)
- [join](string.md#join)
- [length](string.md#length)
- [not_equal](string.md#not_equal)
- [replace](string.md#replace)
- [slice](string.md#slice)
- [to_curves](string.md#to_curves)

## Properties



### length

> _type_: **Integer**
>

> Node [String Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_length.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Properties](string.md#properties)</sub>

## Methods



----------
### equal()

> method

``` python
equal(other)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

Node compare with data_type = 'STRING' and operation = 'EQUAL'

#### Arguments:
- **other** (_string_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### FromValue()

> classmethod

``` python
FromValue(value, decimals=0)
```

> Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html)

#### Arguments:
- **value** (_Float_) : socket 'Value' (Value)
- **decimals** (_Int_ = 0) : socket 'Decimals' (Decimals)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value='', name=None, tip=None)
```

Socket of type String

Node [String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/string.html)

A group input socket of type String is created if the name is not None.

#### Arguments:
- **value** (_str or Socket_ = ) : initial value
- **name** (_str_ = None) : group input socket name if not None
- **tip** (_str_ = None) : user type for group input socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### Join()

> classmethod

``` python
Join(*strings, delimiter=None)
```

> Node [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/join_strings.html)

#### Arguments:
- **strings** (_String_) : socket 'Strings' (Strings)
- **delimiter** (_String_ = None) : socket 'Delimiter' (Delimiter)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### join()

> method

``` python
join(*strings)
```

> Node [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/join_strings.html)



#### Arguments:
- **strings** (_String_) : socket 'Strings' (Strings)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(other)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

Node compare with data_type = 'STRING' and operation = 'NOT_EQUAL'

#### Arguments:
- **other** (_string_) : socket 'B' (B)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### replace()

> method

``` python
replace(find=None, replace=None)
```

> Node [Replace String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/replace_string.html)



#### Arguments:
- **find** (_String_ = None) : socket 'Find' (Find)
- **replace** (_String_ = None) : socket 'Replace' (Replace)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### slice()

> method

``` python
slice(position=0, length=10)
```

> Node [Slice String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/slice_string.html)



#### Arguments:
- **position** (_Integer_ = 0) : socket 'Position' (Position)
- **length** (_Integer_ = 10) : socket 'Length' (Length)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, overflow='OVERFLOW', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT', font=None)
```

> Node [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_curves.html)

#### Arguments:
- **size** (_Float_ = None) : socket 'Size' (Size)
- **character_spacing** (_Float_ = None) : socket 'Character Spacing' (Character Spacing)
- **word_spacing** (_Float_ = None) : socket 'Word Spacing' (Word Spacing)
- **line_spacing** (_Float_ = None) : socket 'Line Spacing' (Line Spacing)
- **text_box_width** (_Float_ = None) : socket 'Text Box Width' (Text Box Width)
- **text_box_height** (_Float_ = None) : socket 'Text Box Height' (Text Box Height)
- **overflow** (_str_ = OVERFLOW) : Node.overflow in ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE')
- **align_x** (_str_ = LEFT) : Node.align_x in ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH')
- **align_y** (_str_ = TOP_BASELINE) : Node.align_y in ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM')
- **pivot_mode** (_str_ = BOTTOM_LEFT) : Node.pivot_mode in ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')
- **font** (_VectorFont_ = None) : Node.font



#### Returns:
- **Curve** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>