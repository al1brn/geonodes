# Group

> Bases classes: [Node](geono-treea-node.md#node)

``` python
Group(group_name, sockets={}, **kwargs)
```

Node Group

> Node ERROR: Node 'Group' not found

Create a node 'Group' with the tree provided with 'group_name' argument.

The sockets can be initialized either using the sockets dictionary or using they snake_case name
as kwargs arguments.

``` python
# Create a utility group
with GeoNodes("Add two values", is_group=True):

    a = Float(0, "a")
    b = Float(0, "b")

    (a + b).out("Sum")

# A node calling the utility group
with GeoNodes("Call a group"):

    Geometry().out()

    c = Group("Add two values", {'a': Float(10, 'a'), 'b': Float(10, 'b')}).sum
    node = Group("Add two values")

    node.a = 100
    node.b = 200

    c.out("c")
    node._out.out("d")
```

#### Arguments:
- **group_name** (_str_) : name of the group to use
- **sockets** (_dict_ = {}) : sockets initialization values
- **kwargs** (_dict_) : sockets  initialization with their snake_case name



#### Returns:
- **Node** : 

### Inherited

[backwards](geono-treea-node.md#backwards) :black_small_square: [bnode](geono-treea-node.md#bnode) :black_small_square: [\_color](node.md#_color) :black_small_square: [data_socket](node.md#data_socket) :black_small_square: [dimensions](geono-treea-node.md#dimensions) :black_small_square: [dump](geono-treea-node.md#dump) :black_small_square: [forwards](geono-treea-node.md#forwards) :black_small_square: [\_\_getattr__](groupf.md#__getattr__) :black_small_square: [\_\_getitem__](domain.md#__getitem__) :black_small_square: [\_has_items](node.md#_has_items) :black_small_square: [has_node_editor](geono-treea-node.md#has_node_editor) :black_small_square: [height](geono-treea-node.md#height) :black_small_square: [in_nodes](geono-treea-node.md#in_nodes) :black_small_square: [inout_socket](node.md#inout_socket) :black_small_square: [InputNodeSocket](node.md#inputnodesocket) :black_small_square: [in_socket](node.md#in_socket) :black_small_square: [in_zone](geono-treea-node.md#in_zone) :black_small_square: [is_child_of](geono-treea-node.md#is_child_of) :black_small_square: [is_frame](geono-treea-node.md#is_frame) :black_small_square: [is_layout](geono-treea-node.md#is_layout) :black_small_square: [is_reroute](geono-treea-node.md#is_reroute) :black_small_square: [\_items](node.md#_items) :black_small_square: [\_label](node.md#_label) :black_small_square: [\_out](node.md#_out) :black_small_square: [out_nodes](geono-treea-node.md#out_nodes) :black_small_square: [out_socket](node.md#out_socket) :black_small_square: [parent](geono-treea-node.md#parent) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [plug_node_into](node.md#plug_node_into) :black_small_square: [plug_selection](node.md#plug_selection) :black_small_square: [plug_value_into_socket](node.md#plug_value_into_socket) :black_small_square: [\_\_repr__](geono-treea-node.md#__repr__) :black_small_square: [\_\_setattr__](node.md#__setattr__) :black_small_square: [set_input_sockets](node.md#set_input_sockets) :black_small_square: [\_\_setitem__](node.md#__setitem__) :black_small_square: [\_set_items](node.md#_set_items) :black_small_square: [set_parameters](node.md#set_parameters) :black_small_square: [socket_keys_to_identifiers](node.md#socket_keys_to_identifiers) :black_small_square: [split_peers](geono-treea-node.md#split_peers) :black_small_square: [\_\_str__](geono-treea-node.md#__str__) :black_small_square: [tree](geono-treea-node.md#tree) :black_small_square: [wait](geono-treea-node.md#wait) :black_small_square: [width](geono-treea-node.md#width) :black_small_square:

## Content

- [\_\_init__](group.md#__init__)
- [Prefix](group.md#prefix)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(group_name, sockets={}, **kwargs)
```

Node Group

> Node ERROR: Node 'Group' not found

Create a node 'Group' with the tree provided with 'group_name' argument.

The sockets can be initialized either using the sockets dictionary or using they snake_case name
as kwargs arguments.

``` python
# Create a utility group
with GeoNodes("Add two values", is_group=True):

    a = Float(0, "a")
    b = Float(0, "b")

    (a + b).out("Sum")

# A node calling the utility group
with GeoNodes("Call a group"):

    Geometry().out()

    c = Group("Add two values", {'a': Float(10, 'a'), 'b': Float(10, 'b')}).sum
    node = Group("Add two values")

    node.a = 100
    node.b = 200

    c.out("c")
    node._out.out("d")
```

#### Arguments:
- **group_name** (_str_) : name of the group to use
- **sockets** (_dict_ = {}) : sockets initialization values
- **kwargs** (_dict_) : sockets  initialization with their snake_case name



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Group](group.md#group) :black_small_square: [Content](group.md#content) :black_small_square: [Methods](group.md#methods)</sub>

----------
### Prefix()

> classmethod

``` python
Prefix(prefix, group_name, sockets={}, **kwargs)
```

Call a Group with a prefixed named.

> Node ERROR: Node 'Group' not found

Using a prefix for groups of the same type can be usefull in big projects with
a lot of groups.

``` python
# Prefix used to identifiy utility groups
UTIL = "UTIL"

# Create a group utility
with GeoNodes("Add two values", prefix=UTIL, is_group=True):

    a = Float(0, "a")
    b = Float(0, "b")

    (a + b).out("Sum")

with GeoNodes("Call a group"):

    Geometry().out()

    # Call the the prefixed utility
    c = Group.Prefix(UTIL, "Add two values", {'a': Float(10, 'a'), 'b': Float(10, 'b')}).sum

    # Call the the prefixed utility
    node = Group.Prefix(UTIL, "Add two values")

    node.a = 100
    node.b = 200

    c.out("c")
    node._out.out("d")
```

#### Arguments:
- **prefix** (_str_) : prefix
- **group_name** (_str_) : name of the group to use
- **sockets** (_dict_ = {}) : sockets initialization values
- **kwargs** (_dict_) : sockets  initialization with their snake_case name



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Group](group.md#group) :black_small_square: [Content](group.md#content) :black_small_square: [Methods](group.md#methods)</sub>