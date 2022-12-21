# Node Special Characters

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)
- geonodes name: `SpecialCharacters`
- bl_idname: `FunctionNodeInputSpecialCharacters`

```python
from geonodes import nodes

node = nodes.SpecialCharacters()
```

### Output sockets:

- **line_break** : [String](String.md)
- **tab** : [String](String.md)

## Implementation

#### class [String](String.md)

 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x168102650>>](String.md#LineBreak-staticmethod)
 - [<bound method Generator.fname of <generator.code_gen.Static object at 0x168102620>>](String.md#Tab-staticmethod)
