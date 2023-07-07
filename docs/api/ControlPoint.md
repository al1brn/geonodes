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

[ID](#ID) | [as_cloud_points](#as_cloud_points) | [as_control_points](#as_control_points) | [as_corners](#as_corners) | [as_edges](#as_edges) | [as_faces](#as_faces) | [as_insts](#as_insts) | [as_splines](#as_splines) | [as_verts](#as_verts) | [count](#count) | [data_socket](#data_socket) | [domain](#domain) | [domain_index](#domain_index) | [index](#index) | [left_handle_offset](#left_handle_offset) | [left_handle_positions](#left_handle_positions) | [normal](#normal) | [parameter](#parameter) | [position](#position) | [position_offset](#position_offset) | [radius](#radius) | [relative_left_handle_positions](#relative_left_handle_positions) | [relative_right_handle_positions](#relative_right_handle_positions) | [right_handle_offset](#right_handle_offset) | [right_handle_positions](#right_handle_positions) | [selection](#selection) | [selection_index](#selection_index) | [tangent](#tangent) | [tilt](#tilt)

**Class and static methods**

[random_boolean](#random_boolean) | [random_float](#random_float) | [random_integer](#random_integer) | [random_vector](#random_vector)

**Methods**

[accumulate_field](#accumulate_field) | [attribute_node](#attribute_node) | [attribute_statistic](#attribute_statistic) | [blur_attribute](#blur_attribute) | [blur_color](#blur_color) | [blur_float](#blur_float) | [blur_integer](#blur_integer) | [blur_vector](#blur_vector) | [capture_attribute](#capture_attribute) | [capture_handle_type_selection](#capture_handle_type_selection) | [capture_handle_type_selection_align](#capture_handle_type_selection_align) | [capture_handle_type_selection_auto](#capture_handle_type_selection_auto) | [capture_handle_type_selection_free](#capture_handle_type_selection_free) | [capture_handle_type_selection_vector](#capture_handle_type_selection_vector) | [curve](#curve) | [delete](#delete) | [duplicate](#duplicate) | [endpoint_selection](#endpoint_selection) | [handle_positions](#handle_positions) | [handle_type_selection](#handle_type_selection) | [handle_type_selection_align](#handle_type_selection_align) | [handle_type_selection_auto](#handle_type_selection_auto) | [handle_type_selection_free](#handle_type_selection_free) | [handle_type_selection_node](#handle_type_selection_node) | [handle_type_selection_vector](#handle_type_selection_vector) | [index_for_sample](#index_for_sample) | [index_of_nearest](#index_of_nearest) | [instance_on](#instance_on) | [interpolate](#interpolate) | [material_selection](#material_selection) | [named_attribute](#named_attribute) | [named_boolean](#named_boolean) | [named_color](#named_color) | [named_float](#named_float) | [named_integer](#named_integer) | [named_vector](#named_vector) | [offset](#offset) | [proximity](#proximity) | [proximity_edges](#proximity_edges) | [proximity_faces](#proximity_faces) | [proximity_points](#proximity_points) | [raycast](#raycast) | [raycast_interpolated](#raycast_interpolated) | [raycast_nearest](#raycast_nearest) | [remove_named_attribute](#remove_named_attribute) | [sample_index](#sample_index) | [select](#select) | [separate](#separate) | [set_ID](#set_ID) | [set_handle_positions](#set_handle_positions) | [set_handle_type](#set_handle_type) | [set_handle_type_node](#set_handle_type_node) | [set_left_handle_positions](#set_left_handle_positions) | [set_position](#set_position) | [set_radius](#set_radius) | [set_right_handle_positions](#set_right_handle_positions) | [set_tilt](#set_tilt) | [socket_stack](#socket_stack) | [store_named_2D_vector](#store_named_2D_vector) | [store_named_attribute](#store_named_attribute) | [store_named_boolean](#store_named_boolean) | [store_named_byte_color](#store_named_byte_color) | [store_named_color](#store_named_color) | [store_named_float](#store_named_float) | [store_named_integer](#store_named_integer) | [store_named_vector](#store_named_vector) | [view](#view) | [viewer](#viewer)

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

### left_handle_offset



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

'left_handle_offset' is a write only property.
Raise an exception if attempt to read.







Setter



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

Node implemented as property setter.

#### Args:
- attr_value: offset







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
- node with sockets ['factor', 'length', 'index']






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

### position_offset



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

'position_offset' is a write only property.
Raise an exception if attempt to read.







Setter



> Node: [Set Position](GeometryNodeSetPosition.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)

Node implemented as property setter.

#### Args:
- attr_value: offset







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

### relative_left_handle_positions



> Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Returns:
- socket `left`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### relative_right_handle_positions



> Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Returns:
- socket `right`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### right_handle_offset



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

'right_handle_offset' is a write only property.
Raise an exception if attempt to read.







Setter



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

Node implemented as property setter.

#### Args:
- attr_value: offset







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
def accumulate_field(self, value=None, group_id=None)
```



> Node: [Accumulate Field](GeometryNodeAccumulateField.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/accumulate_field.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)

#### Args:
- value: ['Vector', 'Float', 'Integer']
- group_id: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

#### Returns:
- node with sockets ['leading', 'trailing', 'total']






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
    - Set the node property :attr:`attr_domain` to self in order to implement the transfer attribute
      mechanism.

#### Args:
- node (Node): The node created by the domain
    
#### Returns:
- The node argument




<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### attribute_statistic

```python
def attribute_statistic(self, attribute=None)
```



> Node: [Attribute Statistic](GeometryNodeAttributeStatistic.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)

#### Args:
- attribute: ['Float', 'Vector']

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

#### Returns:
- node with sockets ['mean', 'median', 'sum', 'min', 'max', 'range', 'standard_deviation', 'variance']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_attribute

```python
def blur_attribute(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_color

```python
def blur_color(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_float

```python
def blur_float(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_integer

```python
def blur_integer(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### blur_vector

```python
def blur_vector(self, value=None, iterations=None, weight=None)
```



> Node: [Blur Attribute](GeometryNodeBlurAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/l.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)

#### Args:
- value: ['Float', 'Integer', 'Vector', 'Color']
- iterations: Integer
- weight: Float

#### Returns:
- socket `value`






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

### capture_handle_type_selection

```python
def capture_handle_type_selection(self, left=True, right=True, handle_type='AUTO')
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_handle_type_selection_align

```python
def capture_handle_type_selection_align(self, left=True, right=True)
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_handle_type_selection_auto

```python
def capture_handle_type_selection_auto(self, left=True, right=True)
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_handle_type_selection_free

```python
def capture_handle_type_selection_free(self, left=True, right=True)
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### capture_handle_type_selection_vector

```python
def capture_handle_type_selection_vector(self, left=True, right=True)
```



> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

#### Returns:
- node with sockets ['selection']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### curve

```python
def curve(self)
```



> Node: [Curve of Point](GeometryNodeCurveOfPoint.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveOfPoint.webp)

#### Returns:
- node with sockets ['curve_index', 'index_in_curve']






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

### handle_positions

```python
def handle_positions(self, relative=None)
```



> Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Args:
- relative: Boolean

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputCurveHandlePositions.webp)

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

### index_of_nearest

```python
def index_of_nearest(self, position=None, group_id=None)
```



> Node: [Index of Nearest](GeometryNodeIndexOfNearest.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/n.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeIndexOfNearest.html)

#### Args:
- position: Vector
- group_id: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeIndexOfNearest.webp)

#### Returns:
- node with sockets ['index', 'has_neighbor']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### instance_on

```python
def instance_on(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```



> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances`






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### interpolate

```python
def interpolate(self, guide_curves=None, guide_up=None, guide_group_id=None, point_up=None, point_group_id=None, max_neighbors=None)
```



> Node: [Interpolate Curves](GeometryNodeInterpolateCurves.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/n.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInterpolateCurves.html)

#### Args:
- guide_curves: Geometry
- guide_up: Vector
- guide_group_id: Integer
- point_up: Vector
- point_group_id: Integer
- max_neighbors: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateCurves.webp)

#### Returns:
- node with sockets ['curves', 'closest_index', 'closest_weight']






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

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputNamedAttribute.webp)

#### Returns:
- node with sockets ['attribute', 'exists']






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
- node with sockets ['is_valid_offset', 'point_index']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity

```python
def proximity(self, target=None, source_position=None, target_element='FACES')
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector
- target_element (str): 'FACES' in [POINTS, EDGES, FACES]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeProximity.webp)

#### Returns:
- node with sockets ['position', 'distance']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_edges

```python
def proximity_edges(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeProximity.webp)

#### Returns:
- node with sockets ['position', 'distance']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_faces

```python
def proximity_faces(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeProximity.webp)

#### Returns:
- node with sockets ['position', 'distance']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### proximity_points

```python
def proximity_points(self, target=None, source_position=None)
```



> Node: [Geometry Proximity](GeometryNodeProximity.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeProximity.webp)

#### Returns:
- node with sockets ['position', 'distance']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast

```python
def raycast(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None, mapping='INTERPOLATED')
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float
- mapping (str): 'INTERPOLATED' in [INTERPOLATED, NEAREST]

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_interpolated

```python
def raycast_interpolated(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### raycast_nearest

```python
def raycast_nearest(self, target_geometry=None, attribute=None, source_position=None, ray_direction=None, ray_length=None)
```



> Node: [Raycast](GeometryNodeRaycast.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/raycast.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)

#### Args:
- target_geometry: Geometry
- attribute: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']
- source_position: Vector
- ray_direction: Vector
- ray_length: Float

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

#### Returns:
- node with sockets ['is_hit', 'hit_position', 'hit_normal', 'hit_distance', 'attribute']






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
- node with sockets ['selection', 'inverted']






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

### set_left_handle_positions

```python
def set_left_handle_positions(self, position=None, offset=None)
```



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector

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

### set_right_handle_positions

```python
def set_right_handle_positions(self, position=None, offset=None)
```



> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector

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

### store_named_2D_vector

```python
def store_named_2D_vector(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_attribute

```python
def store_named_attribute(self, name=None, value=None)
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
def store_named_boolean(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_byte_color

```python
def store_named_byte_color(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_color

```python
def store_named_color(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_float

```python
def store_named_float(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_integer

```python
def store_named_integer(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

### store_named_vector

```python
def store_named_vector(self, name=None, value=None)
```



> Node: [Store Named Attribute](GeometryNodeStoreNamedAttribute.md) | [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) | [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)

#### Args:
- name: String
- value: ['Vector', 'Float', 'Color', 'Boolean', 'Integer']

#### Returns:
- self






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

