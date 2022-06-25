
# Class Domain

Root class for domains

Fields are properties of domains.

Components and domains


- Mesh component
- Point   : point (or points, verts)
- Edge    : edge  (or edges)
- Face    : face  (or faces)
- Corner  : face_corner (or corner or corners)
- Curve component
- Point   : point (or points)
- Spline  : spline (or splines)
- Points
- Point   : point (or points)
- Instances components
- Instance : instans (or insts)
  
POINT domain is share between Mesh, Curve and Points but has not the same methods

The inheritance diagram is the following:

- Interfaces
- PointInterface      : common to points : Vertex, ControlPoint and CloudPoint
- MeshInterface       : common to all mesh domains: Vertex, Edge, Face, Corner
- PEFInterface        : common to Mesh domains except Corner: Vertex, Edge and Face
  
- Classes
- Domain
- Vertex          : POINT
- Edge            : EDGE
- Face            : FACE
- Corner          : CORNER
- ControlPoint    : POINT
- Spline          : CURVE
- CloudPoint      : POINT
- Instance        : INSTANCE
  
  

## \_\_getitem\_\_

Access by index


## as_verts

Force a domain change

For instance, it can be used to manage the faces of instances of meshes


## statistic

<method GeometryNodeAttributeStatistic>



## transfer_attribute

<method GeometryNodeAttributeTransfer>

mapping in ('NEAREST', 'INDEX'):
- NEAREST if index is None
- INDEX otherwise
  
call transfer_attribute_interpolated for NEAREST_FACE_INTERPOLATED



## transfer_index

<method GeometryNodeAttributeTransfer>

call transfer_attribute



## transfer_nearest

<method GeometryNodeAttributeTransfer>

call transfer_attribute



## transfer_nearest_face

<method GeometryNodeAttributeTransfer>

call transfer_attribute



## named_field

> Named field
  
Exposed methods are get_named_attribute and set_named_attribute to be closed to the name of the nodes
These methods use the named_field method (not named named_attribute to avoid misusing).

named_field creates an instance of NamedField and store it in a dedciated dictionnary

Raise an error if different data types are used for the same name


## get_named_attribute

> Get a named attribute socket
  
Make use named_field method


## set_named_attribute

> Set a named attribute socket
  
Make use named_field method

If data_type is None, the data_type is infered from the type of the value


## set_named_boolean

NOT SUPPORTED YET
ef get_named_byte_color(self, name):
return self.get_named_attribute(name, data_type='BYTE_COLOR')



## position

> Property Point position setter
<blid GeometryNodeSetPosition>

### Arguments

- value: Vector
  
  

## offset

> Property Point offset setter
<blid GeometryNodeSetPosition>

### Arguments

- value: Vector
  
  

## duplicate

> Duplicate domain
  
<blid GeometryNodeDuplicateElements>

### Arguments

- amount : Integer

### Returns

- duplicate index
  
  