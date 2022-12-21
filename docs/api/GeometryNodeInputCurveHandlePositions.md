# Node Curve Handle Positions

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
- geonodes name: `CurveHandlePositions`
- bl_idname: `GeometryNodeInputCurveHandlePositions`

```python
from geonodes import nodes

node = nodes.CurveHandlePositions(relative=None)
```

### Args:

#### Input socket arguments:

- **relative**: [Boolean](Boolean.md)

### Output sockets:

- **left** : [Vector](Vector.md)
- **right** : [Vector](Vector.md)

## Implementation

#### [ControlPoint](ControlPoint.md)

 - [handle_positions](ControlPoint.md#handle_positions) ```python nodes.CurveHandlePositions(relative=relative````
 - [left_handle_positions](ControlPoint.md#left_handle_positions-property) ```python nodes.CurveHandlePositions(relative=None````
 - [right_handle_positions](ControlPoint.md#right_handle_positions-property) ```python nodes.CurveHandlePositions(relative=None````
