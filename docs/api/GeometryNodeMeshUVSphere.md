# Node 'UV Sphere'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)
- geonodes name: `UvSphere`
- bl_idname: `GeometryNodeMeshUVSphere`

```python
from geonodes import nodes

node = nodes.UvSphere(segments=None, rings=None, radius=None)
```

### Args:

#### Input socket arguments:

- **segments**: [Integer](Integer.md)
- **rings**: [Integer](Integer.md)
- **radius**: [Float](Float.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

### [Mesh](Mesh.md)

| Name | Definition |
|------|------------|
 | [Circle](Mesh.md#Circle-classmethod) | `def Circle(cls, segments=None, rings=None, radius=None):` |

<sub>Go to [top](#node-{wnode.bnode.name}) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

