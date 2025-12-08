# Group

``` python
Group(group_name: str, named_sockets: dict = {}, **sockets)
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
- **named_sockets** (_dict_ = {}) : sockets initialization values
- **sockets** (_dict_) : sockets  initialization with their snake_case name



#### Returns:
- **Node** : 

### Inherited

['_bnode' not found]() :black_small_square: [\_class_test](boolean.md#_class_test) :black_small_square: [\_color](node.md#_color) :black_small_square: [create_from_socket](node.md#create_from_socket) :black_small_square: [create_socket](node.md#create_socket) :black_small_square: [\_\_enter__](layout.md#__enter__) :black_small_square: [\_\_exit__](layout.md#__exit__) :black_small_square: [\_\_getattr__](g.md#__getattr__) :black_small_square: [\_get_interface_socket](node.md#_get_interface_socket) :black_small_square: [\_\_getitem__](node.md#__getitem__) :black_small_square: [get_signature](bundle.md#get_signature) :black_small_square: [get_socket](node.md#get_socket) :black_small_square: [get_sockets](node.md#get_sockets) :black_small_square: ['_has_dyn_in' not found]() :black_small_square: ['_has_dyn_out' not found]() :black_small_square: ['_has_items' not found]() :black_small_square: ['_inputs' not found]() :black_small_square: ['_interface' not found]() :black_small_square: ['_interface_in_out' not found]() :black_small_square: ['_is_paired_input' not found]() :black_small_square: ['_is_paired_output' not found]() :black_small_square: ['_items' not found]() :black_small_square: [\_label](node.md#_label) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [link_outputs](node.md#link_outputs) :black_small_square: [\_out](node.md#_out) :black_small_square: [out](color.md#out) :black_small_square: ['_outputs' not found]() :black_small_square: ['_paired_input_node' not found]() :black_small_square: ['_paired_output_node' not found]() :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [\_pop](node.md#_pop) :black_small_square: [\_push](node.md#_push) :black_small_square: [\_\_repr__](core-treea-node.md#__repr__) :black_small_square: [\_\_setattr__](domain.md#__setattr__) :black_small_square: [set_input_socket](node.md#set_input_socket) :black_small_square: [\_\_setitem__](node.md#__setitem__) :black_small_square: [set_parameters](node.md#set_parameters) :black_small_square: [set_signature](node.md#set_signature) :black_small_square: [socket_by_identifier](node.md#socket_by_identifier) :black_small_square: [socket_by_index](node.md#socket_by_index) :black_small_square: [socket_by_name](node.md#socket_by_name) :black_small_square: [\_\_str__](core-treea-node.md#__str__) :black_small_square: ['_tree' not found]() :black_small_square: [\_update](node.md#_update) :black_small_square: ['_use_interface' not found]() :black_small_square:

## Content

- [\_\_init__](group.md#__init__)
- [Prefix](group.md#prefix)

## Methods



----------
### \_\_init__()

> method

``` python
__init__(group_name: str, named_sockets: dict = {}, **sockets)
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
- **named_sockets** (_dict_ = {}) : sockets initialization values
- **sockets** (_dict_) : sockets  initialization with their snake_case name



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Group](group.md#group) :black_small_square: [Content](group.md#content) :black_small_square: [Methods](group.md#methods)</sub>

----------
### Prefix()

> classmethod

``` python
Prefix(prefix, group_name, named_sockets={}, **sockets)
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
- **named_sockets** ( = {})
- **sockets** (_dict_) : sockets initialization values



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Group](group.md#group) :black_small_square: [Content](group.md#content) :black_small_square: [Methods](group.md#methods)</sub>