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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x1683b1900>>](Edge.md#angle-property)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x1683b1c00>>](Edge.md#unsigned_angle-property)
 - [<bound method Generator.fname of <generator.code_gen.DomPropAttribute object at 0x1683b29b0>>](Edge.md#signed_angle-property)
