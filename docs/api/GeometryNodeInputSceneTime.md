# Node 'Scene Time'

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)
- geonodes name: `SceneTime`
- bl_idname: `GeometryNodeInputSceneTime`

```python
from geonodes import nodes

node = nodes.SceneTime()
```

[Blender Image](self.node_image_ref)

### Output sockets:

- **seconds** : [Float](Float.md)
- **frame** : [Float](Float.md)

## Implementation

### [Float](Float.md)

| Name | Definition |
|------|------------|
 | [Seconds](Float.md#Seconds-classmethod) | `def Seconds(cls):` |
 | [Frame](Float.md#Frame-classmethod) | `def Frame(cls):` |

<sub>Go to [top](#node-Scene-Time) - [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)</sub>

