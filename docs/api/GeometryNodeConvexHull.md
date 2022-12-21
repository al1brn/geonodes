# Node Convex Hull

> [main](../structure.md) - [nodes](nodes.md) - [nodes menus](nodes_menus.md)

- [Blender reference](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/convex_hull.html)
- [api reference](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)
- geonodes name: `WNode`
- bl_idname: `GeometryNodeConvexHull`

```python
from geonodes import nodes

node = nodes.ConvexHull(geometry=None)
```

#### Input socket arguments:

- geometry: Geometry

#### Output sockets:

- **convex_hull** : Geometry

