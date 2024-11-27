# Rotation

> Bases classes: [Attribute](attribute.md#attribute)

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
  is a tuple containing [Sockets](socket.md#socket)

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

[blur](socket.md#blur) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [hash_value](socket.md#hash_value) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [Named](attribute.md#named) :black_small_square: [NamedAttribute](attribute.md#namedattribute) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square:

## Content

- **A** : [AlignToVector](rotation.md#aligntovector) :black_small_square: [align_to_vector](rotation.md#align_to_vector) :black_small_square: [AlignXToVector](rotation.md#alignxtovector) :black_small_square: [align_x_to_vector](rotation.md#align_x_to_vector) :black_small_square: [AlignYToVector](rotation.md#alignytovector) :black_small_square: [align_y_to_vector](rotation.md#align_y_to_vector) :black_small_square: [AlignZToVector](rotation.md#alignztovector) :black_small_square: [align_z_to_vector](rotation.md#align_z_to_vector) :black_small_square: [AxesToRotation](rotation.md#axestorotation) :black_small_square: [AxisAngleToRotation](rotation.md#axisangletorotation)
- **C** : [Combine](rotation.md#combine)
- **E** : [EulerToRotation](rotation.md#eulertorotation)
- **F** : [FromAxes](rotation.md#fromaxes) :black_small_square: [FromAxisAngle](rotation.md#fromaxisangle) :black_small_square: [FromEuler](rotation.md#fromeuler) :black_small_square: [FromQuaternion](rotation.md#fromquaternion) :black_small_square: [FromXYAxes](rotation.md#fromxyaxes) :black_small_square: [FromXZAxes](rotation.md#fromxzaxes) :black_small_square: [FromYXAxes](rotation.md#fromyxaxes) :black_small_square: [FromYZAxes](rotation.md#fromyzaxes) :black_small_square: [FromZXAxes](rotation.md#fromzxaxes) :black_small_square: [FromZYAxes](rotation.md#fromzyaxes)
- **I** : [\_\_init__](rotation.md#__init__) :black_small_square: [invert](rotation.md#invert)
- **M** : [mix](rotation.md#mix)
- **Q** : [QuaternionToRotation](rotation.md#quaterniontorotation)
- **R** : [Random](rotation.md#random) :black_small_square: [rotate](rotation.md#rotate) :black_small_square: [rotate_global](rotation.md#rotate_global) :black_small_square: [rotate_local](rotation.md#rotate_local) :black_small_square: [rotate_vector](rotation.md#rotate_vector)
- **S** : [separate_xyz](rotation.md#separate_xyz)
- **T** : [to_axis_angle](rotation.md#to_axis_angle) :black_small_square: [to_euler](rotation.md#to_euler) :black_small_square: [to_quaternion](rotation.md#to_quaternion)
- **X** : [x](rotation.md#x)
- **Y** : [y](rotation.md#y)
- **Z** : [z](rotation.md#z)

## Properties



### separate_xyz

> _type_: **Node**
>

> Node <&Separate XYZ"

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Properties](rotation.md#properties)</sub>

### x

> _type_: **Float**
>

Socket 'X' of node ERROR: Node 'XYZ' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Properties](rotation.md#properties)</sub>

### y

> _type_: **Float**
>

Socket 'Y' of node ERROR: Node 'XYZ' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Properties](rotation.md#properties)</sub>

### z

> _type_: **Float**
>

Socket 'Z' of node ERROR: Node 'XYZ' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Properties](rotation.md#properties)</sub>

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
> **Identity** uses method [align_to_vector](rotation.md#align_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **axis** (_str_ = Z) : Node.axis in ('X', 'Y', 'Z')
- **pivot_axis** (_str_ = AUTO) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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
> **Identity** uses method [align_x_to_vector](rotation.md#align_x_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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
> **Identity** uses method [align_y_to_vector](rotation.md#align_y_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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
> **Identity** uses method [align_z_to_vector](rotation.md#align_z_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### AxesToRotation()

> classmethod

``` python
AxesToRotation(primary_axis=None, secondary_axis=None, primary_align='Z', secondary_align='X')
```

> Constructor node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromAxes](rotation.md#fromaxes) constructor
> See also [FromXYAxes](rotation.md#fromxyaxes), [FromYXAxes](rotation.md#fromyxaxes), [FromXZAxes](rotation.md#fromxzaxes), [FromZXAxes](rotation.md#fromzxaxes), [FromYZAxes](rotation.md#fromyzaxes), [FromZYAxes](rotation.md#fromzyaxes),

> [!NOTE]
> In the node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html), the parameter names is the **snake_case** version
> of the sockets (primary_target and 'Primary Target').
> It is why, the corresponding arguments are renamed into **primary_align** and **secondary_align**.

#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (Secondary Axis)
- **primary_align** (_str_ = Z) : Node.primary_axis in ('X', 'Y', 'Z')
- **secondary_align** (_str_ = X) : Node.secondary_axis in ('X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### AxisAngleToRotation()

> classmethod

``` python
AxisAngleToRotation(axis=(0, 0, 1), angle=0)
```

> Node [Axis Angle to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axis_angle_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromAxisAngle](rotation.md#fromaxisangle) constructor

#### Arguments:
- **axis** (_Vector_ = (0, 0, 1)) : socket 'Axis' (Axis)
- **angle** (_Float_ = 0) : socket 'Angle' (Angle)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### EulerToRotation()

> classmethod

``` python
EulerToRotation(euler=(0, 0, 0))
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromEuler](rotation.md#fromeuler) constructor

#### Arguments:
- **euler** (_Vector_ = (0, 0, 0)) : socket 'Euler' (Euler)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromAxes()

> classmethod

``` python
FromAxes(primary_axis=None, secondary_axis=None, primary_align='Z', secondary_align='X')
```

> Constructor node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

> [!NOTE]
> This constructor is synonym of [AxesToRotation](rotation.md#axestorotation) constructor
> See also [FromXYAxes](rotation.md#fromxyaxes), [FromYXAxes](rotation.md#fromyxaxes), [FromXZAxes](rotation.md#fromxzaxes), [FromZXAxes](rotation.md#fromzxaxes), [FromYZAxes](rotation.md#fromyzaxes), [FromZYAxes](rotation.md#fromzyaxes),

> [!NOTE]
> In the node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html), the parameter names is the **snake_case** version
> of the sockets (primary_target and 'Primary Target').
> It is why, the corresponding arguments are renamed into **primary_align** and **secondary_align**.

#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (Secondary Axis)
- **primary_align** (_str_ = Z) : Node.primary_axis in ('X', 'Y', 'Z')
- **secondary_align** (_str_ = X) : Node.secondary_axis in ('X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromAxisAngle()

> classmethod

``` python
FromAxisAngle(axis=(0, 0, 1), angle=0)
```

> Node [Axis Angle to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axis_angle_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [AxisAngleToRotation](rotation.md#axisangletorotation) constructor

#### Arguments:
- **axis** (_Vector_ = (0, 0, 1)) : socket 'Axis' (Axis)
- **angle** (_Float_ = 0) : socket 'Angle' (Angle)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromEuler()

> classmethod

``` python
FromEuler(euler=(0, 0, 0))
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [EulerToRotation](rotation.md#eulertorotation) constructor

#### Arguments:
- **euler** (_Vector_ = (0, 0, 0)) : socket 'Euler' (Euler)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromQuaternion()

> classmethod

``` python
FromQuaternion(w=0, x=0, y=0, z=0)
```

> Node [Quaternion to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/quaternion_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [QuaternionToRotation](rotation.md#quaterniontorotation) constructor

#### Arguments:
- **w** (_Float_ = 0) : socket 'W' (W)
- **x** (_Float_ = 0) : socket 'X' (X)
- **y** (_Float_ = 0) : socket 'Y' (Y)
- **z** (_Float_ = 0) : socket 'Z' (Z)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromXYAxes()

> classmethod

``` python
FromXYAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html), with XY alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with X
- **secondary_axis** (_Vector_ = None) : axis aligned with Y



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromXZAxes()

> classmethod

``` python
FromXZAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html), with XZ alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with X
- **secondary_axis** (_Vector_ = None) : axis aligned with Z



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromYXAxes()

> classmethod

``` python
FromYXAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html), with YX alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with Y
- **secondary_axis** (_Vector_ = None) : axis aligned with X



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromYZAxes()

> classmethod

``` python
FromYZAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html), with YZ alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with Y
- **secondary_axis** (_Vector_ = None) : axis aligned with Z



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromZXAxes()

> classmethod

``` python
FromZXAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html), with ZX alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with Z
- **secondary_axis** (_Vector_ = None) : axis aligned with X



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromZYAxes()

> classmethod

``` python
FromZYAxes(primary_axis=None, secondary_axis=None)
```

> Constructor node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html), with ZY alignment

#### Arguments:
- **primary_axis** (_Vector_ = None) : axis aligned with Z
- **secondary_axis** (_Vector_ = None) : axis aligned with Y



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=(0.0, 0.0, 0.0), name=None, tip=None)
```

> Socket of type ROTATION

If **value** argument is None:
- if **name** argument is None, a node [Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/rotation.html) is added
- otherwise a new group input is created using **tip** argument.

If **value** argument is not None, a new **Rotation** is created from the value:
- using a [Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/rotation.html) node if the **value** is a float or a tuple of floats
- using [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/combine_xyz.html) and [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html) nodes if the **value**
  is a tuple containing [Sockets](socket.md#socket)

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### invert()

> method

``` python
invert()
```

> Node [Invert Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/invert_rotation.html)

#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### QuaternionToRotation()

> classmethod

``` python
QuaternionToRotation(w=0, x=0, y=0, z=0)
```

> Node [Quaternion to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/quaternion_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromQuaternion](rotation.md#fromquaternion) constructor

#### Arguments:
- **w** (_Float_ = 0) : socket 'W' (W)
- **x** (_Float_ = 0) : socket 'X' (X)
- **y** (_Float_ = 0) : socket 'Y' (Y)
- **z** (_Float_ = 0) : socket 'Z' (Z)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(rotate_by=None, rotation_space='GLOBAL')
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html)

> See also [rotate_local](rotation.md#rotate_local) and [rotate_global](rotation.md#rotate_global)

#### Arguments:
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (Rotate By)
- **rotation_space** (_str_ = GLOBAL) : Node.rotation_space in ('GLOBAL', 'LOCAL')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### to_axis_angle()

> method

``` python
to_axis_angle()
```

> Node ERROR: Node 'Rotation to Axis Angle' not found

> [!NOTE]
> The method returns the [Vector](vector.md#vector). To get the angle, you can use
> the **peer socket** naming :

``` python
vect = rotation.to_axis_angle()
angle = vect.angle_ # equivalent to vect.node.angle
```

#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### to_euler()

> method

``` python
to_euler()
```

> Node [Rotation to Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotation_to_euler.html)

#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>