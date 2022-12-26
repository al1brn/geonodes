# Node *Geometry to Instance*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
- geonodes name: `GeometryToInstance`
- bl_idname: `GeometryNodeGeometryToInstance`

```python
from geonodes import nodes

node = nodes.GeometryToInstance(*geometry)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeGeometryToInstance.webp)

### Args:

#### Input socket arguments:

- **geometry**: *[Geometry](Geometry.md)

### Output sockets:

- **instances** : [Instances](Instances.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Geometry](Geometry.md)** |
| [to_instance](Geometry.md#to_instance) | `def to_instance(*geometry):` |
| Global functions |
| [geometry_to_instance](functions.md#geometry_to_instance) | `def geometry_to_instance(*geometry):` |

<sub>Go to [top](#node-Geometry-to-Instance) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

