# class ControlPoint

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)


# Class ControlPoint

Radius and tilt


## tangent

Tangent attribute

Returns:
  Vector
  
getter: :class:`~geonodes.nodes.nodes.CurveTangent`
setter: read only



## set_handle_type

Set handle type

Args:
  handle_type (str): in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
  mode (set of strs): {'LEFT', 'RIGHT'}
  
  
  

## handle_positions

Handle positions node

Args:
  relative (Boolean): relative
  
Returns:
  node CurveHandlePositions
  
Output sockets:
- left : Vector
- right : Vector
  
  

## set_handle_positions

Set handle positions

Args:
  position (Vector): Positions
  offset (Vector): Offset
  mode (str): 'LEFT' or 'RIGHT'
  
- setter: :class:`~geonodes.nodes.nodes.SetHandlePositions`
  
  
  

## left_handles

Left handle positions

Args:
  relative (Boolean): relative
  
Returns:
  Vector: the left output socket of node *CurveHandlePositions*
  
  
  

## right_handles

Right handle positions

Args:
  relative (Boolean): relative
  
Returns:
  Vector: the right output socket of node *CurveHandlePositions*
  
  

## handles_selection

Handle type selection

Args:
  handle_type (str): in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
  left (bool): select left handle
  right (bool): select right handle
  
Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`




## handle_auto

Auto Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## handle_free

Free Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## handle_vector

Vector Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## handle_align

Align Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_auto

Left Auto Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_auto

Right Auto Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_free

Left Free Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_free

Right Free Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_vector

Left Vector Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_vector

Right Vector Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_align

Left Align Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_align

Right Align Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## parameter

Spline parameter attribute

Returns:
  Node SplineParameter
  
Output sockets:
- factor : Float
- length : Float
- index : Integer
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## parameter_factor

Parameter factor attribute

Returns:
  Float: factor socket of parameter
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## parameter_length

Parameter length attribute

Returns:
  Float: length socket of parameter
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## parameter_index

Parameter factor attribute

Returns:
  Integer: index socket of parameter
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## curve_of_point

Curve topology Blender 3.4


## delete

Delete points

Node :class:`~geonodes.nodes.nodes.DeleteGeometry`

Returns:
  self
  
.. code-block:: python

  curve.points(...).delete()
  
  > see [examples](#examples)

## Properties

- [count](#count-property)
- [left_handle_positions](#left_handle_positions-property)
- [parameter](#parameter-property)
- [parameter_factor](#parameter_factor-property)
- [parameter_index](#parameter_index-property)
- [parameter_length](#parameter_length-property)
- [radius](#radius-property)
- [right_handle_positions](#right_handle_positions-property)
- [tangent](#tangent-property)
- [tilt](#tilt-property)



## Methods

- [curve](#curve)
- [delete](#delete)
- [duplicate](#duplicate)
- [endpoint_selection](#endpoint_selection)
- [handle_positions](#handle_positions)
- [handle_type_selection](#handle_type_selection)
- [handle_type_selection](#handle_type_selection)
- [handle_type_selection](#handle_type_selection)
- [handle_type_selection](#handle_type_selection)
- [handle_type_selection](#handle_type_selection)
- [handle_type_selection_node](#handle_type_selection_node)
- [instance_on_points](#instance_on_points)
- [offset](#offset)
- [proximity](#proximity)
- [separate](#separate)
- [set_handle_positions](#set_handle_positions)
- [set_handle_positions_left](#set_handle_positions_left)
- [set_handle_positions_right](#set_handle_positions_right)
- [set_handle_type](#set_handle_type)
- [set_handle_type_node](#set_handle_type_node)
- [set_radius](#set_radius)
- [set_tilt](#set_tilt)

## count <sub>*property*</sub>

```python
def count(self, geometry=None):

```
> Node: [Domain Size](GeometryNodeAttributeDomainSize.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)

#### Returns:
- socket `point_count`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## curve

```python
def curve(self):

```
> Node: [Curve of Point](GeometryNodeCurveOfPoint.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveOfPoint.webp)

#### Returns:
- tuple ('`curve_index`', '`index_in_curve`')

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## delete

```python
def delete(self, mode='ALL'):

```
> Node: [Delete Geometry](GeometryNodeDeleteGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/delete_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)

#### Args:
- mode (str): 'ALL' in [ALL, EDGE_FACE, ONLY_FACE]

#### Returns:
- self

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## duplicate

```python
def duplicate(self, amount=None):

```
> Node: [Duplicate Elements](GeometryNodeDuplicateElements.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/duplicate_elements.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)

#### Args:
- amount: Integer

#### Returns:
- socket `duplicate_index`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## endpoint_selection

```python
def endpoint_selection(self, start_size=None, end_size=None):

```
> Node: [Endpoint Selection](GeometryNodeCurveEndpointSelection.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)

#### Args:
- start_size: Integer
- end_size: Integer

#### Returns:
- socket `selection`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## handle_positions

```python
def handle_positions(self, relative=None):

```
> Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Args:
- relative: Boolean

#### Returns:
- node with sockets ['left', 'right']

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## handle_type_selection

```python
def handle_type_selection(self, left=True, right=True, handle_type='AUTO'):

```
> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## handle_type_selection

```python
def handle_type_selection_free(self, left=True, right=True):

```
> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## handle_type_selection

```python
def handle_type_selection_auto(self, left=True, right=True):

```
> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## handle_type_selection

```python
def handle_type_selection_vector(self, left=True, right=True):

```
> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## handle_type_selection

```python
def handle_type_selection_align(self, left=True, right=True):

```
> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## handle_type_selection_node

```python
def handle_type_selection_node(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):

```
> Node: [Handle Type Selection](GeometryNodeCurveHandleTypeSelection.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- socket `selection`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## instance_on_points

```python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
> Node: [Instance on Points](GeometryNodeInstanceOnPoints.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)

#### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Returns:
- socket `instances` of class Instances

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## left_handle_positions <sub>*property*</sub>

```python
def left_handle_positions(self):

```
> Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Returns:
- socket `left`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## left_handle_positions <sub>*etter*</sub>

```python
def left_handle_positions(self, attr_value):

```
> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

Node implemented as property setter.

#### Args:
- attr_value: position


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## offset

```python
def offset(self, offset=None):

```
> Node: [Offset Point in Curve](GeometryNodeOffsetPointInCurve.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)

#### Args:
- offset: Integer

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetPointInCurve.webp)

#### Returns:
- tuple ('`is_valid_offset`', '`point_index`')

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## parameter <sub>*property*</sub>

```python
def parameter(self):

```
> Node: [Spline Parameter](GeometryNodeSplineParameter.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplineParameter.webp)

#### Returns:
- tuple ('`factor`', '`length`', '`index`')

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## parameter_factor <sub>*property*</sub>

```python
def parameter_factor(self):

```
> Node: [Spline Parameter](GeometryNodeSplineParameter.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- socket `factor`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## parameter_index <sub>*property*</sub>

```python
def parameter_index(self):

```
> Node: [Spline Parameter](GeometryNodeSplineParameter.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- socket `index`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## parameter_length <sub>*property*</sub>

```python
def parameter_length(self):

```
> Node: [Spline Parameter](GeometryNodeSplineParameter.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)

#### Returns:
- socket `length`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## proximity

```python
def proximity(self, target=None, source_position=None):

```
> Node: [Geometry Proximity](GeometryNodeProximity.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_proximity.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)

#### Args:
- target: Geometry
- source_position: Vector

#### Returns:
- socket `distance`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## radius <sub>*property*</sub>

```python
def radius(self):

```
> Node: [Radius](GeometryNodeInputRadius.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)

#### Returns:
- socket `radius`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## radius <sub>*etter*</sub>

```python
def radius(self, attr_value):

```
> Node: [Set Curve Radius](GeometryNodeSetCurveRadius.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

Node implemented as property setter.

#### Args:
- attr_value: radius


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## right_handle_positions <sub>*property*</sub>

```python
def right_handle_positions(self):

```
> Node: [Curve Handle Positions](GeometryNodeInputCurveHandlePositions.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)

#### Returns:
- socket `right`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## right_handle_positions <sub>*etter*</sub>

```python
def right_handle_positions(self, attr_value):

```
> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

Node implemented as property setter.

#### Args:
- attr_value: position


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## separate

```python
def separate(self, geometry=None):

```
> Node: [Separate Geometry](GeometryNodeSeparateGeometry.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_geometry.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)

#### Args:
- geometry: Geometry

![Node Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

#### Returns:
- tuple ('`selection`', '`inverted`')

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_handle_positions

```python
def set_handle_positions(self, position=None, offset=None, mode='LEFT'):

```
> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector
- mode (str): 'LEFT' in [LEFT, RIGHT]

#### Returns:
- self

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_handle_positions_left

```python
def set_handle_positions_left(self, position=None, offset=None):

```
> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- self

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_handle_positions_right

```python
def set_handle_positions_right(self, position=None, offset=None):

```
> Node: [Set Handle Positions](GeometryNodeSetCurveHandlePositions.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)

#### Args:
- position: Vector
- offset: Vector

#### Returns:
- self

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_handle_type

```python
def set_handle_type(self, left=True, right=True, handle_type='AUTO'):

```
> Node: [Set Handle Type](GeometryNodeCurveSetHandles.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

#### Args:
- curve: Curve
- selection: Boolean
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- node with sockets ['curve']

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_handle_type_node

```python
def set_handle_type_node(self, handle_type='AUTO', mode={'LEFT', 'RIGHT'}):

```
> Node: [Set Handle Type](GeometryNodeCurveSetHandles.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)

#### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'LEFT', 'RIGHT'}

#### Returns:
- self

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_radius

```python
def set_radius(self, radius=None):

```
> Node: [Set Curve Radius](GeometryNodeSetCurveRadius.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)

#### Args:
- radius: Float

#### Returns:
- self

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## set_tilt

```python
def set_tilt(self, tilt=None):

```
> Node: [Set Curve Tilt](GeometryNodeSetCurveTilt.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

#### Args:
- tilt: Float

#### Returns:
- self

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## tangent <sub>*property*</sub>

```python
def tangent(self):

```
> Node: [Curve Tangent](GeometryNodeInputTangent.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)

#### Returns:
- socket `tangent`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## tilt <sub>*property*</sub>

```python
def tilt(self):

```
> Node: [Curve Tilt](GeometryNodeInputCurveTilt.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tilt.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)

#### Returns:
- socket `tilt`

<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

## tilt <sub>*etter*</sub>

```python
def tilt(self, attr_value):

```
> Node: [Set Curve Tilt](GeometryNodeSetCurveTilt.md) - [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) - [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)

Node implemented as property setter.

#### Args:
- attr_value: tilt


<sub>Go to [top](#class-ControlPoint) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>


# Class ControlPoint

Radius and tilt


## tangent

Tangent attribute

Returns:
  Vector
  
getter: :class:`~geonodes.nodes.nodes.CurveTangent`
setter: read only



## set_handle_type

Set handle type

Args:
  handle_type (str): in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
  mode (set of strs): {'LEFT', 'RIGHT'}
  
  
  

## handle_positions

Handle positions node

Args:
  relative (Boolean): relative
  
Returns:
  node CurveHandlePositions
  
Output sockets:
- left : Vector
- right : Vector
  
  

## set_handle_positions

Set handle positions

Args:
  position (Vector): Positions
  offset (Vector): Offset
  mode (str): 'LEFT' or 'RIGHT'
  
- setter: :class:`~geonodes.nodes.nodes.SetHandlePositions`
  
  
  

## left_handles

Left handle positions

Args:
  relative (Boolean): relative
  
Returns:
  Vector: the left output socket of node *CurveHandlePositions*
  
  
  

## right_handles

Right handle positions

Args:
  relative (Boolean): relative
  
Returns:
  Vector: the right output socket of node *CurveHandlePositions*
  
  

## handles_selection

Handle type selection

Args:
  handle_type (str): in ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
  left (bool): select left handle
  right (bool): select right handle
  
Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`




## handle_auto

Auto Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## handle_free

Free Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## handle_vector

Vector Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## handle_align

Align Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_auto

Left Auto Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_auto

Right Auto Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_free

Left Free Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_free

Right Free Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_vector

Left Vector Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_vector

Right Vector Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## left_handle_align

Left Align Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## right_handle_align

Right Align Handle selection

Returns:
  Boolean
  
getter: :class:`~geonodes.nodes.nodes.HandleTypeSelection`



## parameter

Spline parameter attribute

Returns:
  Node SplineParameter
  
Output sockets:
- factor : Float
- length : Float
- index : Integer
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## parameter_factor

Parameter factor attribute

Returns:
  Float: factor socket of parameter
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## parameter_length

Parameter length attribute

Returns:
  Float: length socket of parameter
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## parameter_index

Parameter factor attribute

Returns:
  Integer: index socket of parameter
  
getter: :class:`~geonodes.nodes.nodes.SplineParameter`
setter: read only



## curve_of_point

Curve topology Blender 3.4


## delete

Delete points

Node :class:`~geonodes.nodes.nodes.DeleteGeometry`

Returns:
  self
  
.. code-block:: python

  curve.points(...).delete()
  
  