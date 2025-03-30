# Rotation

``` python
Rotation(value=(0.0, 0.0, 0.0), name=None, tip=None, panel='', hide_value=False, hide_in_modifier=False, single_value=False)
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
- **panel** (_str_ = ) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **A** : [AlignToVector](rotation.md#aligntovector) :black_small_square: [align_toVector](rotation.md#align_tovector) :black_small_square: [AlignXToVector](rotation.md#alignxtovector) :black_small_square: [align_x_to_vector](rotation.md#align_x_to_vector) :black_small_square: [AlignYToVector](rotation.md#alignytovector) :black_small_square: [align_y_to_vector](rotation.md#align_y_to_vector) :black_small_square: [AlignZToVector](rotation.md#alignztovector) :black_small_square: [align_z_to_vector](rotation.md#align_z_to_vector) :black_small_square: [axis_angle](rotation.md#axis_angle)
- **F** : [FromAxes](rotation.md#fromaxes) :black_small_square: [FromAxisAngle](rotation.md#fromaxisangle) :black_small_square: [FromEuler](rotation.md#fromeuler) :black_small_square: [FromQuaternion](rotation.md#fromquaternion) :black_small_square: [FromXYAxes](rotation.md#fromxyaxes) :black_small_square: [FromXZAxes](rotation.md#fromxzaxes) :black_small_square: [FromYXAxes](rotation.md#fromyxaxes) :black_small_square: [FromYZAxes](rotation.md#fromyzaxes) :black_small_square: [FromZXAxes](rotation.md#fromzxaxes) :black_small_square: [FromZYAxes](rotation.md#fromzyaxes)
- **H** : [hash_value](rotation.md#hash_value)
- **I** : [\_\_init__](rotation.md#__init__) :black_small_square: [invert](rotation.md#invert)
- **M** : [mix](rotation.md#mix)
- **N** : [Named](rotation.md#named) :black_small_square: [NamedAttribute](rotation.md#namedattribute)
- **R** : [rotate](rotation.md#rotate) :black_small_square: [rotate_global](rotation.md#rotate_global) :black_small_square: [rotate_local](rotation.md#rotate_local) :black_small_square: [rotate_vector](rotation.md#rotate_vector)
- **T** : [to_axis_angle](rotation.md#to_axis_angle) :black_small_square: [to_euler](rotation.md#to_euler) :black_small_square: [to_quaternion](rotation.md#to_quaternion)
- **W** : [wxyz](rotation.md#wxyz)

## Properties



### axis_angle

> _type_: **tuple**
>

> Node ERROR: Node 'Rotation to Axis Angle' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Properties](rotation.md#properties)</sub>

### wxyz

> _type_: **tuple**
>

> Node [Rotation to Quaternion](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotation_to_quaternion.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Properties](rotation.md#properties)</sub>

## Methods



----------
### AlignToVector()

> classmethod

``` python
AlignToVector(vector=None, factor=None, axis='Z', pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : ignored



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **axis** (_str_ = Z) : parameter 'axis' in ['X', 'Y', 'Z']
- **pivot_axis** (_str_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### align_toVector()

> method

``` python
align_toVector(vector=None, factor=None, axis='Z', pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : self



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **axis** (_str_ = Z) : parameter 'axis' in ['X', 'Y', 'Z']
- **pivot_axis** (_str_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### AlignXToVector()

> classmethod

``` python
AlignXToVector(vector=None, factor=None, pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : ignored
- **Parameter** : 'X'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_str_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### align_x_to_vector()

> method

``` python
align_x_to_vector(vector=None, factor=None, pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : self
- **Parameter** : 'X'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_str_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### AlignYToVector()

> classmethod

``` python
AlignYToVector(vector=None, factor=None, pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : ignored
- **Parameter** : 'Y'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_str_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### align_y_to_vector()

> method

``` python
align_y_to_vector(vector=None, factor=None, pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : self
- **Parameter** : 'Y'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_str_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### AlignZToVector()

> classmethod

``` python
AlignZToVector(vector=None, factor=None, pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : ignored
- **Parameter** : 'Z'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_str_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### align_z_to_vector()

> method

``` python
align_z_to_vector(vector=None, factor=None, pivot_axis='AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : self
- **Parameter** : 'Z'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_str_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromAxes()

> classmethod

``` python
FromAxes(primary_axis_1=None, secondary_axis_1=None, primary_axis='Z', secondary_axis='X')
```

> Node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

#### Arguments:
- **primary_axis_1** (_Vector_ = None) : socket 'Primary Axis' (id: Primary Axis)
- **secondary_axis_1** (_Vector_ = None) : socket 'Secondary Axis' (id: Secondary Axis)
- **primary_axis** (_str_ = Z) : parameter 'primary_axis' in ['X', 'Y', 'Z']
- **secondary_axis** (_str_ = X) : parameter 'secondary_axis' in ['X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromAxisAngle()

> classmethod

``` python
FromAxisAngle(axis=None, angle=None)
```

> Node [Axis Angle to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axis_angle_to_rotation.html)

#### Arguments:
- **axis** (_Vector_ = None) : socket 'Axis' (id: Axis)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromEuler()

> classmethod

``` python
FromEuler(euler=None)
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

#### Arguments:
- **euler** (_Vector_ = None) : socket 'Euler' (id: Euler)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromQuaternion()

> classmethod

``` python
FromQuaternion(w=None, x=None, y=None, z=None)
```

> Node [Quaternion to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/quaternion_to_rotation.html)

#### Arguments:
- **w** (_Float_ = None) : socket 'W' (id: W)
- **x** (_Float_ = None) : socket 'X' (id: X)
- **y** (_Float_ = None) : socket 'Y' (id: Y)
- **z** (_Float_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromXYAxes()

> classmethod

``` python
FromXYAxes(primary_axis=None, secondary_axis=None)
```

> Node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

#### Information:
- **Parameter** : 'X'
- **Parameter** : 'Y'



#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (id: Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (id: Secondary Axis)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromXZAxes()

> classmethod

``` python
FromXZAxes(primary_axis=None, secondary_axis=None)
```

> Node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

#### Information:
- **Parameter** : 'X'
- **Parameter** : 'Z'



#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (id: Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (id: Secondary Axis)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromYXAxes()

> classmethod

``` python
FromYXAxes(primary_axis=None, secondary_axis=None)
```

> Node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

#### Information:
- **Parameter** : 'Y'
- **Parameter** : 'X'



#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (id: Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (id: Secondary Axis)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromYZAxes()

> classmethod

``` python
FromYZAxes(primary_axis=None, secondary_axis=None)
```

> Node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

#### Information:
- **Parameter** : 'Y'
- **Parameter** : 'Z'



#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (id: Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (id: Secondary Axis)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromZXAxes()

> classmethod

``` python
FromZXAxes(primary_axis=None, secondary_axis=None)
```

> Node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

#### Information:
- **Parameter** : 'Z'
- **Parameter** : 'X'



#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (id: Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (id: Secondary Axis)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromZYAxes()

> classmethod

``` python
FromZYAxes(primary_axis=None, secondary_axis=None)
```

> Node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

#### Information:
- **Parameter** : 'Z'
- **Parameter** : 'Y'



#### Arguments:
- **primary_axis** (_Vector_ = None) : socket 'Primary Axis' (id: Primary Axis)
- **secondary_axis** (_Vector_ = None) : socket 'Secondary Axis' (id: Secondary Axis)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed=None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ROTATION'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=(0.0, 0.0, 0.0), name=None, tip=None, panel='', hide_value=False, hide_in_modifier=False, single_value=False)
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
- **panel** (_str_ = ) : panel name (overrides tree panel if exists)
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### invert()

> method

``` python
invert()
```

> Node [Invert Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/invert_rotation.html)

#### Information:
- **Socket** : self



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### mix()

> method

``` python
mix(b=None, factor=None, clamp_factor=True)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MIX'
- **Parameter** : False
- **Parameter** : 'ROTATION'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Rotation_ = None) : socket 'B' (id: B_Rotation)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'QUATERNION'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'QUATERNION'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(rotate_by=None, rotation_space='GLOBAL')
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html)

#### Information:
- **Socket** : self



#### Arguments:
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (id: Rotate By)
- **rotation_space** (_str_ = GLOBAL) : parameter 'rotation_space' in ['GLOBAL', 'LOCAL']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### rotate_global()

> method

``` python
rotate_global(rotate_by=None)
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html)

#### Information:
- **Socket** : self
- **Parameter** : 'GLOBAL'



#### Arguments:
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (id: Rotate By)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### rotate_local()

> method

``` python
rotate_local(rotate_by=None)
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LOCAL'



#### Arguments:
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (id: Rotate By)



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

#### Information:
- **Socket** : self



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)



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

#### Information:
- **Socket** : self



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### to_euler()

> method

``` python
to_euler()
```

> Node [Rotation to Euler](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotation_to_euler.html)

#### Information:
- **Socket** : self



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

#### Information:
- **Socket** : self



#### Returns:
- **Float** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>