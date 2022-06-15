
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

<bl_idname GeometryNodeInputID>



## index

<bl_idname GeometryNodeInputIndex>



## normal

<bl_idname GeometryNodeInputNormal>



## position

<bl_idname GeometryNodeInputPosition>



## radius

<bl_idname GeometryNodeInputRadius>



## island

Mesh menu
