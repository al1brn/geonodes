# Node Rotate Euler

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotate_euler.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
- geonodes name: `RotateEuler`
- bl_idname: `FunctionNodeRotateEuler`

```python
from geonodes import nodes

node = nodes.RotateEuler(rotation=None, rotate_by=None, axis=None, angle=None, space='OBJECT', type='EULER')
```

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

### Global functions

| Name | Definition |
|------|------------|
 | [rotate_euler](A.md#rotate_euler) | `def rotate_euler(rotation=None, rotate_by=None, space='OBJECT'): |
 | [rotate_axis_angle](A.md#rotate_axis_angle) | `def rotate_axis_angle(rotation=None, axis=None, angle=None, space='OBJECT'): |

### [Rotation](Rotation.md)

| Name | Definition |
|------|------------|
 | [Euler](Rotation.md#Euler-classmethod) | `def Euler(cls, rotation=None, rotate_by=None, space='OBJECT'): |
 | [AxisAngle](Rotation.md#AxisAngle-classmethod) | `def AxisAngle(cls, rotation=None, axis=None, angle=None, space='OBJECT'): |
 | [rotate_euler](Rotation.md#rotate_euler) | `def rotate_euler(self, rotate_by=None, space='OBJECT'): |
 | [rotate_axis_angle](Rotation.md#rotate_axis_angle) | `def rotate_axis_angle(self, axis=None, angle=None, space='OBJECT'): |

