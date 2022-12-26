# Node *Align Euler to Vector*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/align_euler_to_vector.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
- geonodes name: `AlignEulerToVector`
- bl_idname: `FunctionNodeAlignEulerToVector`

```python
from geonodes import nodes

node = nodes.AlignEulerToVector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeAlignEulerToVector.webp)

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

| Class or method name | Definition |
|----------------------|------------|
| **[Vector](Vector.md)** |
| [align_euler_to_vector](Vector.md#align_euler_to_vector) | `def align_euler_to_vector(self, factor=None, vector=None, axis='X', pivot_axis='AUTO'):` |
| [AlignToVector](Vector.md#AlignToVector) | `@classmethod`<br> `def AlignToVector(cls, factor=None, vector=None, axis='X', pivot_axis='AUTO'):` |
| Global functions |
| [align_euler_to_vector](functions.md#align_euler_to_vector) | `def align_euler_to_vector(rotation=None, factor=None, vector=None, axis='X', pivot_axis='AUTO'):` |

<sub>Go to [top](#node-Align-Euler-to-Vector) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

