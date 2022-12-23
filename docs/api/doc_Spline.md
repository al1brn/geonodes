# Class Spline

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[ID](#ID) | [count](#count) | [cyclic](#cyclic) | [domain_index](#domain_index) | [index](#index) | [length](#length) | [material](#material) | [material_index](#material_index) | [normal](#normal) | [position](#position) | [resolution](#resolution) | [type](#type)



**Methods**

[accumulate_field](#accumulate_field) | [attribute_max](#attribute_max) | [attribute_mean](#attribute_mean) | [attribute_median](#attribute_median) | [attribute_min](#attribute_min) | [attribute_range](#attribute_range) | [attribute_statistic](#attribute_statistic) | [attribute_std](#attribute_std) | [attribute_sum](#attribute_sum) | [attribute_var](#attribute_var) | [capture_attribute](#capture_attribute) | [delete](#delete) | [duplicate](#duplicate) | [field_at_index](#field_at_index) | [get_named_boolean](#get_named_boolean) | [get_named_color](#get_named_color) | [get_named_float](#get_named_float) | [get_named_integer](#get_named_integer) | [get_named_vector](#get_named_vector) | [interpolate](#interpolate) | [material_selection](#material_selection) | [named_attribute](#named_attribute) | [points](#points) | [random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector) | [remove_named_attribute](#remove_named_attribute) | [resample](#resample) | [resample_count](#resample_count) | [resample_evaluated](#resample_evaluated) | [resample_length](#resample_length) | [sample_index](#sample_index) | [separate](#separate) | [set_ID](#set_ID) | [set_cyclic](#set_cyclic) | [set_material](#set_material) | [set_material_index](#set_material_index) | [set_named_boolean](#set_named_boolean) | [set_named_color](#set_named_color) | [set_named_float](#set_named_float) | [set_named_integer](#set_named_integer) | [set_named_vector](#set_named_vector) | [set_normal](#set_normal) | [set_position](#set_position) | [set_resolution](#set_resolution) | [set_type](#set_type) | [store_named_attribute](#store_named_attribute)

## Properties

### ID

 Node ID.

Node reference [ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html)
Developer reference [GeometryNodeInputID](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

#### Returns:
- socket `ID`



Setter

 Node SetID.

Node reference [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
Developer reference [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

Node implemented as property setter.

#### Args:
- attr_value: ID




### count

 Node DomainSize.

Node reference [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html)
Developer reference [GeometryNodeAttributeDomainSize](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `spline_count`



### cyclic

 Node IsSplineCyclic.

Node reference [Is Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html)
Developer reference [GeometryNodeInputSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)

#### Returns:
- socket `cyclic`



Setter

 Node SetSplineCyclic.

Node reference [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html)
Developer reference [GeometryNodeSetSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)

Node implemented as property setter.

#### Args:
- attr_value: cyclic




### domain_index

 Node Index.

Node reference [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html)
Developer reference [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`



### index

 Node Index.

Node reference [Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html)
Developer reference [GeometryNodeInputIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`



### length

 Node SplineLength.

Node reference [Spline Length](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_length.html)
Developer reference [GeometryNodeSplineLength](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)

#### Returns:
- tuple ('length', 'point_count')



### material

 Node SetMaterial.

Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

'material' is a write only property.
Raise an exception if attempt to read.




Setter

 Node SetMaterial.

Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

Node implemented as property setter.

#### Args:
- attr_value: material




### material_index

 Node MaterialIndex.

Node reference [Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html)
Developer reference [GeometryNodeInputMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)

#### Returns:
- socket `material_index`



### normal

 Node Normal.

Node reference [Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html)
Developer reference [GeometryNodeInputNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`



Setter

 Node SetCurveNormal.

Node reference [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html)
Developer reference [GeometryNodeSetCurveNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)

Node implemented as property setter.

#### Args:
- attr_value: mode




### position

 Node Position.

Node reference [Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html)
Developer reference [GeometryNodeInputPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

#### Returns:
- socket `position`



Setter

 Node SetPosition.

Node reference [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
Developer reference [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

Node implemented as property setter.

#### Args:
- attr_value: position




### resolution

 Node SplineResolution.

Node reference [Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_resolution.html)
Developer reference [GeometryNodeInputSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)

#### Returns:
- socket `resolution`



Setter

 Node SetSplineResolution.

Node reference [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html)
Developer reference [GeometryNodeSetSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)

Node implemented as property setter.

#### Args:
- attr_value: resolution




### type

 Node SetSplineType.

Node reference [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html)
Developer reference [GeometryNodeCurveSplineType](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

'type' is a write only property.
Raise an exception if attempt to read.




Setter

 Node SetSplineType.

Node reference [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html)
Developer reference [GeometryNodeCurveSplineType](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

Node implemented as property setter.

#### Args:
- attr_value: spline_type




## Methods

### accumulate_field

```python
def accumulate_field(self, value=None, group_index=None)
```

 Node AccumulateField.

Node reference [Accumulate Field](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html)
Developer reference [GeometryNodeAccumulateField](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)

#### Args:
- value: ['Vector', 'Float', 'Integer']
- group_index: Integer

#### Returns:
- tuple ('leading', 'trailing', 'total')



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_max

```python
def attribute_max(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `max`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_mean

```python
def attribute_mean(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `mean`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_median

```python
def attribute_median(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `median`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_min

```python
def attribute_min(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `min`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_range

```python
def attribute_range(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `range`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_statistic

```python
def attribute_statistic(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_std

```python
def attribute_std(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `standard_deviation`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_sum

```python
def attribute_sum(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `sum`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_var

```python
def attribute_var(self, attribute=None)
```

 Node AttributeStatistic.

Node reference [Attribute Statistic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html)
Developer reference [GeometryNodeAttributeStatistic](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `variance`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute

```python
def capture_attribute(self, value=None)
```

 Node CaptureAttribute.

Node reference [Capture Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html)
Developer reference [GeometryNodeCaptureAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- socket `attribute`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete

```python
def delete(self, mode='ALL')
```

 Node DeleteGeometry.

Node reference [Delete Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html)
Developer reference [GeometryNodeDeleteGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### duplicate

```python
def duplicate(self, amount=None)
```

 Node DuplicateElements.

Node reference [Duplicate Elements](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html)
Developer reference [GeometryNodeDuplicateElements](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### field_at_index

```python
def field_at_index(self, index=None, value=None)
```

 Node FieldAtIndex.

Node reference [Field at Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html)
Developer reference [GeometryNodeFieldAtIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

#### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_boolean

```python
def get_named_boolean(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_color

```python
def get_named_color(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_float

```python
def get_named_float(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_integer

```python
def get_named_integer(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### get_named_vector

```python
def get_named_vector(self, name=None)
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### interpolate

```python
def interpolate(self, value=None)
```

 Node InterpolateDomain.

Node reference [Interpolate Domain](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html)
Developer reference [GeometryNodeFieldOnDomain](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material_selection

```python
def material_selection(self, material=None)
```

 Node MaterialSelection.

Node reference [Material Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html)
Developer reference [GeometryNodeMaterialSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

#### Args:
- material: Material

#### Returns:
- socket `selection`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT')
```

 Node NamedAttribute.

Node reference [Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html)
Developer reference [GeometryNodeInputNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

#### Returns:
- socket `attribute`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### points

```python
def points(self, weights=None, sort_index=None)
```

 Node PointsOfCurve.

Node reference [Points of Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/points_of_curve.html)
Developer reference [GeometryNodePointsOfCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)

#### Args:
- weights: Float
- sort_index: Integer

#### Returns:
- tuple ('point_index', 'total')



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_boolean

```python
def random_boolean(self, probability=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_float

```python
def random_float(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_integer

```python
def random_integer(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_vector

```python
def random_vector(self, min=None, max=None, ID=None, seed=None)
```

 Node RandomValue.

Node reference [Random Value](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html)
Developer reference [FunctionNodeRandomValue](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```

 Node RemoveNamedAttribute.

Node reference [Remove Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)
Developer reference [GeometryNodeRemoveAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### resample

```python
def resample(self, count=None, length=None, mode='COUNT')
```

 Node ResampleCurve.

Node reference [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
Developer reference [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- count: Integer
- length: Float
- mode (str): 'COUNT' in [EVALUATED, COUNT, LENGTH]

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### resample_count

```python
def resample_count(self, count=None)
```

 Node ResampleCurve.

Node reference [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
Developer reference [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- count: Integer

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### resample_evaluated

```python
def resample_evaluated(self)
```

 Node ResampleCurve.

Node reference [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
Developer reference [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### resample_length

```python
def resample_length(self, length=None)
```

 Node ResampleCurve.

Node reference [Resample Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/resample_curve.html)
Developer reference [GeometryNodeResampleCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)

#### Args:
- length: Float

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_index

```python
def sample_index(self, value=None, index=None, clamp=False)
```

 Node SampleIndex.

Node reference [Sample Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html)
Developer reference [GeometryNodeSampleIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False

#### Returns:
- socket `value`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate

```python
def separate(self, geometry=None)
```

 Node SeparateGeometry.

Node reference [Separate Geometry](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html)
Developer reference [GeometryNodeSeparateGeometry](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- geometry: Geometry

#### Returns:
- tuple ('selection', 'inverted')



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_ID

```python
def set_ID(self, ID=None)
```

 Node SetID.

Node reference [Set ID](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
Developer reference [GeometryNodeSetID](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- ID: Integer

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_cyclic

```python
def set_cyclic(self, cyclic=None)
```

 Node SetSplineCyclic.

Node reference [Set Spline Cyclic](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_cyclic.html)
Developer reference [GeometryNodeSetSplineCyclic](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)

#### Args:
- cyclic: Boolean

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material

```python
def set_material(self, material=None)
```

 Node SetMaterial.

Node reference [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html)
Developer reference [GeometryNodeSetMaterial](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)

#### Args:
- material: Material

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_material_index

```python
def set_material_index(self, material_index=None)
```

 Node SetMaterialIndex.

Node reference [Set Material Index](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html)
Developer reference [GeometryNodeSetMaterialIndex](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)

#### Args:
- material_index: Integer

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_boolean

```python
def set_named_boolean(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_color

```python
def set_named_color(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_float

```python
def set_named_float(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_integer

```python
def set_named_integer(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_named_vector

```python
def set_named_vector(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_normal

```python
def set_normal(self, mode='MINIMUM_TWIST')
```

 Node SetCurveNormal.

Node reference [Set Curve Normal](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html)
Developer reference [GeometryNodeSetCurveNormal](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)

#### Args:
- mode (str): 'MINIMUM_TWIST' in [MINIMUM_TWIST, Z_UP]

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_position

```python
def set_position(self, position=None, offset=None)
```

 Node SetPosition.

Node reference [Set Position](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
Developer reference [GeometryNodeSetPosition](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_resolution

```python
def set_resolution(self, resolution=None)
```

 Node SetSplineResolution.

Node reference [Set Spline Resolution](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_resolution.html)
Developer reference [GeometryNodeSetSplineResolution](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)

#### Args:
- resolution: Integer

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_type

```python
def set_type(self, spline_type='POLY')
```

 Node SetSplineType.

Node reference [Set Spline Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_spline_type.html)
Developer reference [GeometryNodeCurveSplineType](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)

#### Args:
- spline_type (str): 'POLY' in [CATMULL_ROM, POLY, BEZIER, NURBS]

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None)
```

 Node StoreNamedAttribute.

Node reference [Store Named Attribute](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html)
Developer reference [GeometryNodeStoreNamedAttribute](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- node with sockets ['geometry']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

