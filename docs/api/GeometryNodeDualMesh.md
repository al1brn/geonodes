# Node Dual Mesh

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/dual_mesh.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)
- geonodes name: `DualMesh`
- bl_idname: `GeometryNodeDualMesh`

```python
from geonodes import nodes

node = nodes.DualMesh(mesh=None, keep_boundaries=None)
```

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **keep_boundaries**: [Boolean](Boolean.md)

### Output sockets:

- **dual_mesh** : [Geometry](Geometry.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [dual_mesh](Mesh.md#dual_mesh)