# Matrix

``` python
Matrix(socket=None, name: str = None, tip: str = '', panel: str = '', user_label: str = None, **props)
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

[add_method](group.md#add_method) :black_small_square: ['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [\_class_test](core-boolean.md#_class_test) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [menu](core-gener-menu---menu.md#menu) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](core-gener-menu-menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](core-color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](core-closure.md#_pop) :black_small_square: [\_push](core-closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](core-cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: [\_test_socket_to_data_type](core-socket.md#_test_socket_to_data_type) :black_small_square: ['_tree' not found]() :black_small_square: [\_ul](core-socket.md#_ul) :black_small_square: ['_use_layout' not found]() :black_small_square: [user_label](core-socket.md#user_label) :black_small_square:

## Content

- **A** : [as_tuple](core-gener-matri-matrix.md#as_tuple)
- **C** : [column_1_row_1](core-gener-matri-matrix.md#column_1_row_1) :black_small_square: [column_1_row_2](core-gener-matri-matrix.md#column_1_row_2) :black_small_square: [column_1_row_3](core-gener-matri-matrix.md#column_1_row_3) :black_small_square: [column_1_row_4](core-gener-matri-matrix.md#column_1_row_4) :black_small_square: [column_2_row_1](core-gener-matri-matrix.md#column_2_row_1) :black_small_square: [column_2_row_2](core-gener-matri-matrix.md#column_2_row_2) :black_small_square: [column_2_row_3](core-gener-matri-matrix.md#column_2_row_3) :black_small_square: [column_2_row_4](core-gener-matri-matrix.md#column_2_row_4) :black_small_square: [column_3_row_1](core-gener-matri-matrix.md#column_3_row_1) :black_small_square: [column_3_row_2](core-gener-matri-matrix.md#column_3_row_2) :black_small_square: [column_3_row_3](core-gener-matri-matrix.md#column_3_row_3) :black_small_square: [column_3_row_4](core-gener-matri-matrix.md#column_3_row_4) :black_small_square: [column_4_row_1](core-gener-matri-matrix.md#column_4_row_1) :black_small_square: [column_4_row_2](core-gener-matri-matrix.md#column_4_row_2) :black_small_square: [column_4_row_3](core-gener-matri-matrix.md#column_4_row_3) :black_small_square: [column_4_row_4](core-gener-matri-matrix.md#column_4_row_4) :black_small_square: [Combine](core-gener-matri-matrix.md#combine) :black_small_square: [CombineTransform](core-gener-matri-matrix.md#combinetransform) :black_small_square: [\_create_input_socket](core-gener-matri-matrix.md#_create_input_socket)
- **D** : [determinant](core-gener-matri-matrix.md#determinant)
- **E** : [enable_output](core-gener-matri-matrix.md#enable_output)
- **H** : [hash_value](core-gener-matri-matrix.md#hash_value)
- **I** : [invert](core-gener-matri-matrix.md#invert)
- **M** : [multiply](core-gener-matri-matrix.md#multiply)
- **N** : [Named](core-gener-matri-matrix.md#named) :black_small_square: [NamedAttribute](core-gener-matri-matrix.md#namedattribute)
- **P** : [project_point](core-gener-matri-matrix.md#project_point)
- **R** : [rotation](core-gener-matri-matrix.md#rotation)
- **S** : [scale](core-gener-matri-matrix.md#scale) :black_small_square: [separate](core-gener-matri-matrix.md#separate) :black_small_square: [separate_matrix](core-gener-matri-matrix.md#separate_matrix) :black_small_square: [separate_transform](core-gener-matri-matrix.md#separate_transform) :black_small_square: [svd](core-gener-matri-matrix.md#svd)
- **T** : [transform_direction](core-gener-matri-matrix.md#transform_direction) :black_small_square: [transform_gizmo](core-gener-matri-matrix.md#transform_gizmo) :black_small_square: [transform_point](core-gener-matri-matrix.md#transform_point) :black_small_square: [translation](core-gener-matri-matrix.md#translation) :black_small_square: [transpose](core-gener-matri-matrix.md#transpose) :black_small_square: [trs](core-gener-matri-matrix.md#trs)

## Properties



### as_tuple

> _type_: **tuple**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_1_row_1

> _type_: **column_1_row_1**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_1_row_2

> _type_: **column_1_row_2**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_1_row_3

> _type_: **column_1_row_3**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_1_row_4

> _type_: **column_1_row_4**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_2_row_1

> _type_: **column_2_row_1**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_2_row_2

> _type_: **column_2_row_2**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_2_row_3

> _type_: **column_2_row_3**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_2_row_4

> _type_: **column_2_row_4**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_3_row_1

> _type_: **column_3_row_1**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_3_row_2

> _type_: **column_3_row_2**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_3_row_3

> _type_: **column_3_row_3**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_3_row_4

> _type_: **column_3_row_4**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_4_row_1

> _type_: **column_4_row_1**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_4_row_2

> _type_: **column_4_row_2**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_4_row_3

> _type_: **column_4_row_3**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### column_4_row_4

> _type_: **column_4_row_4**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### rotation

> _type_: **rotation**
>

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### scale

> _type_: **scale**
>

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### translation

> _type_: **translation**
>

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

### trs

> _type_: **tuple**
>

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Properties](core-gener-matri-matrix.md#properties)</sub>

## Methods



----------
### Combine()

> classmethod

``` python
Combine(column_1_row_1: 'Float' = None, column_1_row_2: 'Float' = None, column_1_row_3: 'Float' = None, column_1_row_4: 'Float' = None, column_2_row_1: 'Float' = None, column_2_row_2: 'Float' = None, column_2_row_3: 'Float' = None, column_2_row_4: 'Float' = None, column_3_row_1: 'Float' = None, column_3_row_2: 'Float' = None, column_3_row_3: 'Float' = None, column_3_row_4: 'Float' = None, column_4_row_1: 'Float' = None, column_4_row_2: 'Float' = None, column_4_row_3: 'Float' = None, column_4_row_4: 'Float' = None)
```

> Node [Combine Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_matrix.html)

#### Arguments:
- **column_1_row_1** (_Float_ = None) : socket 'Column 1 Row 1' (id: Column 1 Row 1)
- **column_1_row_2** (_Float_ = None) : socket 'Column 1 Row 2' (id: Column 1 Row 2)
- **column_1_row_3** (_Float_ = None) : socket 'Column 1 Row 3' (id: Column 1 Row 3)
- **column_1_row_4** (_Float_ = None) : socket 'Column 1 Row 4' (id: Column 1 Row 4)
- **column_2_row_1** (_Float_ = None) : socket 'Column 2 Row 1' (id: Column 2 Row 1)
- **column_2_row_2** (_Float_ = None) : socket 'Column 2 Row 2' (id: Column 2 Row 2)
- **column_2_row_3** (_Float_ = None) : socket 'Column 2 Row 3' (id: Column 2 Row 3)
- **column_2_row_4** (_Float_ = None) : socket 'Column 2 Row 4' (id: Column 2 Row 4)
- **column_3_row_1** (_Float_ = None) : socket 'Column 3 Row 1' (id: Column 3 Row 1)
- **column_3_row_2** (_Float_ = None) : socket 'Column 3 Row 2' (id: Column 3 Row 2)
- **column_3_row_3** (_Float_ = None) : socket 'Column 3 Row 3' (id: Column 3 Row 3)
- **column_3_row_4** (_Float_ = None) : socket 'Column 3 Row 4' (id: Column 3 Row 4)
- **column_4_row_1** (_Float_ = None) : socket 'Column 4 Row 1' (id: Column 4 Row 1)
- **column_4_row_2** (_Float_ = None) : socket 'Column 4 Row 2' (id: Column 4 Row 2)
- **column_4_row_3** (_Float_ = None) : socket 'Column 4 Row 3' (id: Column 4 Row 3)
- **column_4_row_4** (_Float_ = None) : socket 'Column 4 Row 4' (id: Column 4 Row 4)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### CombineTransform()

> classmethod

``` python
CombineTransform(translation: 'Vector' = None, rotation: 'Rotation' = None, scale: 'Vector' = None)
```

> Node [Combine Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_transform.html)

#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (id: Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(name: 'str' = 'Matrix', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'INSTANCE_TRANSFORM']" = 'VALUE', shape: "Literal['AUTO', 'DYNAMIC', 'FIELD', 'SINGLE']" = 'AUTO')
```

