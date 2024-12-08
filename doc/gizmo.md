# Gizmo

> Bases classes: [Node](core-treea-node.md#node)

``` python
Gizmo(node_name, sockets={}, _items={}, link_from=None, _keep=None, **parameters)
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
 - link_with (node | dict = None) : node to link into this tree (see [link_input_from](node.md#link_input_from))
 - **kwargs : node parameters initialization

#### Arguments:
- **node_name**
- **sockets** ( = {})
- **_items** ( = {})
- **link_from** ( = None)
- **_keep** ( = None)
- **parameters**

### Inherited

[backwards](core-treea-node.md#backwards) :black_small_square: [bnode](core-treea-node.md#bnode) :black_small_square: [\_color](node.md#_color) :black_small_square: [data_socket](node.md#data_socket) :black_small_square: [dimensions](core-treea-node.md#dimensions) :black_small_square: [dump](core-treea-node.md#dump) :black_small_square: [forwards](core-treea-node.md#forwards) :black_small_square: [\_\_getattr__](groupf.md#__getattr__) :black_small_square: [\_\_getitem__](domain.md#__getitem__) :black_small_square: [\_has_items](node.md#_has_items) :black_small_square: [has_node_editor](core-treea-node.md#has_node_editor) :black_small_square: [height](core-treea-node.md#height) :black_small_square: [\_\_init__](core-treea-node.md#__init__) :black_small_square: [in_nodes](core-treea-node.md#in_nodes) :black_small_square: [inout_socket](node.md#inout_socket) :black_small_square: [InputNodeSocket](node.md#inputnodesocket) :black_small_square: [in_socket](node.md#in_socket) :black_small_square: [in_zone](core-treea-node.md#in_zone) :black_small_square: [is_child_of](core-treea-node.md#is_child_of) :black_small_square: [is_frame](core-treea-node.md#is_frame) :black_small_square: [is_layout](core-treea-node.md#is_layout) :black_small_square: [is_reroute](core-treea-node.md#is_reroute) :black_small_square: [\_items](node.md#_items) :black_small_square: [\_label](node.md#_label) :black_small_square: [link_input_from](node.md#link_input_from) :black_small_square: [\_out](node.md#_out) :black_small_square: [out_nodes](core-treea-node.md#out_nodes) :black_small_square: [out_socket](node.md#out_socket) :black_small_square: [parent](core-treea-node.md#parent) :black_small_square: [pin_gizmo](node.md#pin_gizmo) :black_small_square: [plug_selection](node.md#plug_selection) :black_small_square: [plug_value_into_socket](node.md#plug_value_into_socket) :black_small_square: [\_\_repr__](core-treea-node.md#__repr__) :black_small_square: [\_\_setattr__](node.md#__setattr__) :black_small_square: [set_input_sockets](node.md#set_input_sockets) :black_small_square: [\_\_setitem__](node.md#__setitem__) :black_small_square: [\_set_items](node.md#_set_items) :black_small_square: [set_parameters](node.md#set_parameters) :black_small_square: [socket_keys_to_identifiers](node.md#socket_keys_to_identifiers) :black_small_square: [split_peers](core-treea-node.md#split_peers) :black_small_square: [\_\_str__](core-treea-node.md#__str__) :black_small_square: [tree](core-treea-node.md#tree) :black_small_square: [wait](core-treea-node.md#wait) :black_small_square: [width](core-treea-node.md#width) :black_small_square:

## Content

- [dial](gizmo.md#dial)
- [linear](gizmo.md#linear)
- [transform](gizmo.md#transform)

## Methods



----------
### dial()

> classmethod

``` python
dial(*value, position=None, up=None, screen_space=None, radius=None, color_id='PRIMARY')
```

> Node ERROR: Node 'Dial Gizmo' not found

#### Arguments:
- **value** (_Float_) : socket 'Value' (Value)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **up** (_Vector_ = None) : socket 'Up' (Up)
- **screen_space** (_Boolean_ = None) : socket 'Screen Space' (Screen Space)
- **radius** (_Float_ = None) : socket 'Radius' (Radius)
- **color_id** (_str_ = PRIMARY) : Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Gizmo](gizmo.md#gizmo) :black_small_square: [Content](gizmo.md#content) :black_small_square: [Methods](gizmo.md#methods)</sub>

----------
### linear()

> classmethod

``` python
linear(*value, position=None, direction=None, color_id='PRIMARY', draw_style='ARROW')
```

> Node ERROR: Node 'Linear Gizmo' not found

#### Arguments:
- **value** (_Float_) : socket 'Value' (Value)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **direction** (_Vector_ = None) : socket 'Direction' (Direction)
- **color_id** (_str_ = PRIMARY) : Node.color_id in ('PRIMARY', 'SECONDARY', 'X', 'Y', 'Z')
- **draw_style** (_str_ = ARROW) : Node.draw_style in ('ARROW', 'CROSS', 'BOX')



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Gizmo](gizmo.md#gizmo) :black_small_square: [Content](gizmo.md#content) :black_small_square: [Methods](gizmo.md#methods)</sub>

----------
### transform()

> classmethod

``` python
transform(*value, position=None, rotation=None, use_rotation=True, use_scale=True, use_translation=True)
```

> Node ERROR: Node 'Transform Gizmo' not found

#### Arguments:
- **value** (_Matrix_) : socket 'Value' (Value)
- **position** (_Vector_ = None) : socket 'Position' (Position)
- **rotation** (_Rotation_ = None) : socket 'Rotation' (Rotation)
- **use_rotation** (_bool or triplet of bools_ = True) : use_rotation_x, use_rotation_y, use_rotation_z
- **use_scale** (_bool or triplet of bools_ = True) : use_scale_x, use_scale_y, use_scale_z
- **use_translation** (_bool or triplet of bools_ = True) : use_translation_x, translation_y, use_translation_z



#### Returns:
- **Geometry** :

##### <sub>:arrow_right: [geonodes](index.md#geonodes) :black_small_square: [Gizmo](gizmo.md#gizmo) :black_small_square: [Content](gizmo.md#content) :black_small_square: [Methods](gizmo.md#methods)</sub>