
# Class Domain

Root class for domains: Points, Faces, Edges, Corners, Curves, Instances

Fields are properties of domains.

Initialization is made in method init_socket called by initializer Socket.__init__




## init_socket

Root class for domains: Points, Faces, Edges, Corners, Curves, Instances

Fields are properties of domains.

Initialization is made in method init_socket called by initializer Socket.__init__




## create_field_node

> Create a **geonodes** from a bl_idname
  
If kwargs is an empty dict, the node is put in cache in the _fields_ dict,
otherwise it is returned directly.

### Attributes

- bl_idname : str
  A valid node bl_idname
- kwargs : dict
  Arguments to pass to initialize the node

### Returns

Node, the created node




## ID

 > Field [ID](/docs/nodes/ID.md)

Blender menu : input/id



## index

 > Field [Index](/docs/nodes/Index.md)

Blender menu : input/input_index



## normal

 > Field [Normal](/docs/nodes/Normal.md)

Blender menu : input/normal



## position

 > Field [Position](/docs/nodes/Position.md)

Blender menu : input/position



## radius

 > Field [Radius](/docs/nodes/Radius.md)

Blender menu : input/radius



## island

Mesh menu
