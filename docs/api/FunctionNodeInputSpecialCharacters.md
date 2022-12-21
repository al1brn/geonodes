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

#### [String](String.md)

 - [LineBreak](String.md#LineBreak-staticmethod)
  ```python
  nodes.SpecialCharacters(  ```

 - [Tab](String.md#Tab-staticmethod)
  ```python
  nodes.SpecialCharacters(  ```

