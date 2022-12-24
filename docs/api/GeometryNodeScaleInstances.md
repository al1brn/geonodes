# Node *Scale Instances*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)
- geonodes name: `ScaleInstances`
- bl_idname: `GeometryNodeScaleInstances`

```python
from geonodes import nodes

node = nodes.ScaleInstances(instances=None, selection=None, scale=None, center=None, local_space=None)
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeScaleInstances.webp)

### Args:

#### Input socket arguments:

- **instances**: [Instances](Instances.md)
- **selection**: [Boolean](Boolean.md)
- **scale**: [Vector](Vector.md)
- **center**: [Vector](Vector.md)
- **local_space**: [Boolean](Boolean.md)

### Output sockets:

- **instances** : [Instances](Instances.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Instance](Instance.md)** |
| [set_scale](Instance.md#set_scale) | `def set_scale(self, scale=None, center=None, local_space=None):` |
| **[Instances](Instances.md)** |
| [set_scale](Instances.md#set_scale) | `def set_scale(self, selection=None, scale=None, center=None, local_space=None):` |

<sub>Go to [top](#node-Scale-Instances) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

