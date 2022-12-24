# Node *Ico Sphere*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/icosphere.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)
- geonodes name: `IcoSphere`
- bl_idname: `GeometryNodeMeshIcoSphere`

```python
from geonodes import nodes

node = nodes.IcoSphere(radius=None, subdivisions=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshIcoSphere.webp)

### Args:

#### Input socket arguments:

- **radius**: [Float](Float.md)
- **subdivisions**: [Integer](Integer.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [IcoSphere](Mesh.md#IcoSphere) | `@classmethod`<br> `def IcoSphere(cls, radius=None, subdivisions=None):` |

<sub>Go to [top](#node-Ico-Sphere) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

