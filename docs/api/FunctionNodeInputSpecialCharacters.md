# Node 'Special Characters'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)
- geonodes name: `SpecialCharacters`
- bl_idname: `FunctionNodeInputSpecialCharacters`

```python
from geonodes import nodes

node = nodes.SpecialCharacters()
```

[Blender Image](self.node_image_ref)

### Output sockets:

- **line_break** : [String](String.md)
- **tab** : [String](String.md)

## Implementation

### [String](String.md)

| Name | Definition |
|------|------------|
 | [LineBreak](String.md#LineBreak-staticmethod) | `def LineBreak():` |
 | [Tab](String.md#Tab-staticmethod) | `def Tab():` |

<sub>Go to [top](#node-Special-Characters) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

