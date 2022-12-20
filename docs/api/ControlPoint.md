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

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def curve(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Curve of Point](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/curve_of_point.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- tuple ('curve_index', 'index_in_curve')
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## domain_size

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def __len__(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Domain Size](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- geometry: Geometry
<sub>Go to [top](#class-ControlPoint)</sub>- component (str): 'MESH' in [MESH, POINTCLOUD, CURVE, INSTANCES]
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['point_count', 'edge_count', 'face_count', 'face_corner_count', 'spline_count', 'instance_count']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## endpoint_selection

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def endpoint_selection(self, start_size=None, end_size=None):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Endpoint Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/endpoint_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- start_size: Integer
<sub>Go to [top](#class-ControlPoint)</sub>- end_size: Integer
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'selection'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## handle_positions

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def handle_positions(self, relative=None):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- relative: Boolean
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['left', 'right']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## handle_type_selection

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def handle_type_selection(self, left=True, right=True, handle_type='AUTO'):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
<sub>Go to [top](#class-ControlPoint)</sub>- mode (set): {'RIGHT', 'LEFT'}
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['selection']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## handle_type_selection

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def handle_type_selection_free(self, left=True, right=True):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
<sub>Go to [top](#class-ControlPoint)</sub>- mode (set): {'RIGHT', 'LEFT'}
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['selection']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## handle_type_selection

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def handle_type_selection_auto(self, left=True, right=True):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
<sub>Go to [top](#class-ControlPoint)</sub>- mode (set): {'RIGHT', 'LEFT'}
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['selection']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## handle_type_selection

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def handle_type_selection_vector(self, left=True, right=True):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
<sub>Go to [top](#class-ControlPoint)</sub>- mode (set): {'RIGHT', 'LEFT'}
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['selection']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## handle_type_selection

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def handle_type_selection_align(self, left=True, right=True):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
<sub>Go to [top](#class-ControlPoint)</sub>- mode (set): {'RIGHT', 'LEFT'}
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['selection']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## handle_type_selection_node

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def handle_type_selection_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Handle Type Selection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/handle_type_selection.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
<sub>Go to [top](#class-ControlPoint)</sub>- mode (set): {'RIGHT', 'LEFT'}
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'selection'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## instance_on_points

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def instance_on_points(self, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Instance on Points](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- instance: Geometry
<sub>Go to [top](#class-ControlPoint)</sub>- pick_instance: Boolean
<sub>Go to [top](#class-ControlPoint)</sub>- instance_index: Integer
<sub>Go to [top](#class-ControlPoint)</sub>- rotation: Vector
<sub>Go to [top](#class-ControlPoint)</sub>- scale: Vector
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'instances'<sub>Go to [top](#class-ControlPoint)</sub> of class Instances
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## left_handle_positions <span style="color:blue">*property*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def left_handle_positions(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'left'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## left_handle_positions <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def left_handle_positions(self, attr_value):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

<sub>Go to [top](#class-ControlPoint)</sub>Node implemented as property setter.

<sub>Go to [top](#class-ControlPoint)</sub>        ###Args:<sub>Go to [top](#class-ControlPoint)</sub>- attr_value: position
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## offset

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def offset(self, offset=None):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Offset Point in Curve](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve_topology/offset_point_in_curve.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- offset: Integer
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- tuple ('is_valid_offset', 'point_index')
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## parameter <span style="color:blue">*property*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def parameter(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- tuple ('factor', 'length', 'index')
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## parameter_factor <span style="color:blue">*property*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def parameter_factor(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'factor'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## parameter_index <span style="color:blue">*property*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def parameter_index(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'index'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## parameter_length <span style="color:blue">*property*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def parameter_length(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Spline Parameter](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/spline_parameter.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'length'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## radius <span style="color:blue">*property*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def radius(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'radius'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## radius <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def radius(self, attr_value):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html) )

<sub>Go to [top](#class-ControlPoint)</sub>Node implemented as property setter.

<sub>Go to [top](#class-ControlPoint)</sub>        ###Args:<sub>Go to [top](#class-ControlPoint)</sub>- attr_value: radius
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## right_handle_positions <span style="color:blue">*property*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def right_handle_positions(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Curve Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'right'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## right_handle_positions <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def right_handle_positions(self, attr_value):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

<sub>Go to [top](#class-ControlPoint)</sub>Node implemented as property setter.

<sub>Go to [top](#class-ControlPoint)</sub>        ###Args:<sub>Go to [top](#class-ControlPoint)</sub>- attr_value: position
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## set_handle_positions

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def set_handle_positions(self, position=None, offset=None, mode='LEFT'):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- position: Vector
<sub>Go to [top](#class-ControlPoint)</sub>- offset: Vector
<sub>Go to [top](#class-ControlPoint)</sub>- mode (str): 'LEFT' in [LEFT, RIGHT]
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## set_handle_positions_left

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def set_handle_positions_left(self, curve=None, position=None, offset=None):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- curve: Curve
<sub>Go to [top](#class-ControlPoint)</sub>- position: Vector
<sub>Go to [top](#class-ControlPoint)</sub>- offset: Vector
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## set_handle_positions_right

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def set_handle_positions_right(self, curve=None, position=None, offset=None):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Handle Positions](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_positions.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- curve: Curve
<sub>Go to [top](#class-ControlPoint)</sub>- position: Vector
<sub>Go to [top](#class-ControlPoint)</sub>- offset: Vector
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## set_handle_type

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def set_handle_type(self, left=True, right=True, handle_type='AUTO'):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- curve: Curve
<sub>Go to [top](#class-ControlPoint)</sub>- selection: Boolean
<sub>Go to [top](#class-ControlPoint)</sub>- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
<sub>Go to [top](#class-ControlPoint)</sub>- mode (set): {'RIGHT', 'LEFT'}
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## set_handle_type_node

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def set_handle_type_node(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Handle Type](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_handle_type.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- handle_type (str): 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
<sub>Go to [top](#class-ControlPoint)</sub>- mode (set): {'RIGHT', 'LEFT'}
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## set_radius

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def set_radius(self, radius=None):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Curve Radius](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- radius: Float
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## set_tilt

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def set_tilt(self, tilt=None):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Args:
<sub>Go to [top](#class-ControlPoint)</sub>- tilt: Float
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>- node with sockets ['curve']
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## tangent <span style="color:blue">*property*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def tangent(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Curve Tangent](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'tangent'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## tilt <span style="color:blue">*property*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def tilt(self):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tilt.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html) )

<sub>Go to [top](#class-ControlPoint)</sub>### Returns:

<sub>Go to [top](#class-ControlPoint)</sub>  socket 'tilt'<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>## tilt <span style="color:blue">*etter*</span>

<sub>Go to [top](#class-ControlPoint)</sub>```python
<sub>Go to [top](#class-ControlPoint)</sub>def tilt(self, attr_value):

<sub>Go to [top](#class-ControlPoint)</sub>```
<sub>Go to [top](#class-ControlPoint)</sub>Node [Set Curve Tilt](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html) ( [api](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html) )

<sub>Go to [top](#class-ControlPoint)</sub>Node implemented as property setter.

<sub>Go to [top](#class-ControlPoint)</sub>        ###Args:<sub>Go to [top](#class-ControlPoint)</sub>- attr_value: tilt
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>
<sub>Go to [top](#class-ControlPoint)</sub>