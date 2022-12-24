# Node *Set Curve Tilt*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_tilt.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
- geonodes name: `SetCurveTilt`
- bl_idname: `GeometryNodeSetCurveTilt`

```python
from geonodes import nodes

node = nodes.SetCurveTilt(curve=None, selection=None, tilt=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveTilt.webp)

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)
- **tilt**: [Float](Float.md)

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [set_tilt](ControlPoint.md#set_tilt) | `def set_tilt(self, tilt=None):` |
| [tilt](ControlPoint.md#tilt) | `@tilt.setter
`<br> `def tilt(self, attr_value):` |

<sub>Go to [top](#node-Set-Curve-Tilt) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

