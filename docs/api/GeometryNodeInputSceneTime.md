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

#### class [{class_name}]({class_name}.md)

 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x1683b2e90>>](Float.md#Seconds-classmethod)
 - [<bound method Generator.fname of <generator.code_gen.Constructor object at 0x1683b00d0>>](Float.md#Frame-classmethod)
