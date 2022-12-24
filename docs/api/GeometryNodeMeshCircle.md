# Node *Mesh Circle*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh_primitives/mesh_circle.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)
- geonodes name: `MeshCircle`
- bl_idname: `GeometryNodeMeshCircle`

```python
from geonodes import nodes

node = nodes.MeshCircle(vertices=None, radius=None, fill_type='NONE')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCircle.webp)

### Args:

#### Input socket arguments:

- **vertices**: [Integer](Integer.md)
- **radius**: [Float](Float.md)

#### Node parameter arguments:

- **fill_type** (str): default = 'NONE' in ('NONE', 'NGON', 'TRIANGLE_FAN')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [Circle](Mesh.md#Circle) | `@classmethod`<br> `def Circle(cls, vertices=None, radius=None, fill_type='NONE'):` |

<sub>Go to [top](#node-Mesh-Circle) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

