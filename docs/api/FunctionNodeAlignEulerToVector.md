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

### Global functions

| Name | Definition |
|------|------------|
 | [align_euler_to_vector](A.md#align_euler_to_vector) | `def align_euler_to_vector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):` |

### [Rotation](Rotation.md)

| Name | Definition |
|------|------------|
 | [align_to_vector](Rotation.md#align_to_vector) | `def align_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):` |

### [Vector](Vector.md)

| Name | Definition |
|------|------------|
 | [align_euler_to_vector](Vector.md#align_euler_to_vector) | `def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):` |

