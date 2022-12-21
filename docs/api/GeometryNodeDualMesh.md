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

#### Input socket arguments:

- mesh: Mesh
- keep_boundaries: Boolean

#### Output sockets:

- **dual_mesh** : Geometry

