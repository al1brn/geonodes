# Node Geometry to Instance

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeGeometryToInstance`

```python
from geonodes import nodes

node = nodes.GeometryToInstance(*geometry)
```

#### Input socket arguments:

- geometry: *Geometry

#### Output sockets:

- **instances** : Instances

