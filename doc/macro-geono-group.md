# Group

> Bases classes: [Node](geono-node.md#node)

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

[\_color](geono-node.md#_color) :black_small_square: [data_socket](geono-node.md#data_socket) :black_small_square: [\_\_getattr__](geono-node.md#__getattr__) :black_small_square: [\_\_getitem__](geono-node.md#__getitem__) :black_small_square: [\_has_items](geono-node.md#_has_items) :black_small_square: [inout_socket](geono-node.md#inout_socket) :black_small_square: [InputNodeSocket](geono-node.md#inputnodesocket) :black_small_square: [in_socket](geono-node.md#in_socket) :black_small_square: [\_items](geono-node.md#_items) :black_small_square: [\_label](geono-node.md#_label) :black_small_square: [\_out](geono-node.md#_out) :black_small_square: [out_socket](geono-node.md#out_socket) :black_small_square: [plug_node_into](geono-node.md#plug_node_into) :black_small_square: [plug_selection](geono-node.md#plug_selection) :black_small_square: [plug_value_into_socket](geono-node.md#plug_value_into_socket) :black_small_square: [\_\_repr__](geono-node.md#__repr__) :black_small_square: [\_\_setattr__](geono-node.md#__setattr__) :black_small_square: [set_input_sockets](geono-node.md#set_input_sockets) :black_small_square: [\_\_setitem__](geono-node.md#__setitem__) :black_small_square: [\_set_items](geono-node.md#_set_items) :black_small_square: [set_parameters](geono-node.md#set_parameters) :black_small_square: [socket_keys_to_identifiers](geono-node.md#socket_keys_to_identifiers) :black_small_square: [\_\_str__](geono-node.md#__str__) :black_small_square:

## Content

- [Prefix](macro-geono-group.md#prefix)

## Methods



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

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Group](macro-geono-group.md#group) :black_small_square: [Content](macro-geono-group.md#content) :black_small_square: [Methods](macro-geono-group.md#methods)</sub>