# Node *Replace String*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/replace_string.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)
- geonodes name: `ReplaceString`
- bl_idname: `FunctionNodeReplaceString`

```python
from geonodes import nodes

node = nodes.ReplaceString(string=None, find=None, replace=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeReplaceString.webp)

### Args:

#### Input socket arguments:

- **string**: [String](String.md)
- **find**: [String](String.md)
- **replace**: [String](String.md)

### Output sockets:

- **string** : [String](String.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[String](String.md)** |
| [replace](String.md#replace) | `def replace(self, find=None, replace=None):` |
| Global functions |
| [replace_string](functions.md#replace_string) | `def replace_string(string=None, find=None, replace=None):` |

<sub>Go to [top](#node-Replace-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

