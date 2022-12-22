# Node *Mesh to Curve*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)
- geonodes name: `MeshToCurve`
- bl_idname: `GeometryNodeMeshToCurve`

```python
from geonodes import nodes

node = nodes.MeshToCurve(mesh=None, selection=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToCurve.webp)

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Edge](Edge.md)** |
| [to_curve](Edge.md#to_curve) | `def to_curve(self):` |
| **[Mesh](Mesh.md)** |
| [to_curve](Mesh.md#to_curve) | `def to_curve(self, selection=None):` |

<sub>Go to [top](#node-Mesh-to-Curve) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

