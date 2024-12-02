# GeoNodes

> Bases classes: [Tree](geono-treea-tree.md#tree)

``` python
GeoNodes(tree_name, clear=True, fake_user=False, is_group=False, prefix=None)
```

> Geometry Nodes

#### Arguments:
- **tree_name** (_str_) : Geometry Nodes name
- **clear** (_bool_ = True) : clear the tree content
- **fake_user** (_bool_ = False) : set fake_user flag
- **is_group** (_bool_ = False) : tree is a group
- **prefix** (_str_ = None) : name prefix

### Inherited

[arrange](tree.md#arrange) :black_small_square: [backwards](geono-treea-node.md#backwards) :black_small_square: [bnode](geono-treea-node.md#bnode) :black_small_square: [btree](geono-treea-tree.md#btree) :black_small_square: [children](frame.md#children) :black_small_square: [clear](tree.md#clear) :black_small_square: [clear_io_sockets](tree.md#clear_io_sockets) :black_small_square: [del_link](geono-treea-tree.md#del_link) :black_small_square: [del_node](geono-treea-tree.md#del_node) :black_small_square: [del_reroutes](geono-treea-tree.md#del_reroutes) :black_small_square: [del_temp_frames](geono-treea-tree.md#del_temp_frames) :black_small_square: [dimensions](frame.md#dimensions) :black_small_square: [\_display_counter](tree.md#_display_counter) :black_small_square: [dump](tree.md#dump) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [first_io_socket_is_geometry](tree.md#first_io_socket_is_geometry) :black_small_square: [forwards](geono-treea-node.md#forwards) :black_small_square: [frame_reroutes](frame.md#frame_reroutes) :black_small_square: [gen_node_headers](tree.md#gen_node_headers) :black_small_square: [\_get_color](tree.md#_get_color) :black_small_square: [get_data_socket_class](tree.md#get_data_socket_class) :black_small_square: [\_\_getitem__](geono-treea-tree.md#__getitem__) :black_small_square: [group_input_per_frame](geono-treea-tree.md#group_input_per_frame) :black_small_square: [group_inputs](geono-treea-tree.md#group_inputs) :black_small_square: [has_node_editor](geono-treea-tree.md#has_node_editor) :black_small_square: [height](geono-treea-node.md#height) :black_small_square: [in_nodes](frame.md#in_nodes) :black_small_square: [input_node](tree.md#input_node) :black_small_square: [in_zone](geono-treea-node.md#in_zone) :black_small_square: [io_socket_exists](tree.md#io_socket_exists) :black_small_square: [is_child_of](geono-treea-node.md#is_child_of) :black_small_square: [is_frame](geono-treea-node.md#is_frame) :black_small_square: [is_layout](geono-treea-node.md#is_layout) :black_small_square: [is_reroute](geono-treea-node.md#is_reroute) :black_small_square: [link](tree.md#link) :black_small_square: [new_frame](geono-treea-tree.md#new_frame) :black_small_square: [new_input](tree.md#new_input) :black_small_square: [new_input_from_input_socket](tree.md#new_input_from_input_socket) :black_small_square: [new_io_socket](tree.md#new_io_socket) :black_small_square: [new_link](geono-treea-tree.md#new_link) :black_small_square: [new_node](geono-treea-tree.md#new_node) :black_small_square: [new_output](tree.md#new_output) :black_small_square: [new_reroute](geono-treea-tree.md#new_reroute) :black_small_square: [out_nodes](frame.md#out_nodes) :black_small_square: [output_node](tree.md#output_node) :black_small_square: [parent](geono-treea-tree.md#parent) :black_small_square: [pop](layout.md#pop) :black_small_square: [push](layout.md#push) :black_small_square: [register_node](tree.md#register_node) :black_small_square: [remove_groups](tree.md#remove_groups) :black_small_square: [\_\_repr__](geono-treea-node.md#__repr__) :black_small_square: [\_reset_counters](tree.md#_reset_counters) :black_small_square: [set_input_socket_default](tree.md#set_input_socket_default) :black_small_square: [single_group_input](geono-treea-tree.md#single_group_input) :black_small_square: [split_peers](geono-treea-node.md#split_peers) :black_small_square: [\_\_str__](geono-treea-tree.md#__str__) :black_small_square: [\_str_stats](tree.md#_str_stats) :black_small_square: [tree](geono-treea-node.md#tree) :black_small_square: [value_to_socket](tree.md#value_to_socket) :black_small_square: [wait](geono-treea-node.md#wait) :black_small_square: [width](geono-treea-node.md#width) :black_small_square: [zones_in_frame](geono-treea-tree.md#zones_in_frame) :black_small_square:

## Content

- [\_\_init__](geono-geono-geonodes.md#__init__)
- [is_tool](geono-geono-geonodes.md#is_tool)
- [Tool](geono-geono-geonodes.md#tool)

## Properties



### is_tool

> _type_: **bool**
>

> Is a tool

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoNodes](geono-geono-geonodes.md#geonodes) :black_small_square: [Content](geono-geono-geonodes.md#content) :black_small_square: [Properties](geono-geono-geonodes.md#properties)</sub>

## Methods



----------
### \_\_init__()

> method

``` python
__init__(tree_name, clear=True, fake_user=False, is_group=False, prefix=None)
```

> Geometry Nodes

#### Arguments:
- **tree_name** (_str_) : Geometry Nodes name
- **clear** (_bool_ = True) : clear the tree content
- **fake_user** (_bool_ = False) : set fake_user flag
- **is_group** (_bool_ = False) : tree is a group
- **prefix** (_str_ = None) : name prefix

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoNodes](geono-geono-geonodes.md#geonodes) :black_small_square: [Content](geono-geono-geonodes.md#content) :black_small_square: [Methods](geono-geono-geonodes.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [GeoNodes](geono-geono-geonodes.md#geonodes) :black_small_square: [Content](geono-geono-geonodes.md#content) :black_small_square: [Methods](geono-geono-geonodes.md#methods)</sub>