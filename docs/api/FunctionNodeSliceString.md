# Node Slice String

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/text/slice_string.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)
- geonodes name: `SliceString`
- bl_idname: `FunctionNodeSliceString`

```python
from geonodes import nodes

node = nodes.SliceString(string=None, position=None, length=None)
```

### Args:

#### Input socket arguments:

- **string**: [String](String.md)
- **position**: [Integer](Integer.md)
- **length**: [Integer](Integer.md)

### Output sockets:

- **string** : [String](String.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x168102a10>>](String.md#slice)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x168102a40>>](function.md#slice_string)
