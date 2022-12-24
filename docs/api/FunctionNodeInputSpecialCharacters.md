# Node *Special Characters*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/special_characters.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)
- geonodes name: `SpecialCharacters`
- bl_idname: `FunctionNodeInputSpecialCharacters`

```python
from geonodes import nodes

node = nodes.SpecialCharacters()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputSpecialCharacters.webp)

### Output sockets:

- **line_break** : [String](String.md)
- **tab** : [String](String.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[String](String.md)** |
| [LineBreak](String.md#LineBreak) | `@staticmethod`<br> `def LineBreak():` |
| [Tab](String.md#Tab) | `@staticmethod`<br> `def Tab():` |

<sub>Go to [top](#node-Special-Characters) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

