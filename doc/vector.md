# Vector

``` python
Vector(value=(0, 0, 0), name=None, tip=None, panel='', subtype='NONE', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Socket of type VECTOR

If **value** argument is None:
- if **name** argument is None, a node 'Vector' is added
- otherwise a new group input is created using **tip** and **subtype**
  arguments

If **value** argument is not None, a new **Vector** is created from the value:
- using a [Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/vector.html) node if the **value** is a float or a tuple of floats
- using a [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/combine_xyz.html) node if the **value** is a tuple containing [Sockets](socket.md#socket)

``` python
vect = Vector()                    # 'Vector' node
vect = Vector((1, 2, 3.14)).       # 'Vector' node
vect = Vector((Float(1), 2, 3.14)) # 'Combine XYZ' node
vect = Vector(name="User input").  # Create a new Vector group input
```

#### Arguments:
- **value** (_tuple of floats or Sockets_ = (0, 0, 0)) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = ) : panel name (overrides tree pane if exists)
- **subtype** (_str in ('NONE', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'EULER', 'XYZ')_ = NONE) : sub type for group input
- **default_attribute** (_str_ = ) : default attribute name
- **default_input** (_str in ('VALUE', 'NORMAL', 'POSITION')_ = VALUE) : default input
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **A** : [abs](vector.md#abs) :black_small_square: [Acceleration](vector.md#acceleration) :black_small_square: [add](vector.md#add)
- **B** : [blur](vector.md#blur) :black_small_square: [bump](vector.md#bump)
- **C** : [ceil](vector.md#ceil) :black_small_square: [CombineXYZ](vector.md#combinexyz) :black_small_square: [cos](vector.md#cos) :black_small_square: [cross](vector.md#cross) :black_small_square: [curves](vector.md#curves)
- **D** : [Direction](vector.md#direction) :black_small_square: [displacement](vector.md#displacement) :black_small_square: [displacement_out](vector.md#displacement_out) :black_small_square: [distance](vector.md#distance) :black_small_square: [divide](vector.md#divide) :black_small_square: [dot](vector.md#dot)
- **E** : [environment_texture](vector.md#environment_texture) :black_small_square: [equal](vector.md#equal) :black_small_square: [Euler](vector.md#euler)
- **F** : [faceforward](vector.md#faceforward) :black_small_square: [floor](vector.md#floor) :black_small_square: [fraction](vector.md#fraction) :black_small_square: [FromRotation](vector.md#fromrotation)
- **G** : [greater_equal](vector.md#greater_equal) :black_small_square: [greater_than](vector.md#greater_than)
- **H** : [hash_value](vector.md#hash_value)
- **I** : [ies_texture](vector.md#ies_texture) :black_small_square: [ies_texture_external](vector.md#ies_texture_external) :black_small_square: [ies_texture_internal](vector.md#ies_texture_internal) :black_small_square: [image_texture](vector.md#image_texture) :black_small_square: [\_\_init__](vector.md#__init__)
- **L** : [length](vector.md#length) :black_small_square: [less_equal](vector.md#less_equal) :black_small_square: [less_than](vector.md#less_than)
- **M** : [mapping](vector.md#mapping) :black_small_square: [max](vector.md#max) :black_small_square: [min](vector.md#min) :black_small_square: [mix](vector.md#mix) :black_small_square: [mix_non_uniform](vector.md#mix_non_uniform) :black_small_square: [mix_uniform](vector.md#mix_uniform) :black_small_square: [modulo](vector.md#modulo) :black_small_square: [multiply](vector.md#multiply) :black_small_square: [multiply_add](vector.md#multiply_add)
- **N** : [Named](vector.md#named) :black_small_square: [NamedAttribute](vector.md#namedattribute) :black_small_square: [Normal](vector.md#normal) :black_small_square: [normal](vector.md#normal) :black_small_square: [normalize](vector.md#normalize) :black_small_square: [NormalMap](vector.md#normalmap) :black_small_square: [not_equal](vector.md#not_equal)
- **O** : [out](vector.md#out)
- **P** : [pack_uv_islands](vector.md#pack_uv_islands) :black_small_square: [point_density](vector.md#point_density) :black_small_square: [Position](vector.md#position) :black_small_square: [power](vector.md#power) :black_small_square: [project](vector.md#project)
- **R** : [Random](vector.md#random) :black_small_square: [reflect](vector.md#reflect) :black_small_square: [refract](vector.md#refract) :black_small_square: [rotate](vector.md#rotate) :black_small_square: [rotate_axis_angle](vector.md#rotate_axis_angle) :black_small_square: [rotate_euler_xyz](vector.md#rotate_euler_xyz) :black_small_square: [rotate_x_axis](vector.md#rotate_x_axis) :black_small_square: [rotate_y_axis](vector.md#rotate_y_axis) :black_small_square: [rotate_z_axis](vector.md#rotate_z_axis)
- **S** : [sample_grid](vector.md#sample_grid) :black_small_square: [sample_grid_index](vector.md#sample_grid_index) :black_small_square: [scale](vector.md#scale) :black_small_square: [separate_xyz](vector.md#separate_xyz) :black_small_square: [sign](vector.md#sign) :black_small_square: [sin](vector.md#sin) :black_small_square: [snap](vector.md#snap) :black_small_square: [subtract](vector.md#subtract)
- **T** : [tan](vector.md#tan) :black_small_square: [Tangent](vector.md#tangent) :black_small_square: [to_rotation](vector.md#to_rotation) :black_small_square: [transform](vector.md#transform) :black_small_square: [Translation](vector.md#translation)
- **U** : [UVMap](vector.md#uvmap) :black_small_square: [UvMap](vector.md#uvmap)
- **V** : [vector_displacement](vector.md#vector_displacement) :black_small_square: [vector_transform](vector.md#vector_transform) :black_small_square: [Velocity](vector.md#velocity)
- **W** : [wrap](vector.md#wrap)
- **X** : [x](vector.md#x) :black_small_square: [xyz](vector.md#xyz) :black_small_square: [XYZ](vector.md#xyz)
- **Y** : [y](vector.md#y)
- **Z** : [z](vector.md#z)

## Properties



### x

> _type_: **x**
>

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Properties](vector.md#properties)</sub>

### xyz

> _type_: **tuple**
>

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Properties](vector.md#properties)</sub>

### y

> _type_: **y**
>

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Properties](vector.md#properties)</sub>

### z

> _type_: **z**
>

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Properties](vector.md#properties)</sub>

## Methods



----------
### abs()

> method

``` python
abs()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ABSOLUTE'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Acceleration()

