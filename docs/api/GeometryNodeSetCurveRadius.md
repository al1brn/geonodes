# Node *Set Curve Radius*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_radius.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)
- geonodes name: `SetCurveRadius`
- bl_idname: `GeometryNodeSetCurveRadius`

```python
from geonodes import nodes

node = nodes.SetCurveRadius(curve=None, selection=None, radius=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveRadius.webp)

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)
- **radius**: [Float](Float.md)

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [set_radius](ControlPoint.md#set_radius) | `def set_radius(self, radius=None):` |
| [radius](ControlPoint.md#radius) | `@radius.setter
`<br> `def radius(self, attr_value):` |

<sub>Go to [top](#node-Set-Curve-Radius) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

