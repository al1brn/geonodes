# Node Scale Instances

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)
- geonodes name: `ScaleInstances`
- bl_idname: `GeometryNodeScaleInstances`

```python
from geonodes import nodes

node = nodes.ScaleInstances(instances=None, selection=None, scale=None, center=None, local_space=None)
```

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

#### class [Instances](Instances.md)

 - [<bound method Generator.fname of <generator.code_gen.StackMethod object at 0x16d4f8970>>](Instances.md#set_scale)
#### class [Instance](Instance.md)

 - [<bound method Generator.fname of <generator.code_gen.DomStackMethod object at 0x16d4f8940>>](Instance.md#set_scale)
