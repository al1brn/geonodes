# Node *ID*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/id.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)
- geonodes name: `ID`
- bl_idname: `GeometryNodeInputID`

```python
from geonodes import nodes

node = nodes.ID()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputID.webp)

### Output sockets:

- **ID** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [ID](Domain.md#ID) | `@property`<br> `def ID(self):` |
| **[Geometry](Geometry.md)** |
| [ID](Geometry.md#ID) | `@property`<br> `def ID(self):` |

<sub>Go to [top](#node-ID) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

