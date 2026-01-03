# Node

``` python
Node(node_name: str, named_sockets: dict = {}, **parameters)
```

Node wrapper.

A node can have dynamic sockets in two ways:
- _has_items : with an items collection
- _use_interface : with a NodeTree

Attributes
----------
- _tree (bpy.types.NodeTree): the tree the node belongs to
- _bnode (bpy.types.Node): the Blender wrapped Node
- _has_dyn_in (bool) : able to create dynamic input sockets
- _has_dyn_out (bool) : able to create dynamic output sockets
- _has_items (bool) : has at least one collection of dynamic items
- _items (dict['INPUT', 'OUTPUT']) : items collections or None
- _use_interface (bool) : the node dynamic sockets are managed with a NodeTree interface
- _interface (TreeInterface) : interface of the node if it exists
_ _interface_in_out (dict['INPUT', 'OUTPUT']) : in_out argument to access the Tree
- _is_paired_input (bool) : the node is the input node of a zone of paired nodes
- _is_paired_output (bool) : the node is the output node of a zone of paired nodes
- _paired_input_node (Node) : paired input node
- _paired_output_node (Node) : paired output node
- _default_menu (str | int) : specific to MenuSwitch and IndexSwitch, forward menu value
- _link_ignore : ignore these sockets in link_inputs method (already set)
- _stack : call stack for warnings

> [!NOTE]
> NodeTree interface is used for Group Input and Output nodes and for Group node.
> - Group Node : the input sockets are interface sockets for the TreeNode
> - Group Input Node : the output sockets are input sockets of the interface
> - Group Output Node : the input sockets are output sockets of the interface

> [!NOTE]
>  The '_out' property returns the first enabled output socket

#### Arguments:
- **node_name** (_str_) : Node name
- **named_sockets** (_dict_ = {}) : initialization values for the node input sockets
- **parameters** : node parameters and sockets

### Inherited

['_bnode' not found]() :black_small_square: ['_created_sockets' not found]() :black_small_square: ['_has_dyn_in' not found]() :black_small_square: ['_has_dyn_out' not found]() :black_small_square: ['_has_items' not found]() :black_small_square: ['_inputs' not found]() :black_small_square: ['_interface' not found]() :black_small_square: ['_interface_in_out' not found]() :black_small_square: ['_is_paired_input' not found]() :black_small_square: ['_is_paired_output' not found]() :black_small_square: ['_items' not found]() :black_small_square: ['_link_ignore' not found]() :black_small_square: ['_outputs' not found]() :black_small_square: ['_paired_input_node' not found]() :black_small_square: ['_paired_output_node' not found]() :black_small_square: ['_stack' not found]() :black_small_square: ['_tree' not found]() :black_small_square: ['_use_interface' not found]() :black_small_square:

## Content

