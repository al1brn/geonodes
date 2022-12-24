# Node *Face Neighbors*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/face_neighbors.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
- geonodes name: `FaceNeighbors`
- bl_idname: `GeometryNodeInputMeshFaceNeighbors`

```python
from geonodes import nodes

node = nodes.FaceNeighbors()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshFaceNeighbors.webp)

### Output sockets:

- **vertex_count** : [Integer](Integer.md)
- **face_count** : [Integer](Integer.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Face](Face.md)** |
| [neighbors](Face.md#neighbors) | `@property`<br> `def neighbors(self):` |
| [neighbors_vertex_count](Face.md#neighbors_vertex_count) | `@property`<br> `def neighbors_vertex_count(self):` |
| [neighbors_face_count](Face.md#neighbors_face_count) | `@property`<br> `def neighbors_face_count(self):` |

<sub>Go to [top](#node-Face-Neighbors) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

