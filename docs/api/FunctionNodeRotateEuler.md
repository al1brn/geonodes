# Node *Rotate Euler*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
- geonodes name: `RotateEuler`
- bl_idname: `FunctionNodeRotateEuler`

```python
from geonodes import nodes

node = nodes.RotateEuler(rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', type='EULER')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRotateEuler.webp)

### Args:

#### Input socket arguments:

- **rotation**: [Vector](Vector.md)
- **rotate_by**: [Vector](Vector.md)
- **axis**: [Vector](Vector.md)
- **angle**: [Float](Float.md)

#### Node parameter arguments:

- **space** (str): default = 'OBJECT' in ('OBJECT', 'LOCAL')
- **type** (str): default = 'EULER' in ('AXIS_ANGLE', 'EULER')

### Output sockets:

- **rotation** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| Global functions |
| [rotate_euler](functions.md#rotate_euler) | `def rotate_euler(rotation=None, rotate_by=None, space='OBJECT'):` |
| [rotate_axis_angle](functions.md#rotate_axis_angle) | `def rotate_axis_angle(rotation=None, axis=None, angle=None, space='OBJECT'):` |

<sub>Go to [top](#node-Rotate-Euler) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

