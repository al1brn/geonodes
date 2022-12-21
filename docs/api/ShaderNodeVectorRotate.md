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

 - [rotate_euler](Vector.md#rotate_euler)
  ```python
  def rotate_euler(self, center=None, rotation=None, invert=False)
  ```

 - [rotate_axis_angle](Vector.md#rotate_axis_angle)
  ```python
  def rotate_axis_angle(self, center=None, axis=None, angle=None, invert=False)
  ```

 - [rotate_x](Vector.md#rotate_x)
  ```python
  def rotate_x(self, center=None, angle=None, invert=False)
  ```

 - [rotate_y](Vector.md#rotate_y)
  ```python
  def rotate_y(self, center=None, angle=None, invert=False)
  ```

 - [rotate_z](Vector.md#rotate_z)
  ```python
  def rotate_z(self, center=None, angle=None, invert=False)
  ```

