# Node *Instance Scale*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html)
- geonodes name: `InstanceScale`
- bl_idname: `GeometryNodeInputInstanceScale`

```python
from geonodes import nodes

node = nodes.InstanceScale()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputInstanceScale.webp)

### Output sockets:

- **scale** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Instance](Instance.md)** |
| [scale](Instance.md#scale) | `@property`<br> `def scale(self):` |
| **[Instances](Instances.md)** |
| [scale](Instances.md#scale) | `@property`<br> `def scale(self):` |

<sub>Go to [top](#node-Instance-Scale) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

