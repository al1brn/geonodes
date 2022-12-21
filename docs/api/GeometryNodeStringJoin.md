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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x168102ad0>>](String.md#join)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x168102b00>>](function.md#join_strings)
