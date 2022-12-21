# Node Translate Instances

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)
- geonodes name: `TranslateInstances`
- bl_idname: `GeometryNodeTranslateInstances`

```python
from geonodes import nodes

node = nodes.TranslateInstances(instances=None, selection=None, translation=None, local_space=None)
```

#### Input socket arguments:

- instances: Instances
- selection: Boolean
- translation: Vector
- local_space: Boolean

#### Output sockets:

- **instances** : Instances

