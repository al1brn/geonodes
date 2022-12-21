# Node Edge Angle

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/edge_angle.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
- geonodes name: `EdgeAngle`
- bl_idname: `GeometryNodeInputMeshEdgeAngle`

```python
from geonodes import nodes

node = nodes.EdgeAngle()
```

### Output sockets:

- **unsigned_angle** : [Float](Float.md)
- **signed_angle** : [Float](Float.md)

## Implementation

#### class [Edge](Edge.md)

 - [angle](Edge.md#angle-property)
 - [unsigned_angle](Edge.md#unsigned_angle-property)
 - [signed_angle](Edge.md#signed_angle-property)
