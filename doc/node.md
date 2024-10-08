# Node

``` python
Node(node_name, sockets={}, _items={}, _keep=None, **parameters)
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
 - **kwargs : node parameters initialization

#### Arguments:
- **node_name**
- **sockets** ( = {})
- **_items** ( = {})
- **_keep** ( = None)
- **parameters**

## Content

- [\_\_init__](node.md#__init__)
- [\_out](node.md#_out)
- [plug_node_into](node.md#plug_node_into)

## Properties



### \_out

> _type_: **Socket**
>

Returns the first enabled output socket.

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Properties](node.md#properties)</sub>

## Methods



----------
### \_\_init__()

> method

``` python
__init__(node_name, sockets={}, _items={}, _keep=None, **parameters)
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
 - **kwargs : node parameters initialization

#### Arguments:
- **node_name**
- **sockets** ( = {})
- **_items** ( = {})
- **_keep** ( = None)
- **parameters**

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>

----------
### plug_node_into()

> method

``` python
plug_node_into(node=None, include=None, exclude=[], rename={}, create=True)
```

Plug the output sockets of a node into the input sockets of the node.

This method is used to connect several sockets in a compact syntax.

If the node argument is None, the sockets are created in the Group Input node.
Use 'include', 'exclude' and 'rename' arguments to control the connexions.

``` python
with GeoNodes("Connect several sockets"):

    # Node with 'Value' output socket
    a = Node("Grid")

    # Create Group inputs to feed the node
    # 'Size X' and 'Size Y' are created in the group input not
    # 'Vertices X' and 'Vertices Y' are connected to the same 'Vertices' which is created
    a.plug_node_into(rename={'Vertices X': 'Vertices', 'Vertices Y': 'Vertices'})

    a = Node("Math")

    # Connect the 'Value' output socket to the 'Value' input socket
    # The third socket is exclude by its index
    # Input values are renamed 'First' and 'Second'
    a.plug_node_into(exclude=2, rename={'Value': 'First', 'Value_001': 'Second'})

    b = Node("Math", operation='SQRT')

    # Plug the previous math node on a single socket
    b.plug_node_into(a, include='Value')
```

#### Arguments:
- **node** (_Node_ = None) : the node to get the outputs from. Use Group Input node if None
- **include** (_list of strs_ = None) : connects only the sockets in the list
- **exclude** (_list of strs_ = []) : exclude sockets in this list
- **rename** (_dict_ = {}) : rename the sockets to the given names
- **create** ( = True)



#### Returns:
- **Node** : self

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Node](node.md#node) :black_small_square: [Content](node.md#content) :black_small_square: [Methods](node.md#methods)</sub>