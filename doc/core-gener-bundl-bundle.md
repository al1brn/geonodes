# Bundle

``` python
Bundle(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
```

> The output socket of a [Node](node.md#node)

**Socket** is the base class for data classes such as [Float](core-gener-float-float.md#float), [Image](core-gener-image-image.md#image) or [Geometry](core-gener-geome-geometry.md#geometry).

It refers to an **output** socket of a [Node](node.md#node). A socket can be set to the **input** socket
of another [Node](node.md#node) to create a link between the two nodes:

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Node("Cube").mesh

# cube is set the to socket 'geometry' of node 'Set Position'
node = Node("Set Position")
node.geometry = cube
```

!!! important
> You can access to the other output sockets of the node in two different ways:
> - using [node](core-socket.md#node) attribute
> - using ***peer socket** naming convention where the **snake_case** name of
>.  the other sockets is suffixed by '_'

The example below shows how to access the to 'UV Map' socket of node [Cube](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cube.html):

``` python
# cube is the output socket 'Mesh' of the node 'Cube'
cube = Mesh.Cube()

# Getting 'UV Map' through the node
uv_map = cube.node.uv_map

# Or using the 'peer socket' naming convention
uv_map = cuve.uv_map_
```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None) : input name if not None
- **tip** (_str_ = ) : description
- **panel** (_str_ = ) : panel name
- **user_label** (_str_ = None) : user label
- **props**

### Inherited

[add_method](group.md#add_method) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](core-boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [menu](core-gener-menu---menu.md#menu) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-gener-menu-menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [Named](core-gener-boole-boolean.md#named) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](core-color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](core-closure.md#_pop) :black_small_square: [\_push](core-closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](core-cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [\_test_socket_to_data_type](core-socket.md#_test_socket_to_data_type) :black_small_square: ['_tree' not found]() :black_small_square: [\_ul](core-socket.md#_ul) :black_small_square: ['_use_layout' not found]() :black_small_square: [user_label](core-socket.md#user_label) :black_small_square:

## Content

- [Combine](core-gener-bundl-bundle.md#combine)
- [\_create_input_socket](core-gener-bundl-bundle.md#_create_input_socket)
- [enable_output](core-gener-bundl-bundle.md#enable_output)
- [get_item](core-gener-bundl-bundle.md#get_item)
- [join](core-gener-bundl-bundle.md#join)
- [join_bundle](core-gener-bundl-bundle.md#join_bundle)
- [separate_bundle](core-gener-bundl-bundle.md#separate_bundle)
- [set_item](core-gener-bundl-bundle.md#set_item)
- [store_item](core-gener-bundl-bundle.md#store_item)

## Methods



----------
### Combine()

> classmethod

``` python
Combine(named_sockets: 'dict' = {}, define_signature=False, **sockets)
```

> Node [Combine Bundle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/utilities/bundles/combine_bundle.html)

#### Arguments:
- **named_sockets** (_dict_ = {})
- **define_signature** (_bool_ = False) : parameter 'define_signature'
- **sockets**



#### Returns:
- **Bundle** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Bundle](core-gener-bundl-bundle.md#bundle) :black_small_square: [Content](core-gener-bundl-bundle.md#content) :black_small_square: [Methods](core-gener-bundl-bundle.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(name: 'str' = 'Bundle', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False)
```

> Bundle Input

New [Bundle](core-gener-bundl-bundle.md#bundle) input with subtype 'NONE'.

Aguments
--------
- name  (str = 'Bundle') : Input socket name
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier

#### Arguments:
- **name** (_str_ = Bundle)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)



#### Returns:
- **Bundle** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Bundle](core-gener-bundl-bundle.md#bundle) :black_small_square: [Content](core-gener-bundl-bundle.md#content) :black_small_square: [Methods](core-gener-bundl-bundle.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BUNDLE'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Bundle** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Bundle](core-gener-bundl-bundle.md#bundle) :black_small_square: [Content](core-gener-bundl-bundle.md#content) :black_small_square: [Methods](core-gener-bundl-bundle.md#methods)</sub>

----------
### get_item()

> method

``` python
get_item(path: 'String' = None, remove: 'Boolean' = None, socket_type: "Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT']" = 'FLOAT', structure_type: "Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE']" = 'AUTO')
```

> Node [Get Bundle Item](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/utilities/bundles/get_bundle_item.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self



#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)
- **remove** (_Boolean_ = None) : socket 'Remove' (id: Remove)
- **socket_type** (_Literal['FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'RGBA', 'ROTATION', 'MATRIX', 'STRING', 'MENU', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'MATERIAL', 'BUNDLE', 'CLOSURE', 'FONT']_ = FLOAT) : parameter 'socket_type' in ('Float', 'Integer', 'Boolean', 'Vector', 'Color', 'Rotation', 'Matrix', 'String', 'Menu', 'Object', 'Image', 'Geometry', 'Collection', 'Material', 'Bundle', 'Closure', 'Font')
- **structure_type** (_Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE']_ = AUTO) : parameter 'structure_type' in ('Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single')



#### Returns:
- **Item** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Bundle](core-gener-bundl-bundle.md#bundle) :black_small_square: [Content](core-gener-bundl-bundle.md#content) :black_small_square: [Methods](core-gener-bundl-bundle.md#methods)</sub>

----------
### join()

> method

``` python
join(*bundle: 'Bundle')
```

> Node [Join Bundle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/utilities/bundles/join_bundle.html)

#### Arguments:
- **bundle** (_Bundle_) : socket 'Bundle' (id: Bundle)



#### Returns:
- **Bundle** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Bundle](core-gener-bundl-bundle.md#bundle) :black_small_square: [Content](core-gener-bundl-bundle.md#content) :black_small_square: [Methods](core-gener-bundl-bundle.md#methods)</sub>

----------
### join_bundle()

> method

``` python
join_bundle(*bundle: 'Bundle')
```

> Node [Join Bundle](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../interface/controls/nodes/types/utilities/bundles/join_bundle.html)

#### Arguments:
- **bundle** (_Bundle_) : socket 'Bundle' (id: Bundle)



#### Returns:
- **Bundle** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Bundle](core-gener-bundl-bundle.md#bundle) :black_small_square: [Content](core-gener-bundl-bundle.md#content) :black_small_square: [Methods](core-gener-bundl-bundle.md#methods)</sub>

----------
### separate_bundle()

> method

``` python
separate_bundle(named_sockets: 'dict' = {}, define_signature=False, **sockets)
```

> Node [Separate Bundle](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/utilities/bundles/separate_bundle.html)

#### Information:
- **Socket** : self



#### Arguments:
- **named_sockets** (_dict_ = {})
- **define_signature** (_bool_ = False) : parameter 'define_signature'
- **sockets**



#### Returns:
- **node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Bundle](core-gener-bundl-bundle.md#bundle) :black_small_square: [Content](core-gener-bundl-bundle.md#content) :black_small_square: [Methods](core-gener-bundl-bundle.md#methods)</sub>

----------
### set_item()

> method

``` python
set_item(path: 'String' = None, item: 'Float' = None, structure_type: "Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE']" = 'AUTO')
```

> Node [Store Bundle Item](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/utilities/bundles/store_bundle_item.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : socket_type



#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)
- **item** (_Float_ = None) : socket 'Item' (id: Item)
- **structure_type** (_Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE']_ = AUTO) : parameter 'structure_type' in ('Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single')



#### Returns:
- **Bundle** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Bundle](core-gener-bundl-bundle.md#bundle) :black_small_square: [Content](core-gener-bundl-bundle.md#content) :black_small_square: [Methods](core-gener-bundl-bundle.md#methods)</sub>

----------
### store_item()

> method

``` python
store_item(path: 'String' = None, item: 'Float' = None, structure_type: "Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE']" = 'AUTO')
```

> Node [Store Bundle Item](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/utilities/bundles/store_bundle_item.html)

> ***Jump*** : Socket refers to node output socket after the call

#### Information:
- **Socket** : self
- **Parameter** : socket_type



#### Arguments:
- **path** (_String_ = None) : socket 'Path' (id: Path)
- **item** (_Float_ = None) : socket 'Item' (id: Item)
- **structure_type** (_Literal['AUTO', 'DYNAMIC', 'FIELD', 'GRID', 'LIST', 'SINGLE']_ = AUTO) : parameter 'structure_type' in ('Auto', 'Dynamic', 'Field', 'Grid', 'List', 'Single')



#### Returns:
- **Bundle** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Bundle](core-gener-bundl-bundle.md#bundle) :black_small_square: [Content](core-gener-bundl-bundle.md#content) :black_small_square: [Methods](core-gener-bundl-bundle.md#methods)</sub>