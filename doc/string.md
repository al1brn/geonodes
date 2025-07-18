# String

``` python
String(value='', name=None, tip=None, panel='', subtype='NONE', hide_value=False, hide_in_modifier=False)
```

Socket of type String

Node [String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/string.html)

A group input socket of type String is created if the name is not None.

#### Arguments:
- **value** (_str or Socket_ = ) : initial value
- **name** (_str_ = None) : group input socket name if not None
- **tip** (_str_ = None) : user type for group input socket
- **panel** (_str_ = ) : panel name (overrides tree pane if exists)
- **subtype** (_str in ('NONE', 'FILE_PATH')_ = NONE) : sub type for group input
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **C** : [contains](string.md#contains)
- **E** : [ends_with](string.md#ends_with) :black_small_square: [equal](string.md#equal)
- **F** : [FilePath](string.md#filepath) :black_small_square: [find](string.md#find) :black_small_square: [find_in_string](string.md#find_in_string) :black_small_square: [Format](string.md#format) :black_small_square: [format](string.md#format)
- **H** : [hash_value](string.md#hash_value)
- **I** : [ImportText](string.md#importtext) :black_small_square: [\_\_init__](string.md#__init__)
- **J** : [Join](string.md#join) :black_small_square: [join](string.md#join)
- **L** : [length](string.md#length)
- **N** : [not_equal](string.md#not_equal)
- **R** : [replace](string.md#replace)
- **S** : [slice](string.md#slice) :black_small_square: [special_characters](string.md#special_characters) :black_small_square: [starts_with](string.md#starts_with)
- **T** : [to_curves](string.md#to_curves)

## Methods



----------
### contains()

> method

``` python
contains(key=None)
```

> Node [Match String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/match_string.html)

#### Information:
- **Socket** : self
- **Parameter** : 'CONTAINS'



#### Arguments:
- **key** (_String_ = None) : socket 'Key' (id: Key)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### ends_with()

> method

``` python
ends_with(key=None)
```

> Node [Match String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/match_string.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ENDS_WITH'



#### Arguments:
- **key** (_String_ = None) : socket 'Key' (id: Key)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b=None)
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
FilePath(value='', name='File Path', tip=None, panel='', hide_value=False, hide_in_modifier=False)
```

File Path input String

New [String](string.md#string) input with subtype 'FILE_PATH'.

#### Arguments:
- **value** ( = )
- **name** ( = File Path)
- **tip** ( = None)
- **panel** ( = )
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### find()

> method

``` python
find(search=None)
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
find_in_string(search=None)
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
Format(format=None)
```

> Node [Format String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/format_string.html)

#### Arguments:
- **format** (_String_ = None) : socket 'Format' (id: Format)



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### format()

> method

``` python
format()
```

> Node [Format String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/format_string.html)

#### Information:
- **Socket** : self



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed=None)
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
ImportText(path=None)
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
__init__(value='', name=None, tip=None, panel='', subtype='NONE', hide_value=False, hide_in_modifier=False)
```

Socket of type String

Node [String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/string.html)

A group input socket of type String is created if the name is not None.

#### Arguments:
- **value** (_str or Socket_ = ) : initial value
- **name** (_str_ = None) : group input socket name if not None
- **tip** (_str_ = None) : user type for group input socket
- **panel** (_str_ = ) : panel name (overrides tree pane if exists)
- **subtype** (_str in ('NONE', 'FILE_PATH')_ = NONE) : sub type for group input
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### Join()

> classmethod

``` python
Join(*strings, delimiter=None)
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
join(*strings)
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
### not_equal()

> method

``` python
not_equal(b=None)
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
replace(find=None, replace=None)
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
slice(position=None, length=None)
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
### special_characters()

> classmethod

``` python
special_characters()
```

> Node [Special Characters](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/special_characters.html)

#### Returns:
- **node** (_String_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### starts_with()

> method

``` python
starts_with(key=None)
```

> Node [Match String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/match_string.html)

#### Information:
- **Socket** : self
- **Parameter** : 'STARTS_WITH'



#### Arguments:
- **key** (_String_ = None) : socket 'Key' (id: Key)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(size=None, character_spacing=None, word_spacing=None, line_spacing=None, text_box_width=None, align_x='LEFT', align_y='TOP_BASELINE', font=None, overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT')
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
- **align_x** (_str_ = LEFT) : parameter 'align_x' in ['LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH']
- **align_y** (_str_ = TOP_BASELINE) : parameter 'align_y' in ['TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM']
- **font** (_Blender VectorFont | str_ = None) : VectorFont, or name of a valid font in bpy.types.fonts (see `utils.get_font`)
- **overflow** (_str_ = OVERFLOW) : parameter 'overflow' in ['OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE']
- **pivot_mode** (_str_ = BOTTOM_LEFT) : parameter 'pivot_mode' in ['MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT']



#### Returns:
- **Instances** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](string.md#string) :black_small_square: [Content](string.md#content) :black_small_square: [Methods](string.md#methods)</sub>