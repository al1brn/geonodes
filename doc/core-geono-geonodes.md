# GeoNodes

``` python
GeoNodes(tree_name: str, clear: bool = True, fake_user: bool = False, is_group: bool = False, prefix: str | None = None)
```

> Geometry Nodes

#### Arguments:
- **tree_name** (_str_) : Geometry Nodes name
- **clear** (_bool_ = True) : clear the tree content
- **fake_user** (_bool_ = False) : set fake_user flag
- **is_group** (_bool_ = False) : tree is a group
- **prefix** (_str | None_ = None) : name prefix

### Inherited

[arrange](tree.md#arrange) :black_small_square: [clear](tree.md#clear) :black_small_square: [current_panel](tree.md#current_panel) :black_small_square: [\_display_counter](tree.md#_display_counter) :black_small_square: [dump](tree.md#dump) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [gen_node_headers](tree.md#gen_node_headers) :black_small_square: [\_get_color](tree.md#_get_color) :black_small_square: [get_data_socket_class](tree.md#get_data_socket_class) :black_small_square: [get_named_attribute](tree.md#get_named_attribute) :black_small_square: [get_socket_names](node.md#get_socket_names) :black_small_square: [get_socket_panel](tree.md#get_socket_panel) :black_small_square: [input_node](core-shade1-shadernodes.md#input_node) :black_small_square: [link](tree.md#link) :black_small_square: [link_nodes](tree.md#link_nodes) :black_small_square: [new_input](tree.md#new_input) :black_small_square: [new_input_from_input_socket](tree.md#new_input_from_input_socket) :black_small_square: [new_output](tree.md#new_output) :black_small_square: [output_node](core-shade1-shadernodes.md#output_node) :black_small_square: [push](layout.md#push) :black_small_square: [register_named_attribute](tree.md#register_named_attribute) :black_small_square: [register_node](tree.md#register_node) :black_small_square: [remove_groups](tree.md#remove_groups) :black_small_square: [\_reset_counters](tree.md#_reset_counters) :black_small_square: [set_input_socket_default](tree.md#set_input_socket_default) :black_small_square: [\_\_str__](core-treea-tree.md#__str__) :black_small_square: [\_str_stats](tree.md#_str_stats) :black_small_square: [value_to_socket](tree.md#value_to_socket) :black_small_square:

## Content

- [\_\_init__](core-geono-geonodes.md#__init__)
- [is_tool](core-geono-geonodes.md#is_tool)
- [Tool](core-geono-geonodes.md#tool)

## Properties



### is_tool

> _type_: **bool**
>

> Is a tool

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoNodes](core-geono-geonodes.md#geonodes) :black_small_square: [Content](core-geono-geonodes.md#content) :black_small_square: [Properties](core-geono-geonodes.md#properties)</sub>

## Methods



----------
### \_\_init__()

> method

``` python
__init__(tree_name: str, clear: bool = True, fake_user: bool = False, is_group: bool = False, prefix: str | None = None)
```

> Geometry Nodes

#### Arguments:
- **tree_name** (_str_) : Geometry Nodes name
- **clear** (_bool_ = True) : clear the tree content
- **fake_user** (_bool_ = False) : set fake_user flag
- **is_group** (_bool_ = False) : tree is a group
- **prefix** (_str | None_ = None) : name prefix

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoNodes](core-geono-geonodes.md#geonodes) :black_small_square: [Content](core-geono-geonodes.md#content) :black_small_square: [Methods](core-geono-geonodes.md#methods)</sub>

----------
### Tool()

> classmethod

``` python
Tool(tree_name, clear=True, fake_user=False, object_mode=True, edit_mode=False, sculpt_mode=False, mesh=True, curve=False, cloud=False, wait_for_click=False)
```

> Tool Geometry Nodes

#### Arguments:
- **tree_name** (_str_) : Geometry Nodes namde
- **clear** (_bool_ = True) : clear the tree content
- **fake_user** (_bool_ = False) : set fake_user flag
- **object_mode** (_bool_ = True) : tool available in object mode
- **edit_mode** (_bool_ = False) : tool available in edit mode
- **sculpt_mode** (_bool_ = False) : tool available in sculpt mode
- **mesh** (_bool_ = True) : mesh tool
- **curve** (_bool_ = False) : curve tool
- **cloud** (_bool_ = False) : cloud tool
- **wait_for_click** (_bool_ = False) : wait for click flag



#### Returns:
- **GeoNodes** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoNodes](core-geono-geonodes.md#geonodes) :black_small_square: [Content](core-geono-geonodes.md#content) :black_small_square: [Methods](core-geono-geonodes.md#methods)</sub>