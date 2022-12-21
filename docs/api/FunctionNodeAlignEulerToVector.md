# Node Align Euler to Vector

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
- geonodes name: `AlignEulerToVector`
- bl_idname: `FunctionNodeAlignEulerToVector`

```python
from geonodes import nodes

node = nodes.AlignEulerToVector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO')
```

### Args:

#### Input socket arguments:

- **rotation**: [Vector](Vector.md)
- **factor**: [Float](Float.md)
- **vector**: [Vector](Vector.md)

#### Node parameter arguments:

- **axis** (str): default = 'X' in ('X', 'Y', 'Z')
- **pivot_axis** (str): default = 'AUTO' in ('AUTO', 'X', 'Y', 'Z')

### Output sockets:

- **rotation** : [Vector](Vector.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b1180>>](Vector.md#align_euler_to_vector)
#### Global functions

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x1683b05e0>>](function.md#align_euler_to_vector)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x1683b1bd0>>](Rotation.md#align_to_vector)
