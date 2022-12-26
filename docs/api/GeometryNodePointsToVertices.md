# Node *Points to Vertices*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)
- geonodes name: `PointsToVertices`
- bl_idname: `GeometryNodePointsToVertices`

```python
from geonodes import nodes

node = nodes.PointsToVertices(points=None, selection=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVertices.webp)

### Args:

#### Input socket arguments:

- **points**: [Points](Points.md)
- **selection**: [Boolean](Boolean.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[CloudPoint](CloudPoint.md)** |
| [to_vertices](CloudPoint.md#to_vertices) | `def to_vertices(self):` |
| **[Points](Points.md)** |
| [to_vertices](Points.md#to_vertices) | `def to_vertices(self, selection=None):` |

<sub>Go to [top](#node-Points-to-Vertices) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

