# String

``` python
String(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', optional_label: bool = False, hide_value: bool = False, hide_in_modifier: bool = False, subtype: str = 'NONE')
```

Socket of type String

Node [String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/string.html)

A group input socket of type String is created if the name is not None.

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : group input socket name if not None
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **optional_label** (_bool_ = False) : Property optional_label
- **hide_value** (_bool_ = False) : Property hide_value
- **hide_in_modifier** (_bool_ = False) : Property hide_in_modifier
- **subtype** (_str_ = NONE) : Socket sub type in ('NONE', 'FILE_PATH')

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [\_classes_test](core-socke-socket.md#_classes_test) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_from](core-socke-socket.md#link_from) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: ['_socket_type' not found]() :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- **C** : [\_create_input_socket](string.md#_create_input_socket)
- **E** : [enable_output](string.md#enable_output) :black_small_square: [equal](string.md#equal)
- **F** : [FilePath](string.md#filepath) :black_small_square: [find](string.md#find) :black_small_square: [find_in_string](string.md#find_in_string) :black_small_square: [Format](string.md#format) :black_small_square: [format](string.md#format)
- **H** : [hash_value](string.md#hash_value)
- **I** : [ImportText](string.md#importtext) :black_small_square: [\_\_init__](string.md#__init__)
- **J** : [Join](string.md#join) :black_small_square: [join](string.md#join)
- **L** : [length](string.md#length)
- **M** : [match_string](string.md#match_string)
- **N** : [not_equal](string.md#not_equal)
- **R** : [replace](string.md#replace)
- **S** : [slice](string.md#slice)
- **T** : [to_curves](string.md#to_curves) :black_small_square: [to_float](string.md#to_float) :black_small_square: [to_integer](string.md#to_integer) :black_small_square: [to_value](string.md#to_value)

## Methods



----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = '', name: 'str' = 'String', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, subtype: 'str' = 'NONE')
```

> String Input

New [String](string.md#string) input with subtype 'NONE'.

Aguments
--------
- value  (object = "") : Default value
- name  (str = 'String') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- subtype (str = 'NONE') : Socket sub type in ('NONE', 'FILE_PATH')

#### Arguments:
- **value** (_object_ = )
- **name** (_str_ = String)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **subtype** (_str_ = NONE)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'STRING'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b: 'String' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'STRING'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'EQUAL'



#### Arguments:
- **b** (_String_ = None) : socket 'B' (id: B_STR)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### FilePath()

> classmethod

``` python
FilePath(value: 'object' = '', name: 'str' = 'FilePath', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> FilePath Input

New [String](string.md#string) input with subtype 'FILE_PATH'.

Aguments
--------
- value  (object = "") : Default value
- name  (str = 'FilePath') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier

#### Arguments:
- **value** (_object_ = )
- **name** (_str_ = FilePath)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### find()

> method

``` python
find(search: 'String' = None)
```

> Node [Find in String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/find_in_string.html)

#### Information:
- **Socket** : self



#### Arguments:
- **search** (_String_ = None) : socket 'Search' (id: Search)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### find_in_string()

> method

``` python
find_in_string(search: 'String' = None)
```

> Node [Find in String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/find_in_string.html)

#### Information:
- **Socket** : self



#### Arguments:
- **search** (_String_ = None) : socket 'Search' (id: Search)



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### Format()

> classmethod

``` python
Format(named_sockets: 'dict' = {}, format: 'String' = None, **sockets)
```

> Node [Format String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/format_string.html)

#### Arguments:
- **named_sockets** (_dict_ = {})
- **format** (_String_ = None) : socket 'Format' (id: Format)
- **sockets**



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### format()

> method

``` python
format(named_sockets: 'dict' = {}, **sockets)
```

> Node [Format String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/format_string.html)

#### Information:
- **Socket** : self



#### Arguments:
- **named_sockets** (_dict_ = {})
- **sockets**



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed: 'Integer' = None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'STRING'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### ImportText()

> classmethod

``` python
ImportText(path: 'String' = None)
```

> Node ERROR: Node 'Import Text' not found

#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value: geonodes.core.socket_class.Socket = None, name: str = None, tip: str = '', panel: str = '', optional_label: bool = False, hide_value: bool = False, hide_in_modifier: bool = False, subtype: str = 'NONE')
```

Socket of type String

Node [String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/string.html)

A group input socket of type String is created if the name is not None.

#### Arguments:
- **value** (_Socket_ = None) : initial value
- **name** (_str_ = None) : group input socket name if not None
- **tip** (_str_ = ) : Property description
- **panel** (_str_ = ) : Panel name
- **optional_label** (_bool_ = False) : Property optional_label
- **hide_value** (_bool_ = False) : Property hide_value
- **hide_in_modifier** (_bool_ = False) : Property hide_in_modifier
- **subtype** (_str_ = NONE) : Socket sub type in ('NONE', 'FILE_PATH')

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### Join()

> classmethod

``` python
Join(*strings: 'String', delimiter: 'String' = None)
```

> Node [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/join_strings.html)

#### Arguments:
- **strings** (_String_) : socket 'Strings' (id: Strings)
- **delimiter** (_String_ = None) : socket 'Delimiter' (id: Delimiter)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### join()

> method

``` python
join(*strings: 'String')
```

> Node [Join Strings](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/join_strings.html)

#### Information:
- **Socket** : self



#### Arguments:
- **strings** (_String_) : socket 'Strings' (id: Strings)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### length()

> method

``` python
length()
```

> Node [String Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_length.html)

#### Information:
- **Socket** : self



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### match_string()

> method

``` python
match_string(operation: "Literal['Starts With', 'Ends With', 'Contains']" = None, key: 'String' = None)
```

> Node [Match String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/match_string.html)

#### Information:
- **Socket** : self



#### Arguments:
- **operation** (_Literal['Starts With', 'Ends With', 'Contains']_ = None) : ('Starts With', 'Ends With', 'Contains')
- **key** (_String_ = None) : socket 'Key' (id: Key)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(b: 'String' = None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'STRING'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'NOT_EQUAL'



#### Arguments:
- **b** (_String_ = None) : socket 'B' (id: B_STR)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### replace()

> method

``` python
replace(find: 'String' = None, replace: 'String' = None)
```

> Node [Replace String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/replace_string.html)

#### Information:
- **Socket** : self



#### Arguments:
- **find** (_String_ = None) : socket 'Find' (id: Find)
- **replace** (_String_ = None) : socket 'Replace' (id: Replace)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### slice()

> method

``` python
slice(position: 'Integer' = None, length: 'Integer' = None)
```

> Node [Slice String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/slice_string.html)

#### Information:
- **Socket** : self



#### Arguments:
- **position** (_Integer_ = None) : socket 'Position' (id: Position)
- **length** (_Integer_ = None) : socket 'Length' (id: Length)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(size: 'Float' = None, character_spacing: 'Float' = None, word_spacing: 'Float' = None, line_spacing: 'Float' = None, text_box_width: 'Float' = None, align_x: "Literal['LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH']" = 'LEFT', align_y: "Literal['TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM']" = 'TOP_BASELINE', font=None, overflow: "Literal['OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE']" = 'OVERFLOW', pivot_mode: "Literal['MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT']" = 'BOTTOM_LEFT')
```

> Node [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **size** (_Float_ = None) : socket 'Size' (id: Size)
- **character_spacing** (_Float_ = None) : socket 'Character Spacing' (id: Character Spacing)
- **word_spacing** (_Float_ = None) : socket 'Word Spacing' (id: Word Spacing)
- **line_spacing** (_Float_ = None) : socket 'Line Spacing' (id: Line Spacing)
- **text_box_width** (_Float_ = None) : socket 'Text Box Width' (id: Text Box Width)
- **align_x** (_Literal['LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH']_ = LEFT) : parameter 'align_x' in ['LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH']
- **align_y** (_Literal['TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM']_ = TOP_BASELINE) : parameter 'align_y' in ['TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM']
- **font** (_Blender VectorFont | str_ = None) : VectorFont, or name of a valid font in bpy.types.fonts (see `utils.get_font`)
- **overflow** (_Literal['OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE']_ = OVERFLOW) : parameter 'overflow' in ['OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE']
- **pivot_mode** (_Literal['MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT']_ = BOTTOM_LEFT) : parameter 'pivot_mode' in ['MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT']



#### Returns:
- **Instances** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### to_float()

> method

``` python
to_float()
```

> Node [String to Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT'



#### Returns:
- **Float** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### to_integer()

> method

``` python
to_integer()
```

> Node [String to Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### to_value()

> method

``` python
to_value(data_type: "Literal['FLOAT', 'INT']" = 'FLOAT')
```

> Node [String to Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_value.html)

#### Information:
- **Socket** : self



#### Arguments:
- **data_type** (_Literal['FLOAT', 'INT']_ = FLOAT) : parameter 'data_type' in ['FLOAT', 'INT']



#### Returns:
- **Float** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>