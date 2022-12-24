# Node *Set Position*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_position.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)
- geonodes name: `SetPosition`
- bl_idname: `GeometryNodeSetPosition`

```python
from geonodes import nodes

node = nodes.SetPosition(geometry=None, selection=None, position=None, offset=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetPosition.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **position**: [Vector](Vector.md)
- **offset**: [Vector](Vector.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [set_position](Domain.md#set_position) | `def set_position(self, position=None, offset=None):` |
| [position](Domain.md#position) | `@position.setter
`<br> `def position(self, attr_value):` |
| **[Geometry](Geometry.md)** |
| [set_position](Geometry.md#set_position) | `def set_position(self, selection=None, position=None, offset=None):` |

<sub>Go to [top](#node-Set-Position) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

