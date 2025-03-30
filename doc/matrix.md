# Matrix

``` python
Matrix(value=None, name=None, tip=None, panel='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

Matrix data socket ('MATRIX')

A Matrix socket can be initialized with an array of size 16 (the shape is ignored)
If **value** is None, a [Combine Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_matrix.html) with no input link is created.

If **name** argument is not None, a group input is created, using value as default initialization

``` python
input = Matrix(None, "My Matrix") # Group input of type 'Matrix' with name 'My Matrix' is created
identity = Matrix() # Identity matrix
matrix = Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]) # Node 'Combine Matrix' with an array 16 floats
```

#### Arguments:
- **value** (_array of 16 Floats_ = None) : initialization values
- **name** (_str_ = None) : Create group input socket with this name if not None
- **tip** ( = None)
- **panel** (_str_ = ) : panel name (overrides tree panel if exists)
- **default_input** (_str in ('VALUE', 'INSTANCE_TRANSFORM')_ = VALUE) : 
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **C** : [column_1_row_1](matrix.md#column_1_row_1) :black_small_square: [column_1_row_2](matrix.md#column_1_row_2) :black_small_square: [column_1_row_3](matrix.md#column_1_row_3) :black_small_square: [column_1_row_4](matrix.md#column_1_row_4) :black_small_square: [column_2_row_1](matrix.md#column_2_row_1) :black_small_square: [column_2_row_2](matrix.md#column_2_row_2) :black_small_square: [column_2_row_3](matrix.md#column_2_row_3) :black_small_square: [column_2_row_4](matrix.md#column_2_row_4) :black_small_square: [column_3_row_1](matrix.md#column_3_row_1) :black_small_square: [column_3_row_2](matrix.md#column_3_row_2) :black_small_square: [column_3_row_3](matrix.md#column_3_row_3) :black_small_square: [column_3_row_4](matrix.md#column_3_row_4) :black_small_square: [column_4_row_1](matrix.md#column_4_row_1) :black_small_square: [column_4_row_2](matrix.md#column_4_row_2) :black_small_square: [column_4_row_3](matrix.md#column_4_row_3) :black_small_square: [column_4_row_4](matrix.md#column_4_row_4) :black_small_square: [Combine](matrix.md#combine) :black_small_square: [CombineTransform](matrix.md#combinetransform)
- **D** : [determinant](matrix.md#determinant)
- **F** : [FromArray](matrix.md#fromarray)
- **H** : [hash_value](matrix.md#hash_value)
- **I** : [\_\_init__](matrix.md#__init__) :black_small_square: [invert](matrix.md#invert)
- **M** : [multiply](matrix.md#multiply)
- **N** : [Named](matrix.md#named) :black_small_square: [NamedAttribute](matrix.md#namedattribute)
- **P** : [project_point](matrix.md#project_point)
- **R** : [rotation](matrix.md#rotation)
- **S** : [scale](matrix.md#scale) :black_small_square: [separate](matrix.md#separate) :black_small_square: [separate_matrix](matrix.md#separate_matrix) :black_small_square: [separate_transform](matrix.md#separate_transform)
- **T** : [transform_direction](matrix.md#transform_direction) :black_small_square: [transform_gizmo](matrix.md#transform_gizmo) :black_small_square: [transform_point](matrix.md#transform_point) :black_small_square: [translation](matrix.md#translation) :black_small_square: [transpose](matrix.md#transpose) :black_small_square: [trs](matrix.md#trs)

## Properties



### column_1_row_1

> _type_: **column_1_row_1**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_1_row_2

> _type_: **column_1_row_2**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_1_row_3

> _type_: **column_1_row_3**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_1_row_4

> _type_: **column_1_row_4**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_2_row_1

> _type_: **column_2_row_1**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_2_row_2

> _type_: **column_2_row_2**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_2_row_3

> _type_: **column_2_row_3**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_2_row_4

> _type_: **column_2_row_4**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_3_row_1

> _type_: **column_3_row_1**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_3_row_2

> _type_: **column_3_row_2**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_3_row_3

> _type_: **column_3_row_3**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_3_row_4

> _type_: **column_3_row_4**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_4_row_1

> _type_: **column_4_row_1**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_4_row_2

> _type_: **column_4_row_2**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_4_row_3

> _type_: **column_4_row_3**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### column_4_row_4

> _type_: **column_4_row_4**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### rotation

> _type_: **rotation**
>

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### scale

> _type_: **scale**
>

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### separate

> _type_: **tuple**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### translation

> _type_: **translation**
>

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

### trs

> _type_: **tuple**
>

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

## Methods



----------
### Combine()

> classmethod

``` python
Combine(column_1_row_1=None, column_1_row_2=None, column_1_row_3=None, column_1_row_4=None, column_2_row_1=None, column_2_row_2=None, column_2_row_3=None, column_2_row_4=None, column_3_row_1=None, column_3_row_2=None, column_3_row_3=None, column_3_row_4=None, column_4_row_1=None, column_4_row_2=None, column_4_row_3=None, column_4_row_4=None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### CombineTransform()

> classmethod

``` python
CombineTransform(translation=None, rotation=None, scale=None)
```

> Node [Combine Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_transform.html)

#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (id: Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (id: Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (id: Scale)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### FromArray()

> classmethod

``` python
FromArray(array)
```

> Constructor node [Combine Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_matrix.html)

#### Arguments:
- **array** (_array of size 16_) : 16 values to use as matrix components



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed=None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MATRIX'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=None, name=None, tip=None, panel='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

Matrix data socket ('MATRIX')

A Matrix socket can be initialized with an array of size 16 (the shape is ignored)
If **value** is None, a [Combine Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_matrix.html) with no input link is created.

If **name** argument is not None, a group input is created, using value as default initialization

``` python
input = Matrix(None, "My Matrix") # Group input of type 'Matrix' with name 'My Matrix' is created
identity = Matrix() # Identity matrix
matrix = Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]) # Node 'Combine Matrix' with an array 16 floats
```

#### Arguments:
- **value** (_array of 16 Floats_ = None) : initialization values
- **name** (_str_ = None) : Create group input socket with this name if not None
- **tip** ( = None)
- **panel** (_str_ = ) : panel name (overrides tree panel if exists)
- **default_input** (_str in ('VALUE', 'INSTANCE_TRANSFORM')_ = VALUE) : 
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(matrix=None)
```

> Node [Multiply Matrices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/multiply_matrices.html)

#### Information:
- **Socket** : self



#### Arguments:
- **matrix** (_Matrix_ = None) : socket 'Matrix' (id: Matrix_001)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT4X4'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT4X4'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### project_point()

> method

``` python
project_point(vector=None)
```

> Node [Project Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/project_point.html)

#### Information:
- **Socket** : self



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### transform_direction()

> method

``` python
transform_direction(direction=None)
```

> Node [Transform Direction](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transform_direction.html)

#### Information:
- **Socket** : self



#### Arguments:
- **direction** (_Vector_ = None) : socket 'Direction' (id: Direction)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### transform_gizmo()

> method

``` python
transform_gizmo(*value, position=None, rotation=None, use_rotation_x=True, use_rotation_y=True, use_rotation_z=True, use_scale_x=True, use_scale_y=True, use_scale_z=True, use_translation_x=True, use_translation_y=True, use_translation_z=True)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### transform_point()

> method

``` python
transform_point(vector=None)
```

> Node [Transform Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transform_point.html)

#### Information:
- **Socket** : self



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>