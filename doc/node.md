# Node

``` python
Node(node_name, sockets={}, _items={}, link_from=None, **parameters)
```

Node wrapper.

 The node wrapper exposes input and output sockets and the node parameters.
 At creation time, input sockets are initialized with a dict using their name as key ;
 parameters are initialized as keyword arguments:

 > [!NOTE]
 > The most often, the name of the socket can be used as key in the initialization dict.
 > But in some cases, this doesn't apply:
 > - Several sockets can share the same names (example: 'Math' node has two 'Value' input socket)
 > - Display name is different from the python name (example: 'Math' node, operation 'COMPARE', actual name
 >   of 'Epsilon' socket is 'Value')

 In order to to handle these specific cases, the dict keys can be:
 - The index of the socket in the list
 - The 'identifier' of the socket

 When the sockets are initialized in there order, the values can be passed
 as a list rather than as a dict.

 ``` python
 with GeoNodes("Node initialization"):

     # Dict syntax to create a circle
     node = Node("Mesh Circle", {'Vertices': 32, 'Radius': 1.}, fill_type='NGON')

     # Dict syntax using the socket identifier as key on a node with homonym sockets
     node = Node("Math", {'Value': 2, 'Value_001': 2}, operation='ADD')

     # Dict key words can be socket index
     node = Node("Math", {0: 2, 1: 2}, operation='ADD')

     # A list of values can be used to initialize the sockets in the order they appear
     # Epsilon is initialized to .1
     node = Node("Math", [2., 2., .1], operation='COMPARE')
 ```

 Once initialized, the sockets can be accessed either as list items keyed by the sockets name,
 index or identifier or as node attribute using their snake case name.

 > [!IMPORTANT]
 > Setting and getting a socket:
 > - **Setting** a node socket is interpretated as plugging a value into an **input socket**
 > - **Getting** a node socket is interpretated as getting an **output socket**

 ``` python
 with GeoNodes("Getting and setting node sockets"):

     # Input geometry socket
     geo = Geometry()

     # Create the node
     node = Node("Extrude Mesh")

     # Change the parameter
     node.mode = 'EDGES'

     # Plug 'Geometry' socket with list item syntax
     node["Mesh"] = geo

     # Plug 'Selection' socket with ordered list syntax
     node["Selection"] = Boolean(True)

     # Plug 'Offset Scale' with snake case syntax
     node.offset_scale = 0.5

     # Read the output geometry : snake case syntax
     extruded_geo = node.mesh

     # Read the top selection : list syntax
     top_selection = node["Top"]

     # Read the side selection : index list syntax
     side_selection = node[2]

     # Use the sockets in another node
     top_selection |= side_selection

     # Connect to the group output geometry
     extruded_geo.out()
 ```

 > [!NOTE]
