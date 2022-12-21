# Node Cube

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)
- geonodes name: `Cube`
- bl_idname: `GeometryNodeMeshCube`

```python
from geonodes import nodes

node = nodes.Cube(size=None, vertices_x=None, vertices_y=None, vertices_z=None)
```

### Args:

#### Input socket arguments:

- **size**: [Vector](Vector.md)
- **vertices_x**: [Integer](Integer.md)
- **vertices_y**: [Integer](Integer.md)
- **vertices_z**: [Integer](Integer.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

#### [Mesh](Mesh.md)

 - [Cube](Mesh.md#Cube-classmethod)
  ```python
  nodes.Cube(size=size, vertices_x=vertices_x, vertices_y=vertices_y, vertices_z=vertices_z  ```

