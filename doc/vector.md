# Vector

``` python
Vector(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

Vector Socket.

`x`, `y`, `z` components can be addressed individually using their properties.
The `xyz` property returns the triplet of the components.

A Vector can be created using a triplet or even a single float or Float.

Use methods Percentage, Factor, Translation, Direction, Velocity, Acceleration, Euler or Xyz
to create input sockets with a subtype.

``` python
from geonodes import GeoNodes, Mesh, Layout, Rotation, Vector, G, Float, Input, pi

with GeoNodes("Vector Test") as tree:
    
    with Layout("Base"):
        a = Vector()
        a += Vector((1, 2, 3))
        a *= Vector(7, name="Vector")
        a = a.mix(Vector.Translation(1, name="Translate"), factor=Input("Factor", subtype="Percentage", default=.5, min=0, max=100))
        
    with Layout("Named Attribute"):
        g = Mesh()
        g.points.The_Vector = a
        
        a = Vector("The Vector")
        a += G().combine_cylindrical(r=10, phi=Input("Phi", subtype="Angle"), z=3)
        g.points.The_Vector = a

    with Layout("Working with components"):
        
        # Getting one of the components
        cx = a.x
        
        # Alternative to separate_xyz
        x, y, z = a.xyz

        # Building from tripler
        a += (x**2, y + cx, z-1)

    a.separate_xyz().out(panel="xyz")
    
    g.out()
    ```

#### Arguments:
- **socket** (_NodeSocket_ = None) : the output socket to wrap
- **name** (_str_ = None)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **props**

### Inherited

['_bsocket' not found]() :black_small_square: [\_cache](nodecache.md#_cache) :black_small_square: ['_cached_nodes' not found]() :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](core-socket.md#check_in_list) :black_small_square: [Constant](core-socket.md#constant) :black_small_square: [default_value](core-socket.md#default_value) :black_small_square: [\_domain_to_geometry](domain.md#_domain_to_geometry) :black_small_square: [Empty](core-socket.md#empty) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_bsocket_from_input](core-socket.md#_get_bsocket_from_input) :black_small_square: [IndexSwitch](core-socket.md#indexswitch) :black_small_square: [index_switch](core-socket.md#index_switch) :black_small_square: [\_\_init__](colorramp.md#__init__) :black_small_square: [Input](input.md#input) :black_small_square: [\_interface_socket](core-socket.md#_interface_socket) :black_small_square: [\_is_empty](core-socket.md#_is_empty) :black_small_square: [is_grid](core-socket.md#is_grid) :black_small_square: [\_jump](domain.md#_jump) :black_small_square: ['_layout' not found]() :black_small_square: [\_lc](node.md#_lc) :black_small_square: [\_lcop](core-socket.md#_lcop) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [MenuSwitch](core-socket.md#menuswitch) :black_small_square: [menu_switch](menu.md#menu_switch) :black_small_square: [\_name](core-socket.md#_name) :black_small_square: [NewInput](core-socket.md#newinput) :black_small_square: [node](core-socket.md#node) :black_small_square: [node_color](core-socket.md#node_color) :black_small_square: [node_label](core-socket.md#node_label) :black_small_square: [\_panel_name](core-socket.md#_panel_name) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](closure.md#_pop) :black_small_square: [\_push](closure.md#_push) :black_small_square: [repeat](core-socket.md#repeat) :black_small_square: [\_reset](cloud.md#_reset) :black_small_square: [simulation](core-socket.md#simulation) :black_small_square: [\_socket_type](core-socket.md#_socket_type) :black_small_square: [\_\_str__](domain.md#__str__) :black_small_square: [Switch](core-socket.md#switch) :black_small_square: [switch](core-socket.md#switch) :black_small_square: [switch_false](core-socket.md#switch_false) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_layout' not found]() :black_small_square:

## Content

- **A** : [abs](vector.md#abs) :black_small_square: [Acceleration](vector.md#acceleration) :black_small_square: [add](vector.md#add) :black_small_square: [advect_grid](vector.md#advect_grid)
- **B** : [blur](vector.md#blur) :black_small_square: [bump](vector.md#bump)
- **C** : [ceil](vector.md#ceil) :black_small_square: [CombineXYZ](vector.md#combinexyz) :black_small_square: [cos](vector.md#cos) :black_small_square: [\_create_input_socket](vector.md#_create_input_socket) :black_small_square: [cross](vector.md#cross) :black_small_square: [curves](vector.md#curves)
- **D** : [Direction](vector.md#direction) :black_small_square: [displacement](vector.md#displacement) :black_small_square: [displacement_out](vector.md#displacement_out) :black_small_square: [distance](vector.md#distance) :black_small_square: [divide](vector.md#divide) :black_small_square: [dot](vector.md#dot)
- **E** : [enable_output](vector.md#enable_output) :black_small_square: [environment_texture](vector.md#environment_texture) :black_small_square: [equal](vector.md#equal) :black_small_square: [Euler](vector.md#euler)
- **F** : [faceforward](vector.md#faceforward) :black_small_square: [Factor](vector.md#factor) :black_small_square: [field_to_grid](vector.md#field_to_grid) :black_small_square: [floor](vector.md#floor) :black_small_square: [fraction](vector.md#fraction) :black_small_square: [FromRotation](vector.md#fromrotation)
- **G** : [greater_equal](vector.md#greater_equal) :black_small_square: [greater_than](vector.md#greater_than) :black_small_square: [grid_curl](vector.md#grid_curl) :black_small_square: [grid_divergence](vector.md#grid_divergence) :black_small_square: [grid_info](vector.md#grid_info)
- **H** : [hash_value](vector.md#hash_value)
- **I** : [ies_texture](vector.md#ies_texture) :black_small_square: [ies_texture_external](vector.md#ies_texture_external) :black_small_square: [ies_texture_internal](vector.md#ies_texture_internal) :black_small_square: [image_texture](vector.md#image_texture)
- **L** : [length](vector.md#length) :black_small_square: [less_equal](vector.md#less_equal) :black_small_square: [less_than](vector.md#less_than)
- **M** : [mapping](vector.md#mapping) :black_small_square: [map_range](vector.md#map_range) :black_small_square: [max](vector.md#max) :black_small_square: [min](vector.md#min) :black_small_square: [mix](vector.md#mix) :black_small_square: [mix_non_uniform](vector.md#mix_non_uniform) :black_small_square: [mix_uniform](vector.md#mix_uniform) :black_small_square: [modulo](vector.md#modulo) :black_small_square: [multiply](vector.md#multiply) :black_small_square: [multiply_add](vector.md#multiply_add)
- **N** : [Named](vector.md#named) :black_small_square: [NamedAttribute](vector.md#namedattribute) :black_small_square: [normal](vector.md#normal) :black_small_square: [normalize](vector.md#normalize) :black_small_square: [NormalMap](vector.md#normalmap) :black_small_square: [not_equal](vector.md#not_equal)
- **O** : [out](vector.md#out)
- **P** : [pack_uv_islands](vector.md#pack_uv_islands) :black_small_square: [Percentage](vector.md#percentage) :black_small_square: [power](vector.md#power) :black_small_square: [project](vector.md#project) :black_small_square: [prune_grid](vector.md#prune_grid)
- **R** : [radial_tiling](vector.md#radial_tiling) :black_small_square: [Random](vector.md#random) :black_small_square: [reflect](vector.md#reflect) :black_small_square: [refract](vector.md#refract) :black_small_square: [rotate](vector.md#rotate) :black_small_square: [rotate_axis_angle](vector.md#rotate_axis_angle) :black_small_square: [rotate_euler_xyz](vector.md#rotate_euler_xyz) :black_small_square: [rotate_x_axis](vector.md#rotate_x_axis) :black_small_square: [rotate_y_axis](vector.md#rotate_y_axis) :black_small_square: [rotate_z_axis](vector.md#rotate_z_axis)
- **S** : [sample_grid](vector.md#sample_grid) :black_small_square: [sample_grid_index](vector.md#sample_grid_index) :black_small_square: [scale](vector.md#scale) :black_small_square: [separate_xyz](vector.md#separate_xyz) :black_small_square: [set_grid_background](vector.md#set_grid_background) :black_small_square: [set_grid_transform](vector.md#set_grid_transform) :black_small_square: [sign](vector.md#sign) :black_small_square: [sin](vector.md#sin) :black_small_square: [snap](vector.md#snap) :black_small_square: [subtract](vector.md#subtract)
- **T** : [tan](vector.md#tan) :black_small_square: [Tangent](vector.md#tangent) :black_small_square: [to_rotation](vector.md#to_rotation) :black_small_square: [transform](vector.md#transform) :black_small_square: [Translation](vector.md#translation)
- **U** : [UVMap](vector.md#uvmap) :black_small_square: [UvMap](vector.md#uvmap) :black_small_square: [uv_tangent](vector.md#uv_tangent)
- **V** : [vector_displacement](vector.md#vector_displacement) :black_small_square: [vector_transform](vector.md#vector_transform) :black_small_square: [Velocity](vector.md#velocity) :black_small_square: [voxel_index](vector.md#voxel_index) :black_small_square: [voxelize_grid](vector.md#voxelize_grid)
- **W** : [wrap](vector.md#wrap)
- **X** : [x](vector.md#x) :black_small_square: [xyz](vector.md#xyz) :black_small_square: [Xyz](vector.md#xyz)
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
Acceleration(value: 'object' = (0, 0, 0), name: 'str' = 'Acceleration', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Acceleration Input

New [Vector](vector.md#vector) input with subtype 'ACCELERATION'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Acceleration') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Acceleration)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### add()

> method

``` python
add(vector: 'Vector' = None)
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
### advect_grid()

