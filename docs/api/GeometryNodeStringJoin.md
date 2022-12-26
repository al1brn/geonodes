# Node *Join Strings*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
- geonodes name: `JoinStrings`
- bl_idname: `GeometryNodeStringJoin`

```python
from geonodes import nodes

node = nodes.JoinStrings(*strings, delimiter=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStringJoin.webp)

### Args:

#### Input socket arguments:

- **delimiter**: [String](String.md)
- **strings**: *[String](String.md)

### Output sockets:

- **string** : [String](String.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[String](String.md)** |
| [join](String.md#join) | `def join(self, *strings):` |
| [string_join](String.md#string_join) | `def string_join(*strings, delimiter=None):` |
| Global functions |
| [join_strings](functions.md#join_strings) | `def join_strings(*strings, delimiter=None):` |

<sub>Go to [top](#node-Join-Strings) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

