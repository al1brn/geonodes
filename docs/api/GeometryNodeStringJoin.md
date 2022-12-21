# Node Join Strings

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/join_strings.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
- geonodes name: `JoinStrings`
- bl_idname: `GeometryNodeStringJoin`

```python
from geonodes import nodes

node = nodes.JoinStrings(*strings, delimiter=None)
```

### Args:

#### Input socket arguments:

- **delimiter**: [String](String.md)
- **strings**: *[String](String.md)

### Output sockets:

- **string** : [String](String.md)

## Implementation

#### Global functions

 - [join_strings](A.md#join_strings)
#### class [String](String.md)

 - [join](String.md#join)
