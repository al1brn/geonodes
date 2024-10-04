# Rotation

> Bases classes: [VectRot](geono-vecto-vectrot.md#vectrot)

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

[\_\_abs__](geono-vecto-vectorlike.md#__abs__) :black_small_square: [abs](geono-vecto-vectrot.md#abs) :black_small_square: [\_\_add__](geono-vecto-vectorlike.md#__add__) :black_small_square: [add](geono-vecto-vectrot.md#add) :black_small_square: [blur](geono-socket.md#blur) :black_small_square: [\_cache](geono-nodecache.md#_cache) :black_small_square: [\_cache_reset](geono-nodecache.md#_cache_reset) :black_small_square: [\_\_ceil__](geono-vecto-vectorlike.md#__ceil__) :black_small_square: [ceil](geono-vecto-vectrot.md#ceil) :black_small_square: [check_in_list](geono-socket.md#check_in_list) :black_small_square: [clamp](geono-vecto-vectrot.md#clamp) :black_small_square: [clamp_range](geono-vecto-vectrot.md#clamp_range) :black_small_square: [Combine](geono-vecto-vectrot.md#combine) :black_small_square: [cos](geono-vecto-vectrot.md#cos) :black_small_square: [cross](geono-vecto-vectrot.md#cross) :black_small_square: [cross_product](geono-vecto-vectrot.md#cross_product) :black_small_square: [curves](geono-vecto-vectrot.md#curves) :black_small_square: [data_type](geono-socket.md#data_type) :black_small_square: [distance](geono-vecto-vectrot.md#distance) :black_small_square: [divide](geono-vecto-vectrot.md#divide) :black_small_square: [dot](geono-vecto-vectrot.md#dot) :black_small_square: [dot_product](geono-vecto-vectrot.md#dot_product) :black_small_square: [equal](geono-vecto-vectrot.md#equal) :black_small_square: [faceforward](geono-vecto-vectrot.md#faceforward) :black_small_square: [\_\_floor__](geono-vecto-vectorlike.md#__floor__) :black_small_square: [floor](geono-vecto-vectrot.md#floor) :black_small_square: [fraction](geono-vecto-vectrot.md#fraction) :black_small_square: [\_geometry_class](geono-socket.md#_geometry_class) :black_small_square: [\_\_getattr__](geono-socket.md#__getattr__) :black_small_square: [get_socket_class](geono-socket.md#get_socket_class) :black_small_square: [greater_equal](geono-vecto-vectrot.md#greater_equal) :black_small_square: [greater_than](geono-vecto-vectrot.md#greater_than) :black_small_square: [\_\_iadd__](geono-vecto-vectorlike.md#__iadd__) :black_small_square: [\_\_imod__](geono-vecto-vectorlike.md#__imod__) :black_small_square: [\_\_imul__](geono-vecto-vectorlike.md#__imul__) :black_small_square: [IndexSwitch](geono-socket.md#indexswitch) :black_small_square: [index_switch](geono-socket.md#index_switch) :black_small_square: [input_type](geono-socket.md#input_type) :black_small_square: [\_\_ipow__](geono-vecto-vectorlike.md#__ipow__) :black_small_square: [\_\_isub__](geono-vecto-vectorlike.md#__isub__) :black_small_square: [\_\_itruediv__](geono-vecto-vectorlike.md#__itruediv__) :black_small_square: [\_jump](geono-socket.md#_jump) :black_small_square: [\_lc](geono-socket.md#_lc) :black_small_square: [\_lcop](geono-socket.md#_lcop) :black_small_square: [length](geono-vecto-vectrot.md#length) :black_small_square: [less_equal](geono-vecto-vectrot.md#less_equal) :black_small_square: [less_than](geono-vecto-vectrot.md#less_than) :black_small_square: [map_range](geono-vecto-vectrot.md#map_range) :black_small_square: [map_range_linear](geono-vecto-vectrot.md#map_range_linear) :black_small_square: [map_range_smooth](geono-vecto-vectrot.md#map_range_smooth) :black_small_square: [map_range_smoother](geono-vecto-vectrot.md#map_range_smoother) :black_small_square: [map_range_stepped](geono-vecto-vectrot.md#map_range_stepped) :black_small_square: [max](geono-vecto-vectrot.md#max) :black_small_square: [MenuSwitch](geono-socket.md#menuswitch) :black_small_square: [menu_switch](geono-socket.md#menu_switch) :black_small_square: [min](geono-vecto-vectrot.md#min) :black_small_square: [\_\_mod__](geono-vecto-vectorlike.md#__mod__) :black_small_square: [modulo](geono-vecto-vectrot.md#modulo) :black_small_square: [\_\_mul__](geono-vecto-vectorlike.md#__mul__) :black_small_square: [multiply](geono-vecto-vectrot.md#multiply) :black_small_square: [multiply_add](geono-vecto-vectrot.md#multiply_add) :black_small_square: [Named](geono-attribute.md#named) :black_small_square: [NamedAttribute](geono-attribute.md#namedattribute) :black_small_square: [\_\_neg__](geono-vecto-vectorlike.md#__neg__) :black_small_square: [node](geono-socket.md#node) :black_small_square: [node_color](geono-socket.md#node_color) :black_small_square: [node_label](geono-socket.md#node_label) :black_small_square: [normalize](geono-vecto-vectrot.md#normalize) :black_small_square: [not_equal](geono-vecto-vectrot.md#not_equal) :black_small_square: [out](geono-socket.md#out) :black_small_square: [\_\_pow__](geono-vecto-vectorlike.md#__pow__) :black_small_square: [project](geono-vecto-vectrot.md#project) :black_small_square: [\_\_radd__](geono-vecto-vectorlike.md#__radd__) :black_small_square: [Random](geono-vecto-vectrot.md#random) :black_small_square: [reflect](geono-vecto-vectrot.md#reflect) :black_small_square: [refract](geono-vecto-vectrot.md#refract) :black_small_square: [\_reset](geono-vecto-vectrot.md#_reset) :black_small_square: [\_\_rmod__](geono-vecto-vectorlike.md#__rmod__) :black_small_square: [\_\_rmul__](geono-vecto-vectorlike.md#__rmul__) :black_small_square: [\_\_rpow__](geono-vecto-vectorlike.md#__rpow__) :black_small_square: [\_\_rsub__](geono-vecto-vectorlike.md#__rsub__) :black_small_square: [\_\_rtruediv__](geono-vecto-vectorlike.md#__rtruediv__) :black_small_square: [scale](geono-vecto-vectrot.md#scale) :black_small_square: [separate_xyz](geono-vecto-vectrot.md#separate_xyz) :black_small_square: [sin](geono-vecto-vectrot.md#sin) :black_small_square: [snap](geono-vecto-vectrot.md#snap) :black_small_square: [socket_type](geono-socket.md#socket_type) :black_small_square: [\_\_str__](geono-socket.md#__str__) :black_small_square: [\_\_sub__](geono-vecto-vectorlike.md#__sub__) :black_small_square: [subtract](geono-vecto-vectrot.md#subtract) :black_small_square: [Switch](geono-socket.md#switch) :black_small_square: [switch](geono-socket.md#switch) :black_small_square: [tan](geono-vecto-vectrot.md#tan) :black_small_square: [\_\_truediv__](geono-vecto-vectorlike.md#__truediv__) :black_small_square: [wrap](geono-vecto-vectrot.md#wrap) :black_small_square: [x](geono-vecto-vectrot.md#x) :black_small_square: [y](geono-vecto-vectrot.md#y) :black_small_square: [z](geono-vecto-vectrot.md#z) :black_small_square:

## Content

- **A** : [AlignToVector](macro-geono-rotation.md#aligntovector) :black_small_square: [align_to_vector](macro-geono-rotation.md#align_to_vector) :black_small_square: [AlignXToVector](macro-geono-rotation.md#alignxtovector) :black_small_square: [align_x_to_vector](macro-geono-rotation.md#align_x_to_vector) :black_small_square: [AlignYToVector](macro-geono-rotation.md#alignytovector) :black_small_square: [align_y_to_vector](macro-geono-rotation.md#align_y_to_vector) :black_small_square: [AlignZToVector](macro-geono-rotation.md#alignztovector) :black_small_square: [align_z_to_vector](macro-geono-rotation.md#align_z_to_vector) :black_small_square: [AxesToRotation](macro-geono-rotation.md#axestorotation) :black_small_square: [AxisAngleToRotation](macro-geono-rotation.md#axisangletorotation)
- **E** : [EulerToRotation](macro-geono-rotation.md#eulertorotation)
- **F** : [FromAxes](macro-geono-rotation.md#fromaxes) :black_small_square: [FromAxisAngle](macro-geono-rotation.md#fromaxisangle) :black_small_square: [FromEuler](macro-geono-rotation.md#fromeuler) :black_small_square: [FromQuaternion](macro-geono-rotation.md#fromquaternion) :black_small_square: [FromXYAxes](macro-geono-rotation.md#fromxyaxes) :black_small_square: [FromXZAxes](macro-geono-rotation.md#fromxzaxes) :black_small_square: [FromYXAxes](macro-geono-rotation.md#fromyxaxes) :black_small_square: [FromYZAxes](macro-geono-rotation.md#fromyzaxes) :black_small_square: [FromZXAxes](macro-geono-rotation.md#fromzxaxes) :black_small_square: [FromZYAxes](macro-geono-rotation.md#fromzyaxes)
- **I** : [invert](macro-geono-rotation.md#invert)
- **M** : [mix](macro-geono-rotation.md#mix)
- **Q** : [QuaternionToRotation](macro-geono-rotation.md#quaterniontorotation)
- **R** : [rotate](macro-geono-rotation.md#rotate) :black_small_square: [rotate_global](macro-geono-rotation.md#rotate_global) :black_small_square: [rotate_local](macro-geono-rotation.md#rotate_local) :black_small_square: [rotate_vector](macro-geono-rotation.md#rotate_vector)
- **T** : [to_axis_angle](macro-geono-rotation.md#to_axis_angle) :black_small_square: [to_euler](macro-geono-rotation.md#to_euler) :black_small_square: [to_quaternion](macro-geono-rotation.md#to_quaternion)

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
> **Identity** uses method [align_to_vector](macro-geono-rotation.md#align_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **axis** (_str_ = Z) : Node.axis in ('X', 'Y', 'Z')
- **pivot_axis** (_str_ = AUTO) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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
> **Identity** uses method [align_x_to_vector](macro-geono-rotation.md#align_x_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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
> **Identity** uses method [align_y_to_vector](macro-geono-rotation.md#align_y_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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
> **Identity** uses method [align_z_to_vector](macro-geono-rotation.md#align_z_to_vector)

#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (Vector)
- **factor** (_Float_ = None) : socket 'Factor' (Factor)
- **pivot_axis** (_str_ = None) : Node.pivot_axis in ('AUTO', 'X', 'Y', 'Z')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### AxesToRotation()

> classmethod

``` python
AxesToRotation(primary_axis=None, secondary_axis=None, primary_align='Z', secondary_align='X')
```

> Constructor node ERROR: Node 'Axes to Rotation' not found

> [!NOTE]
> This constructor is homonym of [FromAxes](macro-geono-rotation.md#fromaxes) constructor
> See also [FromXYAxes](macro-geono-rotation.md#fromxyaxes), [FromYXAxes](macro-geono-rotation.md#fromyxaxes), [FromXZAxes](macro-geono-rotation.md#fromxzaxes), [FromZXAxes](macro-geono-rotation.md#fromzxaxes), [FromYZAxes](macro-geono-rotation.md#fromyzaxes), [FromZYAxes](macro-geono-rotation.md#fromzyaxes),

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### AxisAngleToRotation()

> classmethod

``` python
AxisAngleToRotation(axis=(0, 0, 1), angle=0)
```

> Node [Axis Angle to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axis_angle_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromAxisAngle](macro-geono-rotation.md#fromaxisangle) constructor

#### Arguments:
- **axis** (_Vector_ = (0, 0, 1)) : socket 'Axis' (Axis)
- **angle** (_Float_ = 0) : socket 'Angle' (Angle)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### EulerToRotation()

> classmethod

``` python
EulerToRotation(euler=(0, 0, 0))
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromEuler](macro-geono-rotation.md#fromeuler) constructor

#### Arguments:
- **euler** (_Vector_ = (0, 0, 0)) : socket 'Euler' (Euler)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### FromAxes()

> classmethod

``` python
FromAxes(primary_axis=None, secondary_axis=None, primary_align='Z', secondary_align='X')
```

> Constructor node ERROR: Node 'Axes to Rotation' not found

> [!NOTE]
> This constructor is synonym of [AxesToRotation](macro-geono-rotation.md#axestorotation) constructor
> See also [FromXYAxes](macro-geono-rotation.md#fromxyaxes), [FromYXAxes](macro-geono-rotation.md#fromyxaxes), [FromXZAxes](macro-geono-rotation.md#fromxzaxes), [FromZXAxes](macro-geono-rotation.md#fromzxaxes), [FromYZAxes](macro-geono-rotation.md#fromyzaxes), [FromZYAxes](macro-geono-rotation.md#fromzyaxes),

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### FromAxisAngle()

> classmethod

``` python
FromAxisAngle(axis=(0, 0, 1), angle=0)
```

> Node [Axis Angle to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axis_angle_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [AxisAngleToRotation](macro-geono-rotation.md#axisangletorotation) constructor

#### Arguments:
- **axis** (_Vector_ = (0, 0, 1)) : socket 'Axis' (Axis)
- **angle** (_Float_ = 0) : socket 'Angle' (Angle)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### FromEuler()

> classmethod

``` python
FromEuler(euler=(0, 0, 0))
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [EulerToRotation](macro-geono-rotation.md#eulertorotation) constructor

#### Arguments:
- **euler** (_Vector_ = (0, 0, 0)) : socket 'Euler' (Euler)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### FromQuaternion()

> classmethod

``` python
FromQuaternion(w=0, x=0, y=0, z=0)
```

> Node [Quaternion to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/quaternion_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [QuaternionToRotation](macro-geono-rotation.md#quaterniontorotation) constructor

#### Arguments:
- **w** (_Float_ = 0) : socket 'W' (W)
- **x** (_Float_ = 0) : socket 'X' (X)
- **y** (_Float_ = 0) : socket 'Y' (Y)
- **z** (_Float_ = 0) : socket 'Z' (Z)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### invert()

> method

``` python
invert()
```

> Node [Invert Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/invert_rotation.html)

#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### QuaternionToRotation()

> classmethod

``` python
QuaternionToRotation(w=0, x=0, y=0, z=0)
```

> Node [Quaternion to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/quaternion_to_rotation.html)

> [!NOTE]
> This constructor is homonym of [FromQuaternion](macro-geono-rotation.md#fromquaternion) constructor

#### Arguments:
- **w** (_Float_ = 0) : socket 'W' (W)
- **x** (_Float_ = 0) : socket 'X' (X)
- **y** (_Float_ = 0) : socket 'Y' (Y)
- **z** (_Float_ = 0) : socket 'Z' (Z)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(rotate_by=None, rotation_space='GLOBAL')
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html)

> See also [rotate_local](macro-geono-rotation.md#rotate_local) and [rotate_global](macro-geono-rotation.md#rotate_global)

#### Arguments:
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (Rotate By)
- **rotation_space** (_str_ = GLOBAL) : Node.rotation_space in ('GLOBAL', 'LOCAL')



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

----------
### to_euler()

> method

``` python
to_euler()
```

> Node [Rotation to Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotation_to_euler.html)

#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](macro-geono-rotation.md#rotation) :black_small_square: [Content](macro-geono-rotation.md#content) :black_small_square: [Methods](macro-geono-rotation.md#methods)</sub>