# Boolean

``` python
Boolean(socket=None, name: str = None, tip: str = '', panel: str = '', **props)
```

Boolean socket

> [!CAUTION]
> Boolean operations can't use python operator `and`, `or`,... use `&` `|` instead.


``` python
from geonodes import *

with GeoNodes("Boolean Test"):
    
    with Layout("Base"):
        a = Boolean(False, "False Entry")
        b = Boolean(True, "True Entry")
        # Constant
        c = Boolean(True)

        d = (a | b) & c
        d &= True
        
        d = d.bnot().warning("No output")
        
    with Layout("Named Attribute"):
        g = Mesh()
        g.points._Bool = a
        
        b = Boolean("Bool") | a
        g.faces.store("Another bool", b)

    with Layout("Grid Attribute"):
        vol = g.to_volume()
        vol.store_named_grid("Bool A", a)
    
    vol.enable_output(d).out()
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

- **B** : [band](boolean.md#band) :black_small_square: [bnot](boolean.md#bnot) :black_small_square: [bor](boolean.md#bor)
- **C** : [\_create_input_socket](boolean.md#_create_input_socket)
- **E** : [enable_output](boolean.md#enable_output) :black_small_square: [error](boolean.md#error)
- **F** : [field_to_grid](boolean.md#field_to_grid)
- **G** : [grid_info](boolean.md#grid_info)
- **I** : [imply](boolean.md#imply) :black_small_square: [info](boolean.md#info)
- **N** : [Named](boolean.md#named) :black_small_square: [NamedAttribute](boolean.md#namedattribute) :black_small_square: [nimply](boolean.md#nimply) :black_small_square: [nor](boolean.md#nor) :black_small_square: [not_and](boolean.md#not_and)
- **P** : [prune_grid](boolean.md#prune_grid)
- **R** : [Random](boolean.md#random)
- **S** : [sample_grid](boolean.md#sample_grid) :black_small_square: [sample_grid_index](boolean.md#sample_grid_index) :black_small_square: [set_grid_background](boolean.md#set_grid_background) :black_small_square: [set_grid_transform](boolean.md#set_grid_transform)
- **U** : [uv_unwrap](boolean.md#uv_unwrap)
- **V** : [voxel_index](boolean.md#voxel_index) :black_small_square: [voxelize_grid](boolean.md#voxelize_grid)
- **W** : [warning](boolean.md#warning)
- **X** : [xnor](boolean.md#xnor) :black_small_square: [xor](boolean.md#xor)

## Methods



----------
### band()

> method

``` python
band(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'AND'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### bnot()

> method

``` python
bnot()
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NOT'



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### bor()

> method

``` python
bor(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'OR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### \_create_input_socket()

> classmethod

``` python
_create_input_socket(value: 'object' = False, name: 'str' = 'Boolean', tip: 'str' = '', panel: 'str' = '', optional_label: 'bool' = False, hide_value: 'bool' = False, hide_in_modifier: 'bool' = False, default_attribute: 'str' = '', layer_selection: 'bool' = False, shape: "Literal['AUTO', 'SINGLE']" = 'AUTO')
```

> Boolean Input

New [Boolean](boolean.md#boolean) input with subtype 'NONE'.

Aguments
--------
- value  (object = False) : Default value
- name  (str = 'Boolean') : Input socket name
- tip  (str = '') : Property description
- panel (str = "") : Panel name
- optional_label  (bool = False) : Property optional_label
- hide_value  (bool = False) : Property hide_value
- hide_in_modifier  (bool = False) : Property hide_in_modifier
- default_attribute  (str = '') : Property default_attribute_name
- layer_selection  (bool = False) : Property layer_selection_field
- shape  (str = 'AUTO') : Property structure_type in ('AUTO', 'SINGLE')

#### Arguments:
- **value** (_object_ = False)
- **name** (_str_ = Boolean)
- **tip** (_str_ = )
- **panel** (_str_ = )
- **optional_label** (_bool_ = False)
- **hide_value** (_bool_ = False)
- **hide_in_modifier** (_bool_ = False)
- **default_attribute** (_str_ = )
- **layer_selection** (_bool_ = False)
- **shape** (_Literal['AUTO', 'SINGLE']_ = AUTO)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### enable_output()

> method

``` python
enable_output(enable: 'Boolean' = None)
```

> Node [Enable Output](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../interface/controls/nodes/types/output/enable_output.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **enable** (_Boolean_ = None) : socket 'Enable' (id: Enable)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### error()

> method

``` python
error(message: 'String' = None)
```

> Node [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ERROR'



#### Arguments:
- **message** (_String_ = None) : socket 'Message' (id: Message)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### field_to_grid()

> method

``` python
field_to_grid(named_sockets: 'dict' = {}, **sockets)
```

> Node [Field to Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/field_to_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **named_sockets** (_dict_ = {})
- **sockets**



#### Returns:
- **None** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### grid_info()

> method

``` python
grid_info()
```

> Node [Grid Info](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/grid_info.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Returns:
- **Matrix** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### imply()

> method

``` python
imply(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'IMPLY'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### info()

> method

``` python
info(message: 'String' = None)
```

> Node [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INFO'



#### Arguments:
- **message** (_String_ = None) : socket 'Message' (id: Message)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name: 'String' = None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### nimply()

> method

``` python
nimply(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NIMPLY'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### nor()

> method

``` python
nor(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NOR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### not_and()

> method

``` python
not_and(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NAND'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### prune_grid()

> method

``` python
prune_grid(mode: "Literal['Inactive', 'Threshold', 'SDF']" = None)
```

> Node [Prune Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/prune_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **mode** (_Literal['Inactive', 'Threshold', 'SDF']_ = None) : ('Inactive', 'Threshold', 'SDF')



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(probability: 'Float' = None, id: 'Integer' = None, seed: 'Integer' = None)
```

> Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

#### Information:
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **probability** (_Float_ = None) : socket 'Probability' (id: Probability)
- **id** (_Integer_ = None) : socket 'ID' (id: ID)
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### sample_grid()

> method

``` python
sample_grid(position: 'Vector' = None, interpolation: "Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']" = None)
```

> Node [Sample Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation** (_Literal['Nearest Neighbor', 'Trilinear', 'Triquadratic']_ = None) : ('Nearest Neighbor', 'Trilinear', 'Triquadratic')



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x: 'Integer' = None, y: 'Integer' = None, z: 'Integer' = None)
```

> Node [Sample Grid Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/sample/sample_grid_index.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **x** (_Integer_ = None) : socket 'X' (id: X)
- **y** (_Integer_ = None) : socket 'Y' (id: Y)
- **z** (_Integer_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### set_grid_background()

> method

``` python
set_grid_background(background: 'Boolean' = None)
```

> Node [Set Grid Background](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_background.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **background** (_Boolean_ = None) : socket 'Background' (id: Background)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### set_grid_transform()

> method

``` python
set_grid_transform(transform: 'Matrix' = None)
```

> Node [Set Grid Transform](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/write/set_grid_transform.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **transform** (_Matrix_ = None) : socket 'Transform' (id: Transform)



#### Returns:
- **Boolean** (_Boolean_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### uv_unwrap()

> method

``` python
uv_unwrap(seam: 'Boolean' = None, margin: 'Float' = None, fill_holes: 'Boolean' = None, method: "Literal['Angle Based', 'Conformal']" = None)
```

> Node [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_unwrap.html)

#### Information:
- **Socket** : self



#### Arguments:
- **seam** (_Boolean_ = None) : socket 'Seam' (id: Seam)
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **fill_holes** (_Boolean_ = None) : socket 'Fill Holes' (id: Fill Holes)
- **method** (_Literal['Angle Based', 'Conformal']_ = None) : ('Angle Based', 'Conformal')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### voxel_index()

> classmethod

``` python
voxel_index()
```

> Node [Voxel Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/read/voxel_index.html)

#### Returns:
- **Integer** (_Integer_)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### voxelize_grid()

> method

``` python
voxelize_grid()
```

> Node [Voxelize Grid](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/operations/voxelize_grid.html)

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### warning()

> method

``` python
warning(message: 'String' = None)
```

> Node [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

#### Information:
- **Socket** : self
- **Parameter** : 'WARNING'



#### Arguments:
- **message** (_String_ = None) : socket 'Message' (id: Message)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### xnor()

> method

``` python
xnor(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'XNOR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### xor()

> method

``` python
xor(boolean: 'Boolean' = None)
```

> Node [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'XOR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>