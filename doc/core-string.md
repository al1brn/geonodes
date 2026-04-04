# String

``` python
String(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
```

String Socket.

    A String socket easily operated with python str.

    ``` python
    from geonodes import GeoNodes, Mesh, Layout, String, Boolean, Integer, nd, Input

    with GeoNodes("String Test") as tree:
        
        g = Mesh()
        name = String("Attribute", name="Attr name")
        g.points.store(name, 0.)
        
        a = String("String A ")
        b = a + "String B "
        c = a + (b, Integer(123).to_string())
        d = c.replace("String", "TK")
        s = String.Join(a, b, c, d, delimiter = "/")
        Boolean(True).info(s)
        
        with Layout("Match String"):
            ref_string = String("Matching test string")
            search_string = String("test", name="Search String")
            
            ok = ref_string.match_string(Input("Match"), search_string)
            ok.info(String("'{}' found in '{}'.").format(token=search_string, ref=ref_string))
            ok.bnot().warning(String("'{}' not found in '{}'.").format(token=search_string, ref=ref_string))
            
        with Layout("Conversion"):
            f = String("3.1415926").to_float()
            i = String("123").to_integer()
            
            sf = f.to_string(decimals=4)
            si = i.to_string()
            
            s = String("Float: {:.2f}, Int: {:05d} ({} and {})").format(float=f, integer=i, sfloat=sf, sint=si)
            Boolean(True).info(s)
            
        with Layout("Special"):
            _n = nd.special_characters().line_break
            _t = nd.special_characters().tab
            s = "Text with       and 
"
            s = String(s).replace(_t, "TAB").replace(_n, "LINE_BREAK")
            Boolean(True).info(s)
            
        g.out()
    ```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None) : input name if not None
- **tip** (_str_ = ) : description
- **panel** (_str_ = ) : panel name
- **user_label** (_str_ = None) : user label
- **props**

### Inherited

[add_method](group.md#add_method) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [menu](core-gener-menu---menu.md#menu) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-gener-menu-menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [Named](core-gener-boole-boolean.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](core-color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](core-closure.md#_pop) :black_small_square: [\_push](core-closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](core-cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [\_test_socket_to_data_type](core-socket.md#_test_socket_to_data_type) :black_small_square: ['_tree' not found]() :black_small_square: [\_ul](core-socket.md#_ul) :black_small_square: ['_use_layout' not found]() :black_small_square: [user_label](core-socket.md#user_label) :black_small_square:

## Content

- **C** : [\_create_input_socket](core-string.md#_create_input_socket)
- **E** : [enable_output](core-string.md#enable_output) :black_small_square: [equal](core-string.md#equal)
- **F** : [FilePath](core-string.md#filepath) :black_small_square: [find](core-string.md#find) :black_small_square: [find_in_string](core-string.md#find_in_string) :black_small_square: [Format](core-string.md#format) :black_small_square: [format](core-string.md#format)
- **H** : [hash_value](core-string.md#hash_value)
- **I** : [ImportText](core-string.md#importtext)
- **J** : [Join](core-string.md#join) :black_small_square: [join](core-string.md#join)
- **L** : [length](core-string.md#length)
- **M** : [match_string](core-string.md#match_string)
- **N** : [not_equal](core-string.md#not_equal)
- **R** : [replace](core-string.md#replace)
- **S** : [slice](core-string.md#slice)
- **T** : [to_curves](core-string.md#to_curves) :black_small_square: [to_float](core-string.md#to_float) :black_small_square: [to_integer](core-string.md#to_integer) :black_small_square: [to_value](core-string.md#to_value)

## Methods



----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = '', name: 'str' = 'String', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, subtype: 'str' = 'NONE')
```

> String Input

New [String](core-gener-strin-string.md#string) input with subtype 'NONE'.

Aguments
--------
- value  (object = "") : Default value
- name  (str = 'String') : Input socket name
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
subtype : str, optional
    Socket sub type in ('NONE', 'FILE_PATH') Default: 'NONE'.


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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

----------
### FilePath()

> classmethod

``` python
FilePath(value: 'object' = '', name: 'str' = 'FilePath', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> FilePath Input

New [String](core-gener-strin-string.md#string) input with subtype 'FILE_PATH'.

Aguments
--------
- value  (object = "") : Default value
- name  (str = 'FilePath') : Input socket name
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

----------
### to_curves()

> method

``` python
to_curves(size: 'Float' = None, font: 'Font' = None, align_x: "Literal['Left', 'Center', 'Right', 'Justify', 'Flush']" = None, align_y: "Literal['Top', 'Top Baseline', 'Middle', 'Bottom Baseline', 'Bottom']" = None, pivot_point: "Literal['Midpoint', 'Top Left', 'Top Center', 'Top Right', 'Bottom Left', 'Bottom Center', 'Bottom Right']" = None, character_spacing: 'Float' = None, word_spacing: 'Float' = None, line_spacing: 'Float' = None, overflow: "Literal['Overflow', 'Scale To Fit', 'Truncate']" = None, text_box_width: 'Float' = None, text_box_height: 'Float' = None)
```

> Node [String to Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_curves.html)

#### Information:
- **Socket** : self



#### Arguments:
- **size** (_Float_ = None) : socket 'Size' (id: Size)
- **font** (_Font_ = None) : socket 'Font' (id: Font)
- **align_x** (_Literal['Left', 'Center', 'Right', 'Justify', 'Flush']_ = None) : ('Left', 'Center', 'Right', 'Justify', 'Flush')
- **align_y** (_Literal['Top', 'Top Baseline', 'Middle', 'Bottom Baseline', 'Bottom']_ = None) : ('Top', 'Top Baseline', 'Middle', 'Bottom Baseline', 'Bottom')
- **pivot_point** (_Literal['Midpoint', 'Top Left', 'Top Center', 'Top Right', 'Bottom Left', 'Bottom Center', 'Bottom Right']_ = None) : ('Midpoint', 'Top Left', 'Top Center', 'Top Right', 'Bottom Left', 'Bottom Center', 'Bottom Right')
- **character_spacing** (_Float_ = None) : socket 'Character Spacing' (id: Character Spacing)
- **word_spacing** (_Float_ = None) : socket 'Word Spacing' (id: Word Spacing)
- **line_spacing** (_Float_ = None) : socket 'Line Spacing' (id: Line Spacing)
- **overflow** (_Literal['Overflow', 'Scale To Fit', 'Truncate']_ = None) : ('Overflow', 'Scale To Fit', 'Truncate')
- **text_box_width** (_Float_ = None) : socket 'Text Box Width' (id: Text Box Width)
- **text_box_height** (_Float_ = None) : socket 'Text Box Height' (id: Text Box Height)



#### Returns:
- **Instances** (_String_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>

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
- **data_type** (_Literal['FLOAT', 'INT']_ = FLOAT) : parameter 'data_type' in ('Float', 'Integer')



#### Returns:
- **Float** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [String](core-string.md#string) :black_small_square: [Content](core-string.md#content) :black_small_square: [Methods](core-string.md#methods)</sub>