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

[by_identifier](node.md#by_identifier) :black_small_square: [by_name](node.md#by_name) :black_small_square: [\_color](node.md#_color) :black_small_square: [data_socket](node.md#data_socket) :black_small_square: [get](node.md#get) :black_small_square: [\_\_getattr__](domain.md#__getattr__) :black_small_square: [\_\_getitem__](node.md#__getitem__) :black_small_square: [get_socket_names](node.md#get_socket_names) :black_small_square: [\_has_items](node.md#_has_items) :black_small_square: [identified_bsockets](node.md#identified_bsockets) :black_small_square: [InputNodeSocket](node.md#inputnodesocket) :black_small_square: [\_is_group_node](node.md#_is_group_node) :black_small_square: [\_items](node.md#_items) :black_small_square: [\_label](node.md#_label) :black_small_square: [link_from](node.md#link_from) :black_small_square: [\_out](node.md#_out) :black_small_square: [out](color.md#out) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [plug_selection](node.md#plug_selection) :black_small_square: [plug_value_into_socket](node.md#plug_value_into_socket) :black_small_square: [\_\_repr__](core-treea-node.md#__repr__) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [set_input_sockets](node.md#set_input_sockets) :black_small_square: [\_\_setitem__](node.md#__setitem__) :black_small_square: [\_set_items](node.md#_set_items) :black_small_square: [set_parameters](node.md#set_parameters) :black_small_square: [\_\_str__](core-treea-node.md#__str__) :black_small_square: [\_tree_interface](node.md#_tree_interface) :black_small_square: [valid_names](node.md#valid_names) :black_small_square:

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