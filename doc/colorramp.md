# ColorRamp

``` python
ColorRamp(fac=None, stops=None, interpolation='LINEAR')
```

Node [Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

Exposes utilities to manage the color ramp

``` python
ramp1 = Float(.5).color_ramp(stops=[.1, .9])
ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
```

#### Arguments:
- **fac** (_Float_ = None)
- **stops** (_list of tuple(float, tuple)_ = None) : stops made of (float, color as tuple of floats)
- **interpolation** (_'EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT'_ = LINEAR)

### Inherited

['_bnode' not found]() :black_small_square: [\_class_test](boolean.md#_class_test) :black_small_square: [\_color](node.md#_color) :black_small_square: ['_created_sockets' not found]() :black_small_square: [create_from_socket](node.md#create_from_socket) :black_small_square: [create_socket](node.md#create_socket) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_interface_socket](node.md#_get_interface_socket) :black_small_square: [\_\_getitem__](node.md#__getitem__) :black_small_square: [get_signature](bundle.md#get_signature) :black_small_square: [get_socket](node.md#get_socket) :black_small_square: [get_socket_default_name](node.md#get_socket_default_name) :black_small_square: [get_sockets](node.md#get_sockets) :black_small_square: ['_has_dyn_in' not found]() :black_small_square: ['_has_dyn_out' not found]() :black_small_square: ['_has_items' not found]() :black_small_square: ['_inputs' not found]() :black_small_square: ['_interface' not found]() :black_small_square: ['_interface_in_out' not found]() :black_small_square: ['_is_paired_input' not found]() :black_small_square: ['_is_paired_output' not found]() :black_small_square: ['_items' not found]() :black_small_square: [\_label](node.md#_label) :black_small_square: [\_lc](node.md#_lc) :black_small_square: ['_link_ignore' not found]() :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [link_outputs](node.md#link_outputs) :black_small_square: [method_call](node.md#method_call) :black_small_square: [\_out](node.md#_out) :black_small_square: [out](color.md#out) :black_small_square: ['_outputs' not found]() :black_small_square: ['_paired_input_node' not found]() :black_small_square: ['_paired_output_node' not found]() :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](closure.md#_pop) :black_small_square: [\_push](closure.md#_push) :black_small_square: [\_\_repr__](core-treea-node.md#__repr__) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [set_input_socket](node.md#set_input_socket) :black_small_square: [set_input_socket_value](node.md#set_input_socket_value) :black_small_square: [\_\_setitem__](node.md#__setitem__) :black_small_square: [set_parameters](node.md#set_parameters) :black_small_square: [set_signature](node.md#set_signature) :black_small_square: [socket_by_identifier](node.md#socket_by_identifier) :black_small_square: [socket_by_index](node.md#socket_by_index) :black_small_square: [socket_by_name](node.md#socket_by_name) :black_small_square: [\_socket_created](node.md#_socket_created) :black_small_square: ['_stack' not found]() :black_small_square: [\_\_str__](core-treea-node.md#__str__) :black_small_square: ['_tree' not found]() :black_small_square: ['_use_interface' not found]() :black_small_square:

## Content

- [color_ramp](colorramp.md#color_ramp)
- [\_\_init__](colorramp.md#__init__)
- [interpolation](colorramp.md#interpolation)
- [stops](colorramp.md#stops)

## Properties



### color_ramp

> _type_: **bpy**
>

Returns the node color_ramp structure

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ColorRamp](colorramp.md#colorramp) :black_small_square: [Content](colorramp.md#content) :black_small_square: [Properties](colorramp.md#properties)</sub>

### interpolation

> _type_: **str**
>

Node color_ramp interpolation

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ColorRamp](colorramp.md#colorramp) :black_small_square: [Content](colorramp.md#content) :black_small_square: [Properties](colorramp.md#properties)</sub>

### stops

> _type_: **list**
>

Get the list of stops

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ColorRamp](colorramp.md#colorramp) :black_small_square: [Content](colorramp.md#content) :black_small_square: [Properties](colorramp.md#properties)</sub>

## Methods



----------
### \_\_init__()

> method

``` python
__init__(fac=None, stops=None, interpolation='LINEAR')
```

Node [Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

Exposes utilities to manage the color ramp

``` python
ramp1 = Float(.5).color_ramp(stops=[.1, .9])
ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
```

#### Arguments:
- **fac** (_Float_ = None)
- **stops** (_list of tuple(float, tuple)_ = None) : stops made of (float, color as tuple of floats)
- **interpolation** (_'EASE', 'CARDINAL', 'LINEAR', 'B_SPLINE', 'CONSTANT'_ = LINEAR)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ColorRamp](colorramp.md#colorramp) :black_small_square: [Content](colorramp.md#content) :black_small_square: [Methods](colorramp.md#methods)</sub>