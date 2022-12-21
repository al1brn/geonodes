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

#### Global functions

 - [rotate_euler](function.md#rotate_euler)
 - [rotate_axis_angle](function.md#rotate_axis_angle)
#### class [Rotation](Rotation.md)

 - [Euler](Rotation.md#Euler-classmethod)
 - [AxisAngle](Rotation.md#AxisAngle-classmethod)
 - [rotate_euler](Rotation.md#rotate_euler)
 - [rotate_axis_angle](Rotation.md#rotate_axis_angle)