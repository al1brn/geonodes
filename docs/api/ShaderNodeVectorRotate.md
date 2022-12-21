# Node Vector Rotate

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/vector/vector_rotate.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
- geonodes name: `VectorRotate`
- bl_idname: `ShaderNodeVectorRotate`

```python
from geonodes import nodes

node = nodes.VectorRotate(vector=None, center=None, axis=None, angle=None, rotation=None, invert=False, rotation_type='AXIS_ANGLE')
```

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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54b80>>](Vector.md#rotate_euler)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54b50>>](Vector.md#rotate_axis_angle)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54b20>>](Vector.md#rotate_x)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54af0>>](Vector.md#rotate_y)
 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x16ee54ac0>>](Vector.md#rotate_z)
