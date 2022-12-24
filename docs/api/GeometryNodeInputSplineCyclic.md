# Node *Is Spline Cyclic*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/is_spline_cyclic.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)
- geonodes name: `IsSplineCyclic`
- bl_idname: `GeometryNodeInputSplineCyclic`

```python
from geonodes import nodes

node = nodes.IsSplineCyclic()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputSplineCyclic.webp)

### Output sockets:

- **cyclic** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Spline](Spline.md)** |
| [cyclic](Spline.md#cyclic) | `@property`<br> `def cyclic(self):` |

<sub>Go to [top](#node-Is-Spline-Cyclic) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

