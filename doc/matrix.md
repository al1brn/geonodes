# Matrix

``` python
Matrix(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

Matrix Socket.

You can easily pass from a python 16-items list of tuple to a Matrix.

The Matrix default constructor accepts such as list as initialization argument:

``` python
M = Matrix([0]*16)
```

You can decompose a Matrix directly to a 16-tuple with the property `as_tuple`:

``` python
m = Matrix().as_tuple
```

``` python
from geonodes import GeoNodes, Mesh, Layout, Matrix

with GeoNodes("Matrix Test"):
    
    with Layout("Base"):
        M0 = Matrix()
        M1 = Matrix(name="Your Matrix")
        M = M0 @ M1
        M @= Matrix.CombineTransform((1, 2, 3), (4, 5, 6), (7, 8, 9))
        
    with Layout("Combine"):
        M0 = Matrix([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        vals = M0.as_tuple
        M1 = Matrix(vals)
        
        M @= M1

    with Layout("Named Attribute"):
        g = Mesh()
        g.points.A_Matrix = M
        
        b = M1 @ Matrix("A Matrix")
        g.faces.store("Another matrix", b)
        
    g.out()
```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [out](color.md#out) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](closure.md#_pop) :black_small_square: [\_push](closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- **A** : [as_tuple](matrix.md#as_tuple)
- **C** : [column_1_row_1](matrix.md#column_1_row_1) :black_small_square: [column_1_row_2](matrix.md#column_1_row_2) :black_small_square: [column_1_row_3](matrix.md#column_1_row_3) :black_small_square: [column_1_row_4](matrix.md#column_1_row_4) :black_small_square: [column_2_row_1](matrix.md#column_2_row_1) :black_small_square: [column_2_row_2](matrix.md#column_2_row_2) :black_small_square: [column_2_row_3](matrix.md#column_2_row_3) :black_small_square: [column_2_row_4](matrix.md#column_2_row_4) :black_small_square: [column_3_row_1](matrix.md#column_3_row_1) :black_small_square: [column_3_row_2](matrix.md#column_3_row_2) :black_small_square: [column_3_row_3](matrix.md#column_3_row_3) :black_small_square: [column_3_row_4](matrix.md#column_3_row_4) :black_small_square: [column_4_row_1](matrix.md#column_4_row_1) :black_small_square: [column_4_row_2](matrix.md#column_4_row_2) :black_small_square: [column_4_row_3](matrix.md#column_4_row_3) :black_small_square: [column_4_row_4](matrix.md#column_4_row_4) :black_small_square: [Combine](matrix.md#combine) :black_small_square: [CombineTransform](matrix.md#combinetransform) :black_small_square: [\_create_input_socket](matrix.md#_create_input_socket)
- **D** : [determinant](matrix.md#determinant)
- **E** : [enable_output](matrix.md#enable_output)
- **F** : [FromArray](matrix.md#fromarray)
- **H** : [hash_value](matrix.md#hash_value)
- **I** : [invert](matrix.md#invert)
- **M** : [multiply](matrix.md#multiply)
- **N** : [Named](matrix.md#named) :black_small_square: [NamedAttribute](matrix.md#namedattribute)
- **P** : [project_point](matrix.md#project_point)
- **R** : [rotation](matrix.md#rotation)
- **S** : [scale](matrix.md#scale) :black_small_square: [separate](matrix.md#separate) :black_small_square: [separate_matrix](matrix.md#separate_matrix) :black_small_square: [separate_transform](matrix.md#separate_transform)
- **T** : [transform_direction](matrix.md#transform_direction) :black_small_square: [transform_gizmo](matrix.md#transform_gizmo) :black_small_square: [transform_point](matrix.md#transform_point) :black_small_square: [translation](matrix.md#translation) :black_small_square: [transpose](matrix.md#transpose) :black_small_square: [trs](matrix.md#trs)

## Properties



### as_tuple

> _type_: **tuple**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Properties](matrix.md#properties)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(name: 'str' = 'Matrix', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'INSTANCE_TRANSFORM']" = 'VALUE', shape: "Literal['AUTO', 'DYNAMIC', 'FIELD', 'SINGLE']" = 'AUTO')
```

> Matrix Input

New [Matrix](matrix.md#matrix) input with subtype 'NONE'.

Aguments
--------
- name  (str = 'Matrix') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
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
multiply(matrix: 'Matrix' = None)
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
Named(name: 'String' = None)
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
NamedAttribute(name: 'String' = None)
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
project_point(vector: 'Vector' = None)
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
transform_direction(direction: 'Vector' = None)
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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](matrix.md#matrix) :black_small_square: [Content](matrix.md#content) :black_small_square: [Methods](matrix.md#methods)</sub>

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