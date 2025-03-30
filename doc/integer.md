# Integer

``` python
Integer(value=0, name=None, min=None, max=None, tip=None, panel='', subtype='NONE', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Socket of type INTEGER

> Node [Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/value.html)

If **value** argument is None:
- if **name** argument is None, a node 'Integer' is added
- otherwise a new group input is created using **min**, **max**, **tip** and **subtype**
  arguments

If **value** argument is not None, a new **Integer** is created from the value, either
by transtyping or creating a 'Value' node.

``` python
i = Integer()      # 'Integer' node with default initial vlaue
i = Integer(123). # 'Integer' node with 123 initial value
i = Integer(123, name="User input", subtype='PERCENTAGE') # Create a new integer group input
```

#### Arguments:
- **value** (_integer or Socket_ = 0) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **min** (_float_ = None) : minimum value
- **max** (_float_ = None) : maximum value
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = ) : panel name (overrides tree panel if exists)
- **subtype** (_str in ('NONE', 'PERCENTAGE', 'FACTOR')_ = NONE) : sub type for group input
- **default_attribute** (_str_ = ) : default attribute name
- **default_input** (_str in ('VALUE', 'INDEX', 'ID_OR_INDEX')_ = VALUE) : default input
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

### Inherited

[\_cache](nodecache.md#_cache) :black_small_square: [\_cache_reset](nodecache.md#_cache_reset) :black_small_square: [check_in_list](socket.md#check_in_list) :black_small_square: [data_type](socket.md#data_type) :black_small_square: [\_domain_to_geometry](socket.md#_domain_to_geometry) :black_small_square: [\_geometry_class](socket.md#_geometry_class) :black_small_square: [\_\_getattr__](socket.md#__getattr__) :black_small_square: [get_node_data_type](socket.md#get_node_data_type) :black_small_square: [get_socket_class](socket.md#get_socket_class) :black_small_square: [IndexSwitch](socket.md#indexswitch) :black_small_square: [index_switch](socket.md#index_switch) :black_small_square: [Input](socket.md#input) :black_small_square: [input_type](socket.md#input_type) :black_small_square: [\_interface_socket](socket.md#_interface_socket) :black_small_square: [\_is_group_input](socket.md#_is_group_input) :black_small_square: [\_is_group_output](socket.md#_is_group_output) :black_small_square: [\_is_group_socket](socket.md#_is_group_socket) :black_small_square: [\_jump](socket.md#_jump) :black_small_square: [\_lc](socket.md#_lc) :black_small_square: [\_lcop](socket.md#_lcop) :black_small_square: [link_from](socket.md#link_from) :black_small_square: [\_lock](proplocker.md#_lock) :black_small_square: [\_mark_for_delete](socket.md#_mark_for_delete) :black_small_square: [MenuSwitch](socket.md#menuswitch) :black_small_square: [menu_switch](socket.md#menu_switch) :black_small_square: [\_name](socket.md#_name) :black_small_square: [node](socket.md#node) :black_small_square: [node_color](socket.md#node_color) :black_small_square: [node_label](socket.md#node_label) :black_small_square: [option](socket.md#option) :black_small_square: [option_index](socket.md#option_index) :black_small_square: [out](socket.md#out) :black_small_square: [\_panel_name](socket.md#_panel_name) :black_small_square: [pin_gizmo](socket.md#pin_gizmo) :black_small_square: [\_reset](socket.md#_reset) :black_small_square: [\_run_tests](socket.md#_run_tests) :black_small_square: [\_\_setattr__](socket.md#__setattr__) :black_small_square: [\_set_interface_property](socket.md#_set_interface_property) :black_small_square: [socket_type](socket.md#socket_type) :black_small_square: [\_\_str__](socket.md#__str__) :black_small_square: [Switch](socket.md#switch) :black_small_square: [switch](socket.md#switch) :black_small_square: [switch_false](socket.md#switch_false) :black_small_square: [\_unlock](proplocker.md#_unlock) :black_small_square:

## Content

- **A** : [abs](integer.md#abs) :black_small_square: [add](integer.md#add)
- **B** : [blur](integer.md#blur)
- **D** : [divide](integer.md#divide) :black_small_square: [divide_ceil](integer.md#divide_ceil) :black_small_square: [divide_floor](integer.md#divide_floor) :black_small_square: [divide_round](integer.md#divide_round)
- **E** : [equal](integer.md#equal)
- **F** : [Factor](integer.md#factor) :black_small_square: [floored_modulo](integer.md#floored_modulo)
- **G** : [gcd](integer.md#gcd) :black_small_square: [greater_equal](integer.md#greater_equal) :black_small_square: [greater_than](integer.md#greater_than)
- **H** : [hash_value](integer.md#hash_value)
- **I** : [IdOrIndex](integer.md#idorindex) :black_small_square: [Index](integer.md#index) :black_small_square: [\_\_init__](integer.md#__init__)
- **L** : [lcm](integer.md#lcm) :black_small_square: [less_equal](integer.md#less_equal) :black_small_square: [less_than](integer.md#less_than)
- **M** : [max](integer.md#max) :black_small_square: [min](integer.md#min) :black_small_square: [mix](integer.md#mix) :black_small_square: [modulo](integer.md#modulo) :black_small_square: [multiply](integer.md#multiply) :black_small_square: [multiply_add](integer.md#multiply_add)
- **N** : [Named](integer.md#named) :black_small_square: [NamedAttribute](integer.md#namedattribute) :black_small_square: [negate](integer.md#negate) :black_small_square: [not_equal](integer.md#not_equal)
- **P** : [Percentage](integer.md#percentage) :black_small_square: [power](integer.md#power)
- **S** : [sample_grid](integer.md#sample_grid) :black_small_square: [sample_grid_index](integer.md#sample_grid_index) :black_small_square: [sign](integer.md#sign) :black_small_square: [subtract](integer.md#subtract)
- **T** : [to_string](integer.md#to_string)

## Methods



----------
### abs()

> method

``` python
abs()
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ABSOLUTE'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### add()

