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

#### Input socket arguments:

- vector: [Vector[Vector.md]
- center: [Vector[Vector.md]
- axis: [Vector[Vector.md]
- angle: [Float[Float.md]
- rotation: [Vector[Vector.md]

#### Node parameter arguments:

- invert (bool): Node parameter, default = False
- rotation_type (str): Node parameter, default = 'AXIS_ANGLE' in ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')

#### Output sockets:

- **vector** : Vector

