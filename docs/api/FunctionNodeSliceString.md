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

#### Global functions

 - [slice_string](A.md#slice_string)
#### class [String](String.md)

 - [slice](String.md#slice)
