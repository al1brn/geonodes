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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Method object at 0x1683b3100>>](Mesh.md#dual_mesh)
