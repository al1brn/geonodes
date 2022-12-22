# Node *Subdivide Mesh*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)
- geonodes name: `SubdivideMesh`
- bl_idname: `GeometryNodeSubdivideMesh`

```python
from geonodes import nodes

node = nodes.SubdivideMesh(mesh=None, level=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSubdivideMesh.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **level**: [Integer](Integer.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [subdivide](Mesh.md#subdivide) | `def subdivide(self, level=None):` |

<sub>Go to [top](#node-Subdivide-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

