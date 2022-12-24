# Node *Extrude Mesh*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
- geonodes name: `ExtrudeMesh`
- bl_idname: `GeometryNodeExtrudeMesh`

```python
from geonodes import nodes

node = nodes.ExtrudeMesh(mesh=None, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)
- **offset**: [Vector](Vector.md)
- **offset_scale**: [Float](Float.md)
- **individual**: [Boolean](Boolean.md)

#### Node parameter arguments:

- **mode** (str): default = 'FACES' in ('VERTICES', 'EDGES', 'FACES')

### Output sockets:

- **mesh** : [Mesh](Mesh.md)
- **top** : [Boolean](Boolean.md)
- **side** : [Boolean](Boolean.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Edge](Edge.md)** |
| [extrude](Edge.md#extrude) | `def extrude(self, offset=None, offset_scale=None, individual=None):` |
| **[Face](Face.md)** |
| [extrude](Face.md#extrude) | `def extrude(self, offset=None, offset_scale=None, individual=None):` |
| **[Mesh](Mesh.md)** |
| [extrude](Mesh.md#extrude) | `def extrude(self, selection=None, offset=None, offset_scale=None, individual=None, mode='FACES'):` |
| **[Vertex](Vertex.md)** |
| [extrude](Vertex.md#extrude) | `def extrude(self, offset=None, offset_scale=None, individual=None):` |

<sub>Go to [top](#node-Extrude-Mesh) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