> classmethod

``` python
Acceleration(value=(0.0, 0.0, 0.0), name='Acceleration', tip=None, panel='', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Acceleration group input

New [Vector](vector.md#vector) input with subtype 'ACCELERATION'.

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Acceleration)
- **tip** ( = None)
- **panel** ( = )
- **default_attribute** ( = )
- **default_input** ( = VALUE)
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### add()

> method

``` python
add(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ADD'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### blur()

> method

``` python
blur(iterations=None, weight=None)
```

> Node [Blur Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)
- **weight** (_Float_ = None) : socket 'Weight' (id: Weight)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### bump()

> method

``` python
bump(strength=None, distance=None, height=None, invert=False)
```

> Node [Bump](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/bump.html)

[!SHADER]

> [!NOTE]
> Self Vector is plugged to 'Normal' socket

#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (Strength)
- **distance** (_Float_ = None) : socket 'Distance' (Distance)
- **height** (_Float_ = None) : socket 'Height' (Height)
- **invert** (_bool_ = False) : Node.invert



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### ceil()

> method

``` python
ceil()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'CEIL'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### CombineXYZ()

> classmethod

``` python
CombineXYZ(x=None, y=None, z=None)
```

> Node [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/combine_xyz.html)

#### Arguments:
- **x** (_Float_ = None) : socket 'X' (id: X)
- **y** (_Float_ = None) : socket 'Y' (id: Y)
- **z** (_Float_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### cos()

> method

``` python
cos()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'COSINE'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### cross()

> method

``` python
cross(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'CROSS_PRODUCT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### curves()

> method

``` python
curves(fac=None, curves=None)
```

> Node [Vector Curves](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_curves.html)

A curve is defined by a list of 3-tuples (not list):
- x (float) : x position
- y (float) : y position
- handle_type (str) : handle type in ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

> [!NOTE]
> handle_type is optional, its default value is 'AUTO'. Valid values are ('AUTO', 'AUTO_CLAMPED', 'VECTOR')

#### Information:
- **Socket** : self



#### Arguments:
- **fac** (_Float_ = None) : socket 'Fac' (id: Fac)
- **curves** (_list of lists of tuples (float, float, str)_ = None) : curves points



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Direction()

> classmethod

``` python
Direction(value=(0.0, 0.0, 0.0), name='Direction', tip=None, panel='', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Direction group input

New [Vector](vector.md#vector) input with subtype 'DIRECTION'.

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Direction)
- **tip** ( = None)
- **panel** ( = )
- **default_attribute** ( = )
- **default_input** ( = VALUE)
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### displacement()

> method

``` python
displacement(height=None, midlevel=None, scale=None, space='OBJECT')
```

> Node [Displacement](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/displacement.html)

[!SHADER]

> [!NOTE]
> Self Vector is plugged to 'Normal' socket

#### Arguments:
- **height** (_Float_ = None) : socket 'Height' (Height)
- **midlevel** (_Float_ = None) : socket 'Midlevel' (Midlevel)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **space** (_str_ = OBJECT) : Node.space in ('OBJECT', 'WORLD')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### displacement_out()

> method

``` python
displacement_out(target='ALL')
```

> Plug the value to 'Displacement' socket of [Material Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/material.html) node

[!SHADER]

#### Arguments:
- **target** ( = ALL)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### distance()

> method

``` python
distance(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DISTANCE'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### divide()

> method

``` python
divide(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### dot()

> method

``` python
dot(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DOT_PRODUCT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### environment_texture()

> method

``` python
environment_texture(image=None, interpolation='Linear', projection='EQUIRECTANGULAR')
```

> Node [Environment Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/environment.html)

#### Information:
- **Socket** : self



#### Arguments:
- **image** (_NoneType_ = None) : parameter 'image'
- **interpolation** (_str_ = Linear) : parameter 'interpolation' in ['Linear', 'Closest', 'Cubic', 'Smart']
- **projection** (_str_ = EQUIRECTANGULAR) : parameter 'projection' in ['EQUIRECTANGULAR', 'MIRROR_BALL']



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b=None, epsilon=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'EQUAL'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Euler()

> classmethod

``` python
Euler(value=(0.0, 0.0, 0.0), name='Euler', tip=None, panel='', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Euler group input

New [Vector](vector.md#vector) input with subtype 'EULER'.

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Euler)
- **tip** ( = None)
- **panel** ( = )
- **default_attribute** ( = )
- **default_input** ( = VALUE)
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### faceforward()

> method

``` python
faceforward(incident=None, reference=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FACEFORWARD'



#### Arguments:
- **incident** (_Vector_ = None) : socket 'Incident' (id: Vector_001)
- **reference** (_Vector_ = None) : socket 'Reference' (id: Vector_002)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### floor()

> method

``` python
floor()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOOR'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### fraction()

> method

``` python
fraction()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FRACTION'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### FromRotation()

> classmethod

``` python
FromRotation(rotation=None)
```

> Constructor node ERROR: Node 'to Euler' not found

#### Arguments:
- **rotation** ( = None)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### greater_equal()

> method

``` python
greater_equal(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_EQUAL'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_THAN'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed=None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### ies_texture()

> method

``` python
ies_texture(strength=None, filepath='', ies=None, mode='INTERNAL')
```

> Node [IES Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/ies.html)

#### Information:
- **Socket** : self



#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (id: Strength)
- **filepath** (_str_ = ) : parameter 'filepath'
- **ies** (_NoneType_ = None) : parameter 'ies'
- **mode** (_str_ = INTERNAL) : parameter 'mode' in ['INTERNAL', 'EXTERNAL']



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### ies_texture_external()

> method

``` python
ies_texture_external(strength=None, filepath='', ies=None)
```

> Node [IES Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/ies.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EXTERNAL'



#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (id: Strength)
- **filepath** (_str_ = ) : parameter 'filepath'
- **ies** (_NoneType_ = None) : parameter 'ies'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### ies_texture_internal()

> method

``` python
ies_texture_internal(strength=None, filepath='', ies=None)
```

> Node [IES Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/ies.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INTERNAL'



#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (id: Strength)
- **filepath** (_str_ = ) : parameter 'filepath'
- **ies** (_NoneType_ = None) : parameter 'ies'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### image_texture()

> method

``` python
image_texture(extension='REPEAT', image=None, interpolation='Linear', projection='FLAT', projection_blend=0.0)
```

> Node [Image Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../modeling/geometry_nodes/texture/image.html)

#### Information:
- **Socket** : self



#### Arguments:
- **extension** (_str_ = REPEAT) : parameter 'extension' in ['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']
- **image** (_NoneType_ = None) : parameter 'image'
- **interpolation** (_str_ = Linear) : parameter 'interpolation' in ['Linear', 'Closest', 'Cubic', 'Smart']
- **projection** (_str_ = FLAT) : parameter 'projection' in ['FLAT', 'BOX', 'SPHERE', 'TUBE']
- **projection_blend** (_float_ = 0.0) : parameter 'projection_blend'



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=(0, 0, 0), name=None, tip=None, panel='', subtype='NONE', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Socket of type VECTOR

If **value** argument is None:
- if **name** argument is None, a node 'Vector' is added
- otherwise a new group input is created using **tip** and **subtype**
  arguments

If **value** argument is not None, a new **Vector** is created from the value:
- using a [Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/vector.html) node if the **value** is a float or a tuple of floats
- using a [Combine XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/combine_xyz.html) node if the **value** is a tuple containing [Sockets](socket.md#socket)

``` python
vect = Vector()                    # 'Vector' node
vect = Vector((1, 2, 3.14)).       # 'Vector' node
vect = Vector((Float(1), 2, 3.14)) # 'Combine XYZ' node
vect = Vector(name="User input").  # Create a new Vector group input
```

#### Arguments:
- **value** (_tuple of floats or Sockets_ = (0, 0, 0)) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = ) : panel name (overrides tree pane if exists)
- **subtype** (_str in ('NONE', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'EULER', 'XYZ')_ = NONE) : sub type for group input
- **default_attribute** (_str_ = ) : default attribute name
- **default_input** (_str in ('VALUE', 'NORMAL', 'POSITION')_ = VALUE) : default input
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### length()

> method

``` python
length()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LENGTH'



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### less_equal()

> method

``` python
less_equal(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_EQUAL'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_THAN'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### mapping()

> method

``` python
mapping(location=None, rotation=None, scale=None, vector_type='POINT')
```

> Node [Mapping](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/mapping.html)

[!SHADER]

#### Arguments:
- **location** (_Vector_ = None) : socket 'Location' (Location)
- **rotation** (_Vector_ = None) : socket 'Rotation' (Rotation)
- **scale** (_Vector_ = None) : socket 'Scale' (Scale)
- **vector_type** (_str_ = POINT) : Node.vector_type in ('POINT', 'TEXTURE', 'VECTOR', 'NORMAL')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### max()

> method

``` python
max(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MAXIMUM'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### min()

> method

``` python
min(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MINIMUM'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### mix()

> method

``` python
mix(b=None, factor=None, clamp_factor=True)
```

> Method [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

> [NOTE]
> Call mix_uniform or mix_non_uniform depending on the factor type

#### Information:
- **Socket** : self
- **Parameter** : 'MIX'
- **Parameter** : False
- **Parameter** : 'VECTOR'
- **Parameter** : 'UNIFORM' or 'NON_UNIFORM' depending on factor argument



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_Vector)
- **factor** (_Float or Vector_ = None) : socket 'Factor'
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### mix_non_uniform()

> method

``` python
mix_non_uniform(b=None, factor=None, clamp_factor=True)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MIX'
- **Parameter** : False
- **Parameter** : 'VECTOR'
- **Parameter** : 'NON_UNIFORM'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_Vector)
- **factor** (_Vector_ = None) : socket 'Factor' (id: Factor_Vector)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### mix_uniform()

> method

``` python
mix_uniform(b=None, factor=None, clamp_factor=True)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MIX'
- **Parameter** : False
- **Parameter** : 'VECTOR'
- **Parameter** : 'UNIFORM'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_Vector)
- **factor** (_Float_ = None) : socket 'Factor' (id: Factor_Float)
- **clamp_factor** (_bool_ = True) : parameter 'clamp_factor'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### modulo()

> method

``` python
modulo(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MODULO'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### multiply_add()

> method

``` python
multiply_add(multiplier=None, addend=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY_ADD'



#### Arguments:
- **multiplier** (_Vector_ = None) : socket 'Multiplier' (id: Vector_001)
- **addend** (_Vector_ = None) : socket 'Addend' (id: Vector_002)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Normal()

> classmethod

``` python
Normal(name='Normal', tip=None, panel='', hide_in_modifier=True)
```

> Normal vector group input

New [Vector](vector.md#vector) input with Normal as default value (default_input='NORMAL')

> [!NOTE]
> By default, 'hide_in_modifier' is set to True

#### Arguments:
- **name** ( = Normal)
- **tip** ( = None)
- **panel** ( = )
- **hide_in_modifier** ( = True)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### normal()

> method

``` python
normal()
```

> Node [Normal](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../modeling/geometry_nodes/geometry/read/normal.html)

[!SHADER]

#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### normalize()

> method

``` python
normalize()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NORMALIZE'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### NormalMap()

> classmethod

``` python
NormalMap(strength=None, color=None, space='TANGENT', uv_map='')
```

> Constructor node [Normal Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/normal_map.html)

[!SHADER]

#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (Strength)
- **color** (_Color_ = None) : socket 'Color' (Color)
- **space** (_str_ = TANGENT) : Node.space in ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')
- **uv_map** (_str_ = ) : Node.uv_map



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(b=None, epsilon=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'NOT_EQUAL'



#### Arguments:
- **b** (_Vector_ = None) : socket 'B' (id: B_VEC3)
- **epsilon** (_Float_ = None) : socket 'Epsilon' (id: Epsilon)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### out()

> method

``` python
out(name=None, **props)
```

> Plug the Vector to the group output

[!MIX]

> [!NOTE]
> - [GeoNodes](geonodes.md#geonodes) : the Vector is plug as group output
> - [ShaderNodes](shadernodes.md#shadernodes) : if **name** argument is None, the vecteur is plugged
>.  into the `Displacement` socket of ERROR: Node '&Material Output' not found,
>   otherwise it is plugged to a [AOV Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/aov.html) node.

#### Arguments:
- **name** ( = None)
- **props**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### pack_uv_islands()

> method

``` python
pack_uv_islands(margin=None, rotate=None)
```

> Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/pack_uv_islands.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **rotate** (_Boolean_ = None) : socket 'Rotate' (id: Rotate)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### point_density()

> method

``` python
point_density(interpolation='Linear', object=None, particle_color_source='PARTICLE_AGE', particle_system=None, point_source='PARTICLE_SYSTEM', radius=0.30000001192092896, resolution=100, space='OBJECT', vertex_attribute_name='', vertex_color_source='VERTEX_COLOR')
```

> Node [Point Density](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/point_density.html)

#### Information:
- **Socket** : self



#### Arguments:
- **interpolation** (_str_ = Linear) : parameter 'interpolation' in ['Closest', 'Linear', 'Cubic']
- **object** (_NoneType_ = None) : parameter 'object'
- **particle_color_source** (_str_ = PARTICLE_AGE) : parameter 'particle_color_source' in ['PARTICLE_AGE', 'PARTICLE_SPEED', 'PARTICLE_VELOCITY']
- **particle_system** (_NoneType_ = None) : parameter 'particle_system'
- **point_source** (_str_ = PARTICLE_SYSTEM) : parameter 'point_source' in ['PARTICLE_SYSTEM', 'OBJECT']
- **radius** (_float_ = 0.30000001192092896) : parameter 'radius'
- **resolution** (_int_ = 100) : parameter 'resolution'
- **space** (_str_ = OBJECT) : parameter 'space' in ['OBJECT', 'WORLD']
- **vertex_attribute_name** (_str_ = ) : parameter 'vertex_attribute_name'
- **vertex_color_source** (_str_ = VERTEX_COLOR) : parameter 'vertex_color_source' in ['VERTEX_COLOR', 'VERTEX_WEIGHT', 'VERTEX_NORMAL']



#### Returns:
- **Color** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Position()

> classmethod

``` python
Position(name='Position', tip=None, panel='', hide_in_modifier=True)
```

> Position vector group input

New [Vector](vector.md#vector) input with Position as default value (default_input='POSITION')

> [!NOTE]
> By default, 'hide_in_modifier' is set to True

#### Arguments:
- **name** ( = Position)
- **tip** ( = None)
- **panel** ( = )
- **hide_in_modifier** ( = True)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### power()

> method

``` python
power(exponent=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'POWER'



#### Arguments:
- **exponent** (_Vector_ = None) : socket 'Exponent' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### project()

> method

``` python
project(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'PROJECT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(min=None, max=None, id=None, seed=None)
```

> Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Information:
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **min** (_Vector_ = None) : socket 'Min' (id: Min)
- **max** (_Vector_ = None) : socket 'Max' (id: Max)
- **id** (_Integer_ = None) : socket 'ID' (id: ID)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### reflect()

> method

``` python
reflect(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'REFLECT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### refract()

> method

``` python
refract(vector=None, ior=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'REFRACT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)
- **ior** (_Float_ = None) : socket 'IOR' (id: Scale)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(center=None, axis=None, angle=None, invert=False, rotation_type='AXIS_ANGLE')
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **axis** (_Vector_ = None) : socket 'Axis' (id: Axis)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'
- **rotation_type** (_str_ = AXIS_ANGLE) : parameter 'rotation_type' in ['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_axis_angle()

> method

``` python
rotate_axis_angle(center=None, axis=None, angle=None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'AXIS_ANGLE'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **axis** (_Vector_ = None) : socket 'Axis' (id: Axis)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_euler_xyz()

> method

``` python
rotate_euler_xyz(center=None, rotation=None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'EULER_XYZ'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **rotation** (_Vector_ = None) : socket 'Rotation' (id: Rotation)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_x_axis()

> method

``` python
rotate_x_axis(center=None, angle=None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'X_AXIS'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_y_axis()

> method

``` python
rotate_y_axis(center=None, angle=None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'Y_AXIS'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_z_axis()

> method

``` python
rotate_z_axis(center=None, angle=None, invert=False)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self
- **Parameter** : 'Z_AXIS'



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### sample_grid()

> method

``` python
sample_grid(position=None, interpolation_mode='TRILINEAR')
```

> Node ERROR: Node 'Sample Grid' not found

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation_mode** (_str_ = TRILINEAR) : parameter 'interpolation_mode' in ['NEAREST', 'TRILINEAR', 'TRIQUADRATIC']



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x=None, y=None, z=None)
```

> Node ERROR: Node 'Sample Grid Index' not found

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **x** (_Integer_ = None) : socket 'X' (id: X)
- **y** (_Integer_ = None) : socket 'Y' (id: Y)
- **z** (_Integer_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### scale()

> method

``` python
scale(scale=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SCALE'



#### Arguments:
- **scale** (_Float_ = None) : socket 'Scale' (id: Scale)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### separate_xyz()

> method

``` python
separate_xyz()
```

> Node [Separate XYZ](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html)

#### Information:
- **Socket** : self



#### Returns:
- **node** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### sign()

> method

``` python
sign()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SIGN'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### sin()

> method

``` python
sin()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SINE'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### snap()

> method

``` python
snap(increment=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SNAP'



#### Arguments:
- **increment** (_Vector_ = None) : socket 'Increment' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### subtract()

> method

``` python
subtract(vector=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SUBTRACT'



#### Arguments:
- **vector** (_Vector_ = None) : socket 'Vector' (id: Vector_001)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### tan()

> method

``` python
tan()
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'TANGENT'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Tangent()

> classmethod

``` python
Tangent(axis='Z', direction_type='RADIAL', uv_map='')
```

> Node [Tangent](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/tangent.html)

[!SHADER]

#### Arguments:
- **axis** (_str_ = Z) : Node.axis in ('X', 'Y', 'Z')
- **direction_type** (_str_ = RADIAL) : Node.direction_type in ('RADIAL', 'UV_MAP')
- **uv_map** (_str_ = ) : Node.uv_map



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### to_rotation()

> method

``` python
to_rotation()
```

> Node [Euler to Rotation](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/euler_to_rotation.html)

#### Information:
- **Socket** : self



#### Returns:
- **Rotation** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### transform()

> method

``` python
transform(convert_from='WORLD', convert_to='OBJECT', vector_type='NORMAL')
```

> Node [Vector Transform](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/transform.html)

[!SHADER]

#### Arguments:
- **convert_from** (_str_ = WORLD) : Node.convert_from in ('WORLD', 'OBJECT', 'CAMERA')
- **convert_to** (_str_ = OBJECT) : Node.convert_to in ('WORLD', 'OBJECT', 'CAMERA')
- **vector_type** (_str_ = NORMAL) : Node.vector_type in ('POINT', 'VECTOR', 'NORMAL')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Translation()

> classmethod

``` python
Translation(value=(0.0, 0.0, 0.0), name='Translation', tip=None, panel='', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Translation Vector group input

New [Vector](vector.md#vector) input with subtype 'TRANSLATION'.

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Translation)
- **tip** ( = None)
- **panel** ( = )
- **default_attribute** ( = )
- **default_input** ( = VALUE)
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### UVMap()

> classmethod

``` python
UVMap(uv_map='', from_instancer=False)
```

> Node [UV Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/uv_map.html)

[!SHADER]

#### Arguments:
- **uv_map** (_str_ = ) : Node.uv_map
- **from_instancer** (_bool_ = False) : Node.from_instancer



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### UvMap()

> classmethod

``` python
UvMap(from_instancer=False, uv_map='')
```

> Node [UV Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/uv_map.html)

#### Arguments:
- **from_instancer** (_bool_ = False) : parameter 'from_instancer'
- **uv_map** (_str_ = ) : parameter 'uv_map'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### vector_displacement()

> method

``` python
vector_displacement(midlevel=None, scale=None, space='TANGENT')
```

> Node [Vector Displacement](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/vector_displacement.html)

[!SHADER]

#### Arguments:
- **midlevel** (_Float_ = None) : socket 'Midlevel' (Midlevel)
- **scale** (_Float_ = None) : socket 'Scale' (Scale)
- **space** (_str_ = TANGENT) : Node.space in ('TANGENT', 'OBJECT', 'WORLD')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### vector_transform()

> method

``` python
vector_transform(convert_from='WORLD', convert_to='OBJECT', vector_type='VECTOR')
```

> Node [Vector Transform](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/transform.html)

#### Information:
- **Socket** : self



#### Arguments:
- **convert_from** (_str_ = WORLD) : parameter 'convert_from' in ['WORLD', 'OBJECT', 'CAMERA']
- **convert_to** (_str_ = OBJECT) : parameter 'convert_to' in ['WORLD', 'OBJECT', 'CAMERA']
- **vector_type** (_str_ = VECTOR) : parameter 'vector_type' in ['POINT', 'VECTOR', 'NORMAL']



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Velocity()

> classmethod

``` python
Velocity(value=(0.0, 0.0, 0.0), name='Velocity', tip=None, panel='', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Velocity group input

New [Vector](vector.md#vector) input with subtype 'VELOCITY'.

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Velocity)
- **tip** ( = None)
- **panel** ( = )
- **default_attribute** ( = )
- **default_input** ( = VALUE)
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### wrap()

> method

``` python
wrap(max=None, min=None)
```

> Node [Vector Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'WRAP'



#### Arguments:
- **max** (_Vector_ = None) : socket 'Max' (id: Vector_001)
- **min** (_Vector_ = None) : socket 'Min' (id: Vector_002)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### XYZ()

> classmethod

``` python
XYZ(value=(0.0, 0.0, 0.0), name='XYZ', tip=None, panel='', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> XYZ group input

New [Vector](vector.md#vector) input with subtype 'XYZ'.

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = XYZ)
- **tip** ( = None)
- **panel** ( = )
- **default_attribute** ( = )
- **default_input** ( = VALUE)
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>