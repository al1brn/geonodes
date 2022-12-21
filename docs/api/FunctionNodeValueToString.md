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

#### Input socket arguments:

- value: [Float](Float.md)
- decimals: [Integer](Integer.md)

#### Output sockets:

- **string** : String

