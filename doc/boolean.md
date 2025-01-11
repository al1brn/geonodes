# Boolean

``` python
Boolean(value=False, name=None, tip=None, panel=None, default_attribute='', hide_value=False, layer_selection=False, hide_in_modifier=False, single_value=False)
```

Socket of type BOOLEAN

layer_selection_field

> Node [Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/boolean.html)

#### Arguments:
- **value** (_bool or Socket_ = False) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree pane if exists)
- **default_attribute** (_str_ = ) : default attribute name
- **hide_value** (_bool_ = False) : Hide Value option
- **layer_selection** (_bool_ = False) : Layer selection field
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **B** : [band](boolean.md#band) :black_small_square: [bnot](boolean.md#bnot) :black_small_square: [bor](boolean.md#bor)
- **E** : [error](boolean.md#error)
- **I** : [imply](boolean.md#imply) :black_small_square: [info](boolean.md#info) :black_small_square: [\_\_init__](boolean.md#__init__)
- **N** : [Named](boolean.md#named) :black_small_square: [NamedAttribute](boolean.md#namedattribute) :black_small_square: [nimply](boolean.md#nimply) :black_small_square: [nor](boolean.md#nor) :black_small_square: [not_and](boolean.md#not_and)
- **R** : [Random](boolean.md#random)
- **S** : [sample_grid](boolean.md#sample_grid) :black_small_square: [sample_grid_index](boolean.md#sample_grid_index)
- **U** : [uv_unwrap](boolean.md#uv_unwrap)
- **W** : [warning](boolean.md#warning)
- **X** : [xnor](boolean.md#xnor) :black_small_square: [xor](boolean.md#xor)

## Methods



----------
### band()

> method

``` python
band(boolean=None)
```

> Method [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

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

> Method [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

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
bor(boolean=None)
```

> Method [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'OR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### error()

> method

``` python
error(message=None)
```

> Method [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ERROR'



#### Arguments:
- **message** (_String_ = None) : socket 'Message' (id: Message)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### imply()

> method

``` python
imply(boolean=None)
```

> Method [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

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
info(message=None)
```

> Method [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INFO'



#### Arguments:
- **message** (_String_ = None) : socket 'Message' (id: Message)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=False, name=None, tip=None, panel=None, default_attribute='', hide_value=False, layer_selection=False, hide_in_modifier=False, single_value=False)
```

Socket of type BOOLEAN

layer_selection_field

> Node [Boolean](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/boolean.html)

#### Arguments:
- **value** (_bool or Socket_ = False) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = None) : panel name (overrides tree pane if exists)
- **default_attribute** (_str_ = ) : default attribute name
- **hide_value** (_bool_ = False) : Hide Value option
- **layer_selection** (_bool_ = False) : Layer selection field
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name=None)
```

> Constructor [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

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
NamedAttribute(name=None)
```

> Constructor [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

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
nimply(boolean=None)
```

> Method [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

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
nor(boolean=None)
```

> Method [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

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
not_and(boolean=None)
```

> Method [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NAND'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### Random()

> classmethod

``` python
Random(probability=None, id=None, seed=None)
```

> Constructor [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)

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
sample_grid(position=None, interpolation_mode='TRILINEAR')
```

> Method ERROR: Node 'Sample Grid' not found

#### Information:
- **Socket** : self
- **Parameter** : 'BOOLEAN'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation_mode** (_str_ = TRILINEAR) : parameter 'interpolation_mode' in ('NEAREST', 'TRILINEAR', 'TRIQUADRATIC')



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x=None, y=None, z=None)
```

> Method ERROR: Node 'Sample Grid Index' not found

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
### uv_unwrap()

> method

``` python
uv_unwrap(seam=None, margin=None, fill_holes=None, method='ANGLE_BASED')
```

> Method [UV Unwrap](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_unwrap.html)

#### Information:
- **Socket** : self



#### Arguments:
- **seam** (_Boolean_ = None) : socket 'Seam' (id: Seam)
- **margin** (_Float_ = None) : socket 'Margin' (id: Margin)
- **fill_holes** (_Boolean_ = None) : socket 'Fill Holes' (id: Fill Holes)
- **method** (_str_ = ANGLE_BASED) : parameter 'method' in ('ANGLE_BASED', 'CONFORMAL')



#### Returns:
- **Vector** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>

----------
### warning()

> method

``` python
warning(message=None)
```

> Method [Warning](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/warning.html)

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
xnor(boolean=None)
```

> Method [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

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
xor(boolean=None)
```

> Method [Boolean Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'XOR'



#### Arguments:
- **boolean** (_Boolean_ = None) : socket 'Boolean' (id: Boolean_001)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Boolean](boolean.md#boolean) :black_small_square: [Content](boolean.md#content) :black_small_square: [Methods](boolean.md#methods)</sub>