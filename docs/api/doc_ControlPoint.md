# Class ControlPoint

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

## Content

**Properties**

[ID](#ID) | [count](#count) | [domain_index](#domain_index) | [index](#index) | [left_handle_positions](#left_handle_positions) | [material_index](#material_index) | [normal](#normal) | [parameter](#parameter) | [parameter_factor](#parameter_factor) | [parameter_index](#parameter_index) | [parameter_length](#parameter_length) | [position](#position) | [radius](#radius) | [right_handle_positions](#right_handle_positions) | [tangent](#tangent) | [tilt](#tilt)



**Methods**

[accumulate_field](#accumulate_field) | [attribute_max](#attribute_max) | [attribute_mean](#attribute_mean) | [attribute_median](#attribute_median) | [attribute_min](#attribute_min) | [attribute_range](#attribute_range) | [attribute_statistic](#attribute_statistic) | [attribute_std](#attribute_std) | [attribute_sum](#attribute_sum) | [attribute_var](#attribute_var) | [capture_attribute](#capture_attribute) | [curve](#curve) | [delete](#delete) | [duplicate](#duplicate) | [endpoint_selection](#endpoint_selection) | [field_at_index](#field_at_index) | [get_named_boolean](#get_named_boolean) | [get_named_color](#get_named_color) | [get_named_float](#get_named_float) | [get_named_integer](#get_named_integer) | [get_named_vector](#get_named_vector) | [handle_positions](#handle_positions) | [handle_type_selection](#handle_type_selection) | [handle_type_selection_align](#handle_type_selection_align) | [handle_type_selection_auto](#handle_type_selection_auto) | [handle_type_selection_free](#handle_type_selection_free) | [handle_type_selection_node](#handle_type_selection_node) | [handle_type_selection_vector](#handle_type_selection_vector) | [instance_on_points](#instance_on_points) | [interpolate](#interpolate) | [material_selection](#material_selection) | [named_attribute](#named_attribute) | [offset](#offset) | [proximity](#proximity) | [random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector) | [remove_named_attribute](#remove_named_attribute) | [sample_index](#sample_index) | [separate](#separate) | [set_ID](#set_ID) | [set_handle_positions](#set_handle_positions) | [set_handle_positions_left](#set_handle_positions_left) | [set_handle_positions_right](#set_handle_positions_right) | [set_handle_type](#set_handle_type) | [set_handle_type_node](#set_handle_type_node) | [set_material_index](#set_material_index) | [set_named_boolean](#set_named_boolean) | [set_named_color](#set_named_color) | [set_named_float](#set_named_float) | [set_named_integer](#set_named_integer) | [set_named_vector](#set_named_vector) | [set_position](#set_position) | [set_radius](#set_radius) | [set_tilt](#set_tilt) | [store_named_attribute](#store_named_attribute)

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
- socket `point_count`



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



### left_handle_positions

 Node CurveHandlePositions.

Node reference [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
Developer reference [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Returns:
- socket `left`



Setter

 Node SetHandlePositions.

Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

Node implemented as property setter.

#### Args:
- attr_value: position




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



### parameter

 Node SplineParameter.

Node reference [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
Developer reference [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- tuple ('factor', 'length', 'index')



### parameter_factor

 Node SplineParameter.

Node reference [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
Developer reference [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- socket `factor`



### parameter_index

 Node SplineParameter.

Node reference [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
Developer reference [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- socket `index`



### parameter_length

 Node SplineParameter.

Node reference [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html)
Developer reference [GeometryNodeSplineParameter](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- socket `length`



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




### radius

 Node Radius.

Node reference [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html)
Developer reference [GeometryNodeInputRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

#### Returns:
- socket `radius`



Setter

 Node SetCurveRadius.

Node reference [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html)
Developer reference [GeometryNodeSetCurveRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

Node implemented as property setter.

#### Args:
- attr_value: radius




### right_handle_positions

 Node CurveHandlePositions.

Node reference [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
Developer reference [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Returns:
- socket `right`



Setter

 Node SetHandlePositions.

Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

Node implemented as property setter.

#### Args:
- attr_value: position




### tangent

 Node CurveTangent.

Node reference [Curve Tangent](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html)
Developer reference [GeometryNodeInputTangent](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)

#### Returns:
- socket `tangent`



### tilt

 Node CurveTilt.

Node reference [Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tilt.html)
Developer reference [GeometryNodeInputCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)

#### Returns:
- socket `tilt`



Setter

 Node SetCurveTilt.

Node reference [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html)
Developer reference [GeometryNodeSetCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

Node implemented as property setter.

#### Args:
- attr_value: tilt




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

### curve

```python
def curve(self)
```

 Node CurveOfPoint.

Node reference [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html)
Developer reference [GeometryNodeCurveOfPoint](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)

#### Returns:
- tuple ('curve_index', 'index_in_curve')



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

### endpoint_selection

```python
def endpoint_selection(self, start_size=None, end_size=None)
```

 Node EndpointSelection.

Node reference [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html)
Developer reference [GeometryNodeCurveEndpointSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)

#### Args:
- start_size: Integer
- end_size: Integer

#### Returns:
- socket `selection`



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

### handle_positions

```python
def handle_positions(self, relative=None)
```

 Node CurveHandlePositions.

Node reference [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
Developer reference [GeometryNodeInputCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Args:
- relative: Boolean

#### Returns:
- node with sockets ['left', 'right']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection

```python
def handle_type_selection(self, left=True, right=True, handle_type='AUTO')
```

 Node HandleTypeSelection.

Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_align

```python
def handle_type_selection_align(self, left=True, right=True)
```

 Node HandleTypeSelection.

Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_auto

```python
def handle_type_selection_auto(self, left=True, right=True)
```

 Node HandleTypeSelection.

Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_free

```python
def handle_type_selection_free(self, left=True, right=True)
```

 Node HandleTypeSelection.

Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_node

```python
def handle_type_selection_node(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'})
```

 Node HandleTypeSelection.

Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- socket `selection`



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_vector

```python
def handle_type_selection_vector(self, left=True, right=True)
```

 Node HandleTypeSelection.

Node reference [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html)
Developer reference [GeometryNodeCurveHandleTypeSelection](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instance_on_points

```python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

 Node InstanceOnPoints.

Node reference [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
Developer reference [GeometryNodeInstanceOnPoints](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances` [Instances](Instances.md)



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

### offset

```python
def offset(self, offset=None)
```

 Node OffsetPointInCurve.

Node reference [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html)
Developer reference [GeometryNodeOffsetPointInCurve](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)

#### Args:
- offset: Integer

#### Returns:
- tuple ('is_valid_offset', 'point_index')



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity

```python
def proximity(self, target=None, source_position=None)
```

 Node GeometryProximity.

Node reference [Geometry Proximity](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html)
Developer reference [GeometryNodeProximity](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`



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

### set_handle_positions

```python
def set_handle_positions(self, position=None, offset=None, mode='LEFT')
```

 Node SetHandlePositions.

Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector
- mode (str): 'LEFT' in [LEFT, RIGHT]

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_handle_positions_left

```python
def set_handle_positions_left(self, position=None, offset=None)
```

 Node SetHandlePositions.

Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_handle_positions_right

```python
def set_handle_positions_right(self, position=None, offset=None)
```

 Node SetHandlePositions.

Node reference [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html)
Developer reference [GeometryNodeSetCurveHandlePositions](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_handle_type

```python
def set_handle_type(self, left=True, right=True, handle_type='AUTO')
```

 Node SetHandleType.

Node reference [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html)
Developer reference [GeometryNodeCurveSetHandles](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

#### Args:
- curve: Curve
- selection: Boolean
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_handle_type_node

```python
def set_handle_type_node(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'})
```

 Node SetHandleType.

Node reference [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html)
Developer reference [GeometryNodeCurveSetHandles](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['curve']



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

### set_radius

```python
def set_radius(self, radius=None)
```

 Node SetCurveRadius.

Node reference [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html)
Developer reference [GeometryNodeSetCurveRadius](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

#### Args:
- radius: Float

#### Returns:
- node with sockets ['curve']



<sub>Go to [top](#class-Collection) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_tilt

```python
def set_tilt(self, tilt=None)
```

 Node SetCurveTilt.

Node reference [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html)
Developer reference [GeometryNodeSetCurveTilt](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

#### Args:
- tilt: Float

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

