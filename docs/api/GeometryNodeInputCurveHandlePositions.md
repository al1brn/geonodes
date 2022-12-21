# Node 'Curve Handle Positions'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_handle_position.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
- geonodes name: `CurveHandlePositions`
- bl_idname: `GeometryNodeInputCurveHandlePositions`

```python
from geonodes import nodes

node = nodes.CurveHandlePositions(relative=None)
```

[Blender Image](self.node_image_ref)

### Args:

#### Input socket arguments:

- **relative**: [Boolean](Boolean.md)

### Output sockets:

- **left** : [Vector](Vector.md)
- **right** : [Vector](Vector.md)

## Implementation

### [ControlPoint](ControlPoint.md)

| Name | Definition |
|------|------------|
 | [handle_positions](ControlPoint.md#handle_positions) | `def handle_positions(self, relative=None):` |
 | [left_handle_positions](ControlPoint.md#left_handle_positions-property) | `def left_handle_positions(self):` |
 | [right_handle_positions](ControlPoint.md#right_handle_positions-property) | `def right_handle_positions(self):` |

<sub>Go to [top](#node-Curve-Handle-Positions) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

