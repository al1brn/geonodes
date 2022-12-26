# Node *Value to String*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)
- geonodes name: `ValueToString`
- bl_idname: `FunctionNodeValueToString`

```python
from geonodes import nodes

node = nodes.ValueToString(value=None, decimals=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeValueToString.webp)

### Args:

#### Input socket arguments:

- **value**: [Float](Float.md)
- **decimals**: [Integer](Integer.md)

### Output sockets:

- **string** : [String](String.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Float](Float.md)** |
| [to_string](Float.md#to_string) | `def to_string(self, decimals=None):` |
| **[Integer](Integer.md)** |
| [to_string](Integer.md#to_string) | `def to_string(self):` |
| Global functions |
| [value_to_string](functions.md#value_to_string) | `def value_to_string(value=None, decimals=None):` |

<sub>Go to [top](#node-Value-to-String) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

