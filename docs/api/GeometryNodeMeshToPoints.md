# Node *Mesh to Points*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)
- geonodes name: `MeshToPoints`
- bl_idname: `GeometryNodeMeshToPoints`

```python
from geonodes import nodes

node = nodes.MeshToPoints(mesh=None, selection=None, position=None, radius=None, mode='VERTICES')
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToPoints.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)
- **position**: [Vector](Vector.md)
- **radius**: [Float](Float.md)

#### Node parameter arguments:

- **mode** (str): default = 'VERTICES' in ('VERTICES', 'EDGES', 'FACES', 'CORNERS')

### Output sockets:

- **points** : [Points](Points.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Mesh](Mesh.md)** |
| [to_points](Mesh.md#to_points) | `def to_points(self, selection=None, position=None, radius=None, mode='VERTICES'):` |
| **[Vertex](Vertex.md)** |
| [to_points](Vertex.md#to_points) | `def to_points(self, position=None, radius=None, mode='VERTICES'):` |

<sub>Go to [top](#node-Mesh-to-Points) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

