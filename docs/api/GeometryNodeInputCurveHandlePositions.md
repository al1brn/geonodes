# Node *Curve Handle Positions*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
- geonodes name: `CurveHandlePositions`
- bl_idname: `GeometryNodeInputCurveHandlePositions`

```python
from geonodes import nodes

node = nodes.CurveHandlePositions(relative=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputCurveHandlePositions.webp)

### Args:

#### Input socket arguments:

- **relative**: [Boolean](Boolean.md)

### Output sockets:

- **left** : [Vector](Vector.md)
- **right** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [handle_positions](ControlPoint.md#handle_positions) | `def handle_positions(self, relative=None):` |
| [left_handle_positions](ControlPoint.md#left_handle_positions) | `@property`<br> `def left_handle_positions(self):` |
| [right_handle_positions](ControlPoint.md#right_handle_positions) | `@property`<br> `def right_handle_positions(self):` |

<sub>Go to [top](#node-Curve-Handle-Positions) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

