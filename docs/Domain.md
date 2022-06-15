
# Class Domain

Root class for domains: PointDomain, FaceDomain, EdgeDomain, CornerDomain, CurveDomain and Instance

Fields are properties of domains.

Initialization is made in method init_socket called by initializer Socket.__init__

Domains classes


Domain classes are implemented as properties of geometries:
- Mesh owns `point`, `edge`, `face` and `corner` properties (`vertex` and `face_corner`
can be used rather than `point` and `corner`)
- Curve owns `point` and `spline` (`control_point` can be used rather than `point`)
- Points owns `point`
- Instances has no domain properties, fields are direct properties of this class
  
To get the index of a point, use the syntax:

```python
position = mesh.point.position
```

Thanks to this syntax, you always know which field you want.

```python
# mesh, curve and instances are initialized respectively as Mesh, Curve ans Instances

mesh.point.position  # position of the vertices
mesg.vertex.position # same
mesh.face.position   # position of the faces
mesh.face.area       # faces area
curve.point.position # location of the curve control_points
instances.index      # Indices of the individual instances
instances.position   # Location of the instances
```



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
  
Blender menu : **input/id**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Property

### Returns

Integer



## index

> Field [Index](/docs/nodes/Index.md)
  
Blender menu : **input/input_index**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Property

### Returns

Integer



## normal

> Field [Normal](/docs/nodes/Normal.md)
  
Blender menu : **input/normal**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Property

### Returns

Vector



## position

> Field [Position](/docs/nodes/Position.md)
  
Blender menu : **input/position**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Property

### Returns

Vector



## radius

> Field [Radius](/docs/nodes/Radius.md)
  
Blender menu : **input/radius**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Property

### Returns

Float



## named_attribute

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : **input/named_attribute**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

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
  
Blender menu : **input/named_attribute**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Call [named_attribute](#named_attribute) with data_type = 'FLOAT'

### Returns

Float



## named_integer

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : **input/named_attribute**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Call [named_attribute](#named_attribute) with data_type = 'INT'
  
  

## named_vector

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : **input/named_attribute**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Call [named_attribute](#named_attribute) with data_type = 'FLOAT_VECTOR'

### Returns

Vector



## named_color

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : **input/named_attribute**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Call [named_attribute](#named_attribute) with data_type = 'FLOAT_COLOR'

### Returns

Color



## named_boolean

> Field [NamedAttribute](/docs/nodes/NamedAttribute.md)
  
Blender menu : **input/named_attribute**
<sub>go to [top](#domain) [index](/docs/index.md)</sub>

  Call [named_attribute](#named_attribute) with data_type = 'BOOLEAN'

### Returns

Boolean

