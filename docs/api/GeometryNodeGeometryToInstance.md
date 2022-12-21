# Node Geometry to Instance

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
- geonodes name: `GeometryToInstance`
- bl_idname: `GeometryNodeGeometryToInstance`

```python
from geonodes import nodes

node = nodes.GeometryToInstance(*geometry)
```

### Args:

#### Input socket arguments:

- **geometry**: *[Geometry](Geometry.md)

### Output sockets:

- **instances** : [Instances](Instances.md)

## Implementation

#### Global functions

 - [geometry_to_instance](A.md#geometry_to_instance)
#### class [Geometry](Geometry.md)

 - [to_instance](Geometry.md#to_instance)