- **C** : [create_from_socket](node.md#create_from_socket) :black_small_square: [create_socket](node.md#create_socket)
- **G** : [get_signature](node.md#get_signature) :black_small_square: [get_socket](node.md#get_socket) :black_small_square: [get_socket_default_name](node.md#get_socket_default_name) :black_small_square: [get_sockets](node.md#get_sockets)
- **I** : [\_\_init__](node.md#__init__)
- **L** : [\_lc](node.md#_lc) :black_small_square: [link_inputs](node.md#link_inputs) :black_small_square: [link_outputs](node.md#link_outputs)
- **M** : [method_call](node.md#method_call)
- **O** : [\_out](node.md#_out) :black_small_square: [out](node.md#out)
- **S** : [set_input_socket](node.md#set_input_socket) :black_small_square: [set_input_socket_value](node.md#set_input_socket_value) :black_small_square: [set_signature](node.md#set_signature) :black_small_square: [socket_by_index](node.md#socket_by_index) :black_small_square: [socket_by_name](node.md#socket_by_name) :black_small_square: [\_socket_created](node.md#_socket_created)

## Properties



### \_out

> _type_: **Socket**
>

Returns the first enabled output socket.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Properties](node.md#properties)</sub>

## Methods



----------
### create_from_socket()

> method

``` python
create_from_socket(in_out: Literal['INPUT', 'OUTPUT'], socket: geonodes.core.nodeclass.Socket, name: str = None, panel: str = '', **props) -> geonodes.core.nodeclass.Socket
```

Create a new socket from a socket and link them

#### Raises:
- **NodeError** : 



#### Arguments:
- **in_out** (_Literal_) : input or output socket
- **socket** (_Socket_) : socket to create from
- **name** (_str_ = None)
- **panel** (_str_ = ) : creation panel
- **props** (_dict_) : additional properties



#### Returns:
- **Socket** : the created socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### create_socket()

> method

``` python
create_socket(in_out: Literal['INPUT', 'OUTPUT'], socket_type: str | geonodes.core.sockettype.SocketType, name: str, panel: str = '', **props) -> geonodes.core.nodeclass.Socket
```

Create a new socket.

#### Raises:
- **NodeError** : 



#### Arguments:
- **in_out** (_Literal_) : input or output socket
- **socket_type** (_str | geonodes.core.sockettype.SocketType_) : type of socket to create
- **name** (_str_)
- **panel** (_str_ = ) : creation panel
- **props** (_dict_) : additional properties



#### Returns:
- **Socket** (_output_) : the created socket

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### get_signature()

> method

``` python
get_signature(include: list = None, exclude: list = [], enabled_only: bool = False, free_only: bool = False, with_sockets: bool = False) -> geonodes.core.signature.Signature
```

Build the signature of the node.

#### Arguments:
- **include** (_list_ = None) : sockets to include
- **exclude** (_list_ = []) : sockets to exclude
- **enabled_only** (_bool_ = False) : (bool = True) : ignore disabled sockets
- **free_only** (_bool_ = False) : (bool = False) : ignore linked sockets
- **with_sockets** (_bool_ = False)



#### Returns:
- **Signature** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### get_socket()

> method

``` python
get_socket(in_out: Literal['INPUT', 'OUTPUT'], name: str | int | geonodes.core.nodeclass.Socket, socket_type: str, enabled_only: bool = True, free_only: bool = False, halt: bool = True) -> geonodes.core.nodeclass.Socket
```

Get a socket by a reference

#### Arguments:
- **in_out** (_Literal_) : input or output sockets
- **name** (_str | int | geonodes.core.nodeclass.Socket_) : socket index, name, identifier or the socket itself
- **socket_type** (_str_) : socket type
- **enabled_only** (_bool_ = True) : (bool = True) : ignore disabled sockets
- **free_only** (_bool_ = False) : ignore linked sockets
- **halt** (_bool_ = True) : raises an error if not found



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### get_socket_default_name()

> method

``` python
get_socket_default_name(in_out: Literal['INPUT', 'OUTPUT'], value) -> str
```

Get the socket default name from a value

#### Arguments:
- **in_out** (_Literal_) : for input or output socket
- **value** (_Any_) : the value to name



#### Returns:
- **str**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### get_sockets()

> method

``` python
get_sockets(in_out: Literal['INPUT', 'OUTPUT'], include: list = None, exclude: list = [], enabled_only: bool = True, free_only: bool = False, panel: str = '') -> list[str, geonodes.core.nodeclass.Socket]
```

Build a list of sockets.

#### Arguments:
- **in_out** (_Literal_) : input or output sockets
- **include** (_list_ = None) : sockets to include
- **exclude** (_list_ = []) : sockets to exclude
- **enabled_only** (_bool_ = True) : (bool = True) : ignore disabled sockets
- **free_only** (_bool_ = False) : (bool = False) : ignore linked sockets
- **panel** (_str_ = )



#### Returns:
- **list** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(node_name: str, named_sockets: dict = {}, **parameters)
```

Node wrapper.

A node can have dynamic sockets in two ways:
- _has_items : with an items collection
- _use_interface : with a NodeTree

Attributes
----------
- _tree (bpy.types.NodeTree): the tree the node belongs to
- _bnode (bpy.types.Node): the Blender wrapped Node
- _has_dyn_in (bool) : able to create dynamic input sockets
- _has_dyn_out (bool) : able to create dynamic output sockets
- _has_items (bool) : has at least one collection of dynamic items
- _items (dict['INPUT', 'OUTPUT']) : items collections or None
- _use_interface (bool) : the node dynamic sockets are managed with a NodeTree interface
- _interface (TreeInterface) : interface of the node if it exists
_ _interface_in_out (dict['INPUT', 'OUTPUT']) : in_out argument to access the Tree
- _is_paired_input (bool) : the node is the input node of a zone of paired nodes
- _is_paired_output (bool) : the node is the output node of a zone of paired nodes
- _paired_input_node (Node) : paired input node
- _paired_output_node (Node) : paired output node
- _default_menu (str | int) : specific to MenuSwitch and IndexSwitch, forward menu value
- _link_ignore : ignore these sockets in link_inputs method (already set)
- _stack : call stack for warnings

> [!NOTE]
> NodeTree interface is used for Group Input and Output nodes and for Group node.
> - Group Node : the input sockets are interface sockets for the TreeNode
> - Group Input Node : the output sockets are input sockets of the interface
> - Group Output Node : the input sockets are output sockets of the interface

> [!NOTE]
>  The '_out' property returns the first enabled output socket

#### Arguments:
- **node_name** (_str_) : Node name
- **named_sockets** (_dict_ = {}) : initialization values for the node input sockets
- **parameters** : node parameters and sockets

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### \_lc()

> method

``` python
_lc(label=None, color=None)
```

Set node label and color.

This method returns self to be chained:

#### Arguments:
- **label** (_str_ = None) : node label
- **color** (_color_ = None) : node color



#### Returns:
- **self** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### link_inputs()

> method

``` python
link_inputs(from_node: geonodes.core.nodeclass.Node = None, from_panel: str = '', *, include: list = None, exclude: list = [], panel: str = '')
```

Link input socket from another node

If from_node is None, the current input node is taken.

Sockets which has been set at initialization time and sockets already linked are ignored.

If from node is able to create output sockets, they are created, otherwise only the sockets
with matchin names and types are linked.

#### Arguments:
- **from_node** (_Node_ = None) : node to get output sockets from
- **from_panel** (_str_ = ) : the panel to use in from_node
- **include** (_list_ = None) : sockets to include
- **exclude** (_list_ = []) : sockets to exclude
- **panel** (_str_ = ) : panel to select input socket in



#### Returns:
- **self** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### link_outputs()

> method

``` python
link_outputs(to_node: geonodes.core.nodeclass.Node = None, to_panel: str = '', *, include: list = None, exclude: list = [], panel: str = '')
```

Link output socket to another node

if to_node is None, the current output node is taken.

If from node is able to create output sockets, they are created, otherwise only the sockets
with matchin names and types are linked.

#### Arguments:
- **to_node** (_Node_ = None) : node to plug into
- **to_panel** (_str_ = ) : the panel to use in to_node
- **include** (_list_ = None) : sockets to include
- **exclude** (_list_ = []) : sockets to exclude
- **panel** (_str_ = ) : panel to select input socket in

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### method_call()

> method

``` python
method_call(*args, ret_class=None, **kwargs)
```

Link the input sockets with method arguments

#### Arguments:
- **args** (_tuple_) : values of the first sockets (but self_ if not None)
- **ret_class** (_type_ = None) : output class
- **kwargs** (_dict_) : named sockets



#### Returns:
- **Socket** : node._out

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### out()

> method

``` python
out(panel: str = '')
```

Plug the output sockets to the current tree output.

#### Arguments:
- **panel** (_str_ = ) : panel to use

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### set_input_socket()

> method

``` python
set_input_socket(name: str | int, value: Any, create: bool = True, panel: str = '', **props)
```

Set a value to an input socket.

If name is None (for instance when called by Socket.out()):
- The first free input socket of the proper type is chosen
- If not found, a socket is created when possible

#### Raises:
- **AttributeError** : 



#### Arguments:
- **name** (_str | int_) : socket name of socket index
- **value** (_Any_) : value to set to the socket
- **create** (_bool_ = True) : create the value (only for node with dynamic input sockets)
- **panel** (_str_ = ) : creation panel
- **props** (_dict_) : additional properties (ignored)



#### Returns:
- **The** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### set_input_socket_value()

> method

``` python
set_input_socket_value(socket, value)
```

Set a value to an input socket

#### Arguments:
- **socket** (_Socket_) : the input socket
- **value** (_Any_) : the value to set



#### Returns:
- **socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### set_signature()

> method

``` python
set_signature(in_out: Literal['INPUT', 'OUTPUT', 'BOTH'], signature: geonodes.core.signature.Signature, panel: str = '')
```

Set the signature .

#### Arguments:
- **in_out** (_Literal_) : input or output sockets or both
- **signature** (_Signature_) : the signature to apply
- **panel** (_str_ = ) : the panel where to create the sockets



#### Returns:
- **dict** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### socket_by_index()

> method

``` python
socket_by_index(in_out: Literal['INPUT', 'OUTPUT'], index: int, enabled_only: bool = True) -> geonodes.core.nodeclass.Socket
```

Get a socket by its index

#### Raises:
- **IndexError** : 



#### Arguments:
- **in_out** (_Literal_) : input or output sockets
- **index** (_int_) : socket index
- **enabled_only** (_bool_ = True) : (bool = True) : ignore disabled sockets



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### socket_by_name()

> method

``` python
socket_by_name(in_out: Literal['INPUT', 'OUTPUT'], name: str, socket_type: str, enabled_only: bool = True, free_only: bool = False, halt: bool = True) -> geonodes.core.nodeclass.Socket
```

Get a socket by its name

Get a socket by its name. Valid names are:
- The socket name possibly suffixed by its rank (e.g. `value_1` for second socket named Value)
- The python version

#### Raises:
- **AttributeError** : 



#### Arguments:
- **in_out** (_Literal_) : input or output sockets
- **name** (_str_) : socket name
- **socket_type** (_str_) : socket_type
- **enabled_only** (_bool_ = True) : (bool = True) : ignore disabled sockets
- **free_only** (_bool_ = False) : ignore linked sockets
- **halt** (_bool_ = True) : raises an error if not found



#### Returns:
- **Socket** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### \_socket_created()

> method

``` python
_socket_created(socket)
```

Socket creation call back

#### Arguments:
- **socket**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>