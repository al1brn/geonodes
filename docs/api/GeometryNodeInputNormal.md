# Node *Normal*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/normal.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)
- geonodes name: `Normal`
- bl_idname: `GeometryNodeInputNormal`

```python
from geonodes import nodes

node = nodes.Normal()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputNormal.webp)

### Output sockets:

- **normal** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [normal](Domain.md#normal) | `@property`<br> `def normal(self):` |
| **[Geometry](Geometry.md)** |
| [normal](Geometry.md#normal) | `@property`<br> `def normal(self):` |
| **[Spline](Spline.md)** |
| [normal](Spline.md#normal) | `@property`<br> `def normal(self):` |

<sub>Go to [top](#node-Normal) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

