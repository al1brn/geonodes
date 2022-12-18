
# Class Domain

Root class for domains

Args:
  data_socket (DataSocket): The geometry the domain belongs to
  domain (str): Domain in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
  selection (Boolean): selection input socket
  
  
Components and domains:
- Mesh component
- verts   : Vertex
- edges   : Edge
- faces   : Face
- corners : Corner
  
- Curve component
- points  : ControlPoint
- splines : Spline
  
- Points
- points   : CloudPoint
  
- Instances components
- insts : Instance
  
  
  
  

## \_\_init\_\_

Root class for domains

Args:
  data_socket (DataSocket): The geometry the domain belongs to
  domain (str): Domain in ['POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE']
  selection (Boolean): selection input socket
  
  
Components and domains:
- Mesh component
- verts   : Vertex
- edges   : Edge
- faces   : Face
- corners : Corner
  
- Curve component
- points  : ControlPoint
- splines : Spline
  
- Points
- points   : CloudPoint
  
- Instances components
- insts : Instance
  
  
  
  

## select

Select the domain

Args:
  selection (Boolean): The selection condition
  
If a selection is existing, the resulting selection is a logical and betwenn the two




## stack

Make the owning socket jump to the output socket of the node passed in argumment.

Args:
  node (Node): The node to jump to
  
  

## \_\_getitem\_\_

Access by index


## view

To viewer.

Args:
  socket (DataSocket): The value to view        
  
  

## as_verts

Type cast to Vertex.


## as_edges

Type cast to Edge.


## as_faces

Type cast to Face.


## as_corners

Type cast to Corner.


## as_control_points

Type cast to ControlPoint.


## as_splines

Type cast to Spline.


## as_cloud_points

Type cast to CloudPoint.


## as_insts

Type cast to Instance.


## statistic

Attribute statistic

call :class:`~geonodes.nodes.nodes.AttributeStatistic`




## count

Count the number of items by return static.max + 1

Returns:
  Integer
  
getter: :class:`AttributeStatistic`
setter: read only




## attribute

Define an input node as attribute

Args:
  node (Node): The node created by the domain
  
Returns:
  The node argument
  
Called when creating an input node in a property getter. Performs two actions:

- Call the method :func:`Node.as_attribute` to tag the node as being an attribute.
  This will allow the :func:`Tree.check_attributes` to see if it is necessary to create
  a *Capture Attribute* for this field.
- Set the nde property :attr:`field_of` to self in order to implement the transfer attribute
  mechanism.
  
  
  

## get_named_attribute

Get a named attribute

Called by methods set_named_xxx:

- :func:`get_named_boolean`
- :func:`get_named_integer`
- :func:`get_named_float`
- :func:`get_named_vector`
- :func:`get_named_color`
  
  
  

## set_named_attribute

Set a named attribute

Called by classes set_named_xxx:

- :func:`set_named_boolean`
- :func:`set_named_integer`
- :func:`set_named_float`
- :func:`set_named_vector`
- :func:`set_named_color`
- :func:`set_named_byte_color`
  
  
  

## get_named_boolean

Get named attribute of type BOOLEAN


## get_named_integer

Get named attribute of type INT


## get_named_float

Get named attribute of type FLOAT


## get_named_vector

Get named attribute of type FLOAT_VECTOR


## get_named_color

Get named attribute of type FLOAT_COLOR


## set_named_boolean

Set named attribute of type BOOLEAN


## set_named_integer

Set named attribute of type INT


## set_named_float

Set named attribute of type FLOAT


## set_named_vector

Set named attribute of type FLOAT_VECTOR


## set_named_color

Set named attribute of type FLOAT_COLOR


## set_named_byte_color

Set named attribute of type BYTE_COLOR


## interpolate

Interpolate attribute

Args:
  value (Any): The value to interpolate
  data_type (str): A valid data type
  
Returns:
  As defined by data_type
  
If data_type is None, it is computed from the value type.




## domain_index

Index attribute

Returns:
  Integer
  
- getter: :class:`~geonodes.nodes.nodes.Index`
- setter: Read only
  
  
  

## index

Index attribute

Returns:
  Integer
  
- getter: :class:`~geonodes.nodes.nodes.Index`
- setter: Read only
  
  
  

## position

When implemented +=, __iadd__ returns None


## offset

No setter


## duplicate

Duplicate domain.

Node :class:`~geonodes.nodes.nodes.DuplicateElements`

Args:
  amount : Integer
  
Returns:
  duplicate index
  
  
  

## \_\_imul\_\_

ef __mul__(self, other):
self.duplicate(amount=other)
return self

ef __rmul__(self, other):
return self * other


## field_at_index

Field at index

Args:
  index (Integer): index to use for getting the attributes
  value (Any): the value to collect from the domain
  data_type (str): the value data_type. Can be None
  
Returns:
  The field values
  
If data_type is None, it is computed from the attribute type.




## sample_index

Sample index

Similar to field_at_index but the geometry is used as input

Args:
  index (Integer): index to use for getting the attributes
  value (Any): the value to collect from the domain
  data_type (str): the value data_type. Can be None
  
Returns:
  The field values
  
If data_type is None, it is computed from the attribute type.




## sample_nearest

Sample nearest

Args:
  sample_position (Vector): sample position
  
Returns:
  index
  
  
  