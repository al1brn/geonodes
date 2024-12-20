# ColorRamp

> Bases classes: [Node](core-treea-node.md#node)

``` python
ColorRamp(fac=None, stops=None)
```

Color ramp node

> Node [Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

Exposes utilities to manage the color ramp

``` python
ramp1 = Float(.5).color_ramp(stops=[.1, .9])
ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
```

#### Arguments:
- **fac** (_Float_ = None)
- **stops** (_list of tuple(float, tuple)_ = None) : stops made of (float, color as tuple of floats)

### Inherited

[backwards](core-treea-node.md#backwards) :black_small_square: [bnode](core-treea-node.md#bnode) :black_small_square: [\_color](node.md#_color) :black_small_square: [data_socket](node.md#data_socket) :black_small_square: [dimensions](core-treea-node.md#dimensions) :black_small_square: [dump](core-treea-node.md#dump) :black_small_square: [forwards](core-treea-node.md#forwards) :black_small_square: [\_\_getattr__](groupf.md#__getattr__) :black_small_square: [\_\_getitem__](domain.md#__getitem__) :black_small_square: [\_has_items](node.md#_has_items) :black_small_square: [has_node_editor](core-treea-node.md#has_node_editor) :black_small_square: [height](core-treea-node.md#height) :black_small_square: [in_nodes](core-treea-node.md#in_nodes) :black_small_square: [inout_socket](node.md#inout_socket) :black_small_square: [InputNodeSocket](node.md#inputnodesocket) :black_small_square: [in_socket](node.md#in_socket) :black_small_square: [in_zone](core-treea-node.md#in_zone) :black_small_square: [is_child_of](core-treea-node.md#is_child_of) :black_small_square: [is_frame](core-treea-node.md#is_frame) :black_small_square: [is_layout](core-treea-node.md#is_layout) :black_small_square: [is_reroute](core-treea-node.md#is_reroute) :black_small_square: [\_items](node.md#_items) :black_small_square: [\_label](node.md#_label) :black_small_square: [link_input_from](node.md#link_input_from) :black_small_square: [\_out](node.md#_out) :black_small_square: [out_nodes](core-treea-node.md#out_nodes) :black_small_square: [out_socket](node.md#out_socket) :black_small_square: [parent](core-treea-node.md#parent) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [plug_selection](node.md#plug_selection) :black_small_square: [plug_value_into_socket](node.md#plug_value_into_socket) :black_small_square: [\_\_repr__](core-treea-node.md#__repr__) :black_small_square: [\_\_setattr__](node.md#__setattr__) :black_small_square: [set_input_sockets](node.md#set_input_sockets) :black_small_square: [\_\_setitem__](node.md#__setitem__) :black_small_square: [\_set_items](node.md#_set_items) :black_small_square: [set_parameters](node.md#set_parameters) :black_small_square: [socket_keys_to_identifiers](node.md#socket_keys_to_identifiers) :black_small_square: [split_peers](core-treea-node.md#split_peers) :black_small_square: [\_\_str__](core-treea-node.md#__str__) :black_small_square: [tree](core-treea-node.md#tree) :black_small_square: [wait](core-treea-node.md#wait) :black_small_square: [width](core-treea-node.md#width) :black_small_square:

## Content

- [color_ramp](colorramp.md#color_ramp)
- [\_\_init__](colorramp.md#__init__)
- [set_stops](colorramp.md#set_stops)

## Properties



### color_ramp

> _type_: **bpy**
>

Returns the node color_ramp structure

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ColorRamp](colorramp.md#colorramp) :black_small_square: [Content](colorramp.md#content) :black_small_square: [Properties](colorramp.md#properties)</sub>

## Methods



----------
### \_\_init__()

> method

``` python
__init__(fac=None, stops=None)
```

Color ramp node

> Node [Color Ramp](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/../../editors/texture_node/types/converter/color_ramp.html)

Exposes utilities to manage the color ramp

``` python
ramp1 = Float(.5).color_ramp(stops=[.1, .9])
ramp2 = ColorRamp(.5, stops=[(.1, (1, 0, 0)), (.5, 1), (.9, (0, 0, 1))])
```

#### Arguments:
- **fac** (_Float_ = None)
- **stops** (_list of tuple(float, tuple)_ = None) : stops made of (float, color as tuple of floats)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ColorRamp](colorramp.md#colorramp) :black_small_square: [Content](colorramp.md#content) :black_small_square: [Methods](colorramp.md#methods)</sub>

----------
### set_stops()

> method

``` python
set_stops(*stops)
```

Set the color ramp stops

``` python
ramp =

#### Arguments:
- **stops** : list of tuple (position, color)

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [ColorRamp](colorramp.md#colorramp) :black_small_square: [Content](colorramp.md#content) :black_small_square: [Methods](colorramp.md#methods)</sub>