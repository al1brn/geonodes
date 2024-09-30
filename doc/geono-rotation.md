# Rotation

> Bases classes: [ValueSocket](geono-valuesocket.md#valuesocket)

``` python
Rotation(value=(0.0, 0.0, 0.0), name=None, tip=None)
```

> Socket of type ROTATION

If **value** argument is None:
- if **name** argument is None, a node [Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/rotation.html) is added
- otherwise a new group input is created using **tip** argument.

If **value** argument is not None, a new **Rotation** is created from the value:
- using a [Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/rotation.html) node if the **value** is a float or a tuple of floats
- using [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/combine_xyz.html) and [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html) nodes if the **value**
  is a tuple containing [Sockets](geono-socket.md#socket)

``` python
rot = Rotation()                    # 'Rotation' node
rot = Rotation((1, 2, 3.14)).       # 'Rotation' node
rot = Rotation((Float(1), 2, 3.14)) # 'Combine XYZ' + 'Euler to Rotation' nodes
rot = Rotation(name="User input").  # Create a new Rotation group input
```

#### Arguments:
- **value** (_tuple of floats or Sockets_ = (0.0, 0.0, 0.0)) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)

### Inherited

[blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [Named](geono-valuesocket.md#named) :black_small_square: [NamedAttribute](geono-valuesocket.md#namedattribute) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [out](geono-socket.md#out) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [to_output](geono-socket.md#to_output) :black_small_square:

## Content

- **A** : [AlignToVector](geono-rotation.md#aligntovector) :black_small_square: [align_to_vector](geono-rotation.md#align_to_vector) :black_small_square: [AlignXToVector](geono-rotation.md#alignxtovector) :black_small_square: [align_x_to_vector](geono-rotation.md#align_x_to_vector) :black_small_square: [AlignYToVector](geono-rotation.md#alignytovector) :black_small_square: [align_y_to_vector](geono-rotation.md#align_y_to_vector) :black_small_square: [AlignZToVector](geono-rotation.md#alignztovector) :black_small_square: [align_z_to_vector](geono-rotation.md#align_z_to_vector) :black_small_square: [AxesToRotation](geono-rotation.md#axestorotation) :black_small_square: [AxisAngleToRotation](geono-rotation.md#axisangletorotation)
- **C** : [Combine](geono-rotation.md#combine)
- **E** : [EulerToRotation](geono-rotation.md#eulertorotation)
- **F** : [FromAxes](geono-rotation.md#fromaxes) :black_small_square: [FromAxisAngle](geono-rotation.md#fromaxisangle) :black_small_square: [FromEuler](geono-rotation.md#fromeuler) :black_small_square: [FromQuaternion](geono-rotation.md#fromquaternion) :black_small_square: [FromXYAxes](geono-rotation.md#fromxyaxes) :black_small_square: [FromXZAxes](geono-rotation.md#fromxzaxes) :black_small_square: [FromYXAxes](geono-rotation.md#fromyxaxes) :black_small_square: [FromYZAxes](geono-rotation.md#fromyzaxes) :black_small_square: [FromZXAxes](geono-rotation.md#fromzxaxes) :black_small_square: [FromZYAxes](geono-rotation.md#fromzyaxes)
- **I** : [invert](geono-rotation.md#invert)
- **M** : [mix](geono-rotation.md#mix)
- **Q** : [QuaternionToRotation](geono-rotation.md#quaterniontorotation)
- **R** : [Random](geono-rotation.md#random) :black_small_square: [rotate](geono-rotation.md#rotate) :black_small_square: [rotate_global](geono-rotation.md#rotate_global) :black_small_square: [rotate_local](geono-rotation.md#rotate_local) :black_small_square: [rotate_vector](geono-rotation.md#rotate_vector)
- **S** : [separate_xyz](geono-rotation.md#separate_xyz)
- **T** : [to_axis_angle](geono-rotation.md#to_axis_angle) :black_small_square: [to_euler](geono-rotation.md#to_euler) :black_small_square: [to_quaternion](geono-rotation.md#to_quaternion)
- **X** : [x](geono-rotation.md#x)
- **Y** : [y](geono-rotation.md#y)
- **Z** : [z](geono-rotation.md#z)

## Properties



### separate_xyz

> _type_: **Node**
>

> Node <&Separate XYZ"

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Properties](geono-rotation.md#properties)</sub>

### x

> _type_: **Float**
>

Socket 'X' of node ERROR: Node 'XYZ' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Properties](geono-rotation.md#properties)</sub>

### y

> _type_: **Float**
>

Socket 'Y' of node ERROR: Node 'XYZ' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Properties](geono-rotation.md#properties)</sub>

### z

> _type_: **Float**
>

Socket 'Z' of node ERROR: Node 'XYZ' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Properties](geono-rotation.md#properties)</sub>

## Methods



----------
### AlignToVector()

> classmethod

``` python
AlignToVector(vector=None, factor=None, axis='Z', pivot_axis='AUTO')
```

> Constructor node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

> [!NOTE]
> This constructor creates a [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html) node without
> connecting the 'Rotation' input socket. To align a **Rotation** other than
> **Identity** uses method [align_to_vector](geono-rotation.md#align_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **axis** (_str_ = Z) : Node.axis in ('X', 'Y', 'Z')
- **pivot_axis** (_str_ = AUTO) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### align_to_vector()

> method

``` python
align_to_vector(vector=None, factor=None, axis='Z', pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **axis** (_str_ = Z) : Node.axis in ('X', 'Y', 'Z')
- **pivot_axis** (_str_ = AUTO) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### AlignXToVector()

> classmethod

``` python
AlignXToVector(vector=None, factor=None, pivot_axis=None)
```

> Constructor node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html), axis = X

> [!NOTE]
> This constructor creates a [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html) node without
> connecting the 'Rotation' input socket. To align a **Rotation** other than
> **Identity** uses method [align_x_to_vector](geono-rotation.md#align_x_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### align_x_to_vector()

> method

``` python
align_x_to_vector(vector=None, factor=None, pivot_axis=None)
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html), axis = 'X'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### AlignYToVector()

> classmethod

``` python
AlignYToVector(vector=None, factor=None, pivot_axis=None)
```

> Constructor node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html), axis = Y

> [!NOTE]
> This constructor creates a [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html) node without
> connecting the 'Rotation' input socket. To align a **Rotation** other than
> **Identity** uses method [align_y_to_vector](geono-rotation.md#align_y_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### align_y_to_vector()

> method

``` python
align_y_to_vector(vector=None, factor=None, pivot_axis=None)
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html), axis = 'Y'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### AlignZToVector()

> classmethod

``` python
AlignZToVector(vector=None, factor=None, pivot_axis=None)
```

> Constructor node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html), axis = Z

> [!NOTE]
> This constructor creates a [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html) node without
> connecting the 'Rotation' input socket. To align a **Rotation** other than
> **Identity** uses method [align_z_to_vector](geono-rotation.md#align_z_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### align_z_to_vector()

> method

``` python
align_z_to_vector(vector=None, factor=None, pivot_axis=None)
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html), axis = 'Z'

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### AxesToRotation()

> classmethod

``` python
AxesToRotation(primary_axis=None, secondary_axis=None, primary_align='Z', secondary_align='X')
```

> Constructor node ERROR: Node 'Axes to Rotation' not found

> [!NOTE]
> This constructor is homonym of [FromAxes](geono-rotation.md#fromaxes) constructor
> See also [FromXYAxes](geono-rotation.md#fromxyaxes), [FromYXAxes](geono-rotation.md#fromyxaxes), [FromXZAxes](geono-rotation.md#fromxzaxes), [FromZXAxes](geono-rotation.md#fromzxaxes), [FromYZAxes](geono-rotation.md#fromyzaxes), [FromZYAxes](geono-rotation.md#fromzyaxes),

> [!NOTE]
> In the node ERROR: Node 'Axes to Rotation' not found, the parameter names is the **snake_case** version
> of the sockets (primary_target and 'Primary Target').
> It is why, the corresponding arguments are renamed into **primary_align** and **secondary_align**.

#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (Secondary Axis)
- **primary_align** (_str_ = Z) : Node.primary_axis in ('X', 'Y', 'Z')
- **secondary_align** (_str_ = X) : Node.secondary_axis in ('X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### AxisAngleToRotation()

> classmethod

``` python
AxisAngleToRotation(axis=(0, 0, 1), angle=0)
```

> Node [Axis Angle to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axis_angle_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromAxisAngle](geono-rotation.md#fromaxisangle) constructor

#### Arguments:
- **axis** (_Vector_ = (0, 0, 1)) : socket 'Axis' (Axis)
- **angle** (_Float_ = 0) : socket 'Angle' (Angle)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### Combine()

> classmethod

``` python
Combine(x, y, z)
```

Constructor node ERROR: Node 'XYZ' not found

#### Arguments:
- **x**
- **y**
- **z**



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### EulerToRotation()

> classmethod

``` python
EulerToRotation(euler=(0, 0, 0))
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromEuler](geono-rotation.md#fromeuler) constructor

#### Arguments:
- **euler** (_Vector_ = (0, 0, 0)) : socket 'Euler' (Euler)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromAxes()

> classmethod

``` python
FromAxes(primary_axis=None, secondary_axis=None, primary_align='Z', secondary_align='X')
```

> Constructor node ERROR: Node 'Axes to Rotation' not found

> [!NOTE]
> This constructor is synonym of [AxesToRotation](geono-rotation.md#axestorotation) constructor
> See also [FromXYAxes](geono-rotation.md#fromxyaxes), [FromYXAxes](geono-rotation.md#fromyxaxes), [FromXZAxes](geono-rotation.md#fromxzaxes), [FromZXAxes](geono-rotation.md#fromzxaxes), [FromYZAxes](geono-rotation.md#fromyzaxes), [FromZYAxes](geono-rotation.md#fromzyaxes),

> [!NOTE]
> In the node ERROR: Node 'Axes to Rotation' not found, the parameter names is the **snake_case** version
> of the sockets (primary_target and 'Primary Target').
> It is why, the corresponding arguments are renamed into **primary_align** and **secondary_align**.

#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (Secondary Axis)
- **primary_align** (_str_ = Z) : Node.primary_axis in ('X', 'Y', 'Z')
- **secondary_align** (_str_ = X) : Node.secondary_axis in ('X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromAxisAngle()

> classmethod

``` python
FromAxisAngle(axis=(0, 0, 1), angle=0)
```

> Node [Axis Angle to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axis_angle_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [AxisAngleToRotation](geono-rotation.md#axisangletorotation) constructor

#### Arguments:
- **axis** (_Vector_ = (0, 0, 1)) : socket 'Axis' (Axis)
- **angle** (_Float_ = 0) : socket 'Angle' (Angle)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromEuler()

> classmethod

``` python
FromEuler(euler=(0, 0, 0))
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [EulerToRotation](geono-rotation.md#eulertorotation) constructor

#### Arguments:
- **euler** (_Vector_ = (0, 0, 0)) : socket 'Euler' (Euler)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromQuaternion()

> classmethod

``` python
FromQuaternion(w=0, x=0, y=0, z=0)
```

> Node [Quaternion to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/quaternion_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [QuaternionToRotation](geono-rotation.md#quaterniontorotation) constructor

#### Arguments:
- **w** (_Float_ = 0) : socket 'W' (W)
- **x** (_Float_ = 0) : socket 'X' (X)
- **y** (_Float_ = 0) : socket 'Y' (Y)
- **z** (_Float_ = 0) : socket 'Z' (Z)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromXYAxes()

> classmethod

``` python
FromXYAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node ERROR: Node 'Axes to Rotation' not found, with XY alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with X
- **secondary_axis** (_Vector_ = None) : axis aligned with Y



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromXZAxes()

> classmethod

``` python
FromXZAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node ERROR: Node 'Axes to Rotation' not found, with XZ alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with X
- **secondary_axis** (_Vector_ = None) : axis aligned with Z



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromYXAxes()

> classmethod

``` python
FromYXAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node ERROR: Node 'Axes to Rotation' not found, with YX alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with Y
- **secondary_axis** (_Vector_ = None) : axis aligned with X



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromYZAxes()

> classmethod

``` python
FromYZAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node ERROR: Node 'Axes to Rotation' not found, with YZ alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with Y
- **secondary_axis** (_Vector_ = None) : axis aligned with Z



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromZXAxes()

> classmethod

``` python
FromZXAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node ERROR: Node 'Axes to Rotation' not found, with ZX alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with Z
- **secondary_axis** (_Vector_ = None) : axis aligned with X



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### FromZYAxes()

> classmethod

``` python
FromZYAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node ERROR: Node 'Axes to Rotation' not found, with ZY alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with Z
- **secondary_axis** (_Vector_ = None) : axis aligned with Y



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### invert()

> method

``` python
invert()
```

> Node [Invert Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/invert_rotation.html)

#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### mix()

> method

``` python
mix(factor=None, other=None, clamp_factor=None)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor_Float)
- **other** (_Rotation_ = None) : socket 'B' (B_Float)
- **clamp_factor** (_bool_ = None) : Node.clamp_factor



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### QuaternionToRotation()

> classmethod

``` python
QuaternionToRotation(w=0, x=0, y=0, z=0)
```

> Node [Quaternion to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/quaternion_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromQuaternion](geono-rotation.md#fromquaternion) constructor

#### Arguments:
- **w** (_Float_ = 0) : socket 'W' (W)
- **x** (_Float_ = 0) : socket 'X' (X)
- **y** (_Float_ = 0) : socket 'Y' (Y)
- **z** (_Float_ = 0) : socket 'Z' (Z)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(min=None, max=None, id=None, seed=None)
```

Constructor node [Value](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../modeling/geometry_nodes/input/constant/value.html)

#### Arguments:
- **min** ( = None)
- **max** ( = None)
- **id** ( = None)
- **seed** ( = None)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(rotate_by=None, rotation_space='GLOBAL')
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html)

> See also [rotate_local](geono-rotation.md#rotate_local) and [rotate_global](geono-rotation.md#rotate_global)

#### Arguments:
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (Rotate By)
- **rotation_space** (_str_ = GLOBAL) : Node.rotation_space in ('GLOBAL', 'LOCAL')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### rotate_global()

> method

``` python
rotate_global(rotate_by=None)
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html), rotation_space='GLOBAL'

> [!NOTE]
> Operator **@** can be used as an alternative

``` python
# Rotate rotation r
s = rotation.rotate_global(r)

# or
s = rotation @ r
```

#### Arguments:
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (Rotate By)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### rotate_local()

> method

``` python
rotate_local(rotate_by=None)
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html), rotation_space='LOCAL'

#### Arguments:
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (Rotate By)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### rotate_vector()

> method

``` python
rotate_vector(vector=None)
```

> Node [Rotate Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_vector.html)

> [!NOTE]
> Operator **@** can be used as an alternative

``` python
# Rotate vector v
w = rotation.rotate_vector(v)

# or
w = rotation @ v
```

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### to_axis_angle()

> method

``` python
to_axis_angle()
```

> Node ERROR: Node 'Rotation to Axis Angle' not found

> [!NOTE]
> The method returns the [Vector](geono-vector.md#vector). To get the angle, you can use
> the **peer socket** naming :

``` python
vect = rotation.to_axis_angle()
angle = vect.angle_ # equivalent to vect.node.angle
```

#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### to_euler()

> method

``` python
to_euler()
```

> Node [Rotation to Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotation_to_euler.html)

#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>

----------
### to_quaternion()

> method

``` python
to_quaternion()
```

> Node [Rotation to Quaternion](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotation_to_quaternion.html)

> [!CAUTION]
> By exception, this method returns the node, not the first output socket

``` python
quat = rotation.to_quaternion()
w = quat.w
x = quat.x
y = quat.y
z = quat.z
```

#### Returns:
- **Node** : node with **w**, **x**, **y** and **z** properties

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](geono-rotation.md#rotation) :black_small_square: [Content](geono-rotation.md#content) :black_small_square: [Methods](geono-rotation.md#methods)</sub>