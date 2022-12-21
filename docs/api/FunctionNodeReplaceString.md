# Node Replace String

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)
- geonodes name: `ReplaceString`
- bl_idname: `FunctionNodeReplaceString`

```python
from geonodes import nodes

node = nodes.ReplaceString(string=None, find=None, replace=None)
```

### Args:

#### Input socket arguments:

- **string**: [String](String.md)
- **find**: [String](String.md)
- **replace**: [String](String.md)

### Output sockets:

- **string** : [String](String.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x168102a70>>](String.md#replace)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x168102aa0>>](function.md#replace_string)
