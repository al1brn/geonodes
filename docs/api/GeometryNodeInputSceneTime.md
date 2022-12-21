# Node Scene Time

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene_time.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)
- geonodes name: `SceneTime`
- bl_idname: `GeometryNodeInputSceneTime`

```python
from geonodes import nodes

node = nodes.SceneTime()
```

### Output sockets:

- **seconds** : [Float](Float.md)
- **frame** : [Float](Float.md)

## Implementation

#### class [Float](Float.md)

 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16d4f8be0>>](Float.md#Seconds-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x16d4f8bb0>>](Float.md#Frame-classmethod)
