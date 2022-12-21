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

#### Input socket arguments:

- instances: Instances
- selection: Boolean
- scale: Vector
- center: Vector
- local_space: Boolean

#### Output sockets:

- **instances** : Instances

