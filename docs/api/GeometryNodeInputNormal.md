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
| **[Curve](Curve.md)** |
| [normal](Curve.md#normal) | `@property`<br> `def normal(self):` |
| **[Domain](Domain.md)** |
| [normal](Domain.md#normal) | `@property`<br> `def normal(self):` |
| **[Instances](Instances.md)** |
| [normal](Instances.md#normal) | `@property`<br> `def normal(self):` |
| **[Mesh](Mesh.md)** |
| [normal](Mesh.md#normal) | `@property`<br> `def normal(self):` |
| **[Points](Points.md)** |
| [normal](Points.md#normal) | `@property`<br> `def normal(self):` |
| **[Spline](Spline.md)** |
| [normal](Spline.md#normal) | `@property`<br> `def normal(self):` |

<sub>Go to [top](#node-Normal) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

