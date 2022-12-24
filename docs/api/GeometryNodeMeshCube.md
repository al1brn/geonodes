# Node *Cube*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/cube.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)
- geonodes name: `Cube`
- bl_idname: `GeometryNodeMeshCube`

```python
from geonodes import nodes

node = nodes.Cube(size=None, vertices_x=None, vertices_y=None, vertices_z=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCube.webp)

### Args:

#### Input socket arguments:

- **size**: [Vector](Vector.md)
- **vertices_x**: [Integer](Integer.md)
- **vertices_y**: [Integer](Integer.md)
- **vertices_z**: [Integer](Integer.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [Cube](Mesh.md#Cube) | `@classmethod`<br> `def Cube(cls, size=None, vertices_x=None, vertices_y=None, vertices_z=None):` |

<sub>Go to [top](#node-Cube) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

