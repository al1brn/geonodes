# Rotation

``` python
Rotation(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

> The output socket of a [Node](node.md#node)

**Socket** is the base class for data classes such as [Float](float.md#float), [Image](image.md#image) or [Geometry](geometry.md#geometry).

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
> - using ['#node' not found]() attribute
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
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socke-socket.md#check_in_list) :black_small_square: [Constant](core-socke-socket.md#constant) :black_small_square: [default_value](core-socke-socket.md#default_value) :black_small_square: [\_domain_to_geometry](core-socke-socket.md#_domain_to_geometry) :black_small_square: [Empty](core-socke-socket.md#empty) :black_small_square: [\_\_enter__](core-socke-socket.md#__enter__) :black_small_square: [\_\_exit__](core-socke-socket.md#__exit__) :black_small_square: [\_\_getattr__](core-socke-socket.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socke-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socke-socket.md#indexswitch) :black_small_square: [index_switch](core-socke-socket.md#index_switch) :black_small_square: [\_\_init__](core-socke-socket.md#__init__) :black_small_square: [Input](core-socke-socket.md#input) :black_small_square: [\_interface_socket](core-socke-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socke-socket.md#_is_empty) :black_small_square: [is_grid](core-socke-socket.md#is_grid) :black_small_square: [\_jump](core-socke-socket.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](core-socke-socket.md#_lc) :black_small_square: [\_lcop](core-socke-socket.md#_lcop) :black_small_square: [link_inputs](core-socke-socket.md#link_inputs) :black_small_square: [MenuSwitch](core-socke-socket.md#menuswitch) :black_small_square: [menu_switch](core-socke-socket.md#menu_switch) :black_small_square: [\_name](core-socke-socket.md#_name) :black_small_square: [NewInput](core-socke-socket.md#newinput) :black_small_square: [node](core-socke-socket.md#node) :black_small_square: [node_color](core-socke-socket.md#node_color) :black_small_square: [node_label](core-socke-socket.md#node_label) :black_small_square: [out](core-socke-socket.md#out) :black_small_square: [\_panel_name](core-socke-socket.md#_panel_name) :black_small_square: [pin_gizmo](core-socke-socket.md#pin_gizmo) :black_small_square: [\_pop](core-socke-socket.md#_pop) :black_small_square: [\_push](core-socke-socket.md#_push) :black_small_square: [repeat](core-socke-socket.md#repeat) :black_small_square: [\_reset](core-socke-socket.md#_reset) :black_small_square: [simulation](core-socke-socket.md#simulation) :black_small_square: [\_socket_type](core-socke-socket.md#_socket_type) :black_small_square: [\_\_str__](core-socke-socket.md#__str__) :black_small_square: [Switch](core-socke-socket.md#switch) :black_small_square: [switch](core-socke-socket.md#switch) :black_small_square: [switch_false](core-socke-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- **A** : [AlignToVector](rotation.md#aligntovector) :black_small_square: [align_to_vector](rotation.md#align_to_vector) :black_small_square: [AlignXToVector](rotation.md#alignxtovector) :black_small_square: [align_x_to_vector](rotation.md#align_x_to_vector) :black_small_square: [AlignYToVector](rotation.md#alignytovector) :black_small_square: [align_y_to_vector](rotation.md#align_y_to_vector) :black_small_square: [AlignZToVector](rotation.md#alignztovector) :black_small_square: [align_z_to_vector](rotation.md#align_z_to_vector) :black_small_square: [axis_angle](rotation.md#axis_angle)
- **C** : [\_create_input_socket](rotation.md#_create_input_socket)
- **E** : [enable_output](rotation.md#enable_output)
- **F** : [FromAxes](rotation.md#fromaxes) :black_small_square: [FromAxisAngle](rotation.md#fromaxisangle) :black_small_square: [FromEuler](rotation.md#fromeuler) :black_small_square: [FromQuaternion](rotation.md#fromquaternion) :black_small_square: [FromXYAxes](rotation.md#fromxyaxes) :black_small_square: [FromXZAxes](rotation.md#fromxzaxes) :black_small_square: [FromYXAxes](rotation.md#fromyxaxes) :black_small_square: [FromYZAxes](rotation.md#fromyzaxes) :black_small_square: [FromZXAxes](rotation.md#fromzxaxes) :black_small_square: [FromZYAxes](rotation.md#fromzyaxes)
- **H** : [hash_value](rotation.md#hash_value)
- **I** : [invert](rotation.md#invert)
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
AlignToVector(vector: 'Vector' = None, factor: 'Float' = None, axis: "Literal['X', 'Y', 'Z']" = 'Z', pivot_axis: "Literal['AUTO', 'X', 'Y', 'Z']" = 'AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : ignored



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **axis** (_Literal['X', 'Y', 'Z']_ = Z) : parameter 'axis' in ['X', 'Y', 'Z']
- **pivot_axis** (_Literal['AUTO', 'X', 'Y', 'Z']_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### align_to_vector()

> method

``` python
align_to_vector(vector: 'Vector' = None, factor: 'Float' = None, axis: "Literal['X', 'Y', 'Z']" = 'Z', pivot_axis: "Literal['AUTO', 'X', 'Y', 'Z']" = 'AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : self



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **axis** (_Literal['X', 'Y', 'Z']_ = Z) : parameter 'axis' in ['X', 'Y', 'Z']
- **pivot_axis** (_Literal['AUTO', 'X', 'Y', 'Z']_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### AlignXToVector()

> classmethod

``` python
AlignXToVector(vector: 'Vector' = None, factor: 'Float' = None, pivot_axis: "Literal['AUTO', 'X', 'Y', 'Z']" = 'AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : ignored
- **Parameter** : 'X'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_Literal['AUTO', 'X', 'Y', 'Z']_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### align_x_to_vector()

> method

``` python
align_x_to_vector(vector: 'Vector' = None, factor: 'Float' = None, pivot_axis: "Literal['AUTO', 'X', 'Y', 'Z']" = 'AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : self
- **Parameter** : 'X'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_Literal['AUTO', 'X', 'Y', 'Z']_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### AlignYToVector()

> classmethod

``` python
AlignYToVector(vector: 'Vector' = None, factor: 'Float' = None, pivot_axis: "Literal['AUTO', 'X', 'Y', 'Z']" = 'AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : ignored
- **Parameter** : 'Y'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_Literal['AUTO', 'X', 'Y', 'Z']_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### align_y_to_vector()

> method

``` python
align_y_to_vector(vector: 'Vector' = None, factor: 'Float' = None, pivot_axis: "Literal['AUTO', 'X', 'Y', 'Z']" = 'AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : self
- **Parameter** : 'Y'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_Literal['AUTO', 'X', 'Y', 'Z']_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### AlignZToVector()

> classmethod

``` python
AlignZToVector(vector: 'Vector' = None, factor: 'Float' = None, pivot_axis: "Literal['AUTO', 'X', 'Y', 'Z']" = 'AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : ignored
- **Parameter** : 'Z'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_Literal['AUTO', 'X', 'Y', 'Z']_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### align_z_to_vector()

> method

``` python
align_z_to_vector(vector: 'Vector' = None, factor: 'Float' = None, pivot_axis: "Literal['AUTO', 'X', 'Y', 'Z']" = 'AUTO')
```

> Node [Align Rotation to Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_rotation_to_vector.html)

#### Information:
- **Socket** : self
- **Parameter** : 'Z'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor)
- **pivot_axis** (_Literal['AUTO', 'X', 'Y', 'Z']_ = AUTO) : parameter 'pivot_axis' in ['AUTO', 'X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = (0, 0, 0), name: 'str' = 'Rotation', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', shape: "Literal['AUTO', 'DYNAMIC', 'FIELD', 'SINGLE']" = 'AUTO')
```

> Rotation Input

New [Rotation](rotation.md#rotation) input with subtype 'NONE'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Rotation') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'DYNAMIC', 'FIELD', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Rotation)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **shape** (_Literal['AUTO', 'DYNAMIC', 'FIELD', 'SINGLE']_ = AUTO)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ROTATION'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromAxes()

> classmethod

``` python
FromAxes(primary_axis_1: 'Vector' = None, secondary_axis_1: 'Vector' = None, primary_axis: "Literal['X', 'Y', 'Z']" = 'Z', secondary_axis: "Literal['X', 'Y', 'Z']" = 'X')
```

> Node [Axes to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/axes_to_rotation.html)

#### Arguments:
- **primary_axis_1** (_Vector_ = None) : socket 'Primary Axis' (id: Primary Axis)
- **secondary_axis_1** (_Vector_ = None) : socket 'Secondary Axis' (id: Secondary Axis)
- **primary_axis** (_Literal['X', 'Y', 'Z']_ = Z) : parameter 'primary_axis' in ['X', 'Y', 'Z']
- **secondary_axis** (_Literal['X', 'Y', 'Z']_ = X) : parameter 'secondary_axis' in ['X', 'Y', 'Z']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### FromAxisAngle()

> classmethod

``` python
FromAxisAngle(axis: 'Vector' = None, angle: 'Float' = None)
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
FromEuler(euler: 'Vector' = None)
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
FromQuaternion(w: 'Float' = None, x: 'Float' = None, y: 'Float' = None, z: 'Float' = None)
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
FromXYAxes(primary_axis: 'Vector' = None, secondary_axis: 'Vector' = None)
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
FromXZAxes(primary_axis: 'Vector' = None, secondary_axis: 'Vector' = None)
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
FromYXAxes(primary_axis: 'Vector' = None, secondary_axis: 'Vector' = None)
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
FromYZAxes(primary_axis: 'Vector' = None, secondary_axis: 'Vector' = None)
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
FromZXAxes(primary_axis: 'Vector' = None, secondary_axis: 'Vector' = None)
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
FromZYAxes(primary_axis: 'Vector' = None, secondary_axis: 'Vector' = None)
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
hash_value(seed: 'Integer' = None)
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
mix(b: 'Rotation' = None, factor: 'Float' = None, clamp_factor=True)
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
Named(name: 'String' = None)
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
NamedAttribute(name: 'String' = None)
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
rotate(rotate_by: 'Rotation' = None, rotation_space: "Literal['GLOBAL', 'LOCAL']" = 'GLOBAL')
```

> Node [Rotate Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_rotation.html)

#### Information:
- **Socket** : self



#### Arguments:
- **rotate_by** (_Rotation_ = None) : socket 'Rotate By' (id: Rotate By)
- **rotation_space** (_Literal['GLOBAL', 'LOCAL']_ = GLOBAL) : parameter 'rotation_space' in ['GLOBAL', 'LOCAL']



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Rotation](rotation.md#rotation) :black_small_square: [Content](rotation.md#content) :black_small_square: [Methods](rotation.md#methods)</sub>

----------
### rotate_global()

> method

``` python
rotate_global(rotate_by: 'Rotation' = None)
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
rotate_local(rotate_by: 'Rotation' = None)
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
rotate_vector(vector: 'Vector' = None)
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