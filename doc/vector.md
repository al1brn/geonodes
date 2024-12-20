# Vector

> Bases classes: [Attribute](attribute.md#attribute)

``` python
Vector(value=(0, 0, 0), name=None, tip=None, subtype='NONE')
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
- **subtype** (_str_ = NONE) : sub type for group input

### Inherited

[blur](socket.md#blur) :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [hash_value](socket.md#hash_value) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [Named](attribute.md#named) :black_small_square: [NamedAttribute](attribute.md#namedattribute) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square:

## Content

- **A** : [Acceleration](vector.md#acceleration)
- **B** : [bump](vector.md#bump)
- **C** : [Combine](vector.md#combine)
- **D** : [Direction](vector.md#direction) :black_small_square: [displacement](vector.md#displacement) :black_small_square: [displacement_out](vector.md#displacement_out)
- **E** : [Euler](vector.md#euler)
- **F** : [FromRotation](vector.md#fromrotation)
- **I** : [index_of_nearest](vector.md#index_of_nearest) :black_small_square: [\_\_init__](vector.md#__init__)
- **M** : [mapping](vector.md#mapping) :black_small_square: [mix](vector.md#mix) :black_small_square: [mix_non_uniform](vector.md#mix_non_uniform) :black_small_square: [mix_uniform](vector.md#mix_uniform)
- **N** : [normal](vector.md#normal) :black_small_square: [NormalMap](vector.md#normalmap)
- **O** : [out](vector.md#out)
- **R** : [Random](vector.md#random) :black_small_square: [rotate](vector.md#rotate) :black_small_square: [rotate_axis](vector.md#rotate_axis) :black_small_square: [rotate_euler](vector.md#rotate_euler) :black_small_square: [rotate_x](vector.md#rotate_x) :black_small_square: [rotate_y](vector.md#rotate_y) :black_small_square: [rotate_z](vector.md#rotate_z)
- **S** : [separate_xyz](vector.md#separate_xyz)
- **T** : [Tangent](vector.md#tangent) :black_small_square: [to_rotation](vector.md#to_rotation) :black_small_square: [transform](vector.md#transform) :black_small_square: [Translation](vector.md#translation)
- **U** : [UVMap](vector.md#uvmap)
- **V** : [vector_displacement](vector.md#vector_displacement) :black_small_square: [vector_rotate](vector.md#vector_rotate) :black_small_square: [Velocity](vector.md#velocity)
- **X** : [x](vector.md#x) :black_small_square: [XYZ](vector.md#xyz)
- **Y** : [y](vector.md#y)
- **Z** : [z](vector.md#z)

## Properties



### separate_xyz

> _type_: **Node**
>

> Node <&Separate XYZ"

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Properties](vector.md#properties)</sub>

### x

> _type_: **Float**
>

Socket 'X' of node ERROR: Node 'XYZ' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Properties](vector.md#properties)</sub>

### y

> _type_: **Float**
>

Socket 'Y' of node ERROR: Node 'XYZ' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Properties](vector.md#properties)</sub>

### z

> _type_: **Float**
>

Socket 'Z' of node ERROR: Node 'XYZ' not found

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Properties](vector.md#properties)</sub>

## Methods



----------
### Acceleration()

> classmethod

``` python
Acceleration(value=(0.0, 0.0, 0.0), name='Acceleration', tip=None)
```

> Acceleration group input

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Acceleration)
- **tip** ( = None)



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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Direction()

> classmethod

``` python
Direction(value=(0.0, 0.0, 0.0), name='Direction', tip=None)
```

> Direction group input

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Direction)
- **tip** ( = None)



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
### Euler()

> classmethod

``` python
Euler(value=(0.0, 0.0, 0.0), name='Euler', tip=None)
```

> Euler group input

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Euler)
- **tip** ( = None)



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
### index_of_nearest()

> method

``` python
index_of_nearest(group_id=None)
```

> Node ERROR: Node 'Index of Nearest' not found

#### Arguments:
- **group_id** (_Integer_ = None) : socket 'Group ID' (Group ID)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=(0, 0, 0), name=None, tip=None, subtype='NONE')
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
- **subtype** (_str_ = NONE) : sub type for group input

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
### mix()

> method

``` python
mix(factor=None, other=None, clamp_factor=None, factor_mode=None)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor'
- **other** (_Vector_ = None) : socket 'B'
- **clamp_factor** (_bool_ = None) : clamp_factor parameter
- **factor_mode** (_str in 'UNIFORM', 'NON_UNIFORM'_ = None)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### mix_non_uniform()

> method

``` python
mix_non_uniform(factor=None, other=None, clamp_factor=None)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html), factor_mode = 'NON_UNIFORM'

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor'
- **other** (_Vector_ = None) : socket 'B'
- **clamp_factor** (_bool_ = None) : clamp_factor parameter



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### mix_uniform()

> method

``` python
mix_uniform(factor=None, other=None, clamp_factor=None)
```

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html), factor_mode = 'UNIFORM'

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor'
- **other** (_Vector_ = None) : socket 'B'
- **clamp_factor** (_bool_ = None) : clamp_factor parameter



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
### out()

> method

``` python
out(name=None)
```

> Plug the Vector to the group output

[!MIX]

> [!NOTE]
> - [GeoNodes](core-geono-geonodes.md#geonodes) : the Vector is plug as group output
> - [ShaderNodes](shade-shade1-shadernodes.md#shadernodes) : if **name** argument is None, the vecteur is plugged
>.  into the `Displacement` socket of ERROR: Node '&Material Output' not found,
>   otherwise it is plugged to a [AOV Output](https://docs.blender.org/manual/en/latest/render/shader_nodes/output/aov.html) node.

#### Arguments:
- **name** ( = None)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate()

> method

``` python
rotate(rotation=None)
```

> Node [Rotate Vector](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_vector.html)

#### Arguments:
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_axis()

> method

``` python
rotate_axis(center=None, axis=None, angle=None, invert=None)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html), rotation_type = 'AXIS_ANGLE'

