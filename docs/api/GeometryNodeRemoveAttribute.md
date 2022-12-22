# Node *Remove Named Attribute*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)
- geonodes name: `RemoveNamedAttribute`
- bl_idname: `GeometryNodeRemoveAttribute`

```python
from geonodes import nodes

node = nodes.RemoveNamedAttribute(geometry=None, name=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRemoveAttribute.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)
- **name**: [String](String.md)

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Domain](Domain.md)** |
| [remove_named_attribute](Domain.md#remove_named_attribute) | `def remove_named_attribute(self, name=None):` |
| **[Geometry](Geometry.md)** |
| [remove_named_attribute](Geometry.md#remove_named_attribute) | `def remove_named_attribute(self, name=None):` |

<sub>Go to [top](#node-Remove-Named-Attribute) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

