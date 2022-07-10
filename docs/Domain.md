
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


## transfer_attribute

Transfer attribute

Args:
  attribute (Any): The attribute to transfer
  source_position (Vector): Source position socket
  index (Integer): Index socket
  data_type (str): A valid data type
  mapping (str): str in ('NEAREST', 'INDEX', 'NEAREST_FACE_INTERPOLATED').
  
Returns:
  As defined by data_type
  
If data_type is None, it is computed from the attribute type.

This method is called by a DataSocket with a property :attr:`field_of` pointing on the domain:

.. code-block:: python


### Domain Vertex

verts = mesh.verts


### Attribute position: position.field_of = verts

position = verts.position


### Transfer to a var

location = position.index_transfer()


### Which is equivalent to:

location = verts.index_transfer(verts.position)





## index_transfer

Transfer attribute with INDEX mapping

Args:
  attribute (Any): The attribute to transfer
  index (Integer): Index
  
Returns:
  Same as attribute
  
  

## nearest_transfer

Transfer attribute with NEAREST mapping

Args:
  attribute (Any): The attribute to transfer
  source_position (Vector): Source position socket
  
Returns:
  Same as attribute
  
  

## nearest_face_transfer

Transfer attribute with NEAREST_FACE_INTERPOLATED mapping

Args:
  attribute (Any): The attribute to transfer
  source_position (Vector): Source position socket
  
Returns:
  Same as attribute
  
  

## index

Index attribute

Returns:
  Integer
  
- setter: :class:`~geonodes.nodes.nodes.Index`
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
  
  
  