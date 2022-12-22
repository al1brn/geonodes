# Node *Set ID*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/set_id.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)
- geonodes name: `SetID`
- bl_idname: `GeometryNodeSetID`

```python
from geonodes import nodes

node = nodes.SetID(geometry=None, selection=None, ID=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetID.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **selection**: [Boolean](Boolean.md)
- **ID**: [Integer](Integer.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [set_ID](Domain.md#set_ID) | `def set_ID(self, ID=None):` |
| [ID](Domain.md#ID) | `@ID.setter
`<br> `def ID(self, attr_value):` |
| **[Geometry](Geometry.md)** |
| [set_ID](Geometry.md#set_ID) | `def set_ID(self, selection=None, ID=None):` |

<sub>Go to [top](#node-Set-ID) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

