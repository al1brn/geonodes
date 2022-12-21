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

#### Input socket arguments:

- geometry: [Geometry](Geometry.md)

#### Output sockets:

- **mesh** : [Mesh](Mesh)
- **point_cloud** : [Geometry](Geometry)
- **curve** : [Curve](Curve)
- **volume** : [Volume](Volume)
- **instances** : [Instances](Instances)

