# Node Instance on Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeInstanceOnPoints`

```python
from geonodes import nodes

node = nodes.InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

#### Input socket arguments:

- points: Points
- selection: Boolean
- instance: Geometry
- pick_instance: Boolean
- instance_index: Integer
- rotation: Vector
- scale: Vector

#### Output sockets:

- **instances** : Instances

