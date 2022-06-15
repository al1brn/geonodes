
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

  Property

### Returns

Integer



## index

> Field [Index](/docs/nodes/Index.md)
  
Blender menu : input/input_index

  Property

### Returns

Integer



## normal

> Field [Normal](/docs/nodes/Normal.md)
  
Blender menu : input/normal

  Property

### Returns

Vector



## position

> Field [Position](/docs/nodes/Position.md)
  
Blender menu : input/position

  Property

### Returns

Vector



## radius

> Field [Radius](/docs/nodes/Radius.md)
  
Blender menu : input/radius

  Property

### Returns

Float



## named_attribute

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : input/named_attribute

  This method is called by the following methods:
    - [named_float](#named_float)
    - [named_integer](#named_integer)
    - [named_vector](#named_vector)
    - [named_color](#named_color)
    - [named_boolean](#named_boolean)

### Returns

Linked to data_type



## named_float

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : input/named_attribute

  Call [named_attribute](#named_attribute) with data_type = 'FLOAT'

### Returns

Float



## named_integer

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : input/named_attribute

  Call [named_attribute](#named_attribute) with data_type = 'INT'
  
  

## named_vector

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : input/named_attribute

  Call [named_attribute](#named_attribute) with data_type = 'FLOAT_VECTOR'

### Returns

Vector



## named_color

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : input/named_attribute

  Call [named_attribute](#named_attribute) with data_type = 'FLOAT_COLOR'

### Returns

Color



## named_boolean

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : input/named_attribute

  Call [named_attribute](#named_attribute) with data_type = 'BOOLEAN'

### Returns

Boolean

