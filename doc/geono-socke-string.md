# String

> Bases classes: [Socket](geono-socke-socket.md#socket)

``` python
String(value='', name=None, tip=None)
```

Socket of type String

A group input socket of type String is created if the name is not None.

#### Arguments:
- **value** (_str or Socket_ = ) : initial value
- **name** (_str_ = None) : group input socket name if not None
- **tip** (_str_ = None) : user type for group input socket

### Inherited

[blur](geono-socke-socket.md#blur) :black_small_square: [\_cache](geono-socke-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-socke-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socke-socket.md#check_in_list) :black_small_square: [data_type](geono-socke-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socke-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socke-socket.md#__getattr__) :black_small_square: [IndexSwitch](geono-socke-socket.md#indexswitch) :black_small_square: [index_switch](geono-socke-socket.md#index_switch) :black_small_square: [input_type](geono-socke-socket.md#input_type) :black_small_square: [\_jump](geono-socke-socket.md#_jump) :black_small_square: [\_lc](geono-socke-socket.md#_lc) :black_small_square: [\_lcop](geono-socke-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socke-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socke-socket.md#menu_switch) :black_small_square: [node](geono-socke-socket.md#node) :black_small_square: [node_color](geono-socke-socket.md#node_color) :black_small_square: [node_label](geono-socke-socket.md#node_label) :black_small_square: [out](geono-socke-socket.md#out) :black_small_square: [\_reset](geono-socke-socket.md#_reset) :black_small_square: [socket_type](geono-socke-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socke-socket.md#__str__) :black_small_square: [Switch](geono-socke-socket.md#switch) :black_small_square: [switch](geono-socke-socket.md#switch) :black_small_square: [to_output](geono-socke-socket.md#to_output) :black_small_square:

## Content

- [equal](geono-socke-string.md#equal)
- [FromValue](geono-socke-string.md#fromvalue)
- [Join](geono-socke-string.md#join)
- [join](geono-socke-string.md#join)
- [length](geono-socke-string.md#length)
- [not_equal](geono-socke-string.md#not_equal)
- [replace](geono-socke-string.md#replace)
- [slice](geono-socke-string.md#slice)
- [to_curves](geono-socke-string.md#to_curves)

## Properties



### length

> _type_: **Node**
>

Node 'String Length' (FunctionNodeStringLength)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](geono-socke-string.md#string) :black_small_square: [Content](geono-socke-string.md#content) :black_small_square: [Properties](geono-socke-string.md#properties)</sub>

## Methods



----------
### equal()

> method

``` python
equal(other)
```

Node 'Compare' (FunctionNodeCompare)

Node compare with data_type = 'STRING' and operation = 'EQUAL'

#### Arguments:
- **other** (_string_) : socket 'B' (B)



#### Returns:
- **result** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](geono-socke-string.md#string) :black_small_square: [Content](geono-socke-string.md#content) :black_small_square: [Methods](geono-socke-string.md#methods)</sub>

----------
### FromValue()

> classmethod

``` python
FromValue(value, decimals=0)
```

Node 'Value to String' (FunctionNodeValueToString)

#### Arguments:
- **value** (_Float_) : socket 'Value' (Value)
- **decimals** (_Int_ = 0) : socket 'Decimals' (Decimals)



#### Returns:
- **string** (_String_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](geono-socke-string.md#string) :black_small_square: [Content](geono-socke-string.md#content) :black_small_square: [Methods](geono-socke-string.md#methods)</sub>

----------
### Join()

> classmethod

``` python
Join(*strings, delimiter=None)
```

Node 'Join Strings' (GeometryNodeStringJoin)

#### Arguments:
- **strings** (_String_) : socket 'Strings' (Strings)
- **delimiter** (_String_ = None) : socket 'Delimiter' (Delimiter)



#### Returns:
- **string** (_String_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](geono-socke-string.md#string) :black_small_square: [Content](geono-socke-string.md#content) :black_small_square: [Methods](geono-socke-string.md#methods)</sub>

----------
### join()

> method

``` python
join(*strings)
```

Node 'Join Strings' (GeometryNodeStringJoin)

#### Arguments:
- **strings** (_String_) : socket 'Strings' (Strings)



#### Returns:
- **string** (_String_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](geono-socke-string.md#string) :black_small_square: [Content](geono-socke-string.md#content) :black_small_square: [Methods](geono-socke-string.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(other)
```

Node 'Compare' (FunctionNodeCompare)

Node compare with data_type = 'STRING' and operation = 'NOT_EQUAL'

#### Arguments:
- **other** (_string_) : socket 'B' (B)



#### Returns:
- **result** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](geono-socke-string.md#string) :black_small_square: [Content](geono-socke-string.md#content) :black_small_square: [Methods](geono-socke-string.md#methods)</sub>

----------
### replace()

> method

``` python
replace(find=None, replace=None)
```

Node 'Replace String' (FunctionNodeReplaceString)

#### Arguments:
- **find** (_String_ = None) : socket 'Find' (Find)
- **replace** (_String_ = None) : socket 'Replace' (Replace)



#### Returns:
- **string** (_String_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](geono-socke-string.md#string) :black_small_square: [Content](geono-socke-string.md#content) :black_small_square: [Methods](geono-socke-string.md#methods)</sub>

----------
### slice()

> method

``` python
slice(position=0, length=10)
```

Node 'Slice String' (FunctionNodeSliceString)

#### Arguments:
- **position** (_Integer_ = 0) : socket 'Position' (Position)
- **length** (_Integer_ = 10) : socket 'Length' (Length)



#### Returns:
- **string** (_String_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](geono-socke-string.md#string) :black_small_square: [Content](geono-socke-string.md#content) :black_small_square: [Methods](geono-socke-string.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, text_box_height=None, overflow='OVERFLOW', align_x='LEFT', align_y='TOP_BASELINE', pivot_mode='BOTTOM_LEFT', font=None)
```

Node 'String to Curves' (GeometryNodeStringToCurves)

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
- **curve_instances** (_GEOMETRY_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](geono-socke-string.md#string) :black_small_square: [Content](geono-socke-string.md#content) :black_small_square: [Methods](geono-socke-string.md#methods)</sub>