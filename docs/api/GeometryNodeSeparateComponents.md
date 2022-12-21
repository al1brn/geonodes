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

 - [separate_components](Geometry.md#separate_components-property)
 - [mesh_component](Geometry.md#mesh_component-property)
 - [curve_component](Geometry.md#curve_component-property)
 - [points_component](Geometry.md#points_component-property)
 - [volume_component](Geometry.md#volume_component-property)
 - [instances_component](Geometry.md#instances_component-property)