> method

``` python
advect_grid(velocity: 'Vector' = None, time_step: 'Float' = None, integration_scheme: "Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC']" = None, limiter: "Literal['None', 'Clamp', 'Revert']" = None)
```

> Node [Advect Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/advect_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **velocity** (_Vector_ = None) : socket 'Velocity' (id: Velocity)
- **time_step** (_Float_ = None) : socket 'Time Step' (id: Time Step)
- **integration_scheme** (_Literal['Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC']_ = None) : ('Semi-Lagrangian', 'Midpoint', 'Runge-Kutta 3', 'Runge-Kutta 4', 'MacCormack', 'BFECC')
- **limiter** (_Literal['None', 'Clamp', 'Revert']_ = None) : ('None', 'Clamp', 'Revert')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### blur()

> method

``` python
blur(iterations: 'Integer' = None, weight: 'Float' = None)
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

> Node [Bump](https://docs.blender.org/manual/en/latest/render/shader_nodes/displacement/bump.html)

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
CombineXYZ(x: 'Float' = None, y: 'Float' = None, z: 'Float' = None)
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
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = (0, 0, 0), name: 'str' = 'Vector', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO', subtype: 'str' = 'NONE')
```

> Vector Input

New [Vector](vector.md#vector) input with subtype 'NONE'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Vector') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')
- subtype (str = 'NONE') : Socket sub type in ('NONE', 'PERCENTAGE', 'FACTOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'EULER', 'XYZ')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Vector)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)
- **subtype** (_str_ = NONE)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### cross()

> method

``` python
cross(vector: 'Vector' = None)
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
Direction(value: 'object' = (0, 0, 0), name: 'str' = 'Direction', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Direction Input

New [Vector](vector.md#vector) input with subtype 'DIRECTION'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Direction') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Direction)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### displacement()

> method

``` python
displacement(height=None, midlevel=None, scale=None, space='OBJECT')
```

> Node [Displacement](https://docs.blender.org/manual/en/latest/render/shader_nodes/displacement/displacement.html)

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
distance(vector: 'Vector' = None)
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
divide(vector: 'Vector' = None)
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
dot(vector: 'Vector' = None)
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
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### environment_texture()

> method

``` python
environment_texture(image=None, interpolation: "Literal['Linear', 'Closest', 'Cubic', 'Smart']" = 'Linear', projection: "Literal['EQUIRECTANGULAR', 'MIRROR_BALL']" = 'EQUIRECTANGULAR')
```

> Node [Environment Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/environment.html)

#### Information:
- **Socket** : self



#### Arguments:
- **image** (_NoneType_ = None) : parameter 'image'
- **interpolation** (_Literal['Linear', 'Closest', 'Cubic', 'Smart']_ = Linear) : parameter 'interpolation' in ['Linear', 'Closest', 'Cubic', 'Smart']
- **projection** (_Literal['EQUIRECTANGULAR', 'MIRROR_BALL']_ = EQUIRECTANGULAR) : parameter 'projection' in ['EQUIRECTANGULAR', 'MIRROR_BALL']



#### Returns:
- **Color** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b: 'Vector' = None, epsilon: 'Float' = None)
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
Euler(value: 'object' = (0, 0, 0), name: 'str' = 'Euler', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Euler Input

New [Vector](vector.md#vector) input with subtype 'EULER'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Euler') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Euler)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### faceforward()

> method

``` python
faceforward(incident: 'Vector' = None, reference: 'Vector' = None)
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
### Factor()

> classmethod

``` python
Factor(value: 'object' = (0, 0, 0), name: 'str' = 'Factor', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Factor Input

New [Vector](vector.md#vector) input with subtype 'FACTOR'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Factor') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Factor)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### field_to_grid()

> method

``` python
field_to_grid(named_sockets: 'dict' = {}, **sockets)
```

> Node [Field to Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/field_to_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **sockets**



#### Returns:
- **None** :

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
greater_equal(b: 'Vector' = None)
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
greater_than(b: 'Vector' = None)
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
### grid_curl()

> method

``` python
grid_curl()
```

> Node [Grid Curl](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/grid_curl.html)

#### Information:
- **Socket** : self



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### grid_divergence()

> method

``` python
grid_divergence()
```

> Node [Grid Divergence](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/grid_divergence.html)

#### Information:
- **Socket** : self



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### grid_info()

> method

``` python
grid_info()
```

> Node [Grid Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/grid_info.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Returns:
- **Matrix** (_Vector_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed: 'Integer' = None)
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
ies_texture(strength: 'Float' = None, filepath='', ies=None, mode: "Literal['INTERNAL', 'EXTERNAL']" = 'INTERNAL')
```

> Node [IES Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/ies.html)

#### Information:
- **Socket** : self



#### Arguments:
- **strength** (_Float_ = None) : socket 'Strength' (id: Strength)
- **filepath** (_str_ = ) : parameter 'filepath'
- **ies** (_NoneType_ = None) : parameter 'ies'
- **mode** (_Literal['INTERNAL', 'EXTERNAL']_ = INTERNAL) : parameter 'mode' in ['INTERNAL', 'EXTERNAL']



#### Returns:
- **Float** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### ies_texture_external()

> method

``` python
ies_texture_external(strength: 'Float' = None, filepath='', ies=None)
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
ies_texture_internal(strength: 'Float' = None, filepath='', ies=None)
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
image_texture(extension: "Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']" = 'REPEAT', image=None, interpolation: "Literal['Linear', 'Closest', 'Cubic', 'Smart']" = 'Linear', projection: "Literal['FLAT', 'BOX', 'SPHERE', 'TUBE']" = 'FLAT', projection_blend=0.0)
```

> Node [Image Texture](https://docs.blender.org/manual/en/latest/render/shader_nodes/../../modeling/geometry_nodes/texture/image.html)

#### Information:
- **Socket** : self



#### Arguments:
- **extension** (_Literal['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']_ = REPEAT) : parameter 'extension' in ['REPEAT', 'EXTEND', 'CLIP', 'MIRROR']
- **image** (_NoneType_ = None) : parameter 'image'
- **interpolation** (_Literal['Linear', 'Closest', 'Cubic', 'Smart']_ = Linear) : parameter 'interpolation' in ['Linear', 'Closest', 'Cubic', 'Smart']
- **projection** (_Literal['FLAT', 'BOX', 'SPHERE', 'TUBE']_ = FLAT) : parameter 'projection' in ['FLAT', 'BOX', 'SPHERE', 'TUBE']
- **projection_blend** (_float_ = 0.0) : parameter 'projection_blend'



#### Returns:
- **Color** (_Float_)

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
less_equal(b: 'Vector' = None)
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
less_than(b: 'Vector' = None)
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

> Node [Mapping](https://docs.blender.org/manual/en/latest/render/shader_nodes/utilities/vector/mapping.html)

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
### map_range()

> method

``` python
map_range(from_min: 'Vector' = None, from_max: 'Vector' = None, to_min: 'Vector' = None, to_max: 'Vector' = None, clamp=True, interpolation_type: "Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']" = 'LINEAR')
```

> Node [Map Range](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOAT_VECTOR'



#### Arguments:
- **from_min** (_Vector_ = None) : socket 'From Min' (id: From_Min_FLOAT3)
- **from_max** (_Vector_ = None) : socket 'From Max' (id: From_Max_FLOAT3)
- **to_min** (_Vector_ = None) : socket 'To Min' (id: To_Min_FLOAT3)
- **to_max** (_Vector_ = None) : socket 'To Max' (id: To_Max_FLOAT3)
- **clamp** (_bool_ = True) : parameter 'clamp'
- **interpolation_type** (_Literal['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']_ = LINEAR) : parameter 'interpolation_type' in ['LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP']



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### max()

> method

``` python
max(vector: 'Vector' = None)
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
min(vector: 'Vector' = None)
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
mix_non_uniform(b: 'Vector' = None, factor: 'Vector' = None, clamp_factor=True)
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
mix_uniform(b: 'Vector' = None, factor: 'Float' = None, clamp_factor=True)
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
modulo(vector: 'Vector' = None)
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
multiply(vector: 'Vector' = None)
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
multiply_add(multiplier: 'Vector' = None, addend: 'Vector' = None)
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
Named(name: 'String' = None)
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
NamedAttribute(name: 'String' = None)
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

> Constructor node [Normal Map](https://docs.blender.org/manual/en/latest/render/shader_nodes/displacement/normal_map.html)

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
not_equal(b: 'Vector' = None, epsilon: 'Float' = None)
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
pack_uv_islands(margin: 'Float' = None, rotate: 'Boolean' = None, method: "Literal['Bounding Box', 'Convex Hull', 'Exact Shape']" = None)
```

> Node [Pack UV Islands](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/pack_uv_islands.html)

#### Information:
- **Socket** : self
- **Socket** : self[selection]



#### Arguments:
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **rotate** (_Boolean_ = None) : socket 'Rotate' (id: Rotate)
- **method** (_Literal['Bounding Box', 'Convex Hull', 'Exact Shape']_ = None) : ('Bounding Box', 'Convex Hull', 'Exact Shape')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Percentage()

> classmethod

``` python
Percentage(value: 'object' = (0, 0, 0), name: 'str' = 'Percentage', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Percentage Input

New [Vector](vector.md#vector) input with subtype 'PERCENTAGE'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Percentage') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Percentage)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### power()

> method

``` python
power(exponent: 'Vector' = None)
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
project(vector: 'Vector' = None)
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
### prune_grid()

> method

``` python
prune_grid(mode: "Literal['Inactive', 'Threshold', 'SDF']" = None, threshold: 'Vector' = None)
```

> Node [Prune Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/prune_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **mode** (_Literal['Inactive', 'Threshold', 'SDF']_ = None) : ('Inactive', 'Threshold', 'SDF')
- **threshold** (_Vector_ = None) : socket 'Threshold' (id: Threshold)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### radial_tiling()

> method

``` python
radial_tiling(sides: 'Float' = None, roundness: 'Float' = None, normalize=False)
```

> Node [Radial Tiling](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/radial_tiling.html)

#### Information:
- **Socket** : self



#### Arguments:
- **sides** (_Float_ = None) : socket 'Sides' (id: Sides)
- **roundness** (_Float_ = None) : socket 'Roundness' (id: Roundness)
- **normalize** (_bool_ = False) : parameter 'normalize'



#### Returns:
- **Vector** (_Float_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(min: 'Vector' = None, max: 'Vector' = None, id: 'Integer' = None, seed: 'Integer' = None)
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
reflect(vector: 'Vector' = None)
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
refract(vector: 'Vector' = None, ior: 'Float' = None)
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
rotate(center: 'Vector' = None, axis: 'Vector' = None, angle: 'Float' = None, invert=False, rotation_type: "Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']" = 'AXIS_ANGLE')
```

> Node [Vector Rotate](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html)

#### Information:
- **Socket** : self



#### Arguments:
- **center** (_Vector_ = None) : socket 'Center' (id: Center)
- **axis** (_Vector_ = None) : socket 'Axis' (id: Axis)
- **angle** (_Float_ = None) : socket 'Angle' (id: Angle)
- **invert** (_bool_ = False) : parameter 'invert'
- **rotation_type** (_Literal['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']_ = AXIS_ANGLE) : parameter 'rotation_type' in ['AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ']



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### rotate_axis_angle()

> method

``` python
rotate_axis_angle(center: 'Vector' = None, axis: 'Vector' = None, angle: 'Float' = None, invert=False)
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
rotate_euler_xyz(center: 'Vector' = None, rotation: 'Vector' = None, invert=False)
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
rotate_x_axis(center: 'Vector' = None, angle: 'Float' = None, invert=False)
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
rotate_y_axis(center: 'Vector' = None, angle: 'Float' = None, invert=False)
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
rotate_z_axis(center: 'Vector' = None, angle: 'Float' = None, invert=False)
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
sample_grid(position: 'Vector' = None, interpolation: "Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']" = None)
```

> Node [Sample Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation** (_Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']_ = None) : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x: 'Integer' = None, y: 'Integer' = None, z: 'Integer' = None)
```

> Node [Sample Grid Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid_index.html)

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
scale(scale: 'Float' = None)
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
### set_grid_background()

> method

``` python
set_grid_background(background: 'Vector' = None)
```

> Node [Set Grid Background](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_background.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **background** (_Vector_ = None) : socket 'Background' (id: Background)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### set_grid_transform()

> method

``` python
set_grid_transform(transform: 'Matrix' = None)
```

> Node [Set Grid Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_transform.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Arguments:
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Boolean** (_Vector_)

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
snap(increment: 'Vector' = None)
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
subtract(vector: 'Vector' = None)
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

> Node [Vector Transform](https://docs.blender.org/manual/en/latest/render/shader_nodes/utilities/vector/transform.html)

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
Translation(value: 'object' = (0, 0, 0), name: 'str' = 'Translation', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Translation Input

New [Vector](vector.md#vector) input with subtype 'TRANSLATION'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Translation') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Translation)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



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
### uv_tangent()

> method

``` python
uv_tangent(method: "Literal['Exact', 'Fast']" = None)
```

> Node [UV Tangent](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_tangent.html)

#### Information:
- **Socket** : self



#### Arguments:
- **method** (_Literal['Exact', 'Fast']_ = None) : ('Exact', 'Fast')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### vector_displacement()

> method

``` python
vector_displacement(midlevel=None, scale=None, space='TANGENT')
```

> Node [Vector Displacement](https://docs.blender.org/manual/en/latest/render/shader_nodes/displacement/vector_displacement.html)

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
vector_transform(convert_from: "Literal['WORLD', 'OBJECT', 'CAMERA']" = 'WORLD', convert_to: "Literal['WORLD', 'OBJECT', 'CAMERA']" = 'OBJECT', vector_type: "Literal['POINT', 'VECTOR', 'NORMAL']" = 'VECTOR')
```

> Node [Vector Transform](https://docs.blender.org/manual/en/latest/render/shader_nodes/utilities/vector/transform.html)

#### Information:
- **Socket** : self



#### Arguments:
- **convert_from** (_Literal['WORLD', 'OBJECT', 'CAMERA']_ = WORLD) : parameter 'convert_from' in ['WORLD', 'OBJECT', 'CAMERA']
- **convert_to** (_Literal['WORLD', 'OBJECT', 'CAMERA']_ = OBJECT) : parameter 'convert_to' in ['WORLD', 'OBJECT', 'CAMERA']
- **vector_type** (_Literal['POINT', 'VECTOR', 'NORMAL']_ = VECTOR) : parameter 'vector_type' in ['POINT', 'VECTOR', 'NORMAL']



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### Velocity()

> classmethod

``` python
Velocity(value: 'object' = (0, 0, 0), name: 'str' = 'Velocity', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Velocity Input

New [Vector](vector.md#vector) input with subtype 'VELOCITY'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Velocity') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Velocity)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### voxel_index()

> classmethod

``` python
voxel_index()
```

> Node [Voxel Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/voxel_index.html)

#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### voxelize_grid()

> method

``` python
voxelize_grid()
```

> Node [Voxelize Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/voxelize_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'VECTOR'



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>

----------
### wrap()

> method

``` python
wrap(max: 'Vector' = None, min: 'Vector' = None)
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
### Xyz()

> classmethod

``` python
Xyz(value: 'object' = (0, 0, 0), name: 'str' = 'Xyz', min: 'float' = -3.40282e+38, max: 'float' = 3.40282e+38, tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, dimensions: 'int' = 3, default_attribute: 'str' = '', default_input: "Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']" = 'VALUE', shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Xyz Input

New [Vector](vector.md#vector) input with subtype 'XYZ'.

Aguments
--------
- value  (object = (0, 0, 0)) : Default value
- name  (str = 'Xyz') : Input socket name
- min  (float = -3.40282e+38) : Property min_value
- max  (float = 3.40282e+38) : Property max_value
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- dimensions  (int = 3) : Property dimensions
- default_attribute  (str = '') : Property default_attribute_name
- default_input  (str = 'VALUE') : Property default_input in ('VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT')
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = (0, 0, 0))
- **name** (_str_ = Xyz)
- **min** (_float_ = -3.40282e+38)
- **max** (_float_ = 3.40282e+38)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **dimensions** (_int_ = 3)
- **default_attribute** (_str_ = )
- **default_input** (_Literal['VALUE', 'NORMAL', 'POSITION', 'HANDLE_LEFT', 'HANDLE_RIGHT']_ = VALUE)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Vector](vector.md#vector) :black_small_square: [Content](vector.md#content) :black_small_square: [Methods](vector.md#methods)</sub>