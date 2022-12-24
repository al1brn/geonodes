# Node *Instance Rotation*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)
- geonodes name: `InstanceRotation`
- bl_idname: `GeometryNodeInputInstanceRotation`

```python
from geonodes import nodes

node = nodes.InstanceRotation()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputInstanceRotation.webp)

### Output sockets:

- **rotation** : [Vector](Vector.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Instance](Instance.md)** |
| [rotation](Instance.md#rotation) | `@property`<br> `def rotation(self):` |
| **[Instances](Instances.md)** |
| [rotation](Instances.md#rotation) | `@property`<br> `def rotation(self):` |

<sub>Go to [top](#node-Instance-Rotation) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