> Matrix Input

New [Matrix](core-gener-matri-matrix.md#matrix) input with subtype 'NONE'.

Aguments
--------
- name  (str = 'Matrix') : Input socket name
- tip  (str = '') : Property description
panel : str, optional
    Panel name Default: "".

- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'INSTANCE_TRANSFORM')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'DYNAMIC', 'FIELD', 'SINGLE')

#### Arguments:
- **name** (_str_ = Matrix)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'INSTANCE_TRANSFORM']_ = VALUE)
- **shape** (_Literal['AUTO', 'DYNAMIC', 'FIELD', 'SINGLE']_ = AUTO)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### determinant()

> method

``` python
determinant()
```

> Node [Matrix Determinant](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/matrix_determinant.html)

#### Information:
- **Socket** : self



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MATRIX'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed: 'Integer' = None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MATRIX'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### invert()

> method

``` python
invert()
```

> Node [Invert Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/invert_matrix.html)

#### Information:
- **Socket** : self



#### Returns:
- **Matrix** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(matrix: 'Matrix' = None)
```

> Node [Multiply Matrices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/multiply_matrices.html)

#### Information:
- **Socket** : self



#### Arguments:
- **matrix** (_Matrix_ = None) : socket 'Matrix' (id: Matrix_001)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT4X4'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT4X4'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### project_point()

> method

``` python
project_point(vector: 'Vector' = None)
```

> Node [Project Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/project_point.html)

#### Information:
- **Socket** : self



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### separate()

> method

``` python
separate()
```

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

#### Information:
- **Socket** : self



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### separate_matrix()

> method

``` python
separate_matrix()
```

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

#### Information:
- **Socket** : self



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### separate_transform()

> method

``` python
separate_transform()
```

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

#### Information:
- **Socket** : self



#### Returns:
- **node** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### svd()

> method

``` python
svd()
```

> Node [Matrix SVD](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/matrix_svd.html)

#### Information:
- **Socket** : self



#### Returns:
- **Matrix** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### transform_direction()

> method

``` python
transform_direction(direction: 'Vector' = None)
```

> Node [Transform Direction](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transform_direction.html)

#### Information:
- **Socket** : self



#### Arguments:
- **direction** (_Vector_ = None) : socket 'Direction' (id: Direction)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### transform_gizmo()

> method

``` python
transform_gizmo(*value: 'Matrix', position: 'Vector' = None, rotation: 'Rotation' = None, use_rotation_x=True, use_rotation_y=True, use_rotation_z=True, use_scale_x=True, use_scale_y=True, use_scale_z=True, use_translation_x=True, use_translation_y=True, use_translation_z=True)
```

> Node ERROR: Node 'Transform Gizmo' not found

#### Arguments:
- **value** (_Matrix_) : socket 'Value' (id: Value)
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **use_rotation_x** (_bool_ = True) : parameter 'use_rotation_x'
- **use_rotation_y** (_bool_ = True) : parameter 'use_rotation_y'
- **use_rotation_z** (_bool_ = True) : parameter 'use_rotation_z'
- **use_scale_x** (_bool_ = True) : parameter 'use_scale_x'
- **use_scale_y** (_bool_ = True) : parameter 'use_scale_y'
- **use_scale_z** (_bool_ = True) : parameter 'use_scale_z'
- **use_translation_x** (_bool_ = True) : parameter 'use_translation_x'
- **use_translation_y** (_bool_ = True) : parameter 'use_translation_y'
- **use_translation_z** (_bool_ = True) : parameter 'use_translation_z'



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### transform_point()

> method

``` python
transform_point(vector: 'Vector' = None)
```

> Node [Transform Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transform_point.html)

#### Information:
- **Socket** : self



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>

----------
### transpose()

> method

``` python
transpose()
```

> Node [Transpose Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transpose_matrix.html)

#### Information:
- **Socket** : self



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](core-gener-matri-matrix.md#matrix) :black_small_square: [Content](core-gener-matri-matrix.md#content) :black_small_square: [Methods](core-gener-matri-matrix.md#methods)</sub>