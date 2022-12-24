# Node *Set Curve Normal*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/set_curve_normal.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)
- geonodes name: `SetCurveNormal`
- bl_idname: `GeometryNodeSetCurveNormal`

```python
from geonodes import nodes

node = nodes.SetCurveNormal(curve=None, selection=None, mode='MINIMUM_TWIST')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveNormal.webp)

### Args:

#### Input socket arguments:

- **curve**: [Curve](Curve.md)
- **selection**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **mode** (str): default = 'MINIMUM_TWIST' in ('MINIMUM_TWIST', 'Z_UP')

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Spline](Spline.md)** |
| [set_normal](Spline.md#set_normal) | `def set_normal(self, mode='MINIMUM_TWIST'):` |
| [normal](Spline.md#normal) | `@normal.setter
`<br> `def normal(self, attr_value):` |

<sub>Go to [top](#node-Set-Curve-Normal) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

