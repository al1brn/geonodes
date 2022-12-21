# Node String Length

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)
- geonodes name: `StringLength`
- bl_idname: `FunctionNodeStringLength`

```python
from geonodes import nodes

node = nodes.StringLength(string=None)
```

### Args:

#### Input socket arguments:

- **string**: [String](String.md)

### Output sockets:

- **length** : [Integer](Integer.md)

## Implementation

#### class [String](String.md)

 - [length](String.md#length-property)
#### Global functions

 - [string_length](function.md#string_length)