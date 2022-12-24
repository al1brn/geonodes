# Node *Edge Angle*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
- geonodes name: `EdgeAngle`
- bl_idname: `GeometryNodeInputMeshEdgeAngle`

```python
from geonodes import nodes

node = nodes.EdgeAngle()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeAngle.webp)

### Output sockets:

- **unsigned_angle** : [Float](Float.md)
- **signed_angle** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Edge](Edge.md)** |
| [angle](Edge.md#angle) | `@property`<br> `def angle(self):` |
| [unsigned_angle](Edge.md#unsigned_angle) | `@property`<br> `def unsigned_angle(self):` |
| [signed_angle](Edge.md#signed_angle) | `@property`<br> `def signed_angle(self):` |

<sub>Go to [top](#node-Edge-Angle) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

