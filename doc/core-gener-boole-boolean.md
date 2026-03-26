# Boolean

``` python
Boolean(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
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

> [!IMPORTANT]
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

[add_method](group.md#add_method) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](core-boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [menu](core-gener-menu---menu.md#menu) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-gener-menu-menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](core-color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](core-closure.md#_pop) :black_small_square: [\_push](core-closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](core-cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [\_test_socket_to_data_type](core-socket.md#_test_socket_to_data_type) :black_small_square: ['_tree' not found]() :black_small_square: [\_ul](core-socket.md#_ul) :black_small_square: ['_use_layout' not found]() :black_small_square: [user_label](core-socket.md#user_label) :black_small_square:

## Content

- **B** : [band](core-gener-boole-boolean.md#band) :black_small_square: [bnot](core-gener-boole-boolean.md#bnot) :black_small_square: [bor](core-gener-boole-boolean.md#bor)
- **C** : [clip_grid](core-gener-boole-boolean.md#clip_grid) :black_small_square: [\_create_input_socket](core-gener-boole-boolean.md#_create_input_socket) :black_small_square: [CubeGridTopology](core-gener-boole-boolean.md#cubegridtopology)
- **E** : [enable_output](core-gener-boole-boolean.md#enable_output) :black_small_square: [error](core-gener-boole-boolean.md#error)
- **F** : [field_to_grid](core-gener-boole-boolean.md#field_to_grid)
- **G** : [grid_dilate_erode](core-gener-boole-boolean.md#grid_dilate_erode) :black_small_square: [grid_info](core-gener-boole-boolean.md#grid_info) :black_small_square: [grid_to_points](core-gener-boole-boolean.md#grid_to_points)
- **I** : [imply](core-gener-boole-boolean.md#imply) :black_small_square: [info](core-gener-boole-boolean.md#info)
- **N** : [Named](core-gener-boole-boolean.md#named) :black_small_square: [NamedAttribute](core-gener-boole-boolean.md#namedattribute) :black_small_square: [nimply](core-gener-boole-boolean.md#nimply) :black_small_square: [nor](core-gener-boole-boolean.md#nor) :black_small_square: [not_and](core-gener-boole-boolean.md#not_and)
- **P** : [prune_grid](core-gener-boole-boolean.md#prune_grid)
- **R** : [Random](core-gener-boole-boolean.md#random)
- **S** : [sample_grid](core-gener-boole-boolean.md#sample_grid) :black_small_square: [sample_grid_index](core-gener-boole-boolean.md#sample_grid_index) :black_small_square: [set_grid_background](core-gener-boole-boolean.md#set_grid_background) :black_small_square: [set_grid_transform](core-gener-boole-boolean.md#set_grid_transform)
- **U** : [uv_unwrap](core-gener-boole-boolean.md#uv_unwrap)
- **V** : [voxel_index](core-gener-boole-boolean.md#voxel_index) :black_small_square: [voxelize_grid](core-gener-boole-boolean.md#voxelize_grid)
- **W** : [warning](core-gener-boole-boolean.md#warning)
- **X** : [xnor](core-gener-boole-boolean.md#xnor) :black_small_square: [xor](core-gener-boole-boolean.md#xor)

## Methods



----------
### band()

> method

``` python
band(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'AND'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### bnot()

> method

``` python
bnot()
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NOT'



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### bor()

> method

``` python
bor(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'OR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### clip_grid()

> method

``` python
clip_grid(min_x: 'Integer' = None, min_y: 'Integer' = None, min_z: 'Integer' = None, max_x: 'Integer' = None, max_y: 'Integer' = None, max_z: 'Integer' = None)
```

> Node [Clip Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/clip_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **min_x** (_Integer_ = None) : socket 'Min X' (id: Min X)
- **min_y** (_Integer_ = None) : socket 'Min Y' (id: Min Y)
- **min_z** (_Integer_ = None) : socket 'Min Z' (id: Min Z)
- **max_x** (_Integer_ = None) : socket 'Max X' (id: Max X)
- **max_y** (_Integer_ = None) : socket 'Max Y' (id: Max Y)
- **max_z** (_Integer_ = None) : socket 'Max Z' (id: Max Z)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = False, name: 'str' = 'Boolean', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', layer_selection: 'bool' = False, shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Boolean Input

New [Boolean](core-gener-boole-boolean.md#boolean) input with subtype 'NONE'.

Aguments
--------
- value  (object = False) : Default value
- name  (str = 'Boolean') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- layer_selection  (bool = False) : Property layer_selection_field
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = False)
- **name** (_str_ = Boolean)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **layer_selection** (_bool_ = False)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### CubeGridTopology()

> classmethod

``` python
CubeGridTopology(bounds_min: 'Vector' = None, bounds_max: 'Vector' = None, resolution_x: 'Integer' = None, resolution_y: 'Integer' = None, resolution_z: 'Integer' = None, min_x: 'Integer' = None, min_y: 'Integer' = None, min_z: 'Integer' = None)
```

> Node [Cube Grid Topology](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/primitives/cube_grid_topology.html)

#### Arguments:
- **bounds_min** (_Vector_ = None) : socket 'Bounds Min' (id: Bounds Min)
- **bounds_max** (_Vector_ = None) : socket 'Bounds Max' (id: Bounds Max)
- **resolution_x** (_Integer_ = None) : socket 'Resolution X' (id: Resolution X)
- **resolution_y** (_Integer_ = None) : socket 'Resolution Y' (id: Resolution Y)
- **resolution_z** (_Integer_ = None) : socket 'Resolution Z' (id: Resolution Z)
- **min_x** (_Integer_ = None) : socket 'Min X' (id: Min X)
- **min_y** (_Integer_ = None) : socket 'Min Y' (id: Min Y)
- **min_z** (_Integer_ = None) : socket 'Min Z' (id: Min Z)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### error()

> method

``` python
error(message: 'String' = None)
```

> Node [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ERROR'



#### Arguments:
- **message** (_String_ = None) : socket 'Message' (id: Message)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### field_to_grid()

> method

``` python
field_to_grid(named_sockets: 'dict' = {}, **sockets)
```

> Node [Field to Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/field_to_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **sockets**



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### grid_dilate_erode()

> method

``` python
grid_dilate_erode(connectivity: "Literal['Face', 'Edge', 'Vertex']" = None, tiles: "Literal['Ignore', 'Expand', 'Preserve']" = None, steps: 'Integer' = None)
```

> Node ERROR: Node 'Grid Dilate & Erode' not found

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **connectivity** (_Literal['Face', 'Edge', 'Vertex']_ = None) : ('Face', 'Edge', 'Vertex')
- **tiles** (_Literal['Ignore', 'Expand', 'Preserve']_ = None) : ('Ignore', 'Expand', 'Preserve')
- **steps** (_Integer_ = None) : socket 'Steps' (id: Steps)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### grid_info()

> method

``` python
grid_info()
```

> Node [Grid Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/grid_info.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Returns:
- **Matrix** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### grid_to_points()

> method

``` python
grid_to_points()
```

> Node [Grid to Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/grid_to_points.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Returns:
- **Cloud** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### imply()

> method

``` python
imply(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'IMPLY'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### info()

> method

``` python
info(message: 'String' = None)
```

> Node [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INFO'



#### Arguments:
- **message** (_String_ = None) : socket 'Message' (id: Message)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### nimply()

> method

``` python
nimply(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NIMPLY'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### nor()

> method

``` python
nor(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NOR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### not_and()

> method

``` python
not_and(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NAND'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### prune_grid()

> method

``` python
prune_grid(mode: "Literal['Inactive', 'Threshold', 'SDF']" = None)
```

> Node [Prune Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/prune_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **mode** (_Literal['Inactive', 'Threshold', 'SDF']_ = None) : ('Inactive', 'Threshold', 'SDF')



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(probability: 'Float' = None, id: 'Integer' = None, seed: 'Integer' = None)
```

> Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Information:
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **probability** (_Float_ = None) : socket 'Probability' (id: Probability)
- **id** (_Integer_ = None) : socket 'ID' (id: ID)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### sample_grid()

> method

``` python
sample_grid(position: 'Vector' = None, interpolation: "Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']" = None)
```

> Node [Sample Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation** (_Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']_ = None) : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x: 'Integer' = None, y: 'Integer' = None, z: 'Integer' = None)
```

> Node [Sample Grid Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid_index.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **x** (_Integer_ = None) : socket 'X' (id: X)
- **y** (_Integer_ = None) : socket 'Y' (id: Y)
- **z** (_Integer_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### set_grid_background()

> method

``` python
set_grid_background(background: 'Boolean' = None, update_inactive: 'Boolean' = None)
```

> Node [Set Grid Background](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_background.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **background** (_Boolean_ = None) : socket 'Background' (id: Background)
- **update_inactive** (_Boolean_ = None) : socket 'Update Inactive' (id: Update Inactive)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### set_grid_transform()

> method

``` python
set_grid_transform(transform: 'Matrix' = None)
```

> Node [Set Grid Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_transform.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Boolean** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### uv_unwrap()

> method

``` python
uv_unwrap(seam: 'Boolean' = None, margin: 'Float' = None, fill_holes: 'Boolean' = None, method: "Literal['Angle Based', 'Conformal', 'Minimum Stretch']" = None, iterations: 'Integer' = None, no_flip: 'Boolean' = None)
```

> Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_unwrap.html)

#### Information:
- **Socket** : self



#### Arguments:
- **seam** (_Boolean_ = None) : socket 'Seam' (id: Seam)
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **fill_holes** (_Boolean_ = None) : socket 'Fill Holes' (id: Fill Holes)
- **method** (_Literal['Angle Based', 'Conformal', 'Minimum Stretch']_ = None) : ('Angle Based', 'Conformal', 'Minimum Stretch')
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)
- **no_flip** (_Boolean_ = None) : socket 'No Flip' (id: No Flip)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### voxel_index()

> classmethod

``` python
voxel_index()
```

> Node [Voxel Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/voxel_index.html)

#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### voxelize_grid()

> method

``` python
voxelize_grid()
```

> Node [Voxelize Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/voxelize_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### warning()

> method

``` python
warning(message: 'String' = None)
```

> Node [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

#### Information:
- **Socket** : self
- **Parameter** : 'WARNING'



#### Arguments:
- **message** (_String_ = None) : socket 'Message' (id: Message)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### xnor()

> method

``` python
xnor(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'XNOR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>

----------
### xor()

> method

``` python
xor(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'XOR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](core-gener-boole-boolean.md#boolean) :black_small_square: [Content](core-gener-boole-boolean.md#content) :black_small_square: [Methods](core-gener-boole-boolean.md#methods)</sub>