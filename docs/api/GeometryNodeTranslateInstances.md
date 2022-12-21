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

- **instances**: [Instances](Instances.md)
- **selection**: [Boolean](Boolean.md)
- **translation**: [Vector](Vector.md)
- **local_space**: [Boolean](Boolean.md)

#### Output sockets:

- **instances** : [Instances](Instances.md)

