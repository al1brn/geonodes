# Matrix

> Bases classes: [Socket](geono-socket.md#socket)

``` python
Matrix(value=None, name=None, tip=None)
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

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_reset](geono-socket.md#_reset) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_output](geono-socket.md#to_output) :black_small_square:

## Content

- **A** : [array](geono-matrix.md#array)
- **C** : [c1r1](geono-matrix.md#c1r1) :black_small_square: [c1r2](geono-matrix.md#c1r2) :black_small_square: [c1r3](geono-matrix.md#c1r3) :black_small_square: [c1r4](geono-matrix.md#c1r4) :black_small_square: [c2r1](geono-matrix.md#c2r1) :black_small_square: [c2r2](geono-matrix.md#c2r2) :black_small_square: [c2r3](geono-matrix.md#c2r3) :black_small_square: [c2r4](geono-matrix.md#c2r4) :black_small_square: [c3r1](geono-matrix.md#c3r1) :black_small_square: [c3r2](geono-matrix.md#c3r2) :black_small_square: [c3r3](geono-matrix.md#c3r3) :black_small_square: [c3r4](geono-matrix.md#c3r4) :black_small_square: [c4r1](geono-matrix.md#c4r1) :black_small_square: [c4r2](geono-matrix.md#c4r2) :black_small_square: [c4r3](geono-matrix.md#c4r3) :black_small_square: [c4r4](geono-matrix.md#c4r4) :black_small_square: [Combine](geono-matrix.md#combine)
- **F** : [FromArray](geono-matrix.md#fromarray)
- **I** : [invert](geono-matrix.md#invert)
- **M** : [multiply](geono-matrix.md#multiply)
- **N** : [Named](geono-matrix.md#named) :black_small_square: [NamedAttribute](geono-matrix.md#namedattribute)
- **P** : [project_point](geono-matrix.md#project_point)
- **R** : [rotation](geono-matrix.md#rotation)
- **S** : [scale](geono-matrix.md#scale) :black_small_square: [separate_matrix](geono-matrix.md#separate_matrix) :black_small_square: [separate_transform](geono-matrix.md#separate_transform)
- **T** : [Transform](geono-matrix.md#transform) :black_small_square: [transform_direction](geono-matrix.md#transform_direction) :black_small_square: [transform_point](geono-matrix.md#transform_point) :black_small_square: [translation](geono-matrix.md#translation) :black_small_square: [transpose](geono-matrix.md#transpose)

## Properties



### array

> _type_: **numpy**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html) as a numpy array shaped (4, 4)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c1r1

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 1 row 1

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c1r2

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 1 row 2

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c1r3

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 1 row 3

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c1r4

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 1 row 4

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c2r1

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 2 row 1

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c2r2

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 2 row 2

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c2r3

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 2 row 3

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c2r4

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 2 row 4

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c3r1

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 3 row 1

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c3r2

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 3 row 2

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c3r3

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 3 row 3

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c3r4

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 3 row 4

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c4r1

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 4 row 1

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c4r2

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 4 row 2

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c4r3

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 4 row 3

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### c4r4

> _type_: **Float**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html), column 4 row 4

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### rotation

> _type_: **Rotation**
>

> Socket 'Rotation' of node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### scale

> _type_: **Vector**
>

> Socket 'Scale' of node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### separate_matrix

> _type_: **Node**
>

> Node [Separate Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_matrix.html)

> [!CAUTION]
> By exception, this method returns the node, not the first output socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### separate_transform

> _type_: **Node**
>

> Node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

> [!CAUTION]
> By exception, this property returns the node, not the first output socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

### translation

> _type_: **Vector**
>

> Socket 'Translation' of node [Separate Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/separate_transform.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Properties](geono-matrix.md#properties)</sub>

## Methods



----------
### Combine()

> classmethod

``` python
Combine(c1r1=1, c1r2=0, c1r3=0, c1r4=0, c2r1=0, c2r2=1, c2r3=0, c2r4=0, c3r1=0, c3r2=0, c3r3=1, c3r4=0, c4r1=0, c4r2=0, c4r3=0, c4r4=1)
```

> Constructor node [Combine Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_matrix.html)

#### Arguments:
- **c1r1** (_Float_ = 1) : socket 'Column 1 Row 1' (Column 1 Row 1)
- **c1r2** (_Float_ = 0) : socket 'Column 1 Row 2' (Column 1 Row 2)
- **c1r3** (_Float_ = 0) : socket 'Column 1 Row 3' (Column 1 Row 3)
- **c1r4** (_Float_ = 0) : socket 'Column 1 Row 4' (Column 1 Row 4)
- **c2r1** (_Float_ = 0) : socket 'Column 2 Row 1' (Column 2 Row 1)
- **c2r2** (_Float_ = 1) : socket 'Column 2 Row 2' (Column 2 Row 2)
- **c2r3** (_Float_ = 0) : socket 'Column 2 Row 3' (Column 2 Row 3)
- **c2r4** (_Float_ = 0) : socket 'Column 2 Row 4' (Column 2 Row 4)
- **c3r1** (_Float_ = 0) : socket 'Column 3 Row 1' (Column 3 Row 1)
- **c3r2** (_Float_ = 0) : socket 'Column 3 Row 2' (Column 3 Row 2)
- **c3r3** (_Float_ = 1) : socket 'Column 3 Row 3' (Column 3 Row 3)
- **c3r4** (_Float_ = 0) : socket 'Column 3 Row 4' (Column 3 Row 4)
- **c4r1** (_Float_ = 0) : socket 'Column 4 Row 1' (Column 4 Row 1)
- **c4r2** (_Float_ = 0) : socket 'Column 4 Row 2' (Column 4 Row 2)
- **c4r3** (_Float_ = 0) : socket 'Column 4 Row 3' (Column 4 Row 3)
- **c4r4** (_Float_ = 1) : socket 'Column 4 Row 4' (Column 4 Row 4)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

----------
### invert()

> method

``` python
invert()
```

> Node [Invert Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/invert_matrix.html)

#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(other)
```

> Node [Multiply Matrices](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/multiply_matrices.html)

> [!NOTE]
> Operator **@** can be used as an alternative

``` python
# Multiply to matrices
mat3 = mat0.multiply(mat1)

# or
mat3 = mat0 @ mat1
```

#### Arguments:
- **other** (_Matrix_) : socket 'Matrix' (Matrix_001)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

'Named' is a synonym of 'NamedAttribute'

``` python
with GeoNodes("Named Attributes"):

    cube = Mesh.Cube()

    # Create a named attribute
    cube.points.store("Some Value", Float.Random(0, 1, seed=0))

    # Read the random value to offset along z
    cube.points.offset = (0, 0, Float.Named("Some Value"))

    # Remove the named attribute
    cube.remove_named_attribute("Some*", exact=False)

    cube.out()
```

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

'Named' is a synonym of 'NamedAttribute'

``` python
with GeoNodes("Named Attributes"):

    cube = Mesh.Cube()

    # Create a named attribute
    cube.points.store("Some Value", Float.Random(0, 1, seed=0))

    # Read the random value to offset along z
    cube.points.offset = (0, 0, Float.NamedAttribute("Some Value"))

    # Remove the named attribute
    cube.remove_named_attribute("Some*", exact=False)

    cube.out()
```

#### Arguments:
- **name** (_String_) : socket 'Name' (Name)



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

----------
### project_point()

> method

``` python
project_point(vector)
```

> Node [Project Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/project_point.html)

#### Arguments:
- **vector** (_Vector_) : socket 'Vector' (Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

----------
### Transform()

> classmethod

``` python
Transform(translation=None, rotation=None, scale=None)
```

> Constructor node [Combine Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/combine_transform.html)

#### Arguments:
- **translation** (_Vector_ = None) : socket 'Translation' (Translation)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)



#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

----------
### transform_direction()

> method

``` python
transform_direction(vector)
```

> Node [Transform Direction](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transform_direction.html)

#### Arguments:
- **vector**



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

----------
### transform_point()

> method

``` python
transform_point(vector)
```

> Node [Transform Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transform_point.html)

> [!NOTE]
> Operator **@** can be used as an alternative

``` python
# Transform a point
Q = mat.transform_point(P)

# or
Q = mat @ P
```

#### Arguments:
- **vector** (_Vector_) : socket 'Vector' (Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>

----------
### transpose()

> method

``` python
transpose()
```

> Node [Transpose Matrix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/matrix/transpose_matrix.html)

#### Returns:
- **Matrix** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Matrix](geono-matrix.md#matrix) :black_small_square: [Content](geono-matrix.md#content) :black_small_square: [Methods](geono-matrix.md#methods)</sub>