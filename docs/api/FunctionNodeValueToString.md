# Node Value to String

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/value_to_string.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)
- geonodes name: `ValueToString`
- bl_idname: `FunctionNodeValueToString`

```python
from geonodes import nodes

node = nodes.ValueToString(value=None, decimals=None)
```

### Args:

#### Input socket arguments:

- **value**: [Float](Float.md)
- **decimals**: [Integer](Integer.md)

### Output sockets:

- **string** : [String](String.md)

## Implementation

#### class [Float](Float.md)

 - [to_string](Float.md#to_string)
#### class [Integer](Integer.md)

 - [to_string](Integer.md#to_string)
#### Global functions

 - [value_to_string](function.md#value_to_string)