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

 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee55a20>>](function.md#rotate_euler)
 - [<bound method Generator.fname of <generator.code_gen.Function object at 0x16ee559f0>>](function.md#rotate_axis_angle)
#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16ee559c0>>](Rotation.md#Euler-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16ee55990>>](Rotation.md#AxisAngle-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55960>>](Rotation.md#rotate_euler)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee55930>>](Rotation.md#rotate_axis_angle)
