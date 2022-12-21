# Node 'Subdivide Mesh'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/subdivide_mesh.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)
- geonodes name: `SubdivideMesh`
- bl_idname: `GeometryNodeSubdivideMesh`

```python
from geonodes import nodes

node = nodes.SubdivideMesh(mesh=None, level=None)
```

[Blender Image](self.node_image_ref)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **level**: [Integer](Integer.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

### [Mesh](Mesh.md)

| Name | Definition |
|------|------------|
 | [subdivide](Mesh.md#subdivide) | `def subdivide(self, level=None):` |

<sub>Go to [top](#node-Subdivide-Mesh) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

