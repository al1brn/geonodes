# class Domain

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
- [delete](#delete)
- [duplicate](#duplicate)
- [field_at_index](#field_at_index)
- [get_named_boolean](#get_named_boolean)
- [get_named_color](#get_named_color)
- [get_named_float](#get_named_float)
- [get_named_integer](#get_named_integer)
- [get_named_vector](#get_named_vector)
- [material_selection](#material_selection)
- [named_attribute](#named_attribute)
- [random_boolean](#random_boolean)
- [random_float](#random_float)
- [random_integer](#random_integer)
- [random_vector](#random_vector)
- [remove_named_attribute](#remove_named_attribute)
- [sample_index](#sample_index)
- [sample_nearest](#sample_nearest)
- [separate](#separate)
- [set_ID](#set_ID)
- [set_material_index](#set_material_index)
- [set_named_boolean](#set_named_boolean)
- [set_named_color](#set_named_color)
- [set_named_float](#set_named_float)
- [set_named_integer](#set_named_integer)
- [set_named_vector](#set_named_vector)
- [set_position](#set_position)
- [store_named_attribute](#store_named_attribute)

## ID <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def ID(self):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html) )

<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'ID'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## ID <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def ID(self, attr_value):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html) )

<sub>Go to [top](#class-Domain)</sub>

Node implemented as property setter.

<sub>Go to [top](#class-Domain)</sub>

        ###Args:<sub>Go to [top](#class-Domain)</sub>

- attr_value: ID
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## accumulate_field

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def accumulate_field(self, value=None, group_index=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- value: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Domain)</sub>

- group_index: Integer
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- tuple ('leading', 'trailing', 'total')
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## attribute_max

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def attribute_max(self, attribute=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'max'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## attribute_mean

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def attribute_mean(self, attribute=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'mean'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## attribute_median

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def attribute_median(self, attribute=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'median'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## attribute_min

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def attribute_min(self, attribute=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'min'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## attribute_range

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def attribute_range(self, attribute=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'range'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## attribute_statistic

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def attribute_statistic(self, attribute=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## attribute_std

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def attribute_std(self, attribute=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'standard_deviation'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## attribute_sum

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def attribute_sum(self, attribute=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'sum'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## attribute_var

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def attribute_var(self, attribute=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- attribute: ['Float', 'Vector']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'variance'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## capture_attribute

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def capture_attribute(self, value=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'attribute'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## delete

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def delete(self, mode='ALL'):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## domain_index <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def domain_index(self):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html) )

<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'index'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## duplicate

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def duplicate(self, amount=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- amount: Integer
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'duplicate_index'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## field_at_index

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def field_at_index(self, index=None, value=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- index: Integer
<sub>Go to [top](#class-Domain)</sub>

- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'value'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## get_named_boolean

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def get_named_boolean(self, name=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'attribute'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## get_named_color

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def get_named_color(self, name=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'attribute'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## get_named_float

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def get_named_float(self, name=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'attribute'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## get_named_integer

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def get_named_integer(self, name=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'attribute'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## get_named_vector

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def get_named_vector(self, name=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'attribute'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## index <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def index(self):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html) )

<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'index'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## material_index <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def material_index(self):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html) )

<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'material_index'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## material_selection

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def material_selection(self, material=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- material: Material
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'selection'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## named_attribute

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def named_attribute(self, name=None, data_type='FLOAT'):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>

- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'attribute'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## normal <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def normal(self):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html) )

<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'normal'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## position <span style="color:blue">*property*</span>

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def position(self):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html) )

<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'position'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## position <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def position(self, attr_value):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html) )

<sub>Go to [top](#class-Domain)</sub>

Node implemented as property setter.

<sub>Go to [top](#class-Domain)</sub>

        ###Args:<sub>Go to [top](#class-Domain)</sub>

- attr_value: position
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## random_boolean

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def random_boolean(self, probability=None, ID=None, seed=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- probability: Float
<sub>Go to [top](#class-Domain)</sub>

- ID: Integer
<sub>Go to [top](#class-Domain)</sub>

- seed: Integer
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'value'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## random_float

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def random_float(self, min=None, max=None, ID=None, seed=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- min: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Domain)</sub>

- max: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Domain)</sub>

- ID: Integer
<sub>Go to [top](#class-Domain)</sub>

- seed: Integer
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'value'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## random_integer

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def random_integer(self, min=None, max=None, ID=None, seed=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- min: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Domain)</sub>

- max: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Domain)</sub>

- ID: Integer
<sub>Go to [top](#class-Domain)</sub>

- seed: Integer
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'value'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## random_vector

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def random_vector(self, min=None, max=None, ID=None, seed=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) ( [api](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- min: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Domain)</sub>

- max: ['Vector', 'Float', 'Integer']
<sub>Go to [top](#class-Domain)</sub>

- ID: Integer
<sub>Go to [top](#class-Domain)</sub>

- seed: Integer
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'value'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## remove_named_attribute

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def remove_named_attribute(self, name=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## sample_index

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def sample_index(self, value=None, index=None, clamp=False):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
<sub>Go to [top](#class-Domain)</sub>

- index: Integer
<sub>Go to [top](#class-Domain)</sub>

- clamp (bool): False
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'value'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## sample_nearest

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def sample_nearest(self, sample_position=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Sample Nearest](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_nearest.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- sample_position: Vector
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

  socket 'index'<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## separate

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def separate(self, geometry=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- geometry: Geometry
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- tuple ('selection', 'inverted')
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## set_ID

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def set_ID(self, ID=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- ID: Integer
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## set_material_index

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def set_material_index(self, material_index=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- material_index: Integer
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## set_named_boolean

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def set_named_boolean(self, name=None, value=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>

- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## set_named_color

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def set_named_color(self, name=None, value=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>

- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## set_named_float

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def set_named_float(self, name=None, value=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>

- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## set_named_integer

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def set_named_integer(self, name=None, value=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>

- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## set_named_vector

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def set_named_vector(self, name=None, value=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>

- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## set_position

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def set_position(self, position=None, offset=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- position: Vector
<sub>Go to [top](#class-Domain)</sub>

- offset: Vector
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

## store_named_attribute

<sub>Go to [top](#class-Domain)</sub>

```python
<sub>Go to [top](#class-Domain)</sub>

def store_named_attribute(self, name=None, value=None):

<sub>Go to [top](#class-Domain)</sub>

```
<sub>Go to [top](#class-Domain)</sub>

Node [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html) )

<sub>Go to [top](#class-Domain)</sub>

### Args:
<sub>Go to [top](#class-Domain)</sub>

- name: String
<sub>Go to [top](#class-Domain)</sub>

- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

### Returns:

<sub>Go to [top](#class-Domain)</sub>

- node with sockets ['geometry']
<sub>Go to [top](#class-Domain)</sub>


<sub>Go to [top](#class-Domain)</sub>