#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **axis** (_Vector_ = None) : socket 'Axis' (Axis)
- **angle** (_Float_ = None) : socket 'Angle' (Angle)
- **invert** (_bool_ = None) : Node.invert



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_euler()

> method

``` python
rotate_euler(center=None, rotation=None, invert=None)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html), rotation_type = 'EULER_XYZ'

#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **rotation** (_Vector_ = None) : socket 'Rotation' (Rotation)
- **invert** (_bool_ = None) : Node.invert



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_x()

> method

``` python
rotate_x(center=None, angle=None, invert=None)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html), rotation_type = 'X_AXIS'

#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **angle** (_Float_ = None) : socket 'Angle' (Angle)
- **invert** (_bool_ = None) : Node.invert



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_y()

> method

``` python
rotate_y(center=None, angle=None, invert=None)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html), rotation_type = 'Y_AXIS'

#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **angle** (_Float_ = None) : socket 'Angle' (Angle)
- **invert** (_bool_ = None) : Node.invert



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_z()

> method

``` python
rotate_z(center=None, angle=None, invert=None)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html), rotation_type = 'Z_AXIS'

#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **angle** (_Float_ = None) : socket 'Angle' (Angle)
- **invert** (_bool_ = None) : Node.invert



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

Node ERROR: Node 'to Rotation' not found

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
Translation(value=(0.0, 0.0, 0.0), name='Translation', tip=None)
```

> Translation group input

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Translation)
- **tip** ( = None)



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
### vector_rotate()

> method

``` python
vector_rotate(center=None, axis=None, angle=None, rotation=None, invert=None, rotation_type=None)
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (Center)
- **axis** (_Vector_ = None) : socket 'Axis' (Axis)
- **angle** (_Float_ = None) : socket 'Angle' (Angle)
- **rotation** (_Vector_ = None) : socket 'Rotation' (Rotation)
- **invert** (_bool_ = None) : Node.invert
- **rotation_type** (_str_ = None) : Node.rotation_type in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Velocity()

> classmethod

``` python
Velocity(value=(0.0, 0.0, 0.0), name='Velocity', tip=None)
```

> Velocity group input

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = Velocity)
- **tip** ( = None)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### XYZ()

> classmethod

``` python
XYZ(value=(0.0, 0.0, 0.0), name='XYZ', tip=None)
```

> XYZ group input

#### Arguments:
- **value** ( = (0.0, 0.0, 0.0))
- **name** ( = XYZ)
- **tip** ( = None)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>