# Node *String Length*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/string_length.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)
- geonodes name: `StringLength`
- bl_idname: `FunctionNodeStringLength`

```python
from geonodes import nodes

node = nodes.StringLength(string=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeStringLength.webp)

### Args:

#### Input socket arguments:

- **string**: [String](String.md)

### Output sockets:

- **length** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[String](String.md)** |
| [length](String.md#length) | `@property`<br> `def length(self):` |
| Global functions |
| [string_length](functions.md#string_length) | `def string_length(string=None):` |

<sub>Go to [top](#node-String-Length) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

