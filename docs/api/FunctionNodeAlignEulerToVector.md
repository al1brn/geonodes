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

#### Input socket arguments:

- rotation: Vector
- factor: Float
- vector: Vector

#### Node parameter arguments:

- axis (str): Node parameter, default = 'X' in ('X', 'Y', 'Z')
- pivot_axis (str): Node parameter, default = 'AUTO' in ('AUTO', 'X', 'Y', 'Z')

#### Output sockets:

- **rotation** : Vector