> method

``` python
add(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'ADD'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### blur()

> method

``` python
blur(iterations=None, weight=None)
```

> Node [Blur Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **iterations** (_Integer_ = None) : socket 'Iterations' (id: Iterations)
- **weight** (_Float_ = None) : socket 'Weight' (id: Weight)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### divide()

> method

``` python
divide(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### divide_ceil()

> method

``` python
divide_ceil(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE_CEIL'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### divide_floor()

> method

``` python
divide_floor(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE_FLOOR'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### divide_round()

> method

``` python
divide_round(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'DIVIDE_ROUND'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### equal()

> method

``` python
equal(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'EQUAL'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### Factor()

> classmethod

``` python
Factor(value=0, name='Factor', min=0, max=100, tip=None, panel='', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Integer factor group input

New [Integer](integer.md#integer) input with subtype 'FACTOR'.

#### Arguments:
- **value** ( = 0)
- **name** ( = Factor)
- **min** ( = 0)
- **max** ( = 100)
- **tip** ( = None)
- **panel** ( = )
- **default_attribute** ( = )
- **default_input** ( = VALUE)
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### floored_modulo()

> method

``` python
floored_modulo(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'FLOORED_MODULO'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### gcd()

> method

``` python
gcd(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'GCD'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### greater_equal()

> method

``` python
greater_equal(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_EQUAL'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### greater_than()

> method

``` python
greater_than(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'GREATER_THAN'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### hash_value()

> method

``` python
hash_value(seed=None)
```

> Node [Hash Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/hash_value.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **seed** (_Integer_ = None) : socket 'Seed' (id: Seed)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### IdOrIndex()

> classmethod

``` python
IdOrIndex(name='ID or Index', tip=None, panel='', hide_in_modifier=True)
```

> ID or Index Integer group input

New [Integer](integer.md#integer) input with 'ID or Index' as default value (default_input='ID_OR_INDEX')

> [!NOTE]
> By default, 'hide_in_modifier' is set to True

#### Arguments:
- **name** ( = ID or Index)
- **tip** ( = None)
- **panel** ( = )
- **hide_in_modifier** ( = True)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### Index()

> classmethod

``` python
Index(name='Index', tip=None, panel='', hide_in_modifier=True)
```

> Index Integer group input

New [Integer](integer.md#integer) input with Index as default value (default_input='INDEX')

> [!NOTE]
> By default, 'hide_in_modifier' is set to True

#### Arguments:
- **name** ( = Index)
- **tip** ( = None)
- **panel** ( = )
- **hide_in_modifier** ( = True)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(value=0, name=None, min=None, max=None, tip=None, panel='', subtype='NONE', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Socket of type INTEGER

> Node [Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/value.html)

If **value** argument is None:
- if **name** argument is None, a node 'Integer' is added
- otherwise a new group input is created using **min**, **max**, **tip** and **subtype**
  arguments

If **value** argument is not None, a new **Integer** is created from the value, either
by transtyping or creating a 'Value' node.

``` python
i = Integer()      # 'Integer' node with default initial vlaue
i = Integer(123). # 'Integer' node with 123 initial value
i = Integer(123, name="User input", subtype='PERCENTAGE') # Create a new integer group input
```

#### Arguments:
- **value** (_integer or Socket_ = 0) : initial value
- **name** (_str_ = None) : Create an Group Input socket with the provided str if not None
- **min** (_float_ = None) : minimum value
- **max** (_float_ = None) : maximum value
- **tip** (_str_ = None) : User tip (for Group Input sockets)
- **panel** (_str_ = ) : panel name (overrides tree panel if exists)
- **subtype** (_str in ('NONE', 'PERCENTAGE', 'FACTOR')_ = NONE) : sub type for group input
- **default_attribute** (_str_ = ) : default attribute name
- **default_input** (_str in ('VALUE', 'INDEX', 'ID_OR_INDEX')_ = VALUE) : default input
- **hide_value** (_bool_ = False) : Hide Value option
- **hide_in_modifier** (_bool_ = False) : Hide in Modifier option
- **single_value** (_bool_ = False) : Single Value option

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### lcm()

> method

``` python
lcm(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'LCM'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### less_equal()

> method

``` python
less_equal(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_EQUAL'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### less_than()

> method

``` python
less_than(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'LESS_THAN'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### max()

> method

``` python
max(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MAXIMUM'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### min()

> method

``` python
min(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MINIMUM'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### mix()

> method

``` python
mix(factor=None, other=None, clamp_factor=None)
```

> Mix

> Node [Mix](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/color/mix_rgb.html)

#### Arguments:
- **factor** (_Float_ = None) : socket 'Factor' (Factor_Float)
- **other** (_Socket_ = None) : socket 'B' (B_Float)
- **clamp_factor** (_bool_ = None) : Node.clamp_factor



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### modulo()

> method

``` python
modulo(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MODULO'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### multiply()

> method

``` python
multiply(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### multiply_add()

> method

``` python
multiply_add(multiplier=None, addend=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'MULTIPLY_ADD'



#### Arguments:
- **multiplier** (_Integer_ = None) : socket 'Multiplier' (id: Value_001)
- **addend** (_Integer_ = None) : socket 'Addend' (id: Value_002)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### Named()

> classmethod

``` python
Named(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'INT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### NamedAttribute()

> classmethod

``` python
NamedAttribute(name=None)
```

> Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html)

#### Information:
- **Parameter** : 'INT'



#### Arguments:
- **name** (_String_ = None) : socket 'Name' (id: Name)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### negate()

> method

``` python
negate()
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'NEGATE'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### not_equal()

> method

``` python
not_equal(b=None)
```

> Node [Compare](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'
- **Parameter** : 'ELEMENT'
- **Parameter** : 'NOT_EQUAL'



#### Arguments:
- **b** (_Integer_ = None) : socket 'B' (id: B_INT)



#### Returns:
- **Boolean** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### Percentage()

> classmethod

``` python
Percentage(value=0, name='Percentage', min=0, max=100, tip=None, panel='', default_attribute='', default_input='VALUE', hide_value=False, hide_in_modifier=False, single_value=False)
```

> Integer percentage group input

New [Integer](integer.md#integer) input with subtype 'PERCENTAGE'.

#### Arguments:
- **value** ( = 0)
- **name** ( = Percentage)
- **min** ( = 0)
- **max** ( = 100)
- **tip** ( = None)
- **panel** ( = )
- **default_attribute** ( = )
- **default_input** ( = VALUE)
- **hide_value** ( = False)
- **hide_in_modifier** ( = False)
- **single_value** ( = False)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### power()

> method

``` python
power(exponent=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'POWER'



#### Arguments:
- **exponent** (_Integer_ = None) : socket 'Exponent' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### sample_grid()

> method

``` python
sample_grid(position=None, interpolation_mode='TRILINEAR')
```

> Node ERROR: Node 'Sample Grid' not found

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **position** (_Vector_ = None) : socket 'Position' (id: Position)
- **interpolation_mode** (_str_ = TRILINEAR) : parameter 'interpolation_mode' in ['NEAREST', 'TRILINEAR', 'TRIQUADRATIC']



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### sample_grid_index()

> method

``` python
sample_grid_index(x=None, y=None, z=None)
```

> Node ERROR: Node 'Sample Grid Index' not found

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Arguments:
- **x** (_Integer_ = None) : socket 'X' (id: X)
- **y** (_Integer_ = None) : socket 'Y' (id: Y)
- **z** (_Integer_ = None) : socket 'Z' (id: Z)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### sign()

> method

``` python
sign()
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SIGN'



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### subtract()

> method

``` python
subtract(value=None)
```

> Node [Integer Math](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/integer_math.html)

#### Information:
- **Socket** : self
- **Parameter** : 'SUBTRACT'



#### Arguments:
- **value** (_Integer_ = None) : socket 'Value' (id: Value_001)



#### Returns:
- **Integer** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>

----------
### to_string()

> method

``` python
to_string()
```

> Node [Value to String](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html)

#### Information:
- **Socket** : self
- **Parameter** : 'INT'



#### Returns:
- **String** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Integer](integer.md#integer) :black_small_square: [Content](integer.md#content) :black_small_square: [Methods](integer.md#methods)</sub>