>  The '_out' property returns the first enabled output socket

 Arguments
 ---------
 - node_name (str) : Node name
 - sockets (dict or list) : initialization values for the node input sockets
 - _items (dict = {}) : dynamic sockets to create
 - link_with (node | dict = None) : node to link into this tree (see [link_from](node.md#link_from))
 - **kwargs : node parameters initialization

#### Arguments:
- **node_name**
- **sockets** ( = {})
- **_items** ( = {})
- **link_from** ( = None)
- **parameters**

## Content

- [by_name](node.md#by_name)
- [get_socket_names](node.md#get_socket_names)
- [identified_bsockets](node.md#identified_bsockets)
- [\_\_init__](node.md#__init__)
- [link_from](node.md#link_from)
- [\_out](node.md#_out)

## Properties



### \_out

> _type_: **Socket**
>

Returns the first enabled output socket.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Properties](node.md#properties)</sub>

## Methods



----------
### by_name()

> method

``` python
by_name(in_out, name, only_enabled=True, as_argument=True, candidates=False, halt=True)
```

Get a socket by its name

#### Arguments:
- **in_out** (_str_) : str in ('INPUT', 'OUTPUT')
- **name** (_str_) : searched named
- **only_enabled** (_bool_ = True) : consider only enabled sockets
- **as_argument** (_bool_ = True) : the name is argument or socket name
- **candidates** (_bool_ = False) : return all matching names (True) or the first one (False)
- **halt** (_bool_ = True) : raises an error if not found



#### Returns:
- **Node** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### get_socket_names()

> method

``` python
get_socket_names(in_out, only_enabled=True, as_argument=True)
```

Build a dictionary keyed by the socket unique names

The possible names are:
- socket name
- snake case version of the name

These names are combined with the panel name:
- panel name.socket name
- snake case version of this path

Once built, the homonyms are made unique by suffixing its order

#### Arguments:
- **in_out** : str in ('INPUT', 'OUTPUT')
- **only_enabled** ( = True) : use only enabled sockets
- **as_argument** ( = True)



#### Returns:
- **dict** : socket identifier -> list of possible names

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### identified_bsockets()

> method

``` python
identified_bsockets(in_out, names=None)
```

Returns a list of socket identifiers from names

Names can be a list of socket names, arguments or identifiers
if names is None, returns all the sockets

It can also contain panel name. In that case, it includes all the socket
within the panel.

#### Arguments:
- **in_out** (_str_) : str in ('INPUT', 'OUTPUT')
- **names** (_list of strs_ = None) : the names to convert

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### \_\_init__()

> method

``` python
__init__(node_name, sockets={}, _items={}, link_from=None, **parameters)
```

Node wrapper.

 The node wrapper exposes input and output sockets and the node parameters.
 At creation time, input sockets are initialized with a dict using their name as key ;
 parameters are initialized as keyword arguments:

 > [!NOTE]
 > The most often, the name of the socket can be used as key in the initialization dict.
 > But in some cases, this doesn't apply:
 > - Several sockets can share the same names (example: 'Math' node has two 'Value' input socket)
 > - Display name is different from the python name (example: 'Math' node, operation 'COMPARE', actual name
 >   of 'Epsilon' socket is 'Value')

 In order to to handle these specific cases, the dict keys can be:
 - The index of the socket in the list
 - The 'identifier' of the socket

 When the sockets are initialized in there order, the values can be passed
 as a list rather than as a dict.

 ``` python
 with GeoNodes("Node initialization"):

     # Dict syntax to create a circle
     node = Node("Mesh Circle", {'Vertices': 32, 'Radius': 1.}, fill_type='NGON')

     # Dict syntax using the socket identifier as key on a node with homonym sockets
     node = Node("Math", {'Value': 2, 'Value_001': 2}, operation='ADD')

     # Dict key words can be socket index
     node = Node("Math", {0: 2, 1: 2}, operation='ADD')

     # A list of values can be used to initialize the sockets in the order they appear
     # Epsilon is initialized to .1
     node = Node("Math", [2., 2., .1], operation='COMPARE')
 ```

 Once initialized, the sockets can be accessed either as list items keyed by the sockets name,
 index or identifier or as node attribute using their snake case name.

 > [!IMPORTANT]
 > Setting and getting a socket:
 > - **Setting** a node socket is interpretated as plugging a value into an **input socket**
 > - **Getting** a node socket is interpretated as getting an **output socket**

 ``` python
 with GeoNodes("Getting and setting node sockets"):

     # Input geometry socket
     geo = Geometry()

     # Create the node
     node = Node("Extrude Mesh")

     # Change the parameter
     node.mode = 'EDGES'

     # Plug 'Geometry' socket with list item syntax
     node["Mesh"] = geo

     # Plug 'Selection' socket with ordered list syntax
     node["Selection"] = Boolean(True)

     # Plug 'Offset Scale' with snake case syntax
     node.offset_scale = 0.5

     # Read the output geometry : snake case syntax
     extruded_geo = node.mesh

     # Read the top selection : list syntax
     top_selection = node["Top"]

     # Read the side selection : index list syntax
     side_selection = node[2]

     # Use the sockets in another node
     top_selection |= side_selection

     # Connect to the group output geometry
     extruded_geo.out()
 ```

 > [!NOTE]
>  The '_out' property returns the first enabled output socket

 Arguments
 ---------
 - node_name (str) : Node name
 - sockets (dict or list) : initialization values for the node input sockets
 - _items (dict = {}) : dynamic sockets to create
 - link_with (node | dict = None) : node to link into this tree (see [link_from](node.md#link_from))
 - **kwargs : node parameters initialization

#### Arguments:
- **node_name**
- **sockets** ( = {})
- **_items** ( = {})
- **link_from** ( = None)
- **parameters**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### link_from()

> method

``` python
link_from(node: 'Node | Tree | None | str' = 'TREE', include: list[str] | str | None = None, exclude: list[str] | str = [], arguments: dict[slice('name', 'value', None)] = {}, create: bool = True, panel: str | None = None)
```

Plug the output sockets of a node into the input sockets of the node.

This method is used to connect several sockets in a compact syntax.

If the node argument is None, the sockets are created in the Group Input node.
Use 'include', 'exclude' and 'rename' arguments to control the connexions.

> [!NOTE]
> This function is called when initializing a node if the `link_from` argument is not None.
> In that case, `link_argument` value is either the `node` argument or a dictionnary
> of the `link_from` method arguments:

``` python
with GeoNodes("Connect several sockets"):

    # Node with 'Value' output socket
    a = Node("Grid")

    # Create Group inputs to feed the node
    # 'Size X' and 'Size Y' are created in the group input not
    # 'Vertices X' and 'Vertices Y' are connected to the same 'Vertices' which is created
    a.link_from(rename={'Vertices X': 'Vertices', 'Vertices Y': 'Vertices'})

    a = Node("Math")

    # Connect the 'Value' output socket to the 'Value' input socket
    # The third socket is exclude by its index
    # Input values are renamed 'First' and 'Second'
    a.link_from(exclude=2, rename={'Value': 'First', 'Value_001': 'Second'})

    b = Node("Math", operation='SQRT')

    # Plug the previous math node on a single socket
    b.link_from(a, include='Value')

# Call this method when creating a group
# Note: the previous Group is called using functional syntax with G class

with GeoNodes("Create default"):

    # Create the sockets in the input and connect them to Group input

    a = G.connect_several_sockets(link_from='TREE')

with GeoNodes("Create selection"):

    # Create the sockets in the input and connect them to Group input

    a = G.connect_several_sockets(link_from={'exclude': ["Size X", "Size Y"], 'rename': {"Vertices": "Count"}})
```

#### Arguments:
- **node** (_Node | Tree | None | str_ = TREE) : the node to get the outputs from. Use Group Input node if None
- **include** (_list[str] | str | None_ = None) : connects only the sockets in the list
- **exclude** (_list[str] | str_ = []) : exclude sockets in this list
- **arguments** (_dict_ = {}) : arguments used at initialization time. Arguments which are defined in the list are ignored
- **create** (_bool_ = True) : create the output sockets in node if it is a 'Group Input Node'
- **panel** (_str | None_ = None) : panel name to create, use tree default name if None



#### Returns:
- **Node** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>