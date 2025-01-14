# Group

``` python
Group(group_name, sockets={}, link_from=None, **kwargs)
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
- **link_from** ( = None)
- **kwargs** (_dict_) : sockets  initialization with their snake_case name



#### Returns:
- **Node** : 

### Inherited

[by_identifier](node.md#by_identifier) :black_small_square: [by_name](node.md#by_name) :black_small_square: [\_color](node.md#_color) :black_small_square: [data_socket](node.md#data_socket) :black_small_square: [\_\_getattr__](domain.md#__getattr__) :black_small_square: [\_\_getitem__](node.md#__getitem__) :black_small_square: [get_socket_names](node.md#get_socket_names) :black_small_square: [\_has_items](node.md#_has_items) :black_small_square: [identified_bsockets](node.md#identified_bsockets) :black_small_square: [InputNodeSocket](node.md#inputnodesocket) :black_small_square: [\_is_group_node](node.md#_is_group_node) :black_small_square: [\_items](node.md#_items) :black_small_square: [\_label](node.md#_label) :black_small_square: [link_from](node.md#link_from) :black_small_square: [\_out](node.md#_out) :black_small_square: [out](color.md#out) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [plug_selection](node.md#plug_selection) :black_small_square: [plug_value_into_socket](node.md#plug_value_into_socket) :black_small_square: [\_\_repr__](core-treea-node.md#__repr__) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [set_input_sockets](node.md#set_input_sockets) :black_small_square: [\_\_setitem__](node.md#__setitem__) :black_small_square: [\_set_items](node.md#_set_items) :black_small_square: [set_parameters](node.md#set_parameters) :black_small_square: [\_\_str__](core-treea-node.md#__str__) :black_small_square: [\_tree_interface](node.md#_tree_interface) :black_small_square: [valid_names](node.md#valid_names) :black_small_square:

## Content

- [\_\_init__](group.md#__init__)
- [Prefix](group.md#prefix)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(group_name, sockets={}, link_from=None, **kwargs)
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
- **link_from** ( = None)
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