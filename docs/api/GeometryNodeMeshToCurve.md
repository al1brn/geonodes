# Node Mesh to Curve

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)
- geonodes name: `MeshToCurve`
- bl_idname: `GeometryNodeMeshToCurve`

```python
from geonodes import nodes

node = nodes.MeshToCurve(mesh=None, selection=None)
```

### Args:

#### Input socket arguments:

- **mesh**: [Mesh](Mesh.md)
- **selection**: [Boolean](Boolean.md)

### Output sockets:

- **curve** : [Curve](Curve.md)

## Implementation

#### class [Mesh](Mesh.md)

 - [to_curve](Mesh.md#to_curve)
#### class [Edge](Edge.md)

 - [to_curve](Edge.md#to_curve)