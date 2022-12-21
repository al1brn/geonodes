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

#### class [Geometry](Geometry.md)

 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4f96f0>>](Geometry.md#separate_components-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4f96c0>>](Geometry.md#mesh_component-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4f9690>>](Geometry.md#curve_component-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4f9660>>](Geometry.md#points_component-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4f9630>>](Geometry.md#volume_component-property)
 - [<bound method Generator.fname of <generator.code_gen.Property object at 0x16d4f9600>>](Geometry.md#instances_component-property)
