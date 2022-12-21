# Node Separate Components

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/separate_components.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
- geonodes name: `SeparateComponents`
- bl_idname: `GeometryNodeSeparateComponents`

```python
from geonodes import nodes

node = nodes.SeparateComponents(geometry=None)
```

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

### Output sockets:

- **mesh** : [Mesh](Mesh.md)
- **point_cloud** : [Geometry](Geometry.md)
- **curve** : [Curve](Curve.md)
- **volume** : [Volume](Volume.md)
- **instances** : [Instances](Instances.md)

## Implementation

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1683b2200>>](Geometry.md#separate_components-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1683b3d00>>](Geometry.md#mesh_component-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1683b11b0>>](Geometry.md#curve_component-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1683b0af0>>](Geometry.md#points_component-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1683b02e0>>](Geometry.md#volume_component-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x1683b28c0>>](Geometry.md#instances_component-property)
