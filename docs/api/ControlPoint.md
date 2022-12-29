# Class ControlPoint

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

 > **Vertex** is one of the two [domains](Domain.md) of [Curve](Curve.md).

It uses the *'POINT'* string domain.




### Constructor

```python
ControlPoint(self, data_socket, selection=None)
```


#### Args:
- data_socket (DataSocket): the data class the domain belongs to
- selection (any): the selection to use



## Content

**Properties**

[ID](#ID) | [as_cloud_points](#as_cloud_points) | [as_control_points](#as_control_points) | [as_corners](#as_corners) | [as_edges](#as_edges) | [as_faces](#as_faces) | [as_insts](#as_insts) | [as_splines](#as_splines) | [as_verts](#as_verts) | [count](#count) | [data_socket](#data_socket) | [domain](#domain) | [domain_index](#domain_index) | [index](#index) | [left_handle_positions](#left_handle_positions) | [normal](#normal) | [parameter](#parameter) | [parameter_factor](#parameter_factor) | [parameter_index](#parameter_index) | [parameter_length](#parameter_length) | [position](#position) | [radius](#radius) | [right_handle_positions](#right_handle_positions) | [selection](#selection) | [selection_index](#selection_index) | [tangent](#tangent) | [tilt](#tilt)

**Class and static methods**

[random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector)

**Methods**

[accumulate_field](#accumulate_field) | [attribute_max](#attribute_max) | [attribute_mean](#attribute_mean) | [attribute_median](#attribute_median) | [attribute_min](#attribute_min) | [attribute_node](#attribute_node) | [attribute_range](#attribute_range) | [attribute_statistic](#attribute_statistic) | [attribute_std](#attribute_std) | [attribute_sum](#attribute_sum) | [attribute_var](#attribute_var) | [capture_attribute](#capture_attribute) | [curve](#curve) | [delete](#delete) | [duplicate](#duplicate) | [endpoint_selection](#endpoint_selection) | [field_at_index](#field_at_index) | [handle_positions](#handle_positions) | [handle_type_selection](#handle_type_selection) | [handle_type_selection_align](#handle_type_selection_align) | [handle_type_selection_auto](#handle_type_selection_auto) | [handle_type_selection_free](#handle_type_selection_free) | [handle_type_selection_node](#handle_type_selection_node) | [handle_type_selection_vector](#handle_type_selection_vector) | [index_for_sample](#index_for_sample) | [instance_on_points](#instance_on_points) | [interpolate](#interpolate) | [material_selection](#material_selection) | [named_attribute](#named_attribute) | [named_boolean](#named_boolean) | [named_color](#named_color) | [named_float](#named_float) | [named_integer](#named_integer) | [named_vector](#named_vector) | [offset](#offset) | [proximity](#proximity) | [remove_named_attribute](#remove_named_attribute) | [sample_index](#sample_index) | [select](#select) | [separate](#separate) | [set_ID](#set_ID) | [set_handle_positions](#set_handle_positions) | [set_handle_positions_left](#set_handle_positions_left) | [set_handle_positions_right](#set_handle_positions_right) | [set_handle_type](#set_handle_type) | [set_handle_type_node](#set_handle_type_node) | [set_position](#set_position) | [set_radius](#set_radius) | [set_tilt](#set_tilt) | [socket_stack](#socket_stack) | [store_named_attribute](#store_named_attribute) | [store_named_attribute_no_selection](#store_named_attribute_no_selection) | [store_named_boolean](#store_named_boolean) | [store_named_color](#store_named_color) | [store_named_float](#store_named_float) | [store_named_integer](#store_named_integer) | [store_named_vector](#store_named_vector) | [view](#view) | [viewer](#viewer)

## Properties

### ID



> Node: [ID](GeometryNodeInputID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)

#### Returns:
- socket `ID`






Setter



> Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

Node implemented as property setter.

#### Args:
- attr_value: ID







<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_cloud_points

 Type cast to CloudPoint.


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_control_points

 Type cast to ControlPoint.


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_corners

 Type cast to Corner.


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_edges

 Type cast to Edge.


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_faces

 Type cast to Face.


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_insts

 Type cast to Instance.


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_splines

 Type cast to Spline.


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### as_verts

 Type cast to Vertex.


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### count



> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### data_socket

 Returns the data socket it belongs to.       

#### Returns:
- DataSocket



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### domain

 Gives the **Geometry Nodes** domain string to use in the generated nodes.

- Vertex        : 'POINT',
- Edge          : 'EDGE',
- Face          : 'FACE',
- Corner        : 'CORNER',
- ControlPoint  : 'POINT',
- Spline        : 'CURVE',
- CloudPoint    : 'POINT',
- Instance      : 'INSTANCE',

#### Returns:
- domain string (str)



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### domain_index



> Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### index



> Node: [Index](GeometryNodeInputIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/input_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)

#### Returns:
- socket `index`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### left_handle_positions



> Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Returns:
- socket `left`






Setter



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

Node implemented as property setter.

#### Args:
- attr_value: position







<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### normal



> Node: [Normal](GeometryNodeInputNormal.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)

#### Returns:
- socket `normal`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### parameter



> Node: [Spline Parameter](GeometryNodeSplineParameter.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplineParameter.webp)

#### Returns:
- tuple ('`factor`', '`length`', '`index`')






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### parameter_factor



> Node: [Spline Parameter](GeometryNodeSplineParameter.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- socket `factor`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### parameter_index



> Node: [Spline Parameter](GeometryNodeSplineParameter.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- socket `index`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### parameter_length



> Node: [Spline Parameter](GeometryNodeSplineParameter.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- socket `length`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### position



> Node: [Position](GeometryNodeInputPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)

#### Returns:
- socket `position`






Setter



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

Node implemented as property setter.

#### Args:
- attr_value: position







<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### radius



> Node: [Radius](GeometryNodeInputRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

#### Returns:
- socket `radius`






Setter



> Node: [Set Curve Radius](GeometryNodeSetCurveRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

Node implemented as property setter.

#### Args:
- attr_value: radius







<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### right_handle_positions



> Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Returns:
- socket `right`






Setter



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

Node implemented as property setter.

#### Args:
- attr_value: position







<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### selection

 Returns the selection value to use in nodes with a **Selection** socket.  

#### Returns:
- Boolean



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### selection_index

 Returns the selection index.

> CAUTION: raise an error if the selection is not a integer.

#### Returns:
- Integer



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tangent



> Node: [Curve Tangent](GeometryNodeInputTangent.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)

#### Returns:
- socket `tangent`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### tilt



> Node: [Curve Tilt](GeometryNodeInputCurveTilt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tilt.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)

#### Returns:
- socket `tilt`






Setter



> Node: [Set Curve Tilt](GeometryNodeSetCurveTilt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

Node implemented as property setter.

#### Args:
- attr_value: tilt







<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Class and static methods

### random_boolean

```python
@staticmethod
def random_boolean(probability=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- probability: Float
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_float

```python
@staticmethod
def random_float(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_integer

```python
@staticmethod
def random_integer(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### random_vector

```python
@staticmethod
def random_vector(min=None, max=None, ID=None, seed=None)
```



> Node: [Random Value](FunctionNodeRandomValue.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) | [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)

#### Args:
- min: ['Vector', 'Float', 'Integer']
- max: ['Vector', 'Float', 'Integer']
- ID: Integer
- seed: Integer

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## Methods

### accumulate_field

```python
def accumulate_field(self, value=None, group_index=None)
```



> Node: [Accumulate Field](GeometryNodeAccumulateField.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)

#### Args:
- value: ['Vector', 'Float', 'Integer']
- group_index: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

#### Returns:
- tuple ('`leading`', '`trailing`', '`total`')






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_max

```python
def attribute_max(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `max`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_mean

```python
def attribute_mean(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `mean`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_median

```python
def attribute_median(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `median`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_min

```python
def attribute_min(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `min`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_node

```python
def attribute_node(self, node)
```

 Define an input node as attribute

Called when creating an input node in a property getter. Performs two actions:
    
    - Call the method :func:`Node.as_attribute` to tag the node as being an attribute.
      This will allow the :func:`Tree.check_attributes` to see if it is necessary to create
      a *Capture Attribute* for this field.
    - Set the nde property :attr:`field_of` to self in order to implement the transfer attribute
      mechanism.

#### Args:
- node (Node): The node created by the domain
    
#### Returns:
- The node argument




<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_range

```python
def attribute_range(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `range`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_statistic

```python
def attribute_statistic(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_std

```python
def attribute_std(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `standard_deviation`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_sum

```python
def attribute_sum(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `sum`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_var

```python
def attribute_var(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

#### Returns:
- socket `variance`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_attribute

```python
def capture_attribute(self, value=None)
```



> Node: [Capture Attribute](GeometryNodeCaptureAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)

#### Args:
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### curve

```python
def curve(self)
```



> Node: [Curve of Point](GeometryNodeCurveOfPoint.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveOfPoint.webp)

#### Returns:
- tuple ('`curve_index`', '`index_in_curve`')






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### delete

```python
def delete(self, mode='ALL')
```



> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### duplicate

```python
def duplicate(self, amount=None)
```



> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### endpoint_selection

```python
def endpoint_selection(self, start_size=None, end_size=None)
```



> Node: [Endpoint Selection](GeometryNodeCurveEndpointSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)

#### Args:
- start_size: Integer
- end_size: Integer

#### Returns:
- socket `selection`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### field_at_index

```python
def field_at_index(self, index=None, value=None)
```



> Node: [Field at Index](GeometryNodeFieldAtIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field_at_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)

#### Args:
- index: Integer
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_positions

```python
def handle_positions(self, relative=None)
```



> Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Args:
- relative: Boolean

#### Returns:
- node with sockets ['left', 'right']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection

```python
def handle_type_selection(self, left=True, right=True, handle_type='AUTO')
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_align

```python
def handle_type_selection_align(self, left=True, right=True)
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_auto

```python
def handle_type_selection_auto(self, left=True, right=True)
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_free

```python
def handle_type_selection_free(self, left=True, right=True)
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_node

```python
def handle_type_selection_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'})
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- socket `selection`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### handle_type_selection_vector

```python
def handle_type_selection_vector(self, left=True, right=True)
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### index_for_sample

```python
def index_for_sample(self, default=None)
```

 Return default if not None or Input index socket.

The node 'Sample Index' has an input with default value to 0.
If mehod argument is None, create a node 'Input Index' as input.

**sample_index** method is implemented:
    
```python
def sample_index(self, value=None, index=None, clamp=False):
    return nodes.SampleIndex(..., index=self.index_for_sample(index), ...)
```

#### Returns:
- default or Input index



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instance_on_points

```python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```



> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances` of class Instances






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### interpolate

```python
def interpolate(self, value=None)
```



> Node: [Interpolate Domain](GeometryNodeFieldOnDomain.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/interpolate_domain.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### material_selection

```python
def material_selection(self, material=None)
```



> Node: [Material Selection](GeometryNodeMaterialSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)

#### Args:
- material: Material

#### Returns:
- socket `selection`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_attribute

```python
def named_attribute(self, name=None, data_type='FLOAT')
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String
- data_type (str): 'FLOAT' in [FLOAT, INT, FLOAT_VECTOR, FLOAT_COLOR, BOOLEAN]

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_boolean

```python
def named_boolean(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_color

```python
def named_color(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_float

```python
def named_float(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_integer

```python
def named_integer(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### named_vector

```python
def named_vector(self, name=None)
```



> Node: [Named Attribute](GeometryNodeInputNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)

#### Args:
- name: String

#### Returns:
- socket `attribute`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### offset

```python
def offset(self, offset=None)
```



> Node: [Offset Point in Curve](GeometryNodeOffsetPointInCurve.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)

#### Args:
- offset: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetPointInCurve.webp)

#### Returns:
- tuple ('`is_valid_offset`', '`point_index`')






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity

```python
def proximity(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### remove_named_attribute

```python
def remove_named_attribute(self, name=None)
```



> Node: [Remove Named Attribute](GeometryNodeRemoveAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)

#### Args:
- name: String

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### sample_index

```python
def sample_index(self, value=None, index=None, clamp=False)
```



> Node: [Sample Index](GeometryNodeSampleIndex.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample_index.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color', 'Boolean']
- index: Integer
- clamp (bool): False

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### select

```python
def select(self, selection)
```

 Select the domain

If the method is called on a **Domain** which already has a selection, the two selections are combined:
    
```python
verts = mesh.verts[10:20] # Selection of vertices from 10 to 20
v = verts.select((verts.index % 2).equal(0)) # Even indices in the previous selection
```

#### Args:
- selection (Boolean or Integer): The selection condition
    
#### Returns:
- Domain with the given selection (Domain)

If a selection is existing, the resulting selection is a logical and betwenn the two




<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### separate

```python
def separate(self)
```



> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- tuple ('`selection`', '`inverted`')






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_ID

```python
def set_ID(self, ID=None)
```



> Node: [Set ID](GeometryNodeSetID.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)

#### Args:
- ID: Integer

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_handle_positions

```python
def set_handle_positions(self, position=None, offset=None, mode='LEFT')
```



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector
- mode (str): 'LEFT' in [LEFT, RIGHT]

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_handle_positions_left

```python
def set_handle_positions_left(self, position=None, offset=None)
```



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_handle_positions_right

```python
def set_handle_positions_right(self, position=None, offset=None)
```



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_handle_type

```python
def set_handle_type(self, left=True, right=True, handle_type='AUTO')
```



> Node: [Set Handle Type](GeometryNodeCurveSetHandles.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

#### Args:
- curve: Curve
- selection: Boolean
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['curve']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_handle_type_node

```python
def set_handle_type_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'})
```



> Node: [Set Handle Type](GeometryNodeCurveSetHandles.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_position

```python
def set_position(self, position=None, offset=None)
```



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_radius

```python
def set_radius(self, radius=None)
```



> Node: [Set Curve Radius](GeometryNodeSetCurveRadius.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

#### Args:
- radius: Float

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### set_tilt

```python
def set_tilt(self, tilt=None)
```



> Node: [Set Curve Tilt](GeometryNodeSetCurveTilt.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

#### Args:
- tilt: Float

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### socket_stack

```python
def socket_stack(self, node, socket_name=None)
```

 Make the owning socket jump to the output socket of the node passed in argumment.

#### Args:
- node (Node): The node to jump to
- socket_name: The name of the output socket (first one if None)



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None, data_type=None)
```

 Store a named attribute

If selection exists, create an intermediary cloud of points to update selectively the items.

#### Args:
- name (str): name of the attribute
- value (any): value of the attribute
- data_type (str): valeu data type
    
#### Returns:
- data socket (DataSocket)




<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_attribute_no_selection

```python
def store_named_attribute_no_selection(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_boolean

```python
def store_named_boolean(self, name, value)
```

 Store a named attribute of type Boolean

see [store_named_attribute](#store_named_attribute)

#### Args:
- name (str): the attribute name
- value (float): the value to store
    
#### Returns:
- Data socket (DataSocket)



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_color

```python
def store_named_color(self, name, value)
```

 Store a named attribute of type Color

#### Args:
- name (str): the attribute name
- value (float): the value to store
    
see [store_named_attribute](#store_named_attribute)

#### Returns:
- Data socket (DataSocket)



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_float

```python
def store_named_float(self, name, value)
```

 Store a named attribute of type Float

see [store_named_attribute](#store_named_attribute)

#### Args:
- name (str): the attribute name
- value (float): the value to store
    
#### Returns:
- Data socket (DataSocket)



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_integer

```python
def store_named_integer(self, name, value)
```

 Store a named attribute of type Integer

see [store_named_attribute](#store_named_attribute)

#### Args:
- name (str): the attribute name
- value (float): the value to store
    
#### Returns:
- Data socket (DataSocket)



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_vector

```python
def store_named_vector(self, name, value)
```

 Store a named attribute of type Vector

#### Args:
- name (str): the attribute name
- value (float): the value to store
    
see [store_named_attribute](#store_named_attribute)

#### Returns:
- Data socket (DataSocket)



<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### view

```python
def view(self, value=None)
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']

#### Returns:
- node with sockets []






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### viewer

```python
def viewer(self, value=None)
```



> Node: [Viewer](GeometryNodeViewer.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)

#### Args:
- value: ['Float', 'Vector', 'Color', 'Integer', 'Boolean']

#### Returns:
- node with sockets []






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

