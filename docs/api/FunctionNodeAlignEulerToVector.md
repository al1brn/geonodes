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

#### class [Vector](Vector.md)

 - [align_euler_to_vector](Vector.md#align_euler_to_vector)
#### Global functions

 - [align_euler_to_vector](function.md#align_euler_to_vector)
#### class [Rotation](Rotation.md)

 - [align_to_vector](Rotation.md#align_to_vector)