# Node *Slice String*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)
- geonodes name: `SliceString`
- bl_idname: `FunctionNodeSliceString`

```python
from geonodes import nodes

node = nodes.SliceString(string=None, position=None, length=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSliceString.webp)

### Args:

#### Input socket arguments:

- **string**: [String](String.md)
- **position**: [Integer](Integer.md)
- **length**: [Integer](Integer.md)

### Output sockets:

- **string** : [String](String.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[String](String.md)** |
| [slice](String.md#slice) | `def slice(self, position=None, length=None):` |
| Global functions |
| [slice_string](functions.md#slice_string) | `def slice_string(string=None, position=None, length=None):` |

<sub>Go to [top](#node-Slice-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

