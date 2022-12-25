# Node *Realize Instances*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)
- geonodes name: `RealizeInstances`
- bl_idname: `GeometryNodeRealizeInstances`

```python
from geonodes import nodes

node = nodes.RealizeInstances(geometry=None, legacy_behavior=False)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRealizeInstances.webp)

### Args:

#### Input socket arguments:

- **geometry**: [Geometry](Geometry.md)

#### Node parameter arguments:

- **legacy_behavior** (bool): default = False

### Output sockets:

- **geometry** : [Geometry](Geometry.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Instances](Instances.md)** |
| [realize](Instances.md#realize) | `def realize(self, legacy_behavior=False):` |

<sub>Go to [top](#node-Realize-Instances) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

