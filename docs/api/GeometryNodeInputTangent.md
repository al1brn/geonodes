# Node *Curve Tangent*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_tangent.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)
- geonodes name: `CurveTangent`
- bl_idname: `GeometryNodeInputTangent`

```python
from geonodes import nodes

node = nodes.CurveTangent()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputTangent.webp)

### Output sockets:

- **tangent** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[ControlPoint](ControlPoint.md)** |
| [tangent](ControlPoint.md#tangent) | `@property`<br> `def tangent(self):` |

<sub>Go to [top](#node-Curve-Tangent) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

