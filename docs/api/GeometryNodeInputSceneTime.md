# Node *Scene Time*

> [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)
- geonodes name: `SceneTime`
- bl_idname: `GeometryNodeInputSceneTime`

```python
from geonodes import nodes

node = nodes.SceneTime()
```

![Blender Image](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputSceneTime.webp)

### Output sockets:

- **seconds** : [Float](Float.md)
- **frame** : [Float](Float.md)

## Implementation

| Class or method name | Definition |
|----------------------|------------|
| **[Float](Float.md)** |
| [Seconds](Float.md#Seconds) | `@classmethod`<br> `def Seconds(cls):` |
| [Frame](Float.md#Frame) | `@classmethod`<br> `def Frame(cls):` |

<sub>Go to [top](#node-Scene-Time) - [main](../index.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

