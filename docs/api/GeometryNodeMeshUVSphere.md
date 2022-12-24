# Node *UV Sphere*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/uv_sphere.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)
- geonodes name: `UvSphere`
- bl_idname: `GeometryNodeMeshUVSphere`

```python
from geonodes import nodes

node = nodes.UvSphere(segments=None, rings=None, radius=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshUVSphere.webp)

### Args:

#### Input socket arguments:

- **segments**: [Integer](Integer.md)
- **rings**: [Integer](Integer.md)
- **radius**: [Float](Float.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [UVSphere](Mesh.md#UVSphere) | `@classmethod`<br> `def UVSphere(cls, segments=None, rings=None, radius=None):` |

<sub>Go to [top](#node-UV-Sphere) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

