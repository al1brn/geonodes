# Node *Position*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/position.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)
- geonodes name: `Position`
- bl_idname: `GeometryNodeInputPosition`

```python
from geonodes import nodes

node = nodes.Position()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputPosition.webp)

### Output sockets:

- **position** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [position](Domain.md#position) | `@property`<br> `def position(self):` |
| **[Geometry](Geometry.md)** |
| [position](Geometry.md#position) | `@property`<br> `def position(self):` |

<sub>Go to [top](#node-Position) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

