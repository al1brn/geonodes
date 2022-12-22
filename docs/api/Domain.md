# class Domain

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


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
  
  
  > see [examples](#examples)

## Properties

- [ID](#ID-property)
- [domain_index](#domain_index-property)
- [index](#index-property)
- [material_index](#material_index-property)
- [normal](#normal-property)
- [position](#position-property)



## Methods

- [accumulate_field](#accumulate_field)
- [attribute_max](#attribute_max)
- [attribute_mean](#attribute_mean)
- [attribute_median](#attribute_median)
- [attribute_min](#attribute_min)
- [attribute_range](#attribute_range)
- [attribute_statistic](#attribute_statistic)
- [attribute_std](#attribute_std)
- [attribute_sum](#attribute_sum)
- [attribute_var](#attribute_var)
- [capture_attribute](#capture_attribute)
- [field_at_index](#field_at_index)
- [get_named_boolean](#get_named_boolean)
- [get_named_color](#get_named_color)
- [get_named_float](#get_named_float)
- [get_named_integer](#get_named_integer)
- [get_named_vector](#get_named_vector)
- [interpolate](#interpolate)
- [material_selection](#material_selection)
- [named_attribute](#named_attribute)
- [random_boolean](#random_boolean)
- [random_float](#random_float)
- [random_integer](#random_integer)
- [random_vector](#random_vector)
- [remove_named_attribute](#remove_named_attribute)
- [sample_index](#sample_index)
- [set_ID](#set_ID)
- [set_material_index](#set_material_index)
- [set_named_boolean](#set_named_boolean)
- [set_named_color](#set_named_color)
- [set_named_float](#set_named_float)
- [set_named_integer](#set_named_integer)
- [set_named_vector](#set_named_vector)
- [set_position](#set_position)
- [store_named_attribute](#store_named_attribute)

## ID <sub>*property*</sub>

```python
def ID(self):

```
> Node: [ID](GeometryNodeInputID.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

#### Returns:
- socket `ID`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## ID <sub>*etter*</sub>

```python
def ID(self, attr_value):

```
> Node: [Set ID](GeometryNodeSetID.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

Node implemented as property setter.

#### Args:
- attr_value: ID


<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## accumulate_field

```python
def accumulate_field(self, value=None, group_index=None):

```
> Node: [Accumulate Field](GeometryNodeAccumulateField.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)

#### Args:
- value: ['Vector', 'Float', 'Integer']
- group_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

#### Returns:
- tuple ('`leading`', '`trailing`', '`total`')

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## attribute_max

```python
def attribute_max(self, attribute=None):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `max`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## attribute_mean

```python
def attribute_mean(self, attribute=None):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `mean`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## attribute_median

```python
def attribute_median(self, attribute=None):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `median`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## attribute_min

```python
def attribute_min(self, attribute=None):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `min`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## attribute_range

```python
def attribute_range(self, attribute=None):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `range`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## attribute_statistic

```python
def attribute_statistic(self, attribute=None):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## attribute_std

```python
def attribute_std(self, attribute=None):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `standard_deviation`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## attribute_sum

```python
def attribute_sum(self, attribute=None):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `sum`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## attribute_var

```python
def attribute_var(self, attribute=None):

```
> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `variance`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## capture_attribute

```python
def capture_attribute(self, value=None):

```
> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- socket `attribute`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## domain_index <sub>*property*</sub>

```python
def domain_index(self):

```
> Node: [Index](GeometryNodeInputIndex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## field_at_index

```python
def field_at_index(self, index=None, value=None):

```
> Node: [Field at Index](GeometryNodeFieldAtIndex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

#### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

#### Returns:
- socket `value`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## get_named_boolean

```python
def get_named_boolean(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## get_named_color

```python
def get_named_color(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## get_named_float

```python
def get_named_float(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## get_named_integer

```python
def get_named_integer(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## get_named_vector

```python
def get_named_vector(self, name=None):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## index <sub>*property*</sub>

```python
def index(self):

```
> Node: [Index](GeometryNodeInputIndex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## interpolate

```python
def interpolate(self, value=None):

```
> Node: [Interpolate Domain](GeometryNodeFieldOnDomain.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

#### Returns:
- socket `value`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## material_index <sub>*property*</sub>

```python
def material_index(self):

```
> Node: [Material Index](GeometryNodeInputMaterialIndex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

#### Returns:
- socket `material_index`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## material_selection

```python
def material_selection(self, material=None):

```
> Node: [Material Selection](GeometryNodeMaterialSelection.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

#### Args:
- material: Material

#### Returns:
- socket `selection`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT'):

```
> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

#### Returns:
- socket `attribute`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## normal <sub>*property*</sub>

```python
def normal(self):

```
> Node: [Normal](GeometryNodeInputNormal.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## position <sub>*property*</sub>

```python
def position(self):

```
> Node: [Position](GeometryNodeInputPosition.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

#### Returns:
- socket `position`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## position <sub>*etter*</sub>

```python
def position(self, attr_value):

```
> Node: [Set Position](GeometryNodeSetPosition.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

Node implemented as property setter.

#### Args:
- attr_value: position


<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## random_boolean

```python
def random_boolean(self, probability=None, ID=None, seed=None):

```
> Node: [Random Value](FunctionNodeRandomValue.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## random_float

```python
def random_float(self, min=None, max=None, ID=None, seed=None):

```
> Node: [Random Value](FunctionNodeRandomValue.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## random_integer

```python
def random_integer(self, min=None, max=None, ID=None, seed=None):

```
> Node: [Random Value](FunctionNodeRandomValue.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## random_vector

```python
def random_vector(self, min=None, max=None, ID=None, seed=None):

```
> Node: [Random Value](FunctionNodeRandomValue.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) - [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## remove_named_attribute

```python
def remove_named_attribute(self, name=None):

```
> Node: [Remove Named Attribute](GeometryNodeRemoveAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## sample_index

```python
def sample_index(self, value=None, index=None, clamp=False):

```
> Node: [Sample Index](GeometryNodeSampleIndex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False

#### Returns:
- socket `value`

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_ID

```python
def set_ID(self, ID=None):

```
> Node: [Set ID](GeometryNodeSetID.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- ID: Integer

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_material_index

```python
def set_material_index(self, material_index=None):

```
> Node: [Set Material Index](GeometryNodeSetMaterialIndex.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

#### Args:
- material_index: Integer

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_named_boolean

```python
def set_named_boolean(self, name=None, value=None):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_named_color

```python
def set_named_color(self, name=None, value=None):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_named_float

```python
def set_named_float(self, name=None, value=None):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_named_integer

```python
def set_named_integer(self, name=None, value=None):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_named_vector

```python
def set_named_vector(self, name=None, value=None):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_position

```python
def set_position(self, position=None, offset=None):

```
> Node: [Set Position](GeometryNodeSetPosition.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## store_named_attribute

```python
def store_named_attribute(self, name=None, value=None):

```
> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self

<sub>Go to [top](#class-Domain) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>


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
  
  
  