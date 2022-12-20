# class ControlPoint

## Properties

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
- [domain_size](#domain_size)
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
- [set_handle_positions](#set_handle_positions)
- [set_handle_positions_left](#set_handle_positions_left)
- [set_handle_positions_right](#set_handle_positions_right)
- [set_handle_type](#set_handle_type)
- [set_handle_type_node](#set_handle_type_node)
- [set_radius](#set_radius)
- [set_tilt](#set_tilt)

## curve

```python
def curve(self):

```
Node [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html) )

### Returns:
- tuple ('`curve_index`', '`index_in_curve`')

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## domain_size

```python
def __len__(self):

```
Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

### Args:
- geometry: Geometry
- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]

### Returns:
- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## endpoint_selection

```python
def endpoint_selection(self, start_size=None, end_size=None):

```
Node [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html) )

### Args:
- start_size: Integer
- end_size: Integer

### Returns:
- socket `selection`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## handle_positions

```python
def handle_positions(self, relative=None):

```
Node [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html) )

### Args:
- relative: Boolean

### Returns:
- node with sockets ['left', 'right']

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## handle_type_selection

```python
def handle_type_selection(self, left=True, right=True, handle_type='AUTO'):

```
Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## handle_type_selection

```python
def handle_type_selection_free(self, left=True, right=True):

```
Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## handle_type_selection

```python
def handle_type_selection_auto(self, left=True, right=True):

```
Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## handle_type_selection

```python
def handle_type_selection_vector(self, left=True, right=True):

```
Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## handle_type_selection

```python
def handle_type_selection_align(self, left=True, right=True):

```
Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:
- node with sockets ['selection']

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## handle_type_selection_node

```python
def handle_type_selection_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):

```
Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:
- socket `selection`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## instance_on_points

```python
def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

```
Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

### Args:
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

### Returns:
- socket `instances` of class Instances

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## left_handle_positions <sub>*property*</sub>

```python
def left_handle_positions(self):

```
Node [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html) )

### Returns:
- socket `left`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## left_handle_positions <sub>*etter*</sub>

```python
def left_handle_positions(self, attr_value):

```
Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

Node implemented as property setter.

        ###Args:
- attr_value: position


<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## offset

```python
def offset(self, offset=None):

```
Node [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html) )

### Args:
- offset: Integer

### Returns:
- tuple ('`is_valid_offset`', '`point_index`')

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## parameter <sub>*property*</sub>

```python
def parameter(self):

```
Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html) )

### Returns:
- tuple ('`factor`', '`length`', '`index`')

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## parameter_factor <sub>*property*</sub>

```python
def parameter_factor(self):

```
Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html) )

### Returns:
- socket `factor`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## parameter_index <sub>*property*</sub>

```python
def parameter_index(self):

```
Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html) )

### Returns:
- socket `index`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## parameter_length <sub>*property*</sub>

```python
def parameter_length(self):

```
Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html) )

### Returns:
- socket `length`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## radius <sub>*property*</sub>

```python
def radius(self):

```
Node [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html) )

### Returns:
- socket `radius`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## radius <sub>*etter*</sub>

```python
def radius(self, attr_value):

```
Node [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html) )

Node implemented as property setter.

        ###Args:
- attr_value: radius


<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## right_handle_positions <sub>*property*</sub>

```python
def right_handle_positions(self):

```
Node [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html) )

### Returns:
- socket `right`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## right_handle_positions <sub>*etter*</sub>

```python
def right_handle_positions(self, attr_value):

```
Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

Node implemented as property setter.

        ###Args:
- attr_value: position


<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## set_handle_positions

```python
def set_handle_positions(self, position=None, offset=None, mode='LEFT'):

```
Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

### Args:
- position: Vector
- offset: Vector
- mode (str): 'LEFT' in [LEFT, RIGHT]

### Returns:
- self

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## set_handle_positions_left

```python
def set_handle_positions_left(self, curve=None, position=None, offset=None):

```
Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

### Args:
- curve: Curve
- position: Vector
- offset: Vector

### Returns:
- self

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## set_handle_positions_right

```python
def set_handle_positions_right(self, curve=None, position=None, offset=None):

```
Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

### Args:
- curve: Curve
- position: Vector
- offset: Vector

### Returns:
- self

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## set_handle_type

```python
def set_handle_type(self, left=True, right=True, handle_type='AUTO'):

```
Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html) )

### Args:
- curve: Curve
- selection: Boolean
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:
- node with sockets ['curve']

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## set_handle_type_node

```python
def set_handle_type_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):

```
Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html) )

### Args:
- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
- mode (set): {'RIGHT', 'LEFT'}

### Returns:
- self

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## set_radius

```python
def set_radius(self, radius=None):

```
Node [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html) )

### Args:
- radius: Float

### Returns:
- self

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## set_tilt

```python
def set_tilt(self, tilt=None):

```
Node [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html) )

### Args:
- tilt: Float

### Returns:
- self

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## tangent <sub>*property*</sub>

```python
def tangent(self):

```
Node [Curve Tangent](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html) )

### Returns:
- socket `tangent`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## tilt <sub>*property*</sub>

```python
def tilt(self):

```
Node [Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tilt.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html) )

### Returns:
- socket `tilt`

<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

## tilt <sub>*etter*</sub>

```python
def tilt(self, attr_value):

```
Node [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html) )

Node implemented as property setter.

        ###Args:
- attr_value: tilt


<sub>Go to [top](#class-ControlPoint)</sub> [data structure](../structure.md)

