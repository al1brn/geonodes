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

#### [Vector](Vector.md)

 - [rotate_euler](Vector.md#rotate_euler) ```python nodes.VectorRotate(vector=self, center=center, axis=None, angle=None, rotation=rotation, invert=invert, rotation_type='EULER_XYZ'````
 - [rotate_axis_angle](Vector.md#rotate_axis_angle) ```python nodes.VectorRotate(vector=self, center=center, axis=axis, angle=angle, rotation=None, invert=invert, rotation_type='AXIS_ANGLE'````
 - [rotate_x](Vector.md#rotate_x) ```python nodes.VectorRotate(vector=self, center=center, axis=None, angle=angle, rotation=None, invert=invert, rotation_type='X_AXIS'````
 - [rotate_y](Vector.md#rotate_y) ```python nodes.VectorRotate(vector=self, center=center, axis=None, angle=angle, rotation=None, invert=invert, rotation_type='Y_AXIS'````
 - [rotate_z](Vector.md#rotate_z) ```python nodes.VectorRotate(vector=self, center=center, axis=None, angle=angle, rotation=None, invert=invert, rotation_type='Z_AXIS'````
