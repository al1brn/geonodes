# Node *Vector Rotate*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
- geonodes name: `VectorRotate`
- bl_idname: `ShaderNodeVectorRotate`

```python
from geonodes import nodes

node = nodes.VectorRotate(vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorRotate.webp)

### Args:

#### Input socket arguments:

- **vector**: [Vector](Vector.md)
- **center**: [Vector](Vector.md)
- **axis**: [Vector](Vector.md)
- **angle**: [Float](Float.md)
- **rotation**: [Vector](Vector.md)

#### Node parameter arguments:

- **invert** (bool): default = False
- **rotation_type** (str): default = 'AXIS_ANGLE' in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')

### Output sockets:

- **vector** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Vector](Vector.md)** |
| [rotate_euler](Vector.md#rotate_euler) | `def rotate_euler(self, center=None, rotation=None, invert=False):` |
| [rotate_axis_angle](Vector.md#rotate_axis_angle) | `def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False):` |
| [rotate_x](Vector.md#rotate_x) | `def rotate_x(self, center=None, angle=None, invert=False):` |
| [rotate_y](Vector.md#rotate_y) | `def rotate_y(self, center=None, angle=None, invert=False):` |
| [rotate_z](Vector.md#rotate_z) | `def rotate_z(self, center=None, angle=None, invert=False):` |

<sub>Go to [top](#node-Vector-Rotate) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

