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

### Args:

#### Input socket arguments:

- **instances**: [Instances](Instances.md)
- **selection**: [Boolean](Boolean.md)
- **translation**: [Vector](Vector.md)
- **local_space**: [Boolean](Boolean.md)

### Output sockets:

- **instances** : [Instances](Instances.md)

## Implementation

#### class [Instances](Instances.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f8910>>](Instances.md#translate)
#### class [Instance](Instance.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f88e0>>](Instance.md#translate)
