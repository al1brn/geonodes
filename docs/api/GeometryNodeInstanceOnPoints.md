# Node Instance on Points

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)
- geonodes name: `InstanceOnPoints`
- bl_idname: `GeometryNodeInstanceOnPoints`

```python
from geonodes import nodes

node = nodes.InstanceOnPoints(points=None, selection=None, instance=None, pick_instance=None, instance_index=None, rotation=None, scale=None)
```

#### Input socket arguments:

- **points**: [Points](Points.md)
- **selection**: [Boolean](Boolean.md)
- **instance**: [Geometry](Geometry.md)
- **pick_instance**: [Boolean](Boolean.md)
- **instance_index**: [Integer](Integer.md)
- **rotation**: [Vector](Vector.md)
- **scale**: [Vector](Vector.md)

#### Output sockets:

- **instances** : [Instances](Instances.md)

