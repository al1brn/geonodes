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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1681026b0>>](Float.md#to_string)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x168102680>>](Integer.md#to_string)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1681026e0>>](function.md#value_to_string)
