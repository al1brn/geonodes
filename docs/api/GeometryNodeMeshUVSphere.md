# Node UV Sphere

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeMeshUVSphere`

```python
from geonodes import nodes

node = nodes.UvSphere(segments=None, rings=None, radius=None)
```

#### Input socket arguments:

- segments: Integer
- rings: Integer
- radius: Float

#### Output sockets:

- **mesh** : Mesh